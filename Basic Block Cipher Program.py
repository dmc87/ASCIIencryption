# Darcy McIntyre, 10522336
# Created 27/03/2021
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
        ascii_cipher.append(int(bn, 2))
    ascii_cipher = ' '.join(map(str, ascii_cipher))
    return ascii_cipher

def block(bits, length):   # Make blocks to the length of the plaintext binary
    n = len(length)
    lst = [bits[index : index + n] for index in range(0, len(bits), n)]
    return lst

def diffusion(block):
    bit_list = []
    permutation = []
    bits = ''.join(block)
    for bit in bits:
        bit_list.append(bit)
        permutation = (bit_list[1:] + bit_list[:1])
        permutation = ''.join(permutation)
    return permutation

def confusion(pt, ks):  # This function turns the values of a list into ciphertext
    bits = ''.join(pt)
    bits = [bit for bit in bits]
    ciphertext = []
    counter = 0
    for bit in ks:               # Perform the binary xor below
        ciphertext.append(str((int(bit) + (int(bits[counter])))%2))
        counter = counter + 1
    ciphertext = ''.join(ciphertext)
    return ciphertext

def encrypt(block, keystream):
    x = diffusion(block)
    y = confusion(x, keystream)
    return y

def transform_key(keystream):
    bit_list = []
    transformation = []
    for bit in keystream:
        bit_list.append(bit)
        transformation = (bit_list[-1:] + bit_list[:-1])
    return transformation

def reverse_transform_key(keystream):
    bit_list = []
    transformation = []
    for bit in keystream:
        bit_list.append(bit)
        transformation = (bit_list[1:] + bit_list[:1])
    return transformation

def reverse_diffusion(block):
    bit_list = []
    permutation = []
    bits = ''.join(block)
    for bit in bits:
        bit_list.append(bit)
        permutation = (bit_list[-1:] + bit_list[:-1])
        permutation = ''.join(permutation)
    return permutation

def reverse_confusion(pt, ks):
    bits = ''.join(pt)
    bits = [bit for bit in bits]
    ciphertext = []
    counter = 0
    for bit in ks:               # Perform the binary xor below
        ciphertext.append(str((int(bit) - (int(bits[counter])))%2))
        counter = counter + 1
    ciphertext = ''.join(ciphertext)
    return ciphertext

def decrypt(block, keystream):
    y = reverse_confusion(block, keystream)
    y = reverse_diffusion(x)
    return y

      
