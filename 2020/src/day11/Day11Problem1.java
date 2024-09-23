package day11;

import IO.ReadFile;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Day11Problem1 {

    public static int checkOccupied(List<String> sits, int lineIndex, int sitIndex) {

        int sitOccupied = 0;
        String prevLine = null;
        String actualLine;
        String nextLine = null;

        try {
            prevLine = sits.get(lineIndex - 1);
        } catch (Exception e) {}
        actualLine = sits.get(lineIndex);
        try {
            nextLine = sits.get(lineIndex + 1);
        } catch (Exception e) {}

        if (prevLine != null) {

            for (int i = -1; i < 2; i++) {

                try {
                    if (prevLine.charAt(sitIndex + i) == '#')
                        sitOccupied++;
                } catch (Exception e) {}
            }
        }

        for (int i = -1; i < 2; i += 2) {

            try {
                if (actualLine.charAt(sitIndex + i) == '#')
                    sitOccupied++;
            } catch (Exception e) {}
        }

        if (nextLine != null) {

            for (int i = -1; i < 2; i++) {

                try {
                    if (nextLine.charAt(sitIndex + i) == '#')
                        sitOccupied++;
                } catch (Exception e) {}
            }
        }

        return sitOccupied;
    }

    public static void main(String[] args) {

        List<String> lines = ReadFile.readFile("day11_input.in");
        int changeSits;

        do {
            changeSits = 0;
            List<String> linesAux = new ArrayList<>();
            for (String line : lines)
                linesAux.add(String.format("%s",line));

            for (int lineIndex = 0; lineIndex < linesAux.size(); lineIndex++) {

                String line = linesAux.get(lineIndex);
                for (int sitIndex = 0; sitIndex < line.length(); sitIndex++) {

                    char sit = line.charAt(sitIndex);
                    int sitsOccupied = checkOccupied(lines, lineIndex, sitIndex);
                    switch (sit) {

                        case 'L': {
                            if (sitsOccupied == 0) {
                                line = line.substring(0, sitIndex) + '#' + line.substring(sitIndex + 1);
                                changeSits++;
                            }
                            break;
                        }
                        case '#': {
                            if (sitsOccupied >= 4) {
                                line = line.substring(0, sitIndex) + 'L' + line.substring(sitIndex + 1);
                                changeSits++;
                            }
                            break;
                        }
                    }
                }
                linesAux.set(lineIndex, line);
            }
            lines = new ArrayList<>(linesAux);
        } while (changeSits > 0);

        long count = 0;
        for (String line : lines) {
            count += line.chars().filter(c -> c == '#').count();
        }
        System.out.println(count);
    }
}
