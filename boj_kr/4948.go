package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func main() {
	var n int
	w := bufio.NewWriter(os.Stdout)
	for {
		fmt.Scanf("%d\n", &n)
		if n == 0 {
			break
		}
		cnt := 0
		for i := n + 1; i <= 2*n; i++ {
			bound := int(math.Sqrt(float64(i)))
			isPrime := true
			for j := 2; j <= bound; j++ {
				if i%j == 0 {
					isPrime = false
					break
				}
			}
			if isPrime {
				cnt++
			}
		}
		fmt.Fprintf(w, "%d\n", cnt)
	}
	w.Flush()
}
