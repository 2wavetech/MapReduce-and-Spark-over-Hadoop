#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
# This mapper code will input a <word, value> input file, and print out <word value>
# if the value is a number or 'ABC'.
#
#  see https://docs.python.org/2/tutorial/index.html for python tutorials
#
# --------------------------------------------------------------------------

# channel list is not used in this program but is here for reference
channels	= ['ABC','DEF','CNO','NOX','YES','CAB','BAT','MAN','ZOO','XYZ','BOB']

# see https://docs.python.org/2/tutorial/datastructures.html for list details

for line in sys.stdin:
    line       = line.strip()       # strip out carriage return
    key_value  = line.split(',')    # split line, into key and value, returns a list
 
    show_title  = key_value[0]         # key is the first item in list, indexed by 0
    value_in   = key_value[1]          # value is the 2nd item, either viewers number or channel name

    #-----------------------------------------------------
    # Check if the input value is a digit or 'ABC'
    #   if so then print out the title and the number or 'ABC'
    #----------------------------------------------------
    if value_in.isdigit() or value_in[0:3] == 'ABC':

        # -----------------------     
	#now write out the result
        # -----------------------
        print( '%s\t%s' % (show_title, value_in) ) 
