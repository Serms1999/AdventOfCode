package day15;

import IO.ReadFile;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day15Problem2 {

    private static final String RE_NUM = "(\\d+)(.*)";

    public static void main(String[] args) {

        int[] numberSpoken = new int[30000000];
        Map<Integer, Integer> lastOccurrence = new HashMap<>();

        List<String> input = ReadFile.readFile("day15_input.in");
        Pattern pat = Pattern.compile(RE_NUM);
        Matcher mat;
        int cont = 0;
        for (String s : input) {

            mat = pat.matcher(s);
            while (mat.find()) {

                numberSpoken[cont] = Integer.parseInt(mat.group(1));
                lastOccurrence.put(numberSpoken[cont], ++cont);
                mat = pat.matcher(mat.group(2));
            }
        }

        for (int i = cont; i < numberSpoken.length; i++) {

            int lastNumber = numberSpoken[i-1];
            int recent;
            try {
                recent = lastOccurrence.get(lastNumber);
            } catch (Exception e) {
                recent = 0;
                lastOccurrence.put(lastNumber, 0);
            }
            if (recent > 0) numberSpoken[i] = i - recent;
            else numberSpoken[i] = recent;
            lastOccurrence.put(numberSpoken[i-1], i);
        }
        System.out.println(numberSpoken[numberSpoken.length - 1]);
    }
}
