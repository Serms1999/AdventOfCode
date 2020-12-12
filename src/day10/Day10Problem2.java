package day10;

import IO.ReadFile;

import java.util.List;
import java.util.stream.Collectors;

public class Day10Problem2 {

    List<Integer> adapters = ReadFile.readFile("day10_input.in").stream()
            .map(Integer::parseInt).collect(Collectors.toList());

    Tree tree = new Tree();

}
