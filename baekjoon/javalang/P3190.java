package javalang;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

class P3190 {
    static int size;
    static int[][] board;
    static final int EMPTY = -1;
    static final int APPLE = 10;
    // 0: R, 1: D, 2: L, 3:U

    static Map<Integer, Boolean> dirChange;

    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};

    public static boolean endCondition (int headX, int headY) {
        if (headX < 0 || headX >= size || headY < 0 || headY >= size) {
            return true;
        }
        int head = board[headY][headX];
        return head != EMPTY && head != APPLE;
    }

    public static void printBoard() {
        for (int[] row : board) {
            for (int point: row) {
                System.out.printf("%3d ", point);
            }
            System.out.println();
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        size = Integer.parseInt(br.readLine());
        board = new int[size][size];

        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                board[i][j] = EMPTY;
            }
        }
        int numApple = Integer.parseInt(br.readLine());

        for (int i = 0; i < numApple; i++) {
            String[] point = br.readLine().split(" ");
            board[Integer.parseInt(point[0]) - 1][Integer.parseInt(point[1]) - 1] = APPLE;
        }

        int numDirChange = Integer.parseInt(br.readLine());
        dirChange = new HashMap<>();

        for (int i = 0; i < numDirChange; i++) {
            String[] change = br.readLine().split(" ");
            dirChange.put(Integer.parseInt(change[0]), change[1].equals("L"));
        }

        int headX = 0;
        int headY = 0;
        int tailX = 0;
        int tailY = 0;
        int direction = 0; // right - down - left - up
        int length = 1;
        int time = 0;

        while (true) {
            time++;

            headX += dx[direction];
            headY += dy[direction];

            if (endCondition(headX, headY)) {
                break;
            }

            int next = board[headY][headX];
            if (next == APPLE) {
                if (length == 1) {
                    board[tailY][tailX] = direction;
                }
                length++;
            } else if (board[headY][headX] == EMPTY) {
                if (length == 1) {
                    board[tailY][tailX] = EMPTY;
                    tailX = headX;
                    tailY = headY;    
                } else {
                    int tailDir = board[tailY][tailX];
                    board[tailY][tailX] = EMPTY;
                    tailX += dx[tailDir];
                    tailY += dy[tailDir];    
                }
            }

            if (dirChange.containsKey(time)) {
                if (dirChange.get(time)) {
                    direction = (direction + 3) % 4;
                } else {
                    direction = (direction + 1) % 4;
                }
            }
            board[headY][headX] = direction;
        }

        System.out.println(time);

        br.close();
    }
}

/*
Logic
- put direction at point where snake exists 
- every loop
  1. check end condition - out of board before moving on + meet-it-self, i.e. coordinate is neither empty nor apple 
  2. check apple - if exists, keep tail and move head / otherwise, empty tail and move to its direction 
  3. check direction change and save head direction
 */

 /* 
 for (int x : array) {
     ~
 }
 only reads the value, cannot change it -> use coordinate
  */