while True:

    key = []
    cipher = []
    b1=[]
    b2=[]
    b3=[]
    b4=[]
    b5=[]
    b6=[]
    b7=[]
    
    # Print main menu
    print('Welcome to the Basic Block Cipher Program (BBCP)')
    print('Please select from the following options:')
    print('To encrypt a message, press 1')
    print('To decrypt a message, press 2')
    print('To decrypt the message that you encrypted in option 1, press 3')
    print('To exit, press any other character')

        # Enter something
    choice = (input('> '))

    # Encryption chosen
    if choice == '1':
        print('Welcome to the encryption function.')
        
        print('Please enter your ASCII value')
        text = input('> ')
        #text = 'Meet Alice next to the fridge in Building 18 at ECU.'
        
        print('\nPlaintext: ', text)
        print('\nBelow are your ASCII to binary values.\n')
        print(ascii_to_binary(text), '\n')
        print('Length of binary bits is:', len(ascii_x(text)), 'bits.\n')

        # Time to generate a key, and then the keystream
        print('Below, when you enter how long you would like your key to be,\nkeep in mind that the key will be duplicated to the length of the plaintext.\n')
        keylength = (input('how long would you like to make the binary key?: '))

        # Generate a list of bits for the key
        for i in range(1, int(keylength)+1):   
            x = (input('Enter a binary value: '))
            key.append(x)

        # Put plaintext binary into 7 lists (blocks), make keystream
        b = block(ascii_x(text), text)
        bs = len(b[0])
        kl = len(key)
        keystream = key * int(bs/kl)

        # This code legitimately works, it takes values from the front (1, 2, 3) and puts them at the back (4, 5, 6..n)
        y = bs - len(keystream) # Get the difference
        keysafe = keystream     # Put the keystream in a safe
        z = 0                   # Set a counter
        while y != 0:           # While there's a difference, grab values from the start of the list to pad out
            keysafe.append(keystream[z])  # Add numbers to the end of the list from the front of the list
            z = z + 1
            y = y - 1
        keystream = keysafe
        
        # Announce plaintext and keystream lengths     
        print('\nLength of keystream bits is:', len(keystream), 'bits')
        print('Block size:', bs , 'bits\n')

        # Set up blocks from block list
        b1 += [b[0]]
        b2 += [b[1]]
        b3 += [b[2]]
        b4 += [b[3]]
        b5 += [b[4]]
        b6 += [b[5]]
        b7 += [b[6]]

        print("The plaintext data undergoes diffusion, by converting the ASCII into 7-bit binary strings")
        print("The plaintext binary is then divided into 7 blocks.")
        print("The plaintext binary undergoes further diffusion by shifting bits within the block 1 space left.")
        print("After the diffusion, each block undergoes the confusion state,\nwhere the keystream is XOR'ed to the block (key addition).")
        print("After each block undergoes confusion, the keystream is transformed for the next round")
        print("of key addition by shifting all the bits in the keystream to the right.")
        print("This process is repeated 3 times, and the resultant blocks are added together to create the ciphertext.\n")

        print("\nPrinting a sample of a round of block encryption")
        print("\nPlaintext block 1: ")
        print(''.join(b1))
        print("\nDiffusion block 1: ")
        print(diffusion(b1))
        print("\nKeystream: ")
        print(''.join(map(str, keystream)))
        sample = (diffusion(b1))
        print("\nCiphertext transformation block 1: ")
        print(confusion(sample, keystream))
        print("\n\nCommencing 3 rounds of encryption.\n")

        # Round 1
        b1 = encrypt(b1, keystream)
        b2 = encrypt(b2, keystream)
        b3 = encrypt(b3, keystream)
        b4 = encrypt(b4, keystream)
        b5 = encrypt(b5, keystream)
        b6 = encrypt(b6, keystream)
        b7 = encrypt(b7, keystream)
        keystream = transform_key(keystream)

        # Round 2
        b1 = encrypt(b1, keystream)
        b2 = encrypt(b2, keystream)
        b3 = encrypt(b3, keystream)
        b4 = encrypt(b4, keystream)
        b5 = encrypt(b5, keystream)
        b6 = encrypt(b6, keystream)
        b7 = encrypt(b7, keystream)
        keystream = transform_key(keystream)

        # Round 3
        b1 = encrypt(b1, keystream)
        b2 = encrypt(b2, keystream)
        b3 = encrypt(b3, keystream)
        b4 = encrypt(b4, keystream)
        b5 = encrypt(b5, keystream)
        b6 = encrypt(b6, keystream)
        b7 = encrypt(b7, keystream)
        
        CipherText = b1+b2+b3+b4+b5+b6+b7
        print(ciphertext(group7(CipherText)))

        ctvar = ciphertext(group7(CipherText))
        print('\nIf you want to decrypt this message directly,\nselect option 3 from the main menu\nas the ciphertext has been pre-loaded for you.\n')
        print('-'*75,'\n')
        
        print('\n')


    elif choice == '2':
        print('Welcome to the decryption function.')
        
        print('Please enter your ciphertext value')
        text = input('> ')
        
        print('\nCiphertext: ')
        print(text)
        print('\nBelow are your ASCII to binary values.\n')
        print(ascii_to_binary(text), '\n')
        print('Length of binary bits is:', len(ascii_x(text)), 'bits.\n')

        # Time to generate a key, and then the keystream
        print('Below, when you enter how long you would like your key to be,\nkeep in mind that the key will be duplicated to the length of the ciphertext.\n')
        keylength = (input('how long would you like to make the binary key?: '))

        # Generate a list of bits for the key
        for i in range(1, int(keylength)+1):   
            x = (input('Enter a binary value: '))
            key.append(x)

        # Put plaintext binary into 7 lists (blocks), make keystream
        b = block(ascii_x(text), text)
        bs = len(b[0])
        kl = len(key)
        keystream = key * int(bs/kl)

        # This code legitimately works, it takes values from the front (1, 2, 3) and puts them at the back (4, 5, 6..n)
        y = bs - len(keystream) # Get the difference
        keysafe = keystream     # Put the keystream in a safe
        z = 0                   # Set a counter
        while y != 0:           # While there's a difference, grab values from the start of the list to pad out
                  keysafe.append(keystream[z])  # Add numbers to the end of the list from the front of the list
                  z = z + 1
                  y = y - 1
        keystream = keysafe
        
        # Announce plaintext and keystream lengths     
        print('\nLength of keystream bits is:', len(keystream), 'bits')
        print('Block size:', bs , 'bits\n')

        # Set up blocks from block list
        b1 += [b[0]]
        b2 += [b[1]]
        b3 += [b[2]]
        b4 += [b[3]]
        b5 += [b[4]]
        b6 += [b[5]]
        b7 += [b[6]]

        print("The decryption process is the inverse of the encryption process.")
        print("First, the original keystream must be transformed twice. Then the ciphertext undergoes reverse confusion:")
        print('\nPlaintext bit (Xi) = ciphertext bit (Yi) - keystream bit (Si) mod(2)\n')
        print("After the XOR is done, the cipher text needs to do reverse diffusion, by shifting bits right by 1.")
        print("The keystream must then be reverse transformed, shifting bits left by 1.")
        print("Then the reverse confusion is applied, reverse diffusion, and reverse key transformation 2 more times,")
        print("Until the ciphertext is decrypted into plaintext.")

        print('\n\nRunning 3 rounds of decryption')

        # Prepare keystream for decryption
        keystream = transform_key(keystream)
        keystream = transform_key(keystream)

        # 3 rounds of decryption per block (reverse confusion, reverse diffusion, reverse transform key)
        b1 = (reverse_diffusion(reverse_confusion(b1, keystream)))
        b2 = (reverse_diffusion(reverse_confusion(b2, keystream)))
        b3 = (reverse_diffusion(reverse_confusion(b3, keystream)))
        b4 = (reverse_diffusion(reverse_confusion(b4, keystream)))
        b5 = (reverse_diffusion(reverse_confusion(b5, keystream)))
        b6 = (reverse_diffusion(reverse_confusion(b6, keystream)))
        b7 = (reverse_diffusion(reverse_confusion(b7, keystream)))        
        keystream = reverse_transform_key(keystream)

        b1 = (reverse_diffusion(reverse_confusion(b1, keystream)))
        b2 = (reverse_diffusion(reverse_confusion(b2, keystream)))
        b3 = (reverse_diffusion(reverse_confusion(b3, keystream)))
        b4 = (reverse_diffusion(reverse_confusion(b4, keystream)))
        b5 = (reverse_diffusion(reverse_confusion(b5, keystream)))
        b6 = (reverse_diffusion(reverse_confusion(b6, keystream)))
        b7 = (reverse_diffusion(reverse_confusion(b7, keystream)))        
        keystream = reverse_transform_key(keystream)

        b1 = (reverse_diffusion(reverse_confusion(b1, keystream)))
        b2 = (reverse_diffusion(reverse_confusion(b2, keystream)))
        b3 = (reverse_diffusion(reverse_confusion(b3, keystream)))
        b4 = (reverse_diffusion(reverse_confusion(b4, keystream)))
        b5 = (reverse_diffusion(reverse_confusion(b5, keystream)))
        b6 = (reverse_diffusion(reverse_confusion(b6, keystream)))
        b7 = (reverse_diffusion(reverse_confusion(b7, keystream)))        
             
        CipherText = b1+b2+b3+b4+b5+b6+b7
        print('Your decrypted plaintext is:\n')
        print(ciphertext(group7(CipherText)))

        print('-'*75,'\n')
        
        print('\n')

    elif choice == '3':
        print('Welcome to the decryption function.')
        print('\nThis function will decrypt the message you just encrypted,\nassuming you have the right key.')
        
        #print('Please enter your ciphertext value')
        #text = input('> ')
        #text = 'Meet Alice next to the fridge in Building 18 at ECU.'
        text = ctvar
        
        print('\nCiphertext: ')
        print(text)
        print('\nBelow are your ASCII to binary values.\n')
        print(ascii_to_binary(text), '\n')
        print('Length of binary bits is:', len(ascii_x(text)), 'bits.\n')

        # Time to generate a key, and then the keystream
        print('Below, when you enter how long you would like your key to be,\nkeep in mind that the key will be duplicated to the length of the ciphertext.\n')
        keylength = (input('how long would you like to make the binary key?: '))

        # Generate a list of bits for the key
        for i in range(1, int(keylength)+1):   
            x = (input('Enter a binary value: '))
            key.append(x)

        # Put plaintext binary into 7 lists (blocks), make keystream
        b = block(ascii_x(text), text)
        bs = len(b[0])
        kl = len(key)
        keystream = key * int(bs/kl)

        # This code legitimately works, it takes values from the front (1, 2, 3) and puts them at the back (4, 5, 6..n)
        y = bs - len(keystream) # Get the difference
        keysafe = keystream     # Put the keystream in a safe
        z = 0                   # Set a counter
        while y != 0:           # While there's a difference, grab values from the start of the list to pad out
                  keysafe.append(keystream[z])  # Add numbers to the end of the list from the front of the list
                  z = z + 1
                  y = y - 1
        keystream = keysafe
        
        # Announce plaintext and keystream lengths     
        print('\nLength of keystream bits is:', len(keystream), 'bits')
        print('Block size:', bs , 'bits\n')

        # Set up blocks from block list
        b1 += [b[0]]
        b2 += [b[1]]
        b3 += [b[2]]
        b4 += [b[3]]
        b5 += [b[4]]
        b6 += [b[5]]
        b7 += [b[6]]

        print("The decryption process is the inverse of the encryption process.")
        print("First, the original keystream must be transformed twice. Then the ciphertext undergoes reverse confusion:")
        print('\nPlaintext bit (Xi) = ciphertext bit (Yi) - keystream bit (Si) mod(2)\n')
        print("After the XOR is done, the cipher text needs to do reverse diffusion, by shifting bits right by 1.")
        print("The keystream must then be reverse transformed, shifting bits left by 1.")
        print("Then the reverse confusion is applied, reverse diffusion, and reverse key transformation 2 more times,")
        print("Until the ciphertext is decrypted into plaintext.")

        print("Example: previous encryption\n")
        print(ctvar)
        print('\n\nRunning 3 rounds of decryption')

        # Prepare keystream for decryption
        keystream = transform_key(keystream)
        keystream = transform_key(keystream)

        # 3 rounds of decryption per block (reverse confusion, reverse diffusion, reverse transform key)
        b1 = (reverse_diffusion(reverse_confusion(b1, keystream)))
        b2 = (reverse_diffusion(reverse_confusion(b2, keystream)))
        b3 = (reverse_diffusion(reverse_confusion(b3, keystream)))
        b4 = (reverse_diffusion(reverse_confusion(b4, keystream)))
        b5 = (reverse_diffusion(reverse_confusion(b5, keystream)))
        b6 = (reverse_diffusion(reverse_confusion(b6, keystream)))
        b7 = (reverse_diffusion(reverse_confusion(b7, keystream)))        
        keystream = reverse_transform_key(keystream)

        b1 = (reverse_diffusion(reverse_confusion(b1, keystream)))
        b2 = (reverse_diffusion(reverse_confusion(b2, keystream)))
        b3 = (reverse_diffusion(reverse_confusion(b3, keystream)))
        b4 = (reverse_diffusion(reverse_confusion(b4, keystream)))
        b5 = (reverse_diffusion(reverse_confusion(b5, keystream)))
        b6 = (reverse_diffusion(reverse_confusion(b6, keystream)))
        b7 = (reverse_diffusion(reverse_confusion(b7, keystream)))        
        keystream = reverse_transform_key(keystream)

        b1 = (reverse_diffusion(reverse_confusion(b1, keystream)))
        b2 = (reverse_diffusion(reverse_confusion(b2, keystream)))
        b3 = (reverse_diffusion(reverse_confusion(b3, keystream)))
        b4 = (reverse_diffusion(reverse_confusion(b4, keystream)))
        b5 = (reverse_diffusion(reverse_confusion(b5, keystream)))
        b6 = (reverse_diffusion(reverse_confusion(b6, keystream)))
        b7 = (reverse_diffusion(reverse_confusion(b7, keystream)))        
             
        CipherText = b1+b2+b3+b4+b5+b6+b7
        print('Your decrypted plaintext is:\n')
        print(ciphertext(group7(CipherText)))

        print('-'*75,'\n')
        
        print('\n')       
            
        
    else:
        break
