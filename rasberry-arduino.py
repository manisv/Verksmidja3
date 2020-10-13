import serial
ser = serial.Serial('/dev/ttyACM0', 9600)

ser.write(str.encode('3'))
ser.write(str.encode('5'))
ser.write(str.encode('6'))