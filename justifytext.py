#!/usr/bin/python
import sys

# 
# Justify justifies the input file to the expected justify length. It prints the justified 
# text to the console and also returns the justified text in a list 
#

def justify(file_name, justify_length):
	file_object = open(file_name,'r')
	output = open("output.txt",'w')
	buffer_list = []
	out_list = []
	for line in file_object:
		nextLine, buffer_list = distribute_words(line, buffer_list, justify_length)
		out_list.append(print_line(nextLine, justify_length))
	while(len(buffer_list) > 0):
		nextLine, buffer_list = distribute_words("", buffer_list, justify_length)
		out_list.append(print_line(nextLine, justify_length))
	return out_list

def print_line(nextLine, justify_length):
	space_number = justify_length - len_strings(nextLine)
	space_bins = len(nextLine)-1
	if(space_bins < 1):
		const_space = 0
		extra_space = 0	
	else:	
		const_space = space_number/space_bins
		extra_space = space_number%space_bins
	line_string = ""
	for word in nextLine:
		if(extra_space > 0):
			line_string = line_string + word + const_space*" " + " "
		else:
			line_string = line_string + word + const_space*" "
		extra_space = extra_space - 1
	print line_string
	return 	line_string

def len_strings(L):
	length = 0
	if(len(L) < 1):
		return 0;
	for e in L:
		length = length + len(e)
	return length

def distribute_words(line, buffer_list, justify_length):
	nextLine = []
	buffer_list.extend(line.split()) #adds words in current list to the buffer
	while(len(buffer_list) > 0):
		if(len(buffer_list[0]) > justify_length):
			exit("Text error. Word in text longer than justify length")
		if(len_strings(nextLine) + len(nextLine) + len(buffer_list[0]) + 1 < justify_length):
			nextLine.append(buffer_list.pop(0))
		else:
			break
	return nextLine, buffer_list 	



  
# COMPLETE ME

# Program justifies text contents of a given file
# This is the actual code that gets run when the
# program is run. 
#
# DO NOT EDIT BELOW HERE.
if __name__ == "__main__":

    file_name = ''
    length = -1

    # Parse command line arguments
    try:
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-f':
                file_name = sys.argv[i+1]
            elif sys.argv[i] == '-l':
                length = int(sys.argv[i+1])
    except:
        exit('Input error. Example input: justifytext -f mytextfile -l 80')

    if file_name == '' or length < 1:
        exit('Input error. Example input: justifytext -f mytextfile -l 80')
        
    justify(file_name, length)
