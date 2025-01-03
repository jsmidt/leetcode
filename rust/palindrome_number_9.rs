struct Solution;

impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        let x_str = x.to_string(); // Convert the integer to a string
        let len = x_str.len(); // Get the length of the string

        if len == 1 {
            return true; // Single-digit numbers are palindromes
        }

        let n = len / 2; // Calculate the midpoint
        let x1 = &x_str[..n]; // First half of the string
        let x2 = &x_str[len - n..]; // Second half of the string

        // Compare the first half with the reversed second half
        x1 == x2.chars().rev().collect::<String>()
    }
}

fn main() {
    let x = 10;
    let result = Solution::is_palindrome(x);
    println!("{}", result); // Output: true
}
