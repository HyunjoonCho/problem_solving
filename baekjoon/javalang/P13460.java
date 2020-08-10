package javalang;

import java.io.BufferedReader;
import java.io.InputStreamReader;

class P13460 {
    static int height, width;
    static char[][] board;
    static final int[] DX = {0, 0, -1, 1};
    static final int[] DY = {-1, 1, 0, 0};
    static final int FAIL = 20;
    static final int END = 15;

    public static int min(int a, int b) {
        return a < b ? a : b;
    }

    public static int min(int a, int b, int c, int d) {
        int minAB = a < b ? a : b;
        int minCD = c < d ? c : d;
        return minAB < minCD ? minAB : minCD;
    }

    public static void block (boolean isEnded, int y, int x) {
        if (!isEnded) {
            board[y][x] = '#';
        }
    }

    public static void unblock (boolean isEnded, int y, int x) {
        if (!isEnded) {
            board[y][x] = '.';
        }
    }

    // U D L R
    public static int move(int x, int y, int dir) {
        int dx = DX[dir];
        int dy = DY[dir];

        char currentPos;

        do {
            x += dx;
            y += dy;
            currentPos = board[y][x];
            if (currentPos == 'O') {
                return END;
            }
        } while(currentPos != '#');
        return dir < 2? y - dy : x - dx;
    }

    public static int minMovement(int rx, int ry, int bx, int by, int depth, int dir) {
        if (depth++ >= 10) {
            return FAIL;
        }

        boolean isRedEnded = false;
        boolean isBlueEnded = false;

        // vertical or horizontal
        if (dir < 2) {
            if (rx == bx) {
                // (ry < by) ^ (dir % 2 == 1) 
                // (dir == 0 && ry < by) || (dir == 1 && ry > by)
                if ((ry < by) ^ (dir % 2 == 1)) {
                    if ((ry = move(rx, ry, dir)) == END) {
                        isRedEnded = true;
                    }
                    block(isRedEnded, ry, rx);
                    if ((by = move(bx, by, dir)) == END) {
                        isBlueEnded= true;
                    }
                    unblock(isRedEnded, ry, rx);
                } else {
                    if ((by = move(bx, by, dir)) == END) {
                        isBlueEnded= true;
                    }
                    block(isBlueEnded, by, bx);
                    if ((ry = move(rx, ry, dir)) == END) {
                        isRedEnded = true;
                    }
                    unblock(isBlueEnded, by, bx);
                }
            } else {
                if ((ry = move(rx, ry, dir)) == END) {
                    isRedEnded = true;
                }
                if ((by = move(bx, by, dir)) == END) {
                    isBlueEnded = true;
                }
            }
        } else {
            if (ry == by) {
                if ((rx < bx) ^ (dir % 2 == 1)) {
                    if ((rx = move(rx, ry, dir)) == END) {
                        isRedEnded = true;
                    }
                    block(isRedEnded, ry, rx);
                    if ((bx = move(bx, by, dir)) == END) {
                        isBlueEnded = true;
                    }
                    unblock(isRedEnded, ry, rx);
                } else {
                    if ((bx = move(bx, by, dir)) == END) {
                        isBlueEnded = true;
                    }
                    block(isBlueEnded, by, bx);
                    if ((rx = move(rx, ry, dir)) == END) {
                        isRedEnded = true;
                    }
                    unblock(isBlueEnded, by, bx);
                }
            } else {
                if ((rx = move(rx, ry, dir)) == END) {
                    isRedEnded = true;
                }
                if ((bx = move(bx, by, dir)) == END) {
                    isBlueEnded= true;
                }                    
            }
        }

        if (isBlueEnded) {
            return FAIL;
        } else if (isRedEnded) {
            return 1;
        }

        return dir < 2 ? 1 + min(minMovement(rx, ry, bx, by, depth, 2), minMovement(rx, ry, bx, by, depth, 3)) : 1 + min(minMovement(rx, ry, bx, by, depth, 0), minMovement(rx, ry, bx, by, depth, 1));
    }

    public static int movementCount(int rx, int ry, int bx, int by) {        
        return min(minMovement(rx, ry, bx, by, 0, 0),
                minMovement(rx, ry, bx, by, 0, 1),
                minMovement(rx, ry, bx, by, 0, 2),
                minMovement(rx, ry, bx, by, 0, 3)
                );
    }

    public static void main(String[] args) throws Exception {
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

       String spec = br.readLine();
       String[] specs = spec.split(" ");
       height = Integer.parseInt(specs[0]);
       width = Integer.parseInt(specs[1]);

       board = new char[height][width];
       int idx;
       int rx = 0, ry = 0, bx = 0, by = 0;

       for (int i = 0; i < height; i++) {
           String currentLine = br.readLine();
           
           idx = currentLine.indexOf('R');
           if (idx != -1) {
               currentLine.replace('R', '.');
               rx = idx;
               ry = i;
           }

           idx = currentLine.indexOf('B');
           if (idx != -1) {
               currentLine.replace('B', '.');
               bx = idx;
               by = i;
           }

           board[i] = currentLine.toCharArray();
       }
       int count = movementCount(rx, ry, bx, by);
       if (count >= FAIL) {
           count = -1;
       }
       System.out.println(count);

       br.close();
    }
}

/* testcases
- count depth to prevent infinite loop 

4 5
#####
#RBO#
##.##
#####
2: down > right
- even R does not move at first, it can be a solution

5 9
#########
##......#
##.#.#O##
#.B.R####
#########
5? WHY? 
 */