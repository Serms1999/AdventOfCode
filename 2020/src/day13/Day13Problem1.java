package day13;

import IO.ReadFile;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day13Problem1 {

    private static int[] getBuses(String line) {

        List<Integer> aux = new ArrayList<>();

        String RE = "[0-9][0-9]*";
        Pattern pat = Pattern.compile(RE);
        Matcher mat = pat.matcher(line);

        while (mat.find())
            aux.add(Integer.parseInt(mat.group(0)));

        return aux.stream().mapToInt(i->i).toArray();
    }

    public static void main(String[] args) {

        List<String> lines = ReadFile.readFile("day13_input.in");
        int timestamp = Integer.parseInt(lines.get(0));
        int[] buses = getBuses(lines.get(1));

        int busTimeStamp = timestamp;
        int busID = 0;
        boolean found = false;
        do {

            for (int bus = 0; bus < buses.length && !found; bus++) {

                busID = buses[bus];
                if (busTimeStamp % busID == 0)
                    found = true;
            }
            if(!found)
                busTimeStamp++;
        } while (!found);
        System.out.println(busID * (busTimeStamp - timestamp));
    }
}
