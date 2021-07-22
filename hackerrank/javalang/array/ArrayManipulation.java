import java.io.*;
import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.toList;

class ArrayManipulationResult {

    /*
     * Complete the 'arrayManipulation' function below.
     *
     * The function is expected to return a LONG_INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. 2D_INTEGER_ARRAY queries
     */

    public static long arrayManipulation(int n, List<List<Integer>> queries) {
        // Write your code here
        int[] prefixSum = new int[n + 1];

        for (List<Integer> query : queries) {
            int queryStartIdx = query.get(0) - 1;
            int queryEndIdx = query.get(1);
            int summand = query.get(2);

            prefixSum[queryStartIdx] += summand;
            prefixSum[queryEndIdx] -= summand;
        }

        long currentValue = 0;
        long max = 0;
        for (int i = 0; i < n; i++) {
            currentValue += prefixSum[i];
            if (currentValue > max) {
                max = currentValue;
            }
        }

        return max;
    }

}

public class ArrayManipulation {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int n = Integer.parseInt(firstMultipleInput[0]);

        int m = Integer.parseInt(firstMultipleInput[1]);

        List<List<Integer>> queries = new ArrayList<>();

        IntStream.range(0, m).forEach(i -> {
            try {
                queries.add(
                    Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                        .map(Integer::parseInt)
                        .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        long result = ArrayManipulationResult.arrayManipulation(n, queries);

        System.out.println(String.valueOf(result));

        bufferedReader.close();
    }
}