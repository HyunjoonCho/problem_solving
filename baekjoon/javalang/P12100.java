package javalang;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class P12100 {
    static int size;

    public static int scanBoard(int[][] board) {
        int max = 0;
        
        for (int[] row : board) {
            for (int block : row) {
                if (max < block) {
                    max = block;
                }
            }
        }

        return max;
    }

    public static int[][] copyBoard(int[][] board) {
        int[][] copied = new int[size][size];

        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                copied[i][j] = board[i][j];
            }
        }

        return copied;
    }

    public static int[][] move(int[][] board, int dir) {        
        int idx;

        for (int i = 0; i < size; i++) {
            if (dir < 2) {
                idx = 0;
            } else {
                idx = size - 1;
            }
            for (int j = 0; j < size - 1; j++) {
                if (dir == 0) {
                    if (board[idx][i] == 0 || board[idx + 1][i] == 0) {
                        board[idx][i] += board[idx + 1][i];
                        for (int k = idx + 1; k < size - 1; k++) {
                            board[k][i] = board[k + 1][i];
                        }
                        board[size - 1][i] = 0;
                    } else { 
                        if (board[idx][i] == board[idx + 1][i]) {
                            board[idx][i] *= 2;
                            for (int k = idx + 1; k < size - 1; k++) {
                                board[k][i] = board[k + 1][i];
                            }
                            board[size - 1][i] = 0;
                        }
                        idx++;
                    }
                } else if (dir == 1) {
                    if (board[i][idx] == 0 || board[i][idx + 1] == 0) {
                        board[i][idx] += board[i][idx + 1];
                        for (int k = idx + 1; k < size - 1; k++) {
                            board[i][k] = board[i][k + 1];
                        }
                        board[i][size - 1] = 0;
                    } else {
                        if (board[i][idx] == board[i][idx + 1]) {
                            board[i][idx] *= 2;
                            for (int k = idx + 1; k < size - 1; k++) {
                                board[i][k] = board[i][k + 1];
                            }
                            board[i][size - 1] = 0;
                        }
                        idx++;
                    }
                } else if (dir == 2) {
                    if (board[idx][i] == 0 || board[idx - 1][i] == 0) {
                        board[idx][i] += board[idx - 1][i];
                        for (int k = idx - 1; k > 0; k--) {
                            board[k][i] = board[k - 1][i];
                        }
                        board[0][i] = 0;
                    } else {
                        if (board[idx][i] == board[idx - 1][i]) {
                            board[idx][i] *= 2;
                            for (int k = idx - 1; k > 0; k--) {
                                board[k][i] = board[k - 1][i];
                            }
                            board[0][i] = 0;
                        }
                        idx--;
                    }
                } else {
                    if (board[i][idx] == 0 || board[i][idx - 1] == 0) {
                        board[i][idx] += board[i][idx - 1];
                        for (int k = idx - 1; k > 0; k--) {
                            board[i][k] = board[i][k - 1];
                        }
                        board[i][0] = 0;
                    } else {
                         if (board[i][idx] == board[i][idx - 1]) {
                            board[i][idx] *= 2;
                            for (int k = idx - 1; k > 0; k--) {
                                board[i][k] = board[i][k - 1];
                            }
                            board[i][0] = 0;
                        }
                        idx--;
                    }
                }
            }
        }

        return board;
    }

    public static int getMax(int[][] board, int depth) {
        int max = scanBoard(board);
        if (depth++ == 5) {
            return max;
        }

        int childMax;
        // 0: up, 1: left, 2: down, 3: right
        for (int dir = 0; dir < 4; dir ++) {
            int[][] copiedBoard = copyBoard(board);
            childMax = getMax(move(copiedBoard, dir), depth);
            max = max > childMax? max : childMax;
        }

        return max;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String sizeStr = br.readLine();
        size = Integer.parseInt(sizeStr);
        int[][] board = new int[size][size];

        for (int i = 0; i < size; i++) {
            String[] blocks = br.readLine().split(" ");
            for (int j = 0; j < size; j++) {
                board[i][j] = Integer.parseInt(blocks[j]);
            }
        }

        System.out.println(getMax(board, 0));

        br.close();
    }    
}

/*
- Case to check Deep-copy? 
4 16 4
4 4 4
16 4 4 

without deepcopy - up goes first > no more change 
8 16 8
16 8 4 
0 0 0

with deepcopy - 32!
0 0 0
8 16 4
16 8 8

- Case for Empty space between?
3
4 0 0
0 0 0 
4 0 0 
 */