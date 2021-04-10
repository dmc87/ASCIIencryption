# Darcy McIntyre, 10522336
# Created 15/03/2021
# Meet Alice next to the fridge in Building 18 at ECU.
# 1100111

def ascii_to_binary(plaintext):     # This function converts text to binary via decimal
    value = ''                      # and spits it out in 7 bit strings for easy reading
    for character in plaintext:
        binary = ("{0:07b}".format(ord(character)))
        value = value + binary + ' '
    value = value.rstrip()
    return value

def ascii_x(plaintext):             # This function converts text to binary via decimal
    value = ''                      # and spits it out in one whole string 
    for character in plaintext:
        binary = ("{0:07b}".format(ord(character)))
        value = value + binary 
    return value

def bin_list(value):                # Take the binary string and put it in a list to match the keystream list
    return ([char for char in value])

def encrypt(pt, ks):                    # This function turns the values of a list into ciphertext
    ciphertext = []
    counter = 0
    for bit in ks:               # Perform the binary xor below
        ciphertext.append(str((int(bit) + (int(pt[counter])))%2))
        counter = counter + 1
    ciphertext = ''.join(ciphertext)
    return ciphertext

def decrypt(pt, ks):                    # This function turns the values of a list into plaintext
    ciphertext = []
    counter = 0
    for bit in ks:               # Perform the binary xor below
        ciphertext.append(str((int(bit) - (int(pt[counter])))%2))
        counter = counter + 1
    ciphertext = ''.join(ciphertext)
    return ciphertext

def group7(value):                  # This function groups strings together by 7 to make ascii bits
    n = 7
    lst = [value[index : index + n] for index in range(0, len(value), n)]
    return lst

def ciphertext(blist):              # This function grabs the grouped binary in the list and turns them into an ascii string
    ascii_cipher = []
    for bn in blist:                                                                                              
        ascii_cipher.append(chr(int(bn, 2)))
    ascii_cipher = ''.join(map(str, ascii_cipher))
    return ascii_cipher

def dec_cipher(blist):              # This function grabs the grouped binary in the list and turns them into decimal
    ascii_cipher = []
    for bn in blist:
        #ascii_cipher.append(bn)
        ascii_cipher.append(int(bn, 2))
    ascii_cipher = ' '.join(map(str, ascii_cipher))
    return ascii_cipher

    

