package day15;

import IO.ReadFile;

import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day15Problem1 {

    private static final String RE_NUM = "(\\d+)(.*)";

    private static int mostRecent(int[] array, int value, int index) {

        boolean found = false;
        int i;
        for (i = index - 1; i > -1 && !found;) {

            if (array[i] == value) found = true;
            else i--;
        }
        if (found) return i + 1;
        return 0;
    }

    public static void main(String[] args) {

        int[] numberSpoken = new int[2020];

        List<String> input = ReadFile.readFile("day15_input.in");
        Pattern pat = Pattern.compile(RE_NUM);
        Matcher mat;
        int cont = 0;
        for (String s : input) {

            mat = pat.matcher(s);
            while (mat.find()) {

                numberSpoken[cont++] = Integer.parseInt(mat.group(1));
                mat = pat.matcher(mat.group(2));
            }
        }

        for (int i = cont; i < numberSpoken.length; i++) {

            int lastNumber = numberSpoken[i-1];
            int recent = mostRecent(numberSpoken, lastNumber, i-1);
            if (recent > 0) numberSpoken[i] = i - recent;
            else numberSpoken[i] = recent;
        }
        System.out.println(numberSpoken[numberSpoken.length - 1]);
    }
}
