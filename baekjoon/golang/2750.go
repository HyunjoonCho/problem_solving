package main

import (
	"bufio"
	"fmt"
	"os"
)

func mergeSort(nums []int) []int {
	l := len(nums)
	if l == 1 {
		return nums
	}
	sl1 := mergeSort(nums[:l/2])
	sl2 := mergeSort(nums[l/2:])

	sorted := make([]int, l)
	idx1 := 0
	idx2 := 0
	for i := 0; i < l; i++ {
		if idx1 == len(sl1) {
			sorted[i] = sl2[idx2]
			idx2++
			continue
		}
		if idx2 == len(sl2) {
			sorted[i] = sl1[idx1]
			idx1++
			continue
		}
		if sl1[idx1] < sl2[idx2] {
			sorted[i] = sl1[idx1]
			idx1++
		} else {
			sorted[i] = sl2[idx2]
			idx2++
		}
	}
	return sorted
}

func main() {
	var n, tmp int
	fmt.Scanf("%d\n", &n)
	nums := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scanf("%d\n", &tmp)
		nums[i] = tmp
	}
	//let's sort! which algo you wanna use?
	sorted := mergeSort(nums)
	writer := bufio.NewWriter(os.Stdout)
	for _, i := range sorted {
		fmt.Fprintf(writer, "%d\n", i)
	}
	writer.Flush()
}
