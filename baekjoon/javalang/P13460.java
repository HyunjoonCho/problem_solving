package javalang;

import java.io.BufferedReader;
import java.io.InputStreamReader;

class P13460 {
    static int height, width;
    static char[][] board;
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

    public static int moveUp(int x, int y) {
        char currentPos;
        while ((currentPos = board[--y][x]) != '#') {
            if (currentPos == 'O') {
                return END;
            }
        }
        return y + 1;
    }

    public static int moveDown(int x, int y) {
        char currentPos;
        while ((currentPos = board[++y][x]) != '#') {
            if (currentPos == 'O') {
                return END;
            }
        }
        return y - 1;
    }

    public static int moveLeft(int x, int y) {
        char currentPos;
        while ((currentPos = board[y][--x]) != '#') {
            if (currentPos == 'O') {
                return END;
            }
        }
        return x + 1;
    }

    public static int moveRight(int x, int y) {
        char currentPos;
        while ((currentPos = board[y][++x]) != '#') {
            if (currentPos == 'O') {
                return END;
            }
        }
        return x - 1;
    }

    public static int minMovementUp(int rx, int ry, int bx, int by, int depth) {
        if (depth++ >= 10) {
            return FAIL;
        }

        boolean redEnd = false;
        boolean blueEnd = false;

        if (rx == bx) {
            if (ry - 1 == by && board[by - 1][bx] == '#') {
                return FAIL;
            }
            if (ry < by) {
                if ((ry = moveUp(rx, ry)) == END) {
                    redEnd = true;
                }
                if (!redEnd) {
                    board[ry][rx] = '#';
                }
                if ((by = moveUp(bx, by)) == END) {
                    blueEnd = true;
                }
                if (!redEnd) {
                    board[ry][rx] = '.';
                }
            } else {
                if ((by = moveUp(bx, by)) == END) {
                    blueEnd = true;
                }
                if (!blueEnd) {
                    board[by][bx] = '#';
                }
                if ((ry = moveUp(rx, ry)) == END) {
                    redEnd= true;
                }
                if (!blueEnd) {
                    board[by][bx] = '.';
                }
            }
        } else {
            if ((ry = moveUp(rx, ry)) == END) {
                redEnd = true;
            }
            if ((by = moveUp(bx, by)) == END) {
                blueEnd = true;
            }
        }
        
        if (blueEnd) {
            return FAIL;
        } else if (redEnd) {
            return 1;
        }

        return 1 + min(minMovementLeft(rx, ry, bx, by, depth), minMovementRight(rx, ry, bx, by, depth));
    }

    public static int minMovementDown(int rx, int ry, int bx, int by, int depth) {
        if (depth++ >= 10) {
            return FAIL;
        }

        boolean redEnd = false;
        boolean blueEnd = false;

        if (rx == bx) {
            if (ry + 1 == by && board[by + 1][bx] == '#') {
                return FAIL;
            }
            if (ry > by) {
                if ((ry = moveDown(rx, ry)) == END) {
                    redEnd = true;
                }
                if (!redEnd) {
                    board[ry][rx] = '#';
                }
                if ((by = moveDown(bx, by)) == END) {
                    blueEnd = true;
                }
                if (!redEnd) {
                    board[ry][rx] = '.';
                }
            } else {
                if ((by = moveDown(bx, by)) == END) {
                    blueEnd = true;
                }
                if (!blueEnd) {
                    board[by][bx] = '#';
                }
                if ((ry = moveDown(rx, ry)) == END) {
                    redEnd= true;
                }
                if (!blueEnd) {
                    board[by][bx] = '.';
                }
            }
        } else {
            if ((ry = moveDown(rx, ry)) == END) {
                redEnd = true;
            }
            if ((by = moveDown(bx, by)) == END) {
                blueEnd = true;
            }
        }
        
        if (blueEnd) {
            return FAIL;
        } else if (redEnd) {
            return 1;
        }

        return 1 + min(minMovementLeft(rx, ry, bx, by, depth), minMovementRight(rx, ry, bx, by, depth));
    }

    public static int minMovementLeft(int rx, int ry, int bx, int by, int depth) {
        if (depth++ >= 10) {
            return FAIL;
        }

        boolean redEnd = false;
        boolean blueEnd = false;

        if (ry == by) {
            if (rx - 1 == bx && board[by][bx - 1] == '#') {
                return FAIL;
            }
            if (rx < bx) {
                if ((rx = moveLeft(rx, ry)) == END) {
                    redEnd = true;
                }
                if (!redEnd){
                    board[ry][rx] = '#';
                }
                if ((bx = moveLeft(bx, by)) == END) {
                    blueEnd = true;
                }
                if (!redEnd) {
                    board[ry][rx] = '.';
                }
            } else {
                if ((bx = moveLeft(bx, by)) == END) {
                    blueEnd = true;
                }
                if (!blueEnd) {
                    board[by][bx] = '#';
                }
                if ((rx = moveLeft(rx, ry)) == END) {
                    redEnd= true;
                }
                if (!blueEnd) {
                    board[by][bx] = '.';
                }
            }
        } else {
            if ((rx = moveLeft(rx, ry)) == END) {
                redEnd = true;
            }
            if ((bx = moveLeft(bx, by)) == END) {
                blueEnd = true;
            }
        }
        
        if (blueEnd) {
            return FAIL;
        } else if (redEnd) {
            return 1;
        }

        return 1 + min(minMovementUp(rx, ry, bx, by, depth), minMovementDown(rx, ry, bx, by, depth));
    }

    public static int minMovementRight(int rx, int ry, int bx, int by, int depth) {
        if (depth++ >= 10) {
            return FAIL;
        }

        boolean redEnd = false;
        boolean blueEnd = false;

        if (ry == by) {
            if (rx + 1 == bx && board[by][bx + 1] == '#') {
                return FAIL;
            }
            if (rx > bx) {
                if ((rx = moveRight(rx, ry)) == END) {
                    redEnd = true;
                } 
                if (!redEnd) {
                    board[ry][rx] = '#';
                }
                if ((bx = moveRight(bx, by)) == END) {
                    blueEnd = true;
                }
                if (!redEnd) {
                    board[ry][rx] = '.';
                }
            } else {
                if ((bx = moveRight(bx, by)) == END) {
                    blueEnd = true;
                }
                if (!blueEnd) {
                    board[by][bx] = '#';
                }
                if ((rx = moveRight(rx, ry)) == END) {
                    redEnd= true;
                }
                if (!blueEnd) {
                    board[by][bx] = '.';
                }
            }
        } else {
            if ((rx = moveRight(rx, ry)) == END) {
                redEnd = true;
            }
            if ((bx = moveRight(bx, by)) == END) {
                blueEnd = true;
            }
        }
        
        if (blueEnd) {
            return FAIL;
        } else if (redEnd) {
            return 1;
        }

        return 1 + min(minMovementUp(rx, ry, bx, by, depth), minMovementDown(rx, ry, bx, by, depth));
    }


    public static int movementCount(int rx, int ry, int bx, int by) {        
        return min(minMovementUp(rx, ry, bx, by, 0),
                minMovementDown(rx, ry, bx, by, 0),
                minMovementLeft(rx, ry, bx, by, 0),
                minMovementRight(rx, ry, bx, by, 0)
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