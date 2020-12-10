package day3;

import IO.ReadFile;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Day3Problem2 {

    private static final List<Integer[]> slopes = Arrays.asList(
            new Integer[] {1, 1},
            new Integer[] {3, 1},
            new Integer[] {5, 1},
            new Integer[] {7, 1},
            new Integer[] {1, 2}
    );

    private static final List<Integer> results = new ArrayList<>();

    public static void main(String[] args) {

        List<String> lines = ReadFile.readFile("day3_input.in");

        for (Integer[] slope : slopes) {

            int dx = slope[0];
            int dy = slope[1];
            int width = lines.get(0).length();
            int x = 0;
            int trees = 0;

            for (int y = dy; y < lines.size(); y += dy) {
                x = (x + dx) % width;
                if (lines.get(y).charAt(x) == '#') trees++;
            }

            results.add(trees);
        }
        long result = 1;
        for (Integer i : results) {

            result *= i;
        }
        System.out.println(result);
    }
}
