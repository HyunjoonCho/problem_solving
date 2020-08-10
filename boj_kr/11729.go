package main

import (
	"bufio"
	"fmt"
	"os"
)

func printHanoi(w *bufio.Writer, num, src, dest int) {
	if num == 1 {
		fmt.Fprintf(w, "%d %d\n", src, dest)
	} else {
		mid := 6 - src - dest
		printHanoi(w, num-1, src, mid)
		fmt.Fprintf(w, "%d %d\n", src, dest)
		printHanoi(w, num-1, mid, dest)
	}
}
func powerOfTwo(n int) int {
	if n == 1 {
		return 2
	} else {
		return 2 * powerOfTwo(n-1)
	}
}
func main() {
	var n int
	w := bufio.NewWriter(os.Stdout)
	fmt.Scanf("%d", &n)
	fmt.Fprintf(w, "%d\n", powerOfTwo(n)-1)
	printHanoi(w, n, 1, 3)
	w.Flush()
}
