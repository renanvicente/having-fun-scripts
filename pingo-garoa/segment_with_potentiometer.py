#!/usr/bin/env python
from pingo import *
from time import sleep

ard = detect.MyBoard()

# Mapping segment
seg_A = ard.pins[13]
seg_B = ard.pins[12]
seg_C = ard.pins[11]
seg_D = ard.pins[10]
seg_E = ard.pins[9]
seg_F = ard.pins[7]
seg_G = ard.pins[6]
seg_DP = ard.pins[5]

# Mapping potentiometer
pot = ard.pins['A0']


# Setting mode

seg_A.mode = OUT
seg_B.mode = OUT
seg_C.mode = OUT
seg_D.mode = OUT
seg_E.mode = OUT
seg_F.mode = OUT
seg_G.mode = OUT
seg_DP.mode = OUT
pot.mode = IN



# Clear all pins
def null_all():
	seg_A.lo()
	seg_B.lo()
	seg_C.lo()
	seg_D.lo()
	seg_E.lo()
	seg_F.lo()
	seg_G.lo()
	seg_DP.lo()

# Set delay from potentiometer and clean all pins
def gb():
	delay = pot.ratio() + 0.01
	sleep(delay)
	null_all()


# Make an one
def number_one():
	seg_B.hi()
	seg_C.hi()

# Make a two
def number_two():
	seg_A.hi()
	seg_B.hi()
	seg_D.hi()
	seg_E.hi()
	seg_G.hi()

# Make a three
def number_three():
	seg_A.hi()
	seg_B.hi()
	seg_C.hi()
	seg_D.hi()
	seg_G.hi()

# Make a four
def number_four():
	seg_B.hi()
	seg_C.hi()
	seg_G.hi()
	seg_F.hi()

# Make a five
def number_five():
	seg_A.hi()
	seg_F.hi()
	seg_G.hi()
	seg_C.hi()
	seg_D.hi()

# Make a six
def number_six():
	seg_F.hi()
	seg_E.hi()
	seg_D.hi()
	seg_C.hi()
	seg_G.hi()

# Make a seven
def number_seven():
	seg_A.hi()
	seg_B.hi()
	seg_C.hi()

# Make an eight
def number_eight():
	seg_A.hi()
	seg_B.hi()
	seg_C.hi()
	seg_D.hi()
	seg_E.hi()
	seg_F.hi()
	seg_G.hi()

# Make a nine
def number_nine():
	seg_A.hi()
	seg_B.hi()
	seg_C.hi()
	seg_F.hi()
	seg_G.hi()

# Make a zero
def number_zero():
	seg_A.hi()
	seg_B.hi()
	seg_C.hi()
	seg_D.hi()
	seg_E.hi()
	seg_F.hi()

# turn high all pins
def all_pins():
	number_eight()
	seg_POINT.hi()

# Make a simple animation with all pins
def boom():
	for value in range(10):
		null_all()
		all_pins()
		sleep(0.1)
		null_all()


if __name__ == '__main__':
	while True:
		number_nine()
		gb()
		number_eight()
		gb()
		number_seven()
		gb()
		number_six()
		gb()
		number_five()
		gb()
		number_four()
		gb()
		number_three()
		gb()
		number_two()
		gb()
		number_one()
		gb()
		number_zero()
		gb()
		boom()
