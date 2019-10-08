import serial

BAUDRATE = 4800
PORT = "COM5"

ser = serial.Serial(baudrate=BAUDRATE, port=PORT, timeout=1,)

try:
    ser.open()
except:
    pass

error_count = 0
points_logged = 0

with open('nmea.txt', 'a') as f:
    while ser.isOpen():
        try:
            line_str = str(ser.readline().decode("utf-8"))
            #print(line_str)
            if line_str[4] == 'G' and len(line_str) > 50:
                print(line_str)
                f.write(line_str)
                f.flush()
                points_logged += 1
                error_count = 0
        except:
            error_count += 1
            print("Error %s/10" % str(error_count))

        if error_count == 10:
            print("Points Logged: " + str(points_logged))
            ser.close()
