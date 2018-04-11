######
# OR #
######

import sys
from helpers import *

def main():
    # take two inputs and parse them
    num_one_dec = parse_input(sys.argv[1])
    num_two_dec = parse_input(sys.argv[2])
    # compute the answer
    answer = num_one_dec | num_two_dec      # | is Python for OR
    # print the answer to screen
    # log the answer to a file
    write_out(sys.argv[1], sys.argv[2], "OR", answer, num_one_dec, num_two_dec)

main()