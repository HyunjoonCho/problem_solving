package javalang;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class P14499 {
    static int width, height;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int[] nextBottoms = {2, 3, 1, 4};

    public static boolean outOfBoard(int x, int y, int dir) {
        int movedX = x + dx[dir];
        int movedY = y + dy[dir];
        return movedX < 0 || movedX >= width || movedY < 0 || movedY >= height;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] inputs = br.readLine().split(" ");
        height = Integer.parseInt(inputs[0]);
        width = Integer.parseInt(inputs[1]);
        int x = Integer.parseInt(inputs[3]);
        int y = Integer.parseInt(inputs[2]);
        int moveCount = Integer.parseInt(inputs[4]);

        int[][] board = new int[height][width];
        for (int i = 0; i < height; i++) {
            String[] row = br.readLine().split(" ");
            for (int j = 0; j < width; j++) {
                board[i][j] = Integer.parseInt(row[j]);
            }
        }

        int[] dice = new int[6];
        for (int i = 0; i < 6; i++) {
            dice[i] = 0;
        }
        /*
  1
3 0 2 : 0 as bottom 
  4
  5   : 5 on top 
         */

        int bottom, target, nextBottom;
        String[] moves = br.readLine().split(" ");
        for (int i = 0; i < moveCount; i++) {
            int dir = Integer.parseInt(moves[i]) - 1;
            if (!outOfBoard(x, y, dir)) {
                bottom = dice[0];

                nextBottom = nextBottoms[dir];
                dice[0] = dice[nextBottom];
                dice[nextBottom] = dice[5];
                dice[5] = dice[5 - nextBottom];
                dice[5 - nextBottom] = bottom;

                x += dx[dir];
                y += dy[dir];
                target = board[y][x];

                bottom = dice[0];
                if (target == 0) {
                    board[y][x] = bottom;
                } else {
                    dice[0] = board[y][x];
                    board[y][x] = 0;
                }
                System.out.println(dice[5]);
            }
        }
    }    
}

/*
java 2D array is row oriented - be careful about X-Y coordinate

reading one digit number > map[i][j] = str.charAt(idx * 2) - '0' 
 */