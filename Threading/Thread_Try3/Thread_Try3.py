import logging
import threading
import time

import serial

def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count


def thread_function(name):
    logging.info("Thread %s: starting", name)
    #time.sleep(2)

    print('Enter your commands below.\r\nInsert "exit" to leave the application.')

    incoming = 1
    #incomingA='32'
    #incomingB=b'32'

    packet = bytearray()
    packet.append(0x10)
    packet.append(0x02)
    packet.append(0x00)
    packet.append(0x88)
    packet.append(0x07)
    packet.append(0x01)
    packet.append(0xA2)



    while 1:
        # get keyboard input
        # incoming = input(">> ")
        # Python 3 users
        # input = input(">> ")
        if incoming == 'exit':
            ser.close()
            # exit()
            break
        else:
            # send the character to the device
            # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
            #ser.write(str.encode(incomingA)) #(b'h') #str.encode(incomingA))
            #ser.to_bytes(0X10)
            ser.write(packet)

            # let's wait one second before reading output (let's give device time to answer)
            time.sleep(1)
            read_byte = ''
            bytecount = 0
            read_byte = ser.read()
            while string_length(read_byte) is not 0:
                print ('%x' % ord(read_byte))
                read_byte = ser.read()

    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    # configure the serial connections (the parameters differs on the device you are connecting to)
    ser = serial.Serial(
        port="COM2",
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=0.5
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

