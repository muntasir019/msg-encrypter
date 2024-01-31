# function to convert string or integer to binary
def to_bin(input_data):
    if isinstance(input_data, str):
        # Convert each character's ASCII value to binary
        binary_result = ' '.join(format(ord(char), '08b') for char in input_data)
    elif isinstance(input_data, int):
        # Convert the integer to binary
        binary_result = bin(input_data)[2:]
    else:
        raise ValueError("Input must be a string or an integer")

    return binary_result


# function to convert binary to string or integer
def from_bin(binary_data):
    if " " in binary_data:
        # Convert binary to string by grouping 8 bits and converting to ASCII
        result = ''.join([chr(int(binary, 2)) for binary in binary_data.split(' ')])
    else:
        # Convert binary to integer
        result = int(binary_data, 2)
    return result


if __name__ == "__main__":

    def converter():
        # user input to verify what he/she wants
        usr_inp = input("\n\nCONVERT NUMBER OR TEXT TO BINARY AND VICE-VERSA\n\n[+]TO CONVERT IN BINARY [-]TO CONVERT FROM BINARY :")

        if "+" in usr_inp:
            inp = input("[+] ENTER THE MESSAGE HERE :")
            try:
                dynamic_inp = int(inp)
            except:
                dynamic_inp = inp

            outp = to_bin(dynamic_inp)
            print(outp)

        elif "-" in usr_inp:
            bin_msg = input("[-] WRITE THE BINARY MESSAGE HERE:")
            converted_msg = from_bin(bin_msg)
            print(converted_msg)

        else:
            print("\n!! YOU MUST DEFINE WHAT YOU WANT !!\n")
            converter()

        ext = input("""
        press "r" to run again
                 OR
        press enter to exit...
                 """)

        if ext == "":
            pass
        elif ext == "r":
            converter()
    converter()
    