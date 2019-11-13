package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func countNodes(root *TreeNode) int {
	if root == nil {
		return 0
	}

	l, r := 0, 0
	if root.Left != nil {
		l = countNodes(root.Left)
	}
	if root.Right != nil {
		r = countNodes(root.Right)
	}

	return l + r + 1
}

func main() {
	t1 := TreeNode{4, nil, nil}
	t2 := TreeNode{5, nil, nil}
	t3 := TreeNode{2, &t1, &t2}
	t4 := TreeNode{6, nil, nil}
	t5 := TreeNode{3, nil, &t4}
	t6 := TreeNode{1, &t3, &t5}
	fmt.Printf("%d\n", countNodes(&t6))
}

// Top 98.92% runtime
