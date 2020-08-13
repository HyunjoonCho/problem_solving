package main

import "fmt"

func main() {
	var n int
	fmt.Scanf("%d", &n)
	bound := 0
	tmp := n
	for {
		tmp = tmp / 10
		if tmp != 0 {
			bound += 9
		} else {
			break
		}
	}
	if bound > n {
		bound = n
	}
	for i := n - bound; i < n; i++ {
		sum := i
		tmp := i
		for {
			if tmp != 0 {
				sum += tmp % 10
				tmp /= 10
			} else {
				break
			}
		}
		if sum == n {
			fmt.Println(i)
			return
		}
	}
	fmt.Println(0)
}
