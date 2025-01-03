struct Solution;

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let ri_dict = vec![
            ("I", 1),
            ("V", 5),
            ("X", 10),
            ("L", 50),
            ("C", 100),
            ("D", 500),
            ("M", 1000),
            ("IV", 4),
            ("IX", 9),
            ("XL", 40),
            ("XC", 90),
            ("CD", 400),
            ("CM", 900),
        ];
        let ri_map: std::collections::HashMap<&str, i32> = ri_dict.into_iter().collect();

        let chars: Vec<char> = s.chars().collect();
        let mut i = 0;
        let mut total = 0;

        while i < chars.len() {
            if i + 1 < chars.len() {
                let two_chars: String = chars[i..i + 2].iter().collect();
                if let Some(&value) = ri_map.get(&two_chars[..]) {
                    total += value;
                    i += 2;
                    continue;
                }
            }

            if let Some(&value) = ri_map.get(&chars[i].to_string()[..]) {
                total += value;
            }
            i += 1;
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

