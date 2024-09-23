package day14;

import IO.ReadFile;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day14Problem2 {

    private static final String RE_MASK = "mask = ([0|1|X]{36})";
    private static final String RE_MEM = "mem\\[(\\d{1,})\\] = (\\d{1,})";

    private static List<Integer> getFloatingIndexes(String s) {

        List<Integer> list = new ArrayList<Integer>();
        char character = 'X';
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == character){
                list.add(i);
            }
        }
        return Collections.unmodifiableList(list);
    }

    private static List<Long> getAddrWithFloating(char[] addr) {

        List<Integer> indexes = getFloatingIndexes(String.valueOf(addr));
        String format = String.format("%%%ds", indexes.size());
        List<Long> addresses = new ArrayList<>();
        for (int i = 0; i < Math.pow(2,indexes.size()); i++) {

            char[] replace = String.format(format, Integer.toBinaryString(i)).
                    replaceAll(" ", "0").toCharArray();
            int cont = 0;
            for (int index : indexes) {

                addr[index] = replace[cont++];
            }
            addresses.add(Long.parseLong(String.valueOf(addr),2));
        }
        return Collections.unmodifiableList(addresses);
    }

    private static List<Long> applyMask(String mask, String addr) {

        char[] valueArray = String.format("%36s", Integer.toBinaryString(Integer.parseInt(addr))).
                replaceAll(" ", "0").toCharArray();
        for (int i = 0; i < mask.length(); i++) {

            char bit = mask.charAt(i);
            if (bit != '0') {

                valueArray[i] = bit;
            }
        }
        return getAddrWithFloating(valueArray);
    }

    public static void main(String[] args) {

        Map<Long, Long> memory = new HashMap<>();
        String actualMask = null;
        List<Long> addresses;
        long value;

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
                    addresses = applyMask(actualMask,mat_mem.group(1));
                    value = Long.parseLong(mat_mem.group(2));
                    for (long addr : addresses)
                        memory.put(addr, value);
                }
            }
        }
        long result = memory.values().stream().reduce(0L, Long::sum);
        System.out.println(result);
    }
}
