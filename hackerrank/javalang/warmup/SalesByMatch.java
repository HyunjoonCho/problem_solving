import java.io.*;
import java.util.*;

public class SalesByMatch {

    // Complete the sockMerchant function below.
    static int sockMerchant(int n, int[] ar) {
        int[] sockCounts = new int[100];
        for (int i = 0; i < 100; i++) {
            sockCounts[i] = 0;
        }
        
        for (int sock : ar) {
            sockCounts[sock - 1]++;
        }

        int numPairs = 0; 
        for (int sockCount : sockCounts) {
            numPairs += sockCount/2;
        }
        return numPairs;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] ar = new int[n];

        String[] arItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int arItem = Integer.parseInt(arItems[i]);
            ar[i] = arItem;
        }

        int result = sockMerchant(n, ar);

        System.out.println(result);

        scanner.close();
    }
}