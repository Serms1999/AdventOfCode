package day13;

import IO.ReadFile;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day13Problem2 {

    private static int[] getBusesArray(String line) {

        List<Integer> aux = new ArrayList<>();

        String RE = "[0-9][0-9]*";
        Pattern pat = Pattern.compile(RE);
        Matcher mat = pat.matcher(line);

        while (mat.find())
            aux.add(Integer.parseInt(mat.group(0)));

        return aux.stream().mapToInt(i->i).toArray();
    }

    private static Map<Integer, Integer> getBuses(String line) {

        Map<Integer, Integer> nums = new HashMap<>();
        String[] aux = line.split(",");

        for (int i = 0; i < aux.length; i++) {

            try {
                int value = Integer.parseInt(aux[i]);
                nums.put(value, i);
            } catch (Exception ignored) {}
        }
        return Collections.unmodifiableMap(nums);
    }

    public static void main(String[] args) {

        List<String> lines = ReadFile.readFile("day13_input.in");
        Map<Integer, Integer> buses = getBuses(lines.get(1));
        int[] buses2 = getBusesArray(lines.get(1));

        long busTimeStamp = 0;
        long stepSize = buses2[0];

        for (int i = 1; i < buses2.length; i++) {

            int bus = buses2[i];
            while ((busTimeStamp + buses.get(bus)) % bus != 0) {

                busTimeStamp += stepSize;
            }
            stepSize *= bus;
        }

        System.out.println((busTimeStamp));
    }
}
