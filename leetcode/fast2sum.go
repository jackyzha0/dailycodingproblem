package main

func twoSum(nums []int, target int) []int {
	// for each num in nums, check if target - nums exists in nums
	m := make(map[int]int)
	for i, val := range nums {
		m[val] = i
	}
	for i2, val2 := range nums {
		if _, ok := m[target-val2]; ok && !(i2 == m[target-val2]) {
			return []int{i2, m[target-val2]}
		}
	}
	return []int{-1, -1}
}

// Top 94.89% runtime
