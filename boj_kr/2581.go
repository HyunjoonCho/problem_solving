package main

import (
	"fmt"
	"math"
)

func main() {
	var m, n, sum, min int
	fmt.Scanf("%d\n%d\n", &m, &n)
	for i := m; i <= n; i++ {
		if i == 1 {
			continue
		}
		bound := int(math.Sqrt(float64(i)))
		isPrime := true
		for j := 2; j <= bound; j++ {
			if i%j == 0 {
				isPrime = false
				break
			}
		}
		if isPrime {
			sum += i
			if min == 0 {
				min = i
			}
		}
	}
	if min == 0 {
		fmt.Printf("-1\n")
	} else {
		fmt.Println(sum)
		fmt.Println(min)
	}

}
