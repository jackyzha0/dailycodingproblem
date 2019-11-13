package main

import (
	"math"
	"sort"
)

type ByDist [][]int

func (a ByDist) Len() int           { return len(a) }
func (a ByDist) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a ByDist) Less(i, j int) bool { return dist(a[i], a[j]) }

func dist(p1, p2 []int) bool {
	n1 := math.Hypot(float64(p1[0]), float64(p1[1]))
	n2 := math.Hypot(float64(p2[0]), float64(p2[1]))
	return n1 < n2
}

func kClosest(points [][]int, K int) [][]int {
	sort.Sort(ByDist(points))
	return points[:K]
}
