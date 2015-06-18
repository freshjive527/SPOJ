#!/usr/bin/env python2
# -*- coding: utf-8 -*-

test_time = input()
#print type(test_time)
input_number = []
for number in xrange(0,test_time):
	input_range = raw_input()
	input_number.append([input_range.split()[0],input_range.split()[1]])

#print input_number
#print len(input_number)
def findPrime(m,n):
	for i in range(m,n+1,1):
		if isPrime(i):
			print i


def isPrime(test_number):
	if test_number < 2:
		return False

	for j in range(2, int(test_number ** 0.5)+1,1):
		if test_number % j == 0:
			return False
	return True		



for item in input_number:
	findPrime(int(item[0]), int(item[1]))
	print
	

