struct Solution;

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let ri_dict = std::collections::HashMap::from([
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000),
        ]);

        let mut total = 0;
        let mut prev_value = 0;

        // Iterate over the string in reverse
        for c in s.chars().rev() {
            let curr_value = *ri_dict.get(&c).unwrap();

            // Subtraction case
            if curr_value < prev_value {
                total -= curr_value;
            } else {
                total += curr_value;
            }

            prev_value = curr_value;
        }

        total
    }
}

fn main() {
    let s = "III".to_string();
    println!("{}", Solution::roman_to_int(s)); // Output: 3

    let s = "LVIII".to_string();
    println!("{}", Solution::roman_to_int(s)); // Output: 58

    let s = "MCMXCIV".to_string();
    println!("{}", Solution::roman_to_int(s)); // Output: 1994
}

