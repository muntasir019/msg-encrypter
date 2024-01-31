import random

def encrypt():
# ask the user to encrypt or decrypt message
    inp = input("\n\nYOU CAN ENCRYPT OR DECRYPT MESSAGE USING THIS CODE\n[+] TO ENCRYPT / [-] TO DECRYPT\n-->")


    # to encrypt message
    if "+" in inp or "ENCRYPT" in inp:

        # random words list to append to the message 
        # you can change it as you want [!]Remember to keep them 3 letter long or you have to change the decrypt function
        rndm = ["hsd","fyj","dht","aef","rsh","yik","yuo","wfa","uty","wtf","ndf","qar","rwe","tjh","kgo","jrf","zww","eqr"]

        Encrypted_list = []
        msg = input("[+] ENTER THE MESSAGE YOU WANNA ENCRYPT HERE: ")
        words = msg.split(" ")

        for word in words:
            Encrypted_word = random.choice(rndm) + word[1:] + word[0] + random.choice(rndm)
            Encrypted_list.append(Encrypted_word)

        Encrypted_msg = " ".join(Encrypted_list)
        print("THE ENCRYPTED MESSAGE IS: " + Encrypted_msg)


    # to decrypt message
    elif "-" in inp or "decrypt" in inp:
        msg = []
        usr_inp = input("[+] ENTER THE ENCRYPTED MESSAGE YOU WANNA DECRYPT: ")
        words = usr_inp.split(" ")
        for word in words:
            main_word = word[3:-3]
            msg_word = main_word[-1] + main_word[:-1]
            msg.append(msg_word)

        output = " ".join(msg)
        print("THE MESSAGE IS: " + output)

    # if encrypt or decrypt neither in input(inp)
    else:
        print("[!] YOU HAVE TO SPECIFY WHAT YOU WANT TO DO [!]")

    # to ask the user to keep going or close
    close = input("""
    press "r" and enter to run again
                  OR
           Enter to close.
                  """)
    if "r" in close or "R" in close:
        encrypt()
    else:
        pass

encrypt()
