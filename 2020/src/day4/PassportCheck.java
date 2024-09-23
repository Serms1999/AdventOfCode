package day4;

import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class PassportCheck {

    private static final String RE_BYR = "^\\d{4}$";
    private static final String RE_IYR = "^\\d{4}$";
    private static final String RE_EYR = "^\\d{4}$";
    private static final String RE_HGT = "((\\d{3})(cm)|(\\d{2})(in))";
    private static final String RE_HCL = "#(\\d|[a-f]){6}";
    private static final String RE_ECL = "amb|blu|brn|gry|grn|hzl|oth";
    private static final String RE_PID = "^\\d{9}$";
    private static final String RE_CID = ".*";

    private static final byte DATA_BYR = 1;
    private static final byte DATA_IYR = 2;
    private static final byte DATA_EYR = 3;
    private static final byte DATA_HGT = 4;
    private static final byte DATA_HCL = 5;
    private static final byte DATA_ECL = 6;
    private static final byte DATA_PID = 7;
    private static final byte DATA_CID = 8;

    private final Map<String, Boolean> passportCheck = new HashMap<String, Boolean>() {{

        put("byr", false);
        put("iyr", false);
        put("eyr", false);
        put("hgt", false);
        put("hcl", false);
        put("ecl", false);
        put("pid", false);
        put("cid", true);
    }};

    private final Map<String, String> passportData = new HashMap<String, String>() {{

        put("byr", RE_BYR);
        put("iyr", RE_IYR);
        put("eyr", RE_EYR);
        put("hgt", RE_HGT);
        put("hcl", RE_HCL);
        put("ecl", RE_ECL);
        put("pid", RE_PID);
        put("cid", RE_CID);
    }};

    private final Map<String, Byte> passportKeys = new HashMap<String, Byte>() {{

        put("byr", DATA_BYR);
        put("iyr", DATA_IYR);
        put("eyr", DATA_EYR);
        put("hgt", DATA_HGT);
        put("hcl", DATA_HCL);
        put("ecl", DATA_ECL);
        put("pid", DATA_PID);
        put("cid", DATA_CID);
    }};

    public void setProperty(String property, boolean bool) {

        passportCheck.put(property, bool);
    }

    public boolean setPropertyWithCheck(String property, String value) {

        Matcher mat_value = Pattern.compile(passportData.get(property)).matcher(value);
        if(!mat_value.find())
            return false;

        boolean valid = true;
        switch (passportKeys.get(property)) {

            case DATA_BYR: {
                int year = Integer.parseInt(mat_value.group(0));
                valid = year >= 1920 && year <= 2002;
                break;
            }
            case DATA_IYR: {
                int year = Integer.parseInt(mat_value.group(0));
                valid = year >= 2010 && year <= 2020;
                break;
            }
            case DATA_EYR: {
                int year = Integer.parseInt(mat_value.group(0));
                valid = year >= 2020 && year <= 2030;
                break;
            }
            case DATA_HGT: {
                try {
                    int number = Integer.parseInt(mat_value.group(2));
                    valid = number >= 150 && number <= 193;
                } catch (Exception e) {
                    int number = Integer.parseInt(mat_value.group(4));
                    valid = number >= 59 && number <= 76;
                }
                break;
            }
        }
        passportCheck.put(property, valid);
        return valid;
    }

    public boolean getValid() {

        return passportCheck.values().stream().reduce(true, (a, b) -> a && b);
    }
}
