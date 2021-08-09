import java.io.*;
import java.util.stream.*;

class TwoStringsResult {

    /*
     * Complete the 'twoStrings' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts following parameters:
     *  1. STRING s1
     *  2. STRING s2
     */

    public static String twoStrings(String s1, String s2) {
        // Write your code here
        boolean[] isCharInString = new boolean[26];
        for (int i = 0; i < 26; i++) {
            isCharInString[i] = false;
        }
        for (char c : s1.toCharArray()) {
            if (!isCharInString[c - 'a']) {
                isCharInString[c - 'a'] = true;
            }
        }
        for (char c : s2.toCharArray()) {
            if (isCharInString[c - 'a']) {
                return "YES";
            }
        }
        return "NO";
    }

}

public class TwoStrings {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int q = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, q).forEach(qItr -> {
            try {
                String s1 = bufferedReader.readLine();

                String s2 = bufferedReader.readLine();

                String result = TwoStringsResult.twoStrings(s1, s2);

                System.out.println(result);
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
    }
}
