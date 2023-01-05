# Sovannrithyreach Kim 11/11/2021 00:07

# Hex to binary conversion
from pip._vendor.distlib.compat import raw_input

C_Red = '\033[31m'
C_Blue_HL = '\033[7m'
C_Purp = '\033[95m'
C_Green = '\033[92m'
C_Yellow = '\033[33m'
C_Blinking = '\033[5m'
C_Underline = '\033[4m'
C_End = '\033[0m'

def ascii2hex(s):
    output = s.encode('utf-8').hex()
    return output


def hex2bin(s):
    b = format(int(s, 16), '064b')
    return b


# Binary to hexadecimal conversion

def bin2hex(s):
    hex = "{:012x}".format(int(s, 2), "x")
    return hex.upper()


# Binary to decimal conversion
def bin2dec(bin):
    return int(bin, 2)


# Decimal to binary conversion
def dec2bin(num):
    res = bin(num).replace("0b", "")
    if (len(res) % 4 != 0):
        div = len(res) / 4
        div = int(div)
        counter = (4 * (div + 1)) - len(res)
        for i in range(0, counter):
            res = '0' + res
    return res


# Permute function to rearrange the bits
def permute(k, arr, n):
    permutation = ""
    for i in range(0, n):
        permutation = permutation + k[arr[i] - 1]
    return permutation


# shifting the bits towards left by nth shifts
def shift_left(k, nth_shifts):
    s = ""
    for i in range(nth_shifts):
        for j in range(1, len(k)):
            s = s + k[j]
        s = s + k[0]
        k = s
        s = ""
    return k


# XOR Calculation
def xor(a, b):
    ans = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            ans = ans + "0"
        else:
            ans = ans + "1"
    return ans


def encryption(pt, rkb, rkh):
    # Converting the plaintext into BIN
    plaintext_bin = hex2bin(pt)
    plaintext = permute(plaintext_bin, ip, 64)
    left_text = plaintext[0:32]
    right_text = plaintext[32:64]

    print(C_Underline + C_Yellow + "FEISTEL CIPHER STAGE" + C_End)

    for i in range(0, 16):
        expanded_right = permute(right_text, expanding_permute, 48)


        # We then need to XOR the expanded right side with Key[i]
        xor_pt_right = xor(expanded_right, rkb[i])

        print(f'Before sbox after XOR with right round {i+1}', xor_pt_right, bin2hex(xor_pt_right))

        sbox_str = ""
        # print(C_Purp + "S Box" + C_End)
        for bits in range(0, 8):
            row = bin2dec(xor_pt_right[bits * 6] + xor_pt_right[bits * 6 + 5])
            col = bin2dec(xor_pt_right[bits * 6 + 1] + xor_pt_right[bits * 6 + 2] + xor_pt_right[bits * 6 + 3] + xor_pt_right[bits * 6 + 4])
            val = s_box[bits][row][col]
            sbox_str = sbox_str + dec2bin(val)

        sbox_str = permute(sbox_str, per, 32)

        # We then need to the left to the sbox string
        result = xor(left_text, sbox_str)
        print(f'After xor with left part round {i+1}', result, bin2hex(result)[4::])
        left_text = result

        # To swap the last two bits
        if (i != 15):
            left_text, right_text = right_text, left_text
        print("Round", i + 1, " ", bin2hex(left_text), " ", bin2hex(right_text), " ", rkh[i])
        print("")

    # Combining the strings
    combine = left_text + right_text

    # Final perm to get the final rearrangement of the bits
    cipher_text = permute(combine, final_perm, 64)
    cipher_text = bin2hex(cipher_text)
    return cipher_text


# PC-1 Table for key manipulation
pc1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

# PC-2 Table for key compression
pc2 = [14, 17, 11, 24, 1, 5,
       3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8,
       16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53,
       46, 42, 50, 36, 29, 32]

# The shifting table for the keys
shift_table = [1, 1, 2, 2,
               2, 2, 2, 2,
               1, 2, 2, 2,
               2, 2, 2, 1]

# The initial permutation table to be used for plaintext
ip = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# Bit expansion for R0 from 32 to 48 bits
expanding_permute = [32, 1, 2, 3, 4, 5, 4, 5,
                     6, 7, 8, 9, 8, 9, 10, 11,
                     12, 13, 12, 13, 14, 15, 16, 17,
                     16, 17, 18, 19, 20, 21, 20, 21,
                     22, 23, 24, 25, 24, 25, 26, 27,
                     28, 29, 28, 29, 30, 31, 32, 1]

