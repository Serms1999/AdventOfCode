package day9;

import IO.ReadFile;

import java.util.List;
import java.util.stream.Collectors;

public class Day9Problem1 {

    public static void main(String[] args) {

        List<Long> nums = ReadFile.readFile("day9_input.in").stream()
                .map(Long::parseLong).collect(Collectors.toList());

        boolean found = false;
        int preambleLenght = 25;

        int i;
        for (i = preambleLenght; i < nums.size(); i++) {

            found = false;
            for(int j = i - (preambleLenght - 1); j < i && !found; j++) {

                for (int k = i - preambleLenght; k < j && !found; k++) {

                    long numI = nums.get(i);
                    long numJ = nums.get(j);
                    long numK = nums.get(k);
                    if ((numJ + numK) == numI) {
                        found = true;
                    }
                }
            }
            if (!found) break;
        }
        if (!found)
            System.out.println(nums.get(i));
    }
}
