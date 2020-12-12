package day10;

import IO.ReadFile;

import java.util.*;
import java.util.stream.Collectors;

public class Day10Problem1 {

    public static void main(String[] args) {

        List<Integer> adapters = ReadFile.readFile("day10_input.in").stream()
                .map(Integer::parseInt).collect(Collectors.toList());

        Set<Integer> valids = new HashSet<>();
        List<Integer> aux;
        List<Integer>[] diffs = new List[3];
        for (int i = 0; i < 3; i++)
            diffs[i] = new ArrayList<>();

        valids.add(0);
        boolean found;
        int numEle = adapters.size();
        while (numEle > 0) {

            int diff = 1;
            found = false;
            int element = valids.stream().max(Comparator.naturalOrder()).get();

            do {

                int finalDiff = diff;
                aux = adapters.stream().filter(a -> a - element == finalDiff)
                        .collect(Collectors.toList());
                if (aux.size() > 0) found = true;
                else diff++;
            } while (!found);
            int element2 = aux.get(0);
            valids.add(element2);
            diffs[diff - 1].add(element2);
            numEle--;
        }
        int element = valids.stream().max(Comparator.naturalOrder()).get();
        diffs[2].add(element + 3);
        System.out.println(diffs[0].size() * diffs[2].size());
    }
}
