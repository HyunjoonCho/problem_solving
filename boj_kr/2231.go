package main

import "fmt"

func main() {
	var n int
	fmt.Scanf("%d", &n)
	bound := 0
	tmp := n
    result := 0

	for {
		if tmp != 0 {
			bound += 9
		} else {
			break
		}
		tmp = tmp / 10
	}

	if bound > n {
		bound = n - 1 
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
			result = i
			break
		}
	}
	
	fmt.Println(result)
}
