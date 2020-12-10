package day2;

import IO.ReadFile;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Problem1 {

    private static final String RE_PASSWORD_POLICY = "([0-9]*)-([0-9]*) ([a-z]): ([a-z]*)";
    private static final List<PasswordPolicy> passwordsPolicys = new ArrayList<>();

    private static void getPasswordsFromLines(List<String> lines) {

        Pattern patPasswodPolicy = Pattern.compile(RE_PASSWORD_POLICY);
        Matcher matPassworPolicy;
        for (String line : lines) {

            matPassworPolicy = patPasswodPolicy.matcher(line);
            if(matPassworPolicy.find()){

                passwordsPolicys.add(
                        new PasswordPolicy(Integer.parseInt(matPassworPolicy.group(1)),
                                Integer.parseInt(matPassworPolicy.group(2)),
                                matPassworPolicy.group(3),
                                matPassworPolicy.group(4)));
            }
        }
    }

    public static void main(String[] args) {

        getPasswordsFromLines(ReadFile.readFile("day2_input1.in"));
    }
}
