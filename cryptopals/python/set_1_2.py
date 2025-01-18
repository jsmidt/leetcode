from my_cryptopals_tools import xor_hex_strings, xor_byte_strings

hex_string1 = "1c0111001f010100061a024b53535009181c"
hex_string2 = "686974207468652062756c6c277320657965"

xor_hex_strings(hex_string1, hex_string2)

byte_string1 = bytes.fromhex(hex_string1)
byte_string2 = bytes.fromhex(hex_string2)

print (f'String 1 in bytes is {byte_string1}')
print (f'String 2 in bytes is {byte_string2}')
print (f'Xor in bytes is {xor_byte_strings(byte_string1, byte_string2)}')
print (f'Xor solution in hex is {xor_hex_strings(hex_string1, hex_string2)}')
