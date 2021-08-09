import java.io.*;
import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.toList;

public class CountTriplets {

    // Complete the countTriplets function below.
    static long countTriplets(List<Long> arr, long r) {
        Map<Long, Long> secondValCounts = new HashMap<>();
        Map<Long, Long> thirdValCounts = new HashMap<>();

        long count = 0;
        for (long elem : arr) {
            if (thirdValCounts.containsKey(elem)) {
                count += thirdValCounts.get(elem);
            }
            if (secondValCounts.containsKey(elem)) {
                thirdValCounts.put(elem * r, thirdValCounts.containsKey(elem * r)? 
                                    thirdValCounts.get(elem * r) + secondValCounts.get(elem) : secondValCounts.get(elem));
            }
            secondValCounts.put(elem * r, secondValCounts.containsKey(elem * r)? secondValCounts.get(elem * r) + 1 : 1);
        }

        return count;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String[] nr = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int n = Integer.parseInt(nr[0]);

        long r = Long.parseLong(nr[1]);

        List<Long> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Long::parseLong)
            .collect(toList());

        long ans = countTriplets(arr, r);

        System.out.println(String.valueOf(ans));

        bufferedReader.close();
    }
}