while True:

    #Declaring some variables
    choice = ''
    text = ''
    key = []
    keystream = ''
    cipher_binary = []
    cipher_dec = []
    cipher = []
    bin_pt_list = []
     
    # Print main menu
    print('Welcome to my simple ASCII XOR stream cipher program')
    print('Please select from the following options:')
    print('To encrypt, press 1\nTo decrypt, press 2')
    print('To decrypt a cipher from option 1, press 3')
    print('To exit, press any other character')

    # Enter something
    choice = (input('> '))

    # Encryption chosen
    if choice == '1':
          print('Welcome to the encryption function.')
          print('Please enter your ASCII value')
          text = input('> ')

          print('\nBelow are your ASCII to binary values.\n')
          #print('You can check this is correct at:')
          #print('https://www.rapidtables.com/convert/number/binary-to-ascii.html\n')
          print(ascii_to_binary(text), '\n')
          print('Length of binary bits is:', len(ascii_x(text)), 'bits.\n')


          # Time to generate a key, and then the keystream
          print('Below, when you enter how long you would like your key to be,\nkeep in mind that the key will be duplicated to the length of the plaintext.\n')
          keylength = (input('how long would you like to make the binary key?: '))

          # Generate a list of bits for the key
          for i in range(1, int(keylength)+1):   
              x = (input('Enter a binary value: '))
              key.append(x)
          keystream = key * (int((int(len(ascii_x(text)))) / (int(len(key)))))  # This is also important for when we get a keystream < plaintext value
                                                                                # This will always leave it with less bits, not more
          # Announce plaintext and keystream lengths
          print('\nLength of plaintext bits is:', len(ascii_x(text)), 'bits')      
          print('Length of keystream bits is:', len(keystream), 'bits\n')

          # Here I check that the keystream and binary bits are the same length
          if len(keystream) == len(ascii_x(text)):
              print('The length of the keystream is equal to the length of the plaintext,\nready to compute ciphertext...')
              print('\nCiphertext bit (Yi) = plaintext bit (Xi) + keystream bit (Si) mod(2)\n')
              print('Computing...\n')
            
              # Turn each character in of the ASCII text into a binary bit in a list 
              bin_pt_list = bin_list(ascii_x(text))
              # Encrypt the binary ascii plaintext via XOR with keystream, group the result into 7 bits each
              cipher = encrypt(bin_pt_list, keystream)
              cipher = (group7(cipher))
              


              print('\nCiphertext binary code:')
              print(' '.join(map(str, cipher)))              # Print ciphertext in binary
              print('\nCiphertext binary to decimal conversion:')
              print(dec_cipher(cipher))     # Print ciphertext in decimal
              print('\nCiphertext ASCII code:')
              print(str(ciphertext(cipher)))
              ctvar = ciphertext(cipher)
              print('\nIf you would like to decrypt this ciphertext,\nplease select option 3 from the main menu.\n')
              print('-'*75,'\n')

          else:
              print('Looks like the length of the keystream\ndoes not match the length of the plaintext,\ncorrecting...\n')
              print('Taking values from the start of the keystream and adding them to the end')
              print('e.g. 1 in the list gets copied to the end, then 2 etc\nuntil we have padded the keystream to the length of the plaintext')

              # This code legitimately works, it takes values from the front (1, 2, 3) and puts them at the back (4, 5, 6..n)
              y = len(ascii_x(text)) - len(keystream)                             # Get the difference
              keysafe = keystream                                                 # Put the keystream in a safe
              z = 0                                                               # Set a counter
              while y != 0:                                                       # While there's a difference, grab values from the start of the list to pad out
                  keysafe.append(keystream[z])                                    # Add numbers to the end of the list from the front of the list
                  z = z + 1
                  y = y - 1
              print('\nDone. Length of keystream bits is:', len(keysafe), 'bits long,\nready to compute ciphertext...\n')
              print('\nCiphertext bit (Yi) = plaintext bit (Xi) + keystream bit (Si) mod(2)\n')
              print('Computing...\n')
            
              # Turn each character in of the ASCII text into a binary bit in a list 
              bin_pt_list = bin_list(ascii_x(text))
              # Encrypt the binary ascii plaintext via XOR with keystream, group the result into 7 bits each
              cipher = encrypt(bin_pt_list, keystream)
              cipher = (group7(cipher))
              


              print('\nCiphertext binary code:')
              print(' '.join(map(str, cipher)))              # Print ciphertext in binary
              print('\nCiphertext binary to decimal conversion:')
              print(dec_cipher(cipher))     # Print ciphertext in decimal
              print('\nCiphertext ASCII code:')
              print(str(ciphertext(cipher)) + str('<--- Copy from before the arrow into the decryptor\n'))
              print('-'*75,'\n')
                   
    elif choice == '2':
        print('Welcome to the decryption function')
        print('Please enter your ASCII value')
        text = input('> ')

        print('\nBelow are your ASCII to binary values.\n')
        #print('You can check this is correct at:')
        #print('https://www.rapidtables.com/convert/number/binary-to-ascii.html\n')
        print(ascii_to_binary(text), '\n')
        print('Length of binary bits is:', len(ascii_x(text)), 'bits.\n')

        # Time to generate a key, and then the keystream
        print('Below, when you enter how long your key is,\nkeep in mind that the key will be duplicated to the length of the ciphertext.\n')
        keylength = (input('how long is your binary key?: '))

        # Generate a list of bits for the key
        for i in range(1, int(keylength)+1):
            x = (input('Enter a binary value: '))
            key.append(x)
        keystream = key * (int((int(len(ascii_x(text)))) / (int(len(key)))))

        # Announce plaintext and keystream lengths
        print('\nLength of ciphertext bits is:', len(ascii_x(text)), 'bits')      
        print('Length of keystream bits is:', len(keystream), 'bits\n')

        # Here I check that the keystream and binary bits are the same length
        if len(keystream) == len(ascii_x(text)):
            print('The length of the keystream is equal to the length of the plaintext,\nready to compute plaintext...')
            print('\nPlaintext bit (Xi) = ciphertext bit (Yi) - keystream bit (Si) mod(2)\n')
            print('Computing...\n')

            # Turn each character in of the ASCII text into a binary bit in a list 
            bin_pt_list = bin_list(ascii_x(text))
            # decrypt the binary ascii plaintext via XOR with keystream, group the result into 7 bits each
            cipher = decrypt(bin_pt_list, keystream)
            cipher = (group7(cipher))
           
            print('\nPlaintext binary code:')
            print(' '.join(map(str, cipher)))              # Print plaintext in binary
            print('\nPlaintext binary to decimal conversion:')
            print(dec_cipher(cipher))     # Print plaintext in decimal
            print('\nPlaintext ASCII code:')
            print(ciphertext(cipher), '\n')
            print('-'*75,'\n')

        else:
            print('Looks like the length of the keystream\ndoes not match the length of the ciphertext,\ncorrecting...\n')
            print('Taking values from the start of the keystream and adding them to the end')
            print('e.g. 1 in the list gets copied to the end, then 2 etc\nuntil we have padded the keystream to the length of the ciphertext')

            # This code legitimately works, it takes values from the front (1, 2, 3) and puts them at the back (4, 5, 6..n)
            y = len(ascii_x(text)) - len(keystream)                             # Get the difference
            keysafe = keystream                                                 # Put the keystream in a safe
            z = 0                                                               # Set a counter
            while y != 0:                                                       # While there's a difference, grab values from the start of the list to pad out
                keysafe.append(keystream[z])                                    # Add numbers to the end of the list from the front of the list
                z = z + 1
                y = y - 1
            print('\nDone. Length of keystream bits is:', len(keysafe), 'bits long,\nready to decrypt plaintext...\n')
            print('\nPlaintext bit (Xi) = Ciphertext bit (Yi) - keystream bit (Si) mod(2)\n')
            print('Computing...\n')
            
            # Turn each character in of the ASCII text into a binary bit in a list 
            bin_pt_list = bin_list(ascii_x(text))
            # decrypt the binary ascii ciphertext via XOR with keystream, group the result into 7 bits each
            cipher = decrypt(bin_pt_list, keystream)
            cipher = (group7(cipher))
            print('\nPlaintext binary code:')
            print(' '.join(map(str, cipher)))              # Print plaintext in binary
            print('\nPlaintext binary to decimal conversion:')
            print(dec_cipher(cipher))     # Print plaintext in decimal
            print('\nPlaintext ASCII code:')
            print(ciphertext(cipher), '\n')
            print('-'*75,'\n')

    elif choice == '3':
        print('Welcome to the decryption function')
        print('Your ciphertext from option 1 has been copied into this funciton.')
        text = ctvar
        print('\nBelow are your ASCII to binary values.\n')
        #print('You can check this is correct at:')
        #print('https://www.rapidtables.com/convert/number/binary-to-ascii.html\n')
        print(ascii_to_binary(text), '\n')
        print('Length of binary bits is:', len(ascii_x(text)), 'bits.\n')

        # Time to generate a key, and then the keystream
        print('Below, when you enter how long your key is,\nkeep in mind that the key will be duplicated to the length of the ciphertext.\n')
        keylength = (input('how long is your binary key?: '))

        # Generate a list of bits for the key
        for i in range(1, int(keylength)+1):
            x = (input('Enter a binary value: '))
            key.append(x)
        keystream = key * (int((int(len(ascii_x(text)))) / (int(len(key)))))

        # Announce plaintext and keystream lengths
        print('\nLength of ciphertext bits is:', len(ascii_x(text)), 'bits')      
        print('Length of keystream bits is:', len(keystream), 'bits\n')

        # Here I check that the keystream and binary bits are the same length
        if len(keystream) == len(ascii_x(text)):
            print('The length of the keystream is equal to the length of the plaintext,\nready to compute plaintext...')
            print('\nPlaintext bit (Xi) = ciphertext bit (Yi) - keystream bit (Si) mod(2)\n')
            print('Computing...\n')

            # Turn each character in of the ASCII text into a binary bit in a list 
            bin_pt_list = bin_list(ascii_x(text))
            # decrypt the binary ascii plaintext via XOR with keystream, group the result into 7 bits each
            cipher = decrypt(bin_pt_list, keystream)
            cipher = (group7(cipher))
           
            print('\nPlaintext binary code:')
            print(' '.join(map(str, cipher)))              # Print plaintext in binary
            print('\nPlaintext binary to decimal conversion:')
            print(dec_cipher(cipher))     # Print plaintext in decimal
            print('\nPlaintext ASCII code:')
            print(ciphertext(cipher), '\n')
            print('-'*75,'\n')

        else:
            print('Looks like the length of the keystream\ndoes not match the length of the ciphertext,\ncorrecting...\n')
            print('Taking values from the start of the keystream and adding them to the end')
            print('e.g. 1 in the list gets copied to the end, then 2 etc\nuntil we have padded the keystream to the length of the ciphertext')

            # This code legitimately works, it takes values from the front (1, 2, 3) and puts them at the back (4, 5, 6..n)
            y = len(ascii_x(text)) - len(keystream)                             # Get the difference
            keysafe = keystream                                                 # Put the keystream in a safe
            z = 0                                                               # Set a counter
            while y != 0:                                                       # While there's a difference, grab values from the start of the list to pad out
                keysafe.append(keystream[z])                                    # Add numbers to the end of the list from the front of the list
                z = z + 1
                y = y - 1
            print('\nDone. Length of keystream bits is:', len(keysafe), 'bits long,\nready to decrypt plaintext...\n')
            print('\nPlaintext bit (Xi) = Ciphertext bit (Yi) - keystream bit (Si) mod(2)\n')
            print('Computing...\n')
            
            # Turn each character in of the ASCII text into a binary bit in a list 
            bin_pt_list = bin_list(ascii_x(text))
            # decrypt the binary ascii ciphertext via XOR with keystream, group the result into 7 bits each
            cipher = decrypt(bin_pt_list, keystream)
            cipher = (group7(cipher))
            print('\nPlaintext binary code:')
            print(' '.join(map(str, cipher)))              # Print plaintext in binary
            print('\nPlaintext binary to decimal conversion:')
            print(dec_cipher(cipher))     # Print plaintext in decimal
            print('\nPlaintext ASCII code:')
            print(ciphertext(cipher), '\n')
            print('-'*75,'\n')

    else:
        break
