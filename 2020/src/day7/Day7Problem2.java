package day7;

import IO.ReadFile;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day7Problem2 {

    private static final String RE_FULL_EXPRESSION = "([a-z]* [a-z]*) bags contain (.*)\\.";
    private static final String RE_BAGS = "(\\d) ([a-z]* [a-z]*)";

    public static void main(String[] args) {

        List<String> lines = ReadFile.readFile("day7_input.in");
        Set<Bag> bags = new HashSet<>();

        Pattern patFullExp = Pattern.compile(RE_FULL_EXPRESSION);
        Pattern patBags = Pattern.compile(RE_BAGS);
        Matcher matFullExp, matBags;

        String bag;
        Bag b, b2;
        int num;

        for (String line : lines) {

            matFullExp = patFullExp.matcher(line);
            if (matFullExp.find()) {

                bag = matFullExp.group(1);
                b = new Bag(bag);
                if (!bags.add(b)) {

                    String finalBag = bag;
                    b = bags.stream().filter(a -> a.getName().equals(finalBag))
                            .findAny().orElse(null);
                }

                matBags = patBags.matcher(matFullExp.group(2));
                while (matBags.find()) {

                    num = Integer.parseInt(matBags.group(1));
                    b2 = new Bag(matBags.group(2));
                    if (!bags.add(b2)) {

                        String finalBag = matBags.group(2);
                        b2 = bags.stream().filter(a -> a.getName().equals(finalBag))
                                .findAny().orElse(null);
                    }
                    if (b != null)
                        b.addBag(b2, num);
                }
            }
        }
        b = bags.stream().filter(a -> a.getName().equals("shiny gold"))
                .findAny().orElse(null);
        System.out.println(b.getCapacity() - 1);
    }
}
