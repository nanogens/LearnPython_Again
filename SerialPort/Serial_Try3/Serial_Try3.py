import serial

# Open serial port (replace 'COMx' with the actual port name)
ser = serial.Serial('COM3')

record_counter: int = 0
round_robin: int = 0

# Open text file for writing
with open('data.txt', 'w') as f:
    try:
        while True:
            if(round_robin == 0):

                # Read data from serial port until start of packet is found (DLE STX)
                while True:
                    data = ser.read(1)  # Read one byte at a time
                    if data == b'\x10':  # Check for DLE STX (start of packet)
                        break

                while True:
                    data = ser.read(3)  # Read three bytes for header
                    if data == b'\x02\x88\x00':  # Check for DLE STX (start of packet)
                        round_robin = 1
                        break
                    else:
                        round_robin = 0


                if(round_robin == 1):

                    data = b'\x10\x02\x88\x00'

                    # Read the rest of the header
                    header = ser.read(2)  # Read two bytes for header
                    message_lgt, message_id = header

                    header = data + header

                    # Calculate payload length
                    payload_lgt = message_lgt - 7

                    # Read the payload
                    payload = ser.read(payload_lgt)

                    # Read the CRC
                    crc = ser.read(1)

                    # Calculate CRC
                    calculated_crc = sum(header + payload) & 0xFF

                    # Check if CRC matches
                    if crc == bytes([calculated_crc]):
                        # Write the packet to file
                        packet = data + header + payload + crc
                        # Write bytes with comma spacing
                        f.write(', '.join([f'{byte:02X}' for byte in packet]) + '\n')
                        f.flush()  # Flush buffer to ensure data is written immediately
                        record_counter += 1

                    if (record_counter % 100 == 0):
                        print(f'record_counter: {record_counter}\n')

                round_robin = 0

    except KeyboardInterrupt:
        # Close serial port and file when Ctrl+C is pressed
        ser.close()
