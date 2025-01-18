use base64;

fn hex_to_bytes(hex_str: &str) -> Result<Vec<u8>, String> {
    // Ensure the hexadecimal string has an even length
    if hex_str.len() % 2 != 0 {
        return Err("Hex string must have an even length".to_string());
    }

    (0..hex_str.len())
        .step_by(2)
        .map(|i| {
            u8::from_str_radix(&hex_str[i..i + 2], 16)
                .map_err(|e| format!("Invalid hex character at position {}: {}", i, e))
        })
        .collect()

}

fn main() {
    //let hex_string = "48656c6c6f576f726c64"; // "HelloWorld" in hexadecimal
    let hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";

    match hex_to_bytes(hex_string) {
        Ok(bytes) => {
            println!("Bytes: {:?}", bytes);
            println!("String: {}", String::from_utf8_lossy(&bytes));
                        
            // Encode bytes to Base64
            let base64_encoded = base64::encode(&bytes);
            println!("Base64: {}", base64_encoded);
        }
        Err(e) => println!("Error: {}", e),
    }
}
