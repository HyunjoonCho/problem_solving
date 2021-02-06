import java.io.*;

public class CountingValleys {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int steps = Integer.parseInt(bufferedReader.readLine().trim());

        String path = bufferedReader.readLine();

        int result = countingValleys(steps, path);

        System.out.println(result);

        bufferedReader.close();
    }

    public static int countingValleys(int steps, String path) {
        // Write your code here
        int altitude = 0;
        int valleyCount = 0;

        for (int i = 0; i < steps; i++) {
            if (path.charAt(i) == 'D') {
                if (altitude == 0) {
                    valleyCount++;
                }
                altitude--;
            } else {
                altitude++;
            }
        }
        return valleyCount;
    }
}