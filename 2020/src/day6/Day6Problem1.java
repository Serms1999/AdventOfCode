package day6;

import IO.ReadFile;

import java.util.Arrays;
import java.util.List;

public class Day6Problem1 {

    public static void main(String[] args) {

        List<String> lines = ReadFile.readFile("day6_input.in");
        int[] questions = new int[26];
        int count = 0;
        String line;
        for (int i = 0; i < lines.size(); i++) {

            line = lines.get(i);
            Arrays.fill(questions, 0);
            do {
                for (int j = 0; j < line.length(); j++)
                    questions[line.charAt(j) - 'a'] = 1;

                i++;
            } while (i < lines.size() && !((line = lines.get(i)).equals("")));
            for (int question : questions) count += question;
        }
        System.out.println(count);
    }
}
