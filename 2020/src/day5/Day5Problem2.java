package day5;

import IO.ReadFile;

import java.util.ArrayList;
import java.util.List;

public class Day5Problem2 {

    public static void main(String[] args) {

        List<String> lines = ReadFile.readFile("day5_input.in");
        List<Integer> sits = new ArrayList<>();

        for (String line : lines) {

            int rowStart = 0;
            int colStart = 0;
            int rowEnd = 127;
            int colEnd = 7;

            for (int i = 0; i < 7; i++) {

                switch (line.charAt(i)) {

                    case 'F': {
                        rowEnd = (rowEnd - rowStart) / 2 + rowStart;
                        break;
                    }
                    case 'B': {
                        rowStart = (rowEnd - rowStart) / 2 + rowStart + 1;
                        break;
                    }
                }
            }
            for (int i = 7; i < 10; i++) {

                switch (line.charAt(i)) {

                    case 'L': {
                        colEnd = (colEnd - colStart) / 2 + colStart;
                        break;
                    }
                    case 'R': {
                        colStart = (colEnd - colStart) / 2 + colStart + 1;
                        break;
                    }
                }
            }
            sits.add(rowStart * 8 + colStart);
        }
        int min = sits.stream().reduce(Integer.MAX_VALUE, Integer::min);
        int max = sits.stream().reduce(Integer.MIN_VALUE, Integer::max);
        for (int i = min + 1; i < max; i ++)
            if (!sits.contains(i))
                System.out.println(i);
    }
}
