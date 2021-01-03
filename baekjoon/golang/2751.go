package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"time"
)

var sc *bufio.Scanner
var nums []int

func quickSort(left, right int) {
	if left >= right {
		return
	}

	src := rand.NewSource(time.Now().UnixNano())
	ran := rand.New(src)

	pivot := ran.Intn(right-left) + left
	nums[right], nums[pivot] = nums[pivot], nums[right]

	i := left
	curr := left
	pv := nums[right]

	// fmt.Println("before", i, nums)

	for ; i < right; i++ {
		if nums[i] < pv {
			nums[i], nums[curr] = nums[curr], nums[i]
			curr++
		}
	}
	// No need for r decrease > l increase?

	nums[curr], nums[right] = nums[right], nums[curr]
	// fmt.Println("after", curr, nums)

	quickSort(left, curr-1)
	quickSort(curr+1, right)
}

func scanInt() int {
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
	quickSort(0, n-1)
	writer := bufio.NewWriter(os.Stdout)
	for _, i := range nums {
		fmt.Fprintf(writer, "%d\n", i)
	}
	writer.Flush()
}
