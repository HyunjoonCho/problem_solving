package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var n int
	fmt.Scanf("%d\n", &n)
	count := 0
	i := 0
	for {
		if strings.Contains(strconv.Itoa(i), "666") {
			count++
		}
		if count == n {
			break
		}
		i++
	}
	fmt.Println(i)

}

/*
	r := n % 19 // didn't consider 666**, 666***, etc.
	m := (n / 19) * 10000
	if r < 7 { //0666, ..., 5666 and also for r==0
		m += (r-1)*1000 + 666
	} else if r < 17 { //6660, ..., 6669
		m += 6660 + r - 7
	} else {
		m += (r-10)*1000 + 666
	}
	fmt.Println(m)
*/
