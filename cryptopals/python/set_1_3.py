from my_cryptopals_tools import xor_byte_strings, chi_squared_score

hex_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

best_score = 9999999.
for i in range(255):
    byte_string1 = bytes.fromhex(hex_string)
    byte_string2 = i.to_bytes()

    #print (f'Xor in bytes with {i} is {xor_byte_strings(byte_string1, byte_string2)}')
    #print (f'Xor in hex is {xor_byte_strings(byte_string1, byte_string2).decode('utf-8')}')
    raw_string = xor_byte_strings(byte_string1, byte_string2).decode('latin-1')
    score = chi_squared_score(raw_string)
    if score < best_score:
        best_score = score
        best_char = i
        best_string = raw_string

print (f'Best string was: "{best_string}"')
print (f'Best char was: {best_char} or {chr(best_char)}')
print (f'Best score was: {best_score:.2f}')