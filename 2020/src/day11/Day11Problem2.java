package day11;

import IO.ReadFile;

import java.util.ArrayList;
import java.util.List;

public class Day11Problem2 {

    public static int checkOccupied(List<String> sits, int lineIndex, int sitIndex) {

        int sitOccupied = 0;
        boolean found = false;

        // Top
        for (int prevLine = lineIndex - 1; prevLine >= 0 && !found; prevLine--) {

            char sit = sits.get(prevLine).charAt(sitIndex);
            if (sit != '.') {

                found = true;
                if (sit == '#') sitOccupied++;
            }
        }
        found = false;

        // Top Left
        for (int prevLine = lineIndex - 1; prevLine >= 0 && !found && (sitIndex - (lineIndex - prevLine)) >= 0; prevLine--) {

            char sit = sits.get(prevLine).charAt(sitIndex - (lineIndex - prevLine));
            if (sit != '.') {

                found = true;
                if (sit == '#') sitOccupied++;
            }
        }
        found = false;

        // Top Right
        for (int prevLine = lineIndex - 1; prevLine >= 0 && !found && (sitIndex + (lineIndex - prevLine)) < sits.get(lineIndex).length(); prevLine--) {

            char sit = sits.get(prevLine).charAt(sitIndex + (lineIndex - prevLine));
            if (sit != '.') {

                found = true;
                if (sit == '#') sitOccupied++;
            }
        }
        found = false;

        // Left
        for (int prevChar = sitIndex - 1; prevChar >= 0 && !found; prevChar--) {

            char sit = sits.get(lineIndex).charAt(prevChar);
            if (sit != '.') {

                found = true;
                if (sit == '#') sitOccupied++;
            }
        }
        found = false;

        // Right
        for (int nextChar = sitIndex + 1; nextChar < sits.get(lineIndex).length() && !found; nextChar++) {

            char sit = sits.get(lineIndex).charAt(nextChar);
            if (sit != '.') {

                found = true;
                if (sit == '#') sitOccupied++;
            }
        }
        found = false;

        // Down
        for (int nextLine = lineIndex + 1; nextLine < sits.size() && !found; nextLine++) {

            char sit = sits.get(nextLine).charAt(sitIndex);
            if (sit != '.') {

                found = true;
                if (sit == '#') sitOccupied++;
            }
        }
        found = false;

        // Down Left
        for (int nextLine = lineIndex + 1; nextLine < sits.size() && !found && (sitIndex - (nextLine - lineIndex)) >= 0; nextLine++) {

            char sit = sits.get(nextLine).charAt(sitIndex - (nextLine - lineIndex));
            if (sit != '.') {

                found = true;
                if (sit == '#') sitOccupied++;
            }
        }
        found = false;

        // Down Right
        for (int nextLine = lineIndex + 1; nextLine < sits.size() && !found && (sitIndex + (nextLine - lineIndex)) < sits.get(lineIndex).length(); nextLine++) {

            char sit = sits.get(nextLine).charAt(sitIndex + (nextLine - lineIndex));
            if (sit != '.') {

                found = true;
                if (sit == '#') sitOccupied++;
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
                    if (sit != '.') {
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
                                if (sitsOccupied >= 5) {
                                    line = line.substring(0, sitIndex) + 'L' + line.substring(sitIndex + 1);
                                    changeSits++;
                                }
                                break;
                            }
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
