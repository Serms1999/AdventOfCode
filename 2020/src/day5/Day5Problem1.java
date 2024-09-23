package day5;

import IO.ReadFile;

import java.util.List;

public class Day5Problem1 {

    public static void main(String[] args) {

        List<String> lines = ReadFile.readFile("day5_input.in");
        int sit = 0;

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
            int sitAux = rowStart * 8 + colStart;
            if (sitAux > sit) sit = sitAux;
        }
        System.out.println(sit);
    }
}
