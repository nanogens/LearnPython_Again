import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port="COM3",
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

ser.isOpen()

print ('Enter your commands below.\r\nInsert "exit" to leave the application.')

incoming=1
while 1 :
    # get keyboard input
    incoming = input(">> ")
        # Python 3 users
        # input = input(">> ")
    if incoming == 'exit':
        ser.close()
        exit()
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
            print (">>") + out