package javalang;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class P14500 {

    static int[][] tetromino = {
        {0, 1, 1, 0, 0, -1}, 
        {0, 1, 0, 1, 0, 1},
        {1, 0, 1, 0, 1, 0},
        {-1, 0, 0, 1, 0, 1},
        {0, 1, 1, 0, 1, 0},
        {1, 0, 0, -1, 0, -1},
        {0, -1, -1, 0, -1, 0},
        {0, 1, 1, 0, -1, 1},
        {1, 0, 0, -1, 1, 1},
        {0, -1, -1, 0, 1, -1},
        {-1, 0, 0, 1, -1, -1}, 
        {0, 1, 0, 1, 1, 0},
        {1, 0, 1, 0, 0, -1}, 
        {0, -1, 0, -1, -1, 0}, 
        {-1, 0, -1, 0, 0, 1}, 
        {0, 1, 1, 0, 0, 1},
        {1, 0, 0, -1, 1, 0}, 
        {0, 1, -1, 0 ,0, 1},
        {-1, 0, 0, -1, -1, 0}
    };
/*
[0] [1], [2] [3], [4] [5] = ordered movement (dy, dx pair)
since row-oriented

S 1
3 2 

S 1 2 3 * 2(rotation)

1 2 3   S 1 3   S 1 2
S         2         3   * 4(rotation)

S 1       2 3
  2 3   S 1    * 2(rotation)
 */


    static int height, width, x, y, sum;
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
                    x = j;
                    y = i;    
                    sum = board[y][x];

                    for (int c = 0; c < 3; c++) {
                        if (moveBoard(c, t)) {
                            break;
                        }
                    }
                    
                    max = sum > max ? sum : max;
                }
            }
        }
        return max;
    }

    public static boolean moveBoard(int moveCount, int tetrominoCase) {
        y += tetromino[tetrominoCase][moveCount * 2];
        x += tetromino[tetrominoCase][moveCount * 2 + 1];

        if (outOfBoard(x, y)) {
            return true;
        }
        sum += board[y][x];

        return false;
    }

    public static boolean outOfBoard(int x, int y) {
        if (x < 0 || x > width - 1 || y < 0 || y > height - 1 ) {
            return true;
        }
        return false;
    }
}

/*
greedy works? i.e. max of 4 == max of 3 + n
No 
3 4 
4 4 4 1
1 1 1 1  
3 4 3 4

brute force? 2 + 1 + 8 + 8 + 4 = 23 cases
 */