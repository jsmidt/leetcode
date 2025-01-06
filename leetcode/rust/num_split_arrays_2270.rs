struct Solution;

impl Solution {
    pub fn ways_to_split_array(nums: Vec<i32>) -> i32 {
        let total_sum: i64 = nums.iter().map(|&x| x as i64).sum(); // Calculate the total sum once
        let mut left_sum: i64 = 0;
        let mut splits = 0;

        for i in 0..(nums.len() - 1) {
            left_sum += nums[i] as i64; // Incrementally build the left sum
            let right_sum = total_sum - left_sum; // Calculate the right sum

            if left_sum >= right_sum {
                splits += 1;
            }
        }

        splits
    }
}

fn main() {
    let nums = vec![2, 3, 1, 0];
    let result = Solution::ways_to_split_array(nums);
    println!("{}", result); // Output: 2
}

