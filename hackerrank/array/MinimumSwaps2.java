import java.io.*;
import java.util.*;

public class MinimumSwaps2 {

    // Complete the minimumSwaps function below.
    static int minimumSwaps(int[] arr) {
        int swapCount = 0;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != i + 1) {
                int j = i, nextIdx;
                while (true) {
                    nextIdx = arr[j] - 1;
                    arr[j] = j + 1;
                    j = nextIdx;
                    swapCount++;
                    if (arr[j] == i + 1) {
                        arr[j] = j + 1;
                        break;
                    }
                }
            }
        }
        return swapCount;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] arr = new int[n];

        String[] arrItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int arrItem = Integer.parseInt(arrItems[i]);
            arr[i] = arrItem;
        }

        int res = minimumSwaps(arr);

        System.out.println(String.valueOf(res));

        scanner.close();
    }
}