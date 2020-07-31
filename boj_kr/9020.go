package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func isPrime(n int) bool {
	if n == 1 {
		return false
	}
	bound := int(math.Sqrt(float64(n)))
	isPr := true
	for j := 2; j <= bound; j++ {
		if n%j == 0 {
			isPr = false
			break
		}
	}
	return isPr
}

func main() {
	var t, n int
	fmt.Scanf("%d\n", &t)
	w := bufio.NewWriter(os.Stdout)

	for i := 0; i < t; i++ {
		fmt.Scanf("%d\n", &n)
		small := n / 2
		big := n / 2
		for {
			if isPrime(small) && isPrime(big) {
				fmt.Fprintf(w, "%d %d\n", small, big)
				break
			}
			small--
			big++
		}
	}
	w.Flush()
}
