package day3;

import IO.ReadFile;

import java.util.List;

public class Day3Problem1 {

    public static void main(String[] args) {

        List<String> lines = ReadFile.readFile("day3_input.in");

        int width = lines.get(0).length();
        int x = 0;
        int trees = 0;

        for (int y = 1; y < lines.size(); y++) {
            x = (x + 3) % width;
            if (lines.get(y).charAt(x) == '#') trees++;
        }

        System.out.println(trees);
    }
}
