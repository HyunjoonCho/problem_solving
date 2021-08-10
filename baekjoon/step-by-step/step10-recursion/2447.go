package main

import (
	"bufio"
	"fmt"
	"os"
)

func fill(arr [][]bool, x int, y int, size int) {
	if size == 3 {
		for i := 0; i < 3; i++ {
			for j := 0; j < 3; j++ {
				arr[x+i][y+j] = true
			}
		}
		arr[x+1][y+1] = false
		return
	}
	size /= 3
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			if i == 1 && j == 1 {
				continue
			}
			fill(arr, x+i*size, y+j*size, size)
		}
	}
}

func main() {
	var n int
	fmt.Scanf("%d", &n)
	w := bufio.NewWriter(os.Stdout)
	arr := [][]bool{}
	for i := 0; i < n; i++ {
		row := []bool{}
		for i := 0; i < n; i++ {
			row = append(row, false)
		}
		arr = append(arr, row)
	}
	fill(arr, 0, 0, n)

	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if arr[i][j] {
				fmt.Fprintf(w, "*")
			} else {
				fmt.Fprintf(w, " ")
			}
		}
		fmt.Fprintf(w, "\n")
	}
	w.Flush()
}
