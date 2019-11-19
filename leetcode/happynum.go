package main

import "math"

func isHappy(n int) bool {
	if n == 1 {
		return true
	}

	if n == 58 {
		return false
	}

	var s = 0
	for n != 0 {
		s += int(math.Pow(float64(n%10), 2))
		n = n / 10
	}

	return isHappy(s)
}
