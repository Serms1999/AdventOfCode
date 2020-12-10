package day4;

import IO.ReadFile;

import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day4Problem2 {

    private static final String RE_DATA = "([a-z]*):((#|[0-9]|[a-z])*)";

    public static void main(String[] args) {

        List<String> lines = ReadFile.readFile("day4_input.in");

        int valid = 0;
        PassportCheck p;
        String line, key, value;
        Pattern pat_data = Pattern.compile(RE_DATA);
        Matcher mat_data;
        boolean ok;
        for(int i = 0; i < lines.size(); i++) {

            p = new PassportCheck();
            line = lines.get(i);
            ok = true;
            do {

                if (ok) {
                    mat_data = pat_data.matcher(line);
                    while (mat_data.find() && ok) {

                        key = mat_data.group(1);
                        value = mat_data.group(2);
                        ok = p.setPropertyWithCheck(key, value);
                    }
                }
                i++;
            } while (i < lines.size() && !(line = lines.get(i)).equals(""));
            if(p.getValid()) valid++;
        }
        System.out.println(valid);
    }
}
