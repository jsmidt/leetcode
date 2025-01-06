import base64

def hex_to_base64(hex_string):
    """Converts a hexadecimal string to base64."""

    # Convert hex string to bytes
    bytes_data = bytes.fromhex(hex_string)

    # Encode bytes to base64
    base64_data = base64.b64encode(bytes_data)

    # Decode base64 bytes to string
    return base64_data.decode('utf-8')
