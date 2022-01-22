#babyencryption htb challenge. I probably over thought this. *shrugs*
import string

lookup_table = {}
alphabet = [letter for letter in string.printable]
encrypted_secret = open('msg.enc', 'r').read()

for letter in alphabet:
    encrypted_letter = (123 * ord(letter) + 18) % 256
    lookup_table[encrypted_letter] = letter

frame = bytearray.fromhex(encrypted_secret)
letters = [x for x in frame]

decrypted_secret = ''
for value in letters:
    decrypted_secret = decrypted_secret + lookup_table[value]

print(decrypted_secret)
