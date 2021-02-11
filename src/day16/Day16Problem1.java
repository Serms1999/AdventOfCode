package day16;

import IO.ReadFile;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day16Problem1 {

    private static final List<Pair[]> ranges = new ArrayList<>();
    private static final String RE_RANGE = ".*: (.*) or (.*)";

    private static boolean checkNumberInPair(Pair<Integer, Integer> p, int num) {

        return ((num >= p.getElement0()) && (num <= p.getElement1()));
    }

    private static boolean checkNumber(int num) {

        for (Pair[] aux : ranges) {

            boolean aux2 = false;
            for (int i = 0; i < aux.length; i++) {

                aux2 = aux2 || checkNumberInPair(aux[i], num);
            }
            if (!aux2) return false;
        }
        return true;
    }

    public static void main(String[] args) {

        List<String> lines = ReadFile.readFile("prueba.in");
        List<Integer> invalids = new ArrayList<>();

        Pattern pat = Pattern.compile(RE_RANGE);
        Matcher mat;
        Integer[] aux;

        for (String s : lines.subList(0, lines.indexOf("your ticket:") - 1)) {

            mat = pat.matcher(s);
            if (mat.find()) {

                Pair[] pairs = new Pair[2];
                for (int i = 1; i <= 2; i++) {

                    aux = Arrays.stream(mat.group(i).split("-"))
                            .map(Integer::parseInt)
                            .toArray(Integer[]::new);
                    pairs[i - 1] = Pair.createPair(aux[0], aux[1]);
                }
                ranges.add(pairs);
            }
        }
        for (String s : lines.subList(lines.indexOf("nearby tickets:") + 1, lines.size() - 1)) {

            aux = Arrays.stream(s.split(","))
                    .map(Integer::parseInt)
                    .toArray(Integer[]::new);
            for (int num : aux) {

                if (!checkNumber(num))
                    invalids.add(num);
            }
        }
        int value = invalids.stream().reduce(0, Integer::sum);
        System.out.println(value);
    }
}
