import java.io.*;
import java.util.stream.*;
import java.util.*;

class SherlockAndAnagramsResult {

    /*
     * Complete the 'sherlockAndAnagrams' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts STRING s as parameter.
     */
    public static int recursiveAnagramCount(char[] chars, int x, int y, int currentLength) {
        if (x == y) return 0;

        int count = 1; // anagram of current length, starting from x and y individually        
        System.out.printf("%d %d %d\n", x, y, currentLength);
        if (x > 0) {
            if (y > 0 && chars[x - 1] == chars[y - 1]) {
                count += recursiveAnagramCount(chars, x - 1, y - 1, currentLength + 1);
            } else if ((y + currentLength) < chars.length && chars[x - 1] == chars[y + currentLength]) {
                count += recursiveAnagramCount(chars, x - 1, y, currentLength + 1);
            }
        } else if ((x + currentLength) < chars.length) {
            if (y > 0 && chars[x + currentLength] == chars[y - 1]) {
                count += recursiveAnagramCount(chars, x, y - 1, currentLength + 1);
            } else if ((y + currentLength) < chars.length && chars[x + currentLength] == chars[y + currentLength]) {
                count += recursiveAnagramCount(chars, x - 1, y, currentLength + 1);
            }
        }

        return count;
    }

    public static int sherlockAndAnagrams(String s) {
        // Write your code here
        int totalCount = 0;
        char[] chars = s.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            for (int j = i + 1; j < chars.length; j++) {
                if (chars[i] == chars[j]) {
                    totalCount += recursiveAnagramCount(chars, i, j, 1);
                }
            }
        }

        return totalCount;
    }
}

public class SherlockAndAnagrams {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int q = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, q).forEach(qItr -> {
            try {
                String s = bufferedReader.readLine();

                int result = SherlockAndAnagramsResult.sherlockAndAnagrams(s);

                System.out.println(String.valueOf(result));
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
    }
}