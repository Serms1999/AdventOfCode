package day14;

import IO.ReadFile;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.SplittableRandom;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day14Problem1 {

    private static final String RE_MASK = "mask = ([0|1|X]{36})";
    private static final String RE_MEM = "mem\\[(\\d{1,})\\] = (\\d{1,})";

    private static long applyMask(String mask, String value) {

        char[] valueArray = String.format("%36s", Integer.toBinaryString(Integer.parseInt(value))).
                replaceAll(" ", "0").toCharArray();
        for (int i = 0; i < mask.length(); i++) {

            char bit = mask.charAt(i);
            if (bit != 'X') {

                valueArray[i] = bit;
            }
        }
        return Long.parseLong(String.valueOf(valueArray), 2);
    }

    public static void main(String[] args) {

        Map<Long, Long> memory = new HashMap<>();
        String actualMask = null;
        long addr, value;

        Pattern pat_mask = Pattern.compile(RE_MASK);
        Pattern pat_mem = Pattern.compile(RE_MEM);
        Matcher mat_mask, mat_mem;

        List<String> lines = ReadFile.readFile("day14_input.in");
        for (String line : lines) {

            mat_mask = pat_mask.matcher(line);
            if (mat_mask.find()) {

                actualMask = mat_mask.group(1);
            }
            else {

                mat_mem = pat_mem.matcher(line);
                if (mat_mem.find()) {
                    addr = Long.parseLong(mat_mem.group(1));
                    value = applyMask(actualMask,mat_mem.group(2));
                    memory.put(addr, value);
                }
            }
        }
        long result = memory.values().stream().reduce(0L, Long::sum);
        System.out.println(result);
    }
}
