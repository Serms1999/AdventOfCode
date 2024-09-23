package day9;

import IO.ReadFile;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class Day9Problem2 {

    public static void main(String[] args) {

        List<Long> nums = ReadFile.readFile("day9_input.in").stream()
                .map(Long::parseLong).collect(Collectors.toList());

        boolean found;
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
        long number = nums.get(i);
        i = 0;
        found = false;
        List<Long> sublist = new ArrayList<>();
        long number2;
        do {

            for (int j = i + 1; j < nums.size() && !found; j++) {

                sublist = nums.subList(i, j + 1);
                number2 = sublist.stream()
                        .reduce(0L, Long::sum);
                if(number == number2) found = true;
            }
            i++;
        } while (i < nums.size() - 1 && !found);
        long min = sublist.stream().min(Comparator.naturalOrder()).get();
        long max = sublist.stream().max(Comparator.naturalOrder()).get();
        System.out.println(min + max);
    }
}
