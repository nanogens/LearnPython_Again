import logging
import threading
import time

import serial

import sys, string, os

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
            # exit()
            break
        else:
            # let's wait one second before reading output (let's give device time to answer)
            time.sleep(1)

    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":

    os.chdir('C:/EC-Lab Development Package_Latest/Examples/C-C++/VisualStudio/MFCStaticLink/output/');
    os.system("MFCStaticLink.exe -p 10 20")

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