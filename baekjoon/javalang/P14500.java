package javalang;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class P14500 {
    static int[][] tetromino = {
        {0, 0, 1, -1, 0, 1, 0, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1}, // dy(row change)
        {1, 1, 0, 0, 1, 0, -1, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, 1, 0}, // dx(column change)
        {1, 0, 1, 0, 1, 0, -1, 1, 0, -1, 0, 0, 1, 0, -1, 1, 0, -1, 0}, // dy
        {0, 1, 0, 1, 0, -1, 0, 0, -1, 0, 1, 1, 0, -1, 0, 0, -1, 0, -1}, // dx
        {0, 0, 1, 0, 1, 0, -1, -1, 1, 1, -1, 1, 0, -1, 0, 0, 1, 0, -1}, // dy
        {-1, 1, 0, 1, 0, -1, 0, 1, 1, -1, -1, 0, -1, 0, 1, 1, 0, 1, 0} // dx
    };
    static int height, width;
    static int[][] board;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] size = br.readLine().split(" ");
        height = Integer.parseInt(size[0]);
        width = Integer.parseInt(size[1]);

        board = new int[height][width];
        for (int i = 0; i < height; i++) {
            String[] row = br.readLine().split(" ");
            for (int j = 0; j < width; j++) {
                board[i][j] = Integer.parseInt(row[j]);
            }
        }
        
        System.out.println(getMax());
    }

    public static int getMax() {
        int max = 0;
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                for (int t = 0; t < 19; t++) {
                    int x = j;
                    int y = i;
    
                    int sum = board[y][x];
                    y += tetromino[0][t];
                    x += tetromino[1][t];
                    if (x < 0 || x > width - 1 || y < 0 || y > height - 1 ) {
                        continue;
                    }
                    sum += board[y][x];
                    y += tetromino[2][t];
                    x += tetromino[3][t];
                    if (x < 0 || x > width - 1 || y < 0 || y > height - 1 ) {
                        continue;
                    }
                    sum += board[y][x];
                    y += tetromino[4][t];
                    x += tetromino[5][t];
                    if (x < 0 || x > width - 1 || y < 0 || y > height - 1 ) {
                        continue;
                    }
                    sum += board[y][x];
    
                    if (sum > max) {
                        max = sum;
                    }
                }
            }
        }
        return max;
    }
}

/*
S 0
0 0 

S 0 0 0 * 2(rotation)

0 0 0   S 0 0   S 0 0
S         0         0   * 4(rotation)

S 0       0 0
  0 0   S 0    * 2(rotation)

 */

/*
greedy works? i.e. max of 4 == max of 3 + n
No 
4 4 4 1
1 1 1 1  
3 4 3 4

brute force? 2 + 1 + 8 + 8 + 4 = 23 cases
 */