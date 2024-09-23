package day12;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Move {

    private static final String RE = "([A-Z])([0-9]*)";

    private char dir;
    private int num;

    public Move(String line) {

        Pattern pat = Pattern.compile(RE);
        Matcher mat = pat.matcher(line);
        if (mat.find()) {

            dir = mat.group(1).charAt(0);
            num = Integer.parseInt(mat.group(2));
        }
    }

    public char getDir() {
        return dir;
    }

    public int getNum() {
        return num;
    }
}
