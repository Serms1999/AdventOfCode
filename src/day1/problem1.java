package day1;


import IO.ReadFile;

import java.util.List;
import java.util.stream.Collectors;

public class problem1 {

    public static void main(String[] args) {

        List<Integer> lines = ReadFile.readFile("day1_input1.in").stream()
                .map(Integer::parseInt)
                .collect(Collectors.toList());

        boolean end = false;
        int i, j;
        for (i = 0; i < lines.size() && !end; i++)
            for (j = 0; j < i & !end; j++)
                if ((lines.get(i) + lines.get(j)) == 2020) {
                    System.out.println(lines.get(i) * lines.get(j));
                    end = true;
                }

        if (i == lines.size())
            System.out.println("No se ha encontrado");
    }
}
