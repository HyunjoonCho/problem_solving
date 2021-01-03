package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var a, b, c int
	w := bufio.NewWriter(os.Stdout)
	for {
		fmt.Scanf("%d %d %d\n", &a, &b, &c)
		if a == 0 && b == 0 && c == 0 {
			break
		}
		a = a * a
		b = b * b
		c = c * c
		if a+b == c || b+c == a || c+a == b {
			fmt.Fprintf(w, "right\n")
		} else {
			fmt.Fprintf(w, "wrong\n")
		}
	}
	w.Flush()
}
