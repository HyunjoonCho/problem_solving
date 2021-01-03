package main

import (
	"fmt"
	"math"
)

func main() {
	var n, num int
	cnt := 0
	fmt.Scanf("%d\n", &n)
	for i := 0; i < n; i++ {
		fmt.Scanf("%d", &num)
		if num == 1 {
			continue
		}
		bound := int(math.Sqrt(float64(num)))
		for j := 2; j <= bound; j++ {
			if num%j == 0 {
				cnt--
				break
			}
		}
		cnt++
	}
	fmt.Println(cnt)
}
