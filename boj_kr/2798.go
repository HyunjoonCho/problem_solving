package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	var n, m int
	fmt.Scanf("%d %d\n", &n, &m)
	r := bufio.NewReader(os.Stdin)
	text, _ := r.ReadString('\n')
	split := strings.Fields(text)
	var nums []int
	for _, a := range split {
		num, _ := strconv.Atoi(a)
		nums = append(nums, num)
	}

	l := len(nums)
	boundI := l - 2
	boundJ := l - 1
	var max, sum int
	for i := 0; i < boundI; i++ {
		for j := i + 1; j < boundJ; j++ {
			for k := j + 1; k < l; k++ {
				sum = nums[i] + nums[j] + nums[k]
				if sum == m {
					fmt.Println(m)
					return
				} else if sum < m && sum > max {
					max = sum
				}
			}
		}
	}
	fmt.Println(max)
}
