#!/usr/bin/env python

#Create a script that will accept a single integer as a positional argument, and will print a hash
#symbol that amount of times.

import argparse 

times = input("Please enter a single digit number: ")
sign = "#"

parser = argparse.ArugmentParser()
parser.add_argument(sign, action="append")
parser.parse_args(sign.split())
print(



