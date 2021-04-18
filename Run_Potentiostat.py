# Desc : This program demonstrats how to run the Potentiostat .exe program from Python.

# libraries.
import sys, string, os

# change directory.
os.chdir('C:/EC-Lab Development Package_Latest/Examples/C-C++/VisualStudio/MFCStaticLink/output/');

# run the program.
# replace the text string after -p to the technique required and corresponding settings.
# the example below illustrates the OCV technique.
os.system("MFCStaticLink.exe -p OCV 10.0 0.1 0.01 KBIO_ERANGE_AUTO 0")