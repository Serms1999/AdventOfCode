package day2;

import IO.ReadFile;

import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day2Problem2 {

    private static final String RE_PASSWORD_POLICY = "([0-9]*)-([0-9]*) ([a-z]): ([a-z]*)";

    public static void main(String[] args) {

        List<String> lines = (ReadFile.readFile("day2_input.in"));

        Pattern patPasswordPolicy = Pattern.compile(RE_PASSWORD_POLICY);
        Matcher matPasswordPolicy;

        int minValue = 0;
        int maxValue = 0;
        int count = 0;
        String letter = null;
        String password = null;
        for (String line : lines) {

            matPasswordPolicy = patPasswordPolicy.matcher(line);
            if(matPasswordPolicy.find()){

                minValue = Integer.parseInt(matPasswordPolicy.group(1)) - 1;
                maxValue = Integer.parseInt(matPasswordPolicy.group(2)) - 1;
                letter = matPasswordPolicy.group(3);
                password = matPasswordPolicy.group(4);
            }

            assert password != null;
            if (String.valueOf(password.charAt(minValue)).equals(letter) ^
                String.valueOf(password.charAt(maxValue)).equals(letter)) count++;
        }

        System.out.println(count);
    }
}
