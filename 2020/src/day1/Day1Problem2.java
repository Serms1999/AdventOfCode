package day1;

import IO.ReadFile;

import java.util.List;
import java.util.stream.Collectors;

public class Day1Problem2 {

    public static void main(String[] args) {

        List<Integer> lines = ReadFile.readFile("day1_input.in").stream()
                .map(Integer::parseInt)
                .collect(Collectors.toList());

        boolean end = false;
        int i, j, k;
        for (i = 0; i < lines.size() && !end; i++)
            for (j = 0; j < i & !end; j++)
                for (k = 0; k < j && !end; k++)
                    if ((lines.get(i) + lines.get(j) + lines.get(k)) == 2020) {
                        System.out.println(lines.get(i) * lines.get(j) * lines.get(k));
                        end = true;
                    }

        if (i == lines.size())
            System.out.println("Not Found");
    }
}
