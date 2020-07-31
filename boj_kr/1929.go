package main

import (
	"fmt"
	"math"
)

func main() {
	var m, n int
	fmt.Scanf("%d %d", &m, &n)

	for i := m; i <= n; i++ {
		bound := int(math.Sqrt(float64(i)))
		isPrime := true
		if i == 1 {
			continue
		}
		for j := 2; j <= bound; j++ {
			if i%j == 0 {
				isPrime = false
				break
			}
		}
		if isPrime {
			fmt.Println(i)
		}
	}
}
