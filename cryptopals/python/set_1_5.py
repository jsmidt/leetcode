from my_cryptopals_tools import xor_byte_strings


str1 = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = b"ICE"

ans1 = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272'
ans2 = 'a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'

print (f'The original string is: {str1}')
print ('Which should encode as hex as:')
print (ans1)
print (ans2)
print()
encoded = xor_byte_strings(str1, key)
print ('The encoded string in bytes is:')
print (encoded)
encoded = encoded.hex()
print()
print ('The encoded string in hex is:')
print (encoded[:len(ans1)])
print (encoded[len(ans1):])
