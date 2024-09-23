package day6;

import IO.ReadFile;

import java.util.Arrays;
import java.util.List;

public class Day6Problem2 {

    public static void main(String[] args) {

        List<String> lines = ReadFile.readFile("day6_input.in");
        int[] questions = new int[26];
        int count = 0;
        int people;
        String line;
        for (int i = 0; i < lines.size(); i++) {

            line = lines.get(i);
            Arrays.fill(questions, 0);
            people = 0;
            do {
                people++;
                for (int j = 0; j < line.length(); j++)
                    questions[line.charAt(j) - 'a']++;

                i++;
            } while (i < lines.size() && !((line = lines.get(i)).equals("")));
            for (int question : questions)
                if (people == question)
                    count += 1;
        }
        System.out.println(count);
    }
}
