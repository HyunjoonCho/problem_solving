import java.io.*;
import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.toList;

class RansomNoteResult {

    /*
     * Complete the 'checkMagazine' function below.
     *
     * The function accepts following parameters:
     *  1. STRING_ARRAY magazine
     *  2. STRING_ARRAY note
     */

    public static void checkMagazine(List<String> magazine, List<String> note) {
        // Write your code here
        Map<String, Integer> magazineWordCount = new HashMap<>();
        for (String word : magazine) {
            if (!magazineWordCount.containsKey(word)) {
                magazineWordCount.put(word, 1);
            } else {
                magazineWordCount.put(word, magazineWordCount.get(word) + 1);
            }
        }

        for (String word : note) {
            if (!magazineWordCount.containsKey(word) || magazineWordCount.get(word) == 0) {
                System.out.println("No");
                return;
            } else {
                magazineWordCount.put(word, magazineWordCount.get(word) - 1);
            }
        }
        System.out.println("Yes");
    }

}

public class RansomNote {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int m = Integer.parseInt(firstMultipleInput[0]);

        int n = Integer.parseInt(firstMultipleInput[1]);

        List<String> magazine = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .collect(toList());

        List<String> note = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .collect(toList());

        RansomNoteResult.checkMagazine(magazine, note);

        bufferedReader.close();
    }
}
