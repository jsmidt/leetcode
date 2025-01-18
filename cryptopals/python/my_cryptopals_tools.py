import base64
from collections import Counter

def hex_to_base64(hex_string):
    """Converts a hexadecimal string to base64."""

    # Convert hex string to bytes
    bytes_data = bytes.fromhex(hex_string)

    # Encode bytes to base64
    base64_data = base64.b64encode(bytes_data)

    # Decode base64 bytes to string
    return base64_data.decode("utf-8")


def xor_byte_strings(byte_str1: bytes, byte_str2: bytes) -> bytes:
    """
    XOR two byte strings, padding the first byte string with null bytes (0x00)
    if it is not an exact multiple of the second byte string's length.

    :param byte_str1: The first byte string (e.g., 64 bytes)
    :param byte_str2: The second byte string (e.g., 8 bytes)
    :return: A new byte string with the XOR result.
    """
    if len(byte_str2) == 0:
        raise ValueError("The second byte string must not be empty.")

    chunk_size = len(byte_str2)
    padded_length = ((len(byte_str1) + chunk_size - 1) // chunk_size) * chunk_size
    padded_byte_str1 = byte_str1.ljust(padded_length, b'\x00')  # Pad with null bytes (0x00)

    result = bytearray(len(padded_byte_str1))

    for i in range(0, len(padded_byte_str1), chunk_size):
        chunk = padded_byte_str1[i:i + chunk_size]
        result[i:i + chunk_size] = bytes(b1 ^ b2 for b1, b2 in zip(chunk, byte_str2))

    return bytes(result[:len(byte_str1)])


def xor_hex_strings(hex_string1, hex_string2):
    """xors two hex strings and returns hex."""

    # Convert hex string to bytes
    byte_string1 = bytes.fromhex(hex_string1)
    byte_string2 = bytes.fromhex(hex_string2)

    # xor and return text string
    return xor_byte_strings(byte_string1, byte_string2).hex()


def chi_squared_score(s):
    """
    Computes the chi-squared score for how closely the letter distribution of a string matches expected frequencies.
    """
    letter_freqs = {'e': 0.1116, 'a': 0.0850, 'r': 0.0758, 'i': 0.0754, 'o': 0.0716, 
                    't': 0.0665, 's': 0.0573, 'l': 0.0548, 'c': 0.0453, 'u': 0.0363,
                    'd': 0.0384, 'p': 0.0316, 'm': 0.0301, 'h': 0.0300, 'g': 0.0247, 
                    'b': 0.0207, 'f': 0.0181, 'y': 0.0177, 'w': 0.0128, 'k': 0.0110, ' ': 0.2}

    # Normalize: Convert to lowercase and count all characters
    normalized = ''.join(c.lower() if c.lower() in letter_freqs else '#' for c in s)
    
    # Count occurrences of each character
    total_chars = len(normalized)
    if total_chars == 0:  # Avoid division by zero
        return float('inf')
    
    observed_counts = Counter(normalized)
    
    # Calculate chi-squared score
    chi_squared = 0
    for char, expected_freq in letter_freqs.items():
        observed = observed_counts.get(char, 0)
        expected = total_chars * expected_freq
        chi_squared += ((observed - expected) ** 2) / expected if expected > 0 else 0

    # Add penalty for uncommon characters
    uncommon_count = observed_counts.get('#', 0)
    chi_squared += uncommon_count * 10  # Large penalty for each uncommon character
    
    return chi_squared