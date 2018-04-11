#######
# XOR #
#######

import sys
from helpers import *

def main():
    # take two inputs and parse them
    num_one_dec = parse_input(sys.argv[1])
    num_two_dec = parse_input(sys.argv[2])
    # compute the answer
    answer = num_one_dec ^ num_two_dec      # ^ is Python for XOR
    # print the answer to screen
    # log the answer to a file
    write_out(sys.argv[1], sys.argv[2], "XOR", answer, num_one_dec, num_two_dec)

main()
# to do
# implement rotate and shift

# done
# include binary equivalent
# print ascii
# add function to write out computation to a log file
# replicate for other booleans like AND, OR
# include binary display of both inputs in print_out