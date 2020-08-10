package main

import (
	"fmt"
	"math"
)

func main() {
	var r int
	fmt.Scanf("%d\n", &r)
	fmt.Printf("%.4f\n", math.Pi*float64(r)*float64(r))
	fmt.Printf("%.4f\n", 2.0*float64(r)*float64(r))
}
