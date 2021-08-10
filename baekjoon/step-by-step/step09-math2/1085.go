package main

import (
	"fmt"
	"math"
)

func main() {
	var x, y, w, h float64
	fmt.Scanf("%f %f %f %f", &x, &y, &w, &h)
	fmt.Println(int(math.Min(math.Min(x, w-x), math.Min(y, h-y))))
}
