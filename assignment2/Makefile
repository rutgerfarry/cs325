CFLAGS= -Wall -Wshadow 

FILE1= solution

all: 
	g++ -g -o $(FILE1) $(FILE1).cpp

# Doesn't delete the pdf
clean:
	rm -f  $(FILE1) output_bruteforce.txt output_divideandconquer.txt output_enhanceddnc.txt

.PHONY: all show clean ps pdf showps
