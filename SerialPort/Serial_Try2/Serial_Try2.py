import serial

# Open serial port (replace 'COMx' with the actual port name)
ser = serial.Serial('COM3')

# Open text file for writing
with open('data.txt', 'w') as f:
    try:
        while True:
            # Read data from serial port
            data = ser.read(1)  # Read one byte at a time
            if data:
                # Convert bytes to hexadecimal representation and write to file
                hex_str = ' '.join([format(byte, '02X') for byte in data])  # Convert each byte to two-digit hexadecimal
                f.write(hex_str + '\n')  # Write hexadecimal string to file, add newline for readability
                f.flush()  # Flush buffer to ensure data is written immediately
    except KeyboardInterrupt:
        # Close serial port and file when Ctrl+C is pressed
        ser.close()