# SBox to be used in s-box function
s_box = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
          [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
          [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

         [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
          [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
          [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
          [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

         [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
          [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
          [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
          [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

         [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
          [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
          [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
          [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

         [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
          [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
          [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
          [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

         [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
          [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
          [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
          [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

         [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
          [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
          [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
          [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

         [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
          [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
          [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
          [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

# Straight Permutation Table
per = [16, 7, 20, 21,
       29, 12, 28, 17,
       1, 15, 23, 26,
       5, 18, 31, 10,
       2, 8, 24, 14,
       32, 27, 3, 9,
       19, 13, 30, 6,
       22, 11, 4, 25]

# Final Permutation Table
final_perm = [40, 8, 48, 16, 56, 24, 64, 32,
              39, 7, 47, 15, 55, 23, 63, 31,
              38, 6, 46, 14, 54, 22, 62, 30,
              37, 5, 45, 13, 53, 21, 61, 29,
              36, 4, 44, 12, 52, 20, 60, 28,
              35, 3, 43, 11, 51, 19, 59, 27,
              34, 2, 42, 10, 50, 18, 58, 26,
              33, 1, 41, 9, 49, 17, 57, 25]

"""
plaintext = "0123456789ABCDEF"
key1 = "133457799BBCDFF1"
hkey = format(int(key1, 16), '064b')
hkey = [int(i) for element in hkey for i in element]
print(hkey)
print(hex2bin(key1))
"""

ans = True
while ans:
    print("        " + C_Underline + C_Green + "Main Menu" + C_End,
          """
    1. DES Encryption
    2. DES Decryption
    3. ASCII Encryption
    4. ASCII Decryption
    5. End Program
    """)
    ans = raw_input("What would you like to do? ")
    if ans == "1":

        textInput = input("Please enter your text in lowercase: ")
        key = input("Please input 16 bit keys, numbering from 0 to F: ")

        if len(key) > 16:
            print("Key length is : ", len(key))
            print("Please input key again, your key is more than 16 bits.")
            key = input("Please input 16 bit keys, numbering from 0 to F: ")

        print("")
        print(C_Purp + "Plaintext: " + C_End, hex2bin(textInput), textInput)
        print(C_Purp + "Key:" + C_End, hex2bin(key), key)
        print("")

        # first we need to convert the key from HEX into BIN by using the function HEX2BIN

        key = hex2bin(key)

        # We then need to pick 56 bits from the 64 bits key we had earlier

        key = permute(key, pc1, 56)

        # Splitting the keys into 2 halves
        left = key[0:28]
        right = key[28:56]

        roundkey_bin = rkb = []
        roundkey_hex = rkh = []
        print(C_Underline + C_Green + "KEY MANIPULATION STAGE" + C_End)
        for i in range(0, 16):
            # Shifting sequence
            left = shift_left(left, shift_table[i])
            right = shift_left(right, shift_table[i])

            # Concat the left and right key
            combine_str = left + right

            # PC2 permutation
            round_key = permute(combine_str, pc2, 48)

            rkb.append(round_key)
            rkh.append(bin2hex(round_key))
            print("Round ", i + 1, ":", rkb[i], rkh[i])
        print(C_Underline + C_Red + "Final Key:" + C_End, rkh[15])
        print("")

        cipher_text = encryption(textInput, rkb, rkh)
        print(C_Blue_HL + "The cipher text is: " + C_End, C_Red + cipher_text + C_End)
        print("")

    elif ans == "2":

        DecipherInput = input("Please enter your text in lowercase: ")
        key = input("Please input 16 bit keys, numbering from 0 to F: ")

        if len(key) > 16:
            print("Key length is : ", len(key))
            print("Please input key again, your key is more than 16 bits.")
            key = input("Please input 16 bit keys, numbering from 0 to F: ")

        print("")
        print(C_Purp + "Encrypted Input Plaintext: " + C_End, hex2bin(DecipherInput), DecipherInput)
        print(C_Purp + "Key:" + C_End, hex2bin(key), key)
        print("")

        # first we need to convert the key from HEX into BIN by using the function HEX2BIN

        key = hex2bin(key)

        # We then need to pick 56 bits from the 64 bits key we had earlier

        key = permute(key, pc1, 56)

        # Splitting the keys into 2 halves
        left = key[0:28]
        right = key[28:56]

        roundkey_bin = rkb = []
        roundkey_hex = rkh = []
        print(C_Underline + C_Green + " REVERSE KEY MANIPULATION STAGE" + C_End)
        for i in range(0, 16):
            # Shifting sequence
            left = shift_left(left, shift_table[i])
            right = shift_left(right, shift_table[i])

            # Concat the left and right key
            combine_str = left + right

            # PC2 permutation
            round_key = permute(combine_str, pc2, 48)

            rkb.append(round_key)
            rkh.append(bin2hex(round_key))
            print("Round ", i + 1, ":", rkb[i], rkh[i])
        print(C_Underline + C_Red + "Final Key:" + C_End, rkh[15])
        print("")

        rkb_rev = rkb[::-1]
        rkh_rev = rkh[::-1]
        text = encryption(DecipherInput, rkb_rev, rkh_rev)
        print(C_Blue_HL + "The decipher text is: " + C_End, C_Red + text + C_End)
        print("")
    elif ans == "3":

        textInput = input("Please enter your text in lowercase as ASCII: ")
        textInput = textInput.zfill(8)
        textInput = ascii2hex(textInput)
        key = input("Please input 8 bit keys: ")
        if len(key) > 8:
            print("Key length is : ", len(key))
            print("Please input key again, your key is more than 8 bits.")
            key = input("Please enter your text in lowercase as ASCII: ")
        key = key.zfill(8)
        key = ascii2hex(key)

        print("")
        print(C_Purp + "Plaintext: " + C_End, hex2bin(textInput), textInput)
        print(C_Purp + "Key:" + C_End, hex2bin(key), key)
        print("")

        # first we need to convert the key from HEX into BIN by using the function HEX2BIN

        key = hex2bin(key)

        # We then need to pick 56 bits from the 64 bits key we had earlier

        key = permute(key, pc1, 56)

        # Splitting the keys into 2 halves
        left = key[0:28]
        right = key[28:56]

        roundkey_bin = rkb = []
        roundkey_hex = rkh = []
        print(C_Underline + C_Green + "KEY MANIPULATION STAGE" + C_End)
        for i in range(0, 16):
            # Shifting sequence
            left = shift_left(left, shift_table[i])
            right = shift_left(right, shift_table[i])

            # Concat the left and right key
            combine_str = left + right

            # PC2 permutation
            round_key = permute(combine_str, pc2, 48)

            rkb.append(round_key)
            rkh.append(bin2hex(round_key))
            print("Round ", i + 1, ":", rkb[i], rkh[i])
        print(C_Underline + C_Red + "Final Key:" + C_End, rkh[15])
        print("")

        cipher_text = encryption(textInput, rkb, rkh)
        print(C_Blue_HL + "The cipher text is: " + C_End, C_Red + cipher_text + C_End)
        print("")
    elif ans == "4":
        DecipherInput = input("Please enter your text in lowercase as ASCII: ")
        DecipherInput = DecipherInput.zfill(8)
        DecipherInput = ascii2hex(DecipherInput)
        key = input("Please input 8 bit keys: ")
        if len(key) > 8:
            print("Key length is : ", len(key))
            print("Please input key again, your key is more than 8 bits.")
            key = input("Please enter your text in lowercase as ASCII: ")
        key = key.zfill(8)
        key = ascii2hex(key)

        print("")
        print(C_Purp + "Encrypted Input Plaintext: " + C_End, hex2bin(DecipherInput), DecipherInput)
        print(C_Purp + "Key:" + C_End, hex2bin(key), key)
        print("")

        # first we need to convert the key from HEX into BIN by using the function HEX2BIN

        key = hex2bin(key)

        # We then need to pick 56 bits from the 64 bits key we had earlier

        key = permute(key, pc1, 56)

        # Splitting the keys into 2 halves
        left = key[0:28]
        right = key[28:56]

        roundkey_bin = rkb = []
        roundkey_hex = rkh = []
        print(C_Underline + C_Green + " REVERSE KEY MANIPULATION STAGE" + C_End)
        for i in range(0, 16):
            # Shifting sequence
            left = shift_left(left, shift_table[i])
            right = shift_left(right, shift_table[i])

            # Concat the left and right key
            combine_str = left + right

            # PC2 permutation
            round_key = permute(combine_str, pc2, 48)

            rkb.append(round_key)
            rkh.append(bin2hex(round_key))
            print("Round ", i + 1, ":", rkb[i], rkh[i])
        print(C_Underline + C_Red + "Final Key:" + C_End, rkh[15])
        print("")

        rkb_rev = rkb[::-1]
        rkh_rev = rkh[::-1]
        text = encryption(DecipherInput, rkb_rev, rkh_rev)
        print(C_Blue_HL + "The decipher text is: " + C_End, C_Red + text + C_End)
        print("")
    elif ans == "5":
        break
    elif ans != "":
        print("\n Not valid option, Try again!!")
