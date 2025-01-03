struct Solution;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let len = nums.len();
        for i in 0..len {
            for j in (i+1)..len {
                if nums[i] + nums[j] == target {
                    return vec![i as i32, j as i32];
                }
            }
        }
        vec![] // Return an empty vector if no solution is found

    }
}

fn main() {
    let nums = vec![2, 7, 11, 15];
    let target = 9;
    let result = Solution::two_sum(nums, target);
    println!("{:?}", result); // Output: [0, 1]
}
