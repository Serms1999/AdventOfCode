package day10;

import IO.ReadFile;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class Day10Problem2 {

    public static void main(String[] args) {

        List<Integer> adapters = ReadFile.readFile("day10_input.in").stream()
                .map(Integer::parseInt)
                .sorted(Comparator.naturalOrder())
                .collect(Collectors.toList());

        adapters.add(0, 0);
        adapters.add(adapters.size(), adapters.get(adapters.size() - 1) + 3);

        long[] paths = new long[adapters.get(adapters.size() - 1) + 1];
        Arrays.fill(paths, 0);
        paths[0] = 1;

        for (int i = 1; i < paths.length; i++) {

            for (int diff = 1; diff <= 3; diff++)
                if (adapters.contains(i - diff))
                    paths[i] += paths[i - diff];
        }

        System.out.println(paths[paths.length - 1]);
    }
}
