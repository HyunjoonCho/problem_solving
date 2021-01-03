package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var h, w int
	fmt.Scanf("%d %d\n", &h, &w)
	board := make([][]bool, h)
	reader := bufio.NewReader(os.Stdin)
	for i := 0; i < h; i++ {
		board[i] = make([]bool, w)
		text, _ := reader.ReadString('\n')
		for j := 0; j < w; j++ {
			if text[j] == 'W' {
				board[i][j] = true
			} else {
				board[i][j] = false
			}
		}
	}

	min := 32
	for y := 0; y < h-7; y++ {
		for x := 0; x < w-7; x++ {
			count := 0
			//brute force, (x,y) as white/true
			for i := 0; i < 8; i++ {
				for j := 0; j < 8; j++ {
					if (i+j)%2 == 0 {
						if board[y+i][x+j] == false {
							count++
						}
					} else {
						if board[y+i][x+j] == true {
							count++
						}
					}
				}
			}
			if count > 32 { //revrse, i.e. (x,y) as black
				count = 64 - count
			}
			if count < min {
				min = count
			}
		}
	}
	fmt.Println(min)
}
