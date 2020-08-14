package main

import (
	"bufio"
	"fmt"
	"os"

	// "sort"
	"strconv"
)

var sc *bufio.Scanner
var nums []int //maybe it helps..?

func quickSort(pivot, left, right int) {
	if left > right {
		return
	}
	l := left
	r := right
	pv := nums[pivot]
	for {
		for r >= l && nums[r] >= pv {
			r--
		}
		for r >= l && nums[l] <= pv {
			l++
		}
		if l > r {
			break
		} else {
			nums[l], nums[r] = nums[r], nums[l]
		}
	}
	nums[r], nums[pivot] = nums[pivot], nums[r]
	quickSort(pivot, left, r-1)
	quickSort(r+1, r+2, right)
}
func scanInt() int { //to reduce scanning time
	sc.Scan()
	n, _ := strconv.Atoi(sc.Text())
	return n
}

func main() {
	sc = bufio.NewScanner(os.Stdin)
	n := scanInt()
	nums = make([]int, n)
	for i := 0; i < n; i++ {
		nums[i] = scanInt()
	}
	quickSort(0, 1, n-1)
	// sort.Ints(nums)
	writer := bufio.NewWriter(os.Stdout)
	for _, i := range nums {
		fmt.Fprintf(writer, "%d\n", i)
	}
	writer.Flush()
}
