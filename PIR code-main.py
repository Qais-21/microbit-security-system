from microbit import *
while True:
    Motion = pin0.read_digital()
    if Motion == 1:
       pin1.write_digital(1)
       pin2.write_digital(1)
    else :
        pin1.write_digital(0)
        pin2.write_digital(0)