#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
#This reducer code will input a <word, value> input file, and join words together
# Note the input will come as a group of lines with same word (ie the key)
# As it reads words it will hold on to the value field
#
# It will keep track of current word and previous word, if word changes
#   then it will perform the 'join' on the set of held values by merely printing out 
#   the word and values.  In other words, there is no need to explicitly match keys b/c
#   Hadoop has already put them sequentially in the input 
#   
# At the end it will perform the last join
#
#
#  Note, there is NO error checking of the input, it is assumed to be correct, meaning
#   it has word with correct and matching entries, no extra spaces, etc.
#
#  see https://docs.python.org/2/tutorial/index.html for python tutorials
#
#  San Diego Supercomputer Center copyright
# --------------------------------------------------------------------------

prev_title   = "  "                # initialize previous word  to blank string
channels	= ['ABC','DEF','CNO','NOX','YES','CAB','BAT','MAN','ZOO','XYZ','BOB']

title_to_output 		= [] 		# an empty list of title for a given word
viewer_num_to_output    = [] 		# an empty list to hold number of viewers for a given word

# see https://docs.python.org/2/tutorial/datastructures.html for list details

viewer_cnt = 0  # count the number of viewers of a certain title while running through the list from mapper

ABC_found = False

for line in sys.stdin:
    line       = line.strip()       # strip out carriage return
    key_value  = line.split('\t')   # split line, into key and value, returns a list
     
    curr_title  = key_value[0]        # key is first item in list, indexed by 0
    value_in   = key_value[1]         # value is 2nd item, may be viewer number or 'ABC'

    #-----------------------------------------------------------
    # Check if it's a new title and 'ABC' has been found with it
    #    if so then append it to the list of final output
    #-----------------------------------------------------------
    if curr_title != prev_title :

        # -------------------------------------------------------------------     
		# now append the join result on the previous title to the final list
        # -------------------------------------------------------------------
		if ABC_found == True:
			title_to_output.append(prev_title)
			viewer_num_to_output.append(viewer_cnt)
               
	    	prev_title = curr_title  	# set up previous title for the next set of input lines
		ABC_found = False		# initialized for the next title
		viewer_cnt = 0			# counting will be startd over again

	# ---------------------------------------------------------------
    # whether or not the join result was written out, 
    #   now process the current title    
  	
    # determine if the value is 'ABC'
    # ---------------------------------------------------------------
    if (value_in[0:3] == 'ABC'): 
    	ABC_found = True 
        
    else:
    	viewer_cnt = viewer_cnt + int(value_in)  # count the number of viewers
                                         

# ---------------------------------------------------------------
#now write out the LAST join result
# ---------------------------------------------------------------
for i in range(len(title_to_output)):  # loop thru all the titles, indexes start at 0
	print('{0} {1}'.format(title_to_output[i],viewer_num_to_output[i]))
	