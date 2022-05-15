# Backup file for Lab 2 Part II
# In case the server goes down

import os
import base64


def XOR(a, b):
    r = b""
    for x, y in zip(a, b):
        r += (x ^ y).to_bytes(1, "big")
    return r


def gen_OTP(length):
    return bytearray(os.urandom(length))


def decrypt(cipher, OTP):
    # DO NOT change this function
    return XOR(cipher, OTP)


# Original message
original_plaintext = b"Student ID 1000000 gets 0 points\n"

# Randomly generated OTP
OTP = gen_OTP(length=len(original_plaintext))

# Encrypt
original_cipher = XOR(original_plaintext, OTP)

# Decrypt
print(decrypt(original_cipher, OTP))


def hax():
    # TODO: manipulate ciphertext to decrypt to:
    # "Student ID 100XXXX gets 4 points"
    return new_cipher


new_cipher = hax()

# Decrypt function should provide the manipulated message:
print(decrypt(new_cipher, OTP))
