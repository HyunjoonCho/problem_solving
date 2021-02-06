import java.io.*;
import java.util.*;

public class RepeatedString {

    // Complete the repeatedString function below.
    static long repeatedString(String s, long n) {
        long remnant = n % s.length();
        
        long unitCount = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'a') {
                unitCount++;
            }
        }
        
        long remnantCount = 0;
        for (int i = 0; i < remnant; i++) {
            if (s.charAt(i) == 'a') {
                remnantCount++;
            }            
        }
        
        return (n / s.length()) * unitCount + remnantCount;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        String s = scanner.nextLine();

        long n = scanner.nextLong();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        long result = repeatedString(s, n);
        System.out.println(result);

        scanner.close();
    }
}