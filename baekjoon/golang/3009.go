package main

import "fmt"

func main() {
	var x1, x2, x3, y1, y2, y3 int
	fmt.Scanf("%d %d\n", &x1, &y1)
	fmt.Scanf("%d %d\n", &x2, &y2)
	fmt.Scanf("%d %d\n", &x3, &y3)

	var x, y int
	if x1 == x2 {
		x = x3
	} else if x1 == x3 {
		x = x2
	} else {
		x = x1
	}
	if y1 == y2 {
		y = y3
	} else if y1 == y3 {
		y = y2
	} else {
		y = y1
	}

	fmt.Println(x, y)
}
