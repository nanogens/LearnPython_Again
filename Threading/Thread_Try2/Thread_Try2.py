import logging
import threading
import time

import serial

def thread_function(name):
    logging.info("Thread %s: starting", name)
    #time.sleep(2)

    print('Enter your commands below.\r\nInsert "exit" to leave the application.')

    incoming = 1
    while 1:
        # get keyboard input
        incoming = input(">> ")
        # Python 3 users
        # input = input(">> ")
        if incoming == 'exit':
            ser.close()
            # exit()
            break
        else:
            # send the character to the device
            # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
            ser.write(str.encode(incoming) + str.encode('\r\n'))
            out = ''
            # let's wait one second before reading output (let's give device time to answer)
            time.sleep(1)
            while ser.inWaiting() > 0:
                out += ser.read(1)

            if out != '':
                print(">>") + out

    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    # configure the serial connections (the parameters differs on the device you are connecting to)
    ser = serial.Serial(
        port="COM2",
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
    )

    ser.isOpen()

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    x.start()

    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")