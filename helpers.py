##############
# helpers.py #
###############################################
# provide functions common to boolean scripts #
###############################################


def parse_input(input_val):
    # Generic number parsing routine
    # Accept a single input
    # Check to see if it is hex
    # If it is then convert and return
    # the decimal equivalent
    # If not hex then return original
    if input_val[0] == "0":
        if (input_val[1]) == "x":
    #   We have a "0x" format hex number
            input_val = input_val.split("0x")
            input_out = int((input_val[1]), 16)
    elif input_val[-1] == "h":
    #   We have a "h" format hex number
        input_val = input_val.split("h")
        input_out = int((input_val[0]), 16)
    else:
    #   We have a decimal number
        input_out = int(input_val)
    return (input_out)


def write_out(arg1, arg2, arg3, result, arg1_dec, arg2_dec):
    # Generic output routine
    # Accept several inputs
    #  two hex values (arg1, arg2)
    #  the function applied to them (arg3)
    #  the result of the computation (result)
    #  two decimal values (arg1_dec, arg2_dec)
    # Log and print the result in different formats
    # Return nothing

    # write to file
    f = open("bitwise_summary.csv", "a+")
    f.write (str(arg1) + ", " + str(arg3) + ", " + str(arg2) + ", " + str(result) + "\n")
    f.close()

    f = open("bitwise_workings.log", "a+")
    f.write("--------====NEW QUERY BELOW====--------" * 4)
    f.write("\n")
    f.write("Query  -> " + arg1 + " " + arg3 + " " + arg2 + "\n")
    if result < 256:
        try:
            f.write("Answer -> Hex - " + str(hex(result) + "\t| Decimal - " + str(result)) + "\t| Binary - " + str(bin(result)) + "\t| ASCII - " + chr(result) + "\n")
        except:
            f.write("Answer -> Hex - " + str(hex(result)) + "\t| Decimal - " + str(result) + "\t| Binary - " + str(bin(result)) + "\t| ASCII - unprintable.\n")
    else:
         f.write("Answer -> Hex - " + str(hex(result)) + "\t| Decimal - " + str(result)  + "\t| Binary - " + str(bin(result)) + "\t| ASCII - out of range.\n")
    f.write("\n" * 2)
    f.write("{:>34}".format(bin(int(arg1_dec))) + "\n")
    f.write("{:>34}".format(bin(int(arg2_dec))) + "\n")
    dash = 34 - len(arg3)
    f.write(arg3 + ("-" * dash) + "\n")
    f.write("{:>34}".format(bin(int(result))) + "\n")
    f.write("\n")
    f.close()

    # print to screen
    print ()
    print ("{:>34}".format(bin(int(arg1_dec))))
    print ("{:>34}".format(bin(int(arg2_dec))))
    dash=34-len(arg3)
    print (arg3 + ("-" * dash))
    print ("{:>34}".format(bin(int(result))))
    print()
    if result <256:
        try:
            print ("Decimal -", result, "\t|\t Hex -", hex(result), "\t|\t Binary -", bin(result), "\t|\t ASCII -", chr(result))
        except:
            print("Decimal -", result, "\t|\t Hex -", hex(result), "\t|\t Binary -", bin(result), "\t|\t ASCII - unprintable.")
    else:
        print ("Decimal -", result, "\t|\t Hex -", hex(result), "\t|\t Binary -", bin(result), "\t|\t ASCII - out of range.")