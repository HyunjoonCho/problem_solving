package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n int
	fmt.Scanf("%d\n", &n)
	weight := make([]int, n)
	height := make([]int, n)

	var w, h int
	for i := 0; i < n; i++ {
		fmt.Scanf("%d %d\n", &w, &h)
		weight[i] = w
		height[i] = h
	}
	writer := bufio.NewWriter(os.Stdout)
	for i := 0; i < n; i++ {
		rank := 1
		wI := weight[i]
		hI := height[i]
		for j := 0; j < n; j++ {
			if wI < weight[j] && hI < height[j] {
				rank++
			}
		}
		fmt.Fprintf(writer, "%d ", rank)
	}
	writer.Flush()
}
