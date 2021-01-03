package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

// 3
// 0 0 13 40 0 37
// 0 0 3 0 7 4
// 1 1 1 1 1 5 -> share center -> a circle inside another?

func main() {
	var t, x1, y1, x2, y2, r1, r2 int
	fmt.Scanf("%d\n", &t)
	w := bufio.NewWriter(os.Stdout)

	for i := 0; i < t; i++ {
		fmt.Scanf("%d %d %d %d %d %d\n", &x1, &y1, &r1, &x2, &y2, &r2)
		if x1 == x2 && y1 == y2 && r1 == r2 {
			fmt.Fprintf(w, "-1\n") //consider concentric case
			continue
		}

		dist := math.Sqrt(float64((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)))
		rSum := float64(r1 + r2)
		var rSmall, rBig float64
		if r1 < r2 {
			rSmall = float64(r1)
			rBig = float64(r2)
		} else {
			rSmall = float64(r2)
			rBig = float64(r1)
		}
		if dist > rSum || dist+rSmall < rBig {
			fmt.Fprintf(w, "0\n")
		} else if dist == rSum || dist+rSmall == rBig {
			fmt.Fprintf(w, "1\n")
		} else {
			fmt.Fprintf(w, "2\n")
		}
	}
	w.Flush()
}
