from my_cryptopals_tools import xor_byte_strings, chi_squared_score

myfile = open('4.txt','r')

best_score = 9999999.
lines = myfile.readlines()
for jj, line in enumerate(lines):
    hex_string = line.strip()
    for i in range(255):
        byte_string1 = bytes.fromhex(hex_string)
        byte_string2 = i.to_bytes()

        raw_string = xor_byte_strings(byte_string1, byte_string2).decode('latin-1')
        score = chi_squared_score(raw_string)
        if score < best_score:
            best_line = hex_string
            best_snumber = jj
            best_score = score
            best_char = i
            best_string = raw_string

print (f'Best string was: {best_line.strip()}')
print (f'This is line number: {best_snumber}')
print (f'This decodes as: "{best_string.strip()}"')
print (f'Best char was: {best_char} or {chr(best_char)} in ascii')
print (f'Best score was: {best_score:.2f}')
