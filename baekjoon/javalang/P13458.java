package javalang;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class P13458 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int numTestSite = Integer.parseInt(br.readLine());
        int[] numTestTaker = new int[numTestSite];
        String[] numTestTakerString = br.readLine().split(" ");
        for (int i = 0; i < numTestSite; i++) {
            numTestTaker[i] = Integer.parseInt(numTestTakerString[i]);
        }

        String[] capacityString = br.readLine().split(" ");
        int capacityProctor = Integer.parseInt(capacityString[0]);
        int capacitySubProctor = Integer.parseInt(capacityString[1]);

        long totalProctor = 0L;
        for (int num : numTestTaker) {
            totalProctor++;
            if (num > capacityProctor) {
                num -= capacityProctor;
                totalProctor += num % capacitySubProctor == 0 ? num / capacitySubProctor : num / capacitySubProctor + 1;
            }
        } 
        System.out.println(totalProctor);

        br.close();
    }
}

/*
1,000,000 * 1,000,000 = out of int range
 */