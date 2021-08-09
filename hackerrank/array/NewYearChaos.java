import java.util.*;

public class NewYearChaos {

    // Complete the minimumBribes function below.
    static void minimumBribes(int[] q) {
        int sumDiff = 0, maskedSwap = 0;
        
        for (int i = 0; i < q.length; i++) {
            if (i < q[i] - 3) {
                System.out.println("Too chaotic");
                return;            
            }
            sumDiff += abs(q[i] - 1, i);
            if (q[i] <= i + 1) {
                // bigger-in-front && smaller-in-backward -> masked swap
                if (i >= 1 && q[i - 1] > q[i]) {
                    for (int j = i + 1; j < q.length; j++) {
                        if (q[j] < q[i]) {
                            maskedSwap++;
                            break;
                        }
                    }                 
                } 
            }
        }
        
        System.out.println(maskedSwap + sumDiff/2);
    }

    private static int abs(int x, int y) {
        return x < y? y - x : x - y;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int t = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int tItr = 0; tItr < t; tItr++) {
            int n = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            int[] q = new int[n];

            String[] qItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int i = 0; i < n; i++) {
                int qItem = Integer.parseInt(qItems[i]);
                q[i] = qItem;
            }

            minimumBribes(q);
        }

        scanner.close();
    }
}
