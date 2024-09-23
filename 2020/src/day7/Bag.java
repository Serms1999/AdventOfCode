package day7;

import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

public class Bag {

    private final String name;
    private final Map<Bag, Integer> bags;

    public Bag(String name) {

        this.name = name;
        bags = new HashMap<>();
    }

    public String getName() {
        return name;
    }

    public void addBag(Bag bag, int num) {

        if (bags.containsKey(bag)) {
            bags.put(bag, bags.get(bag) + num);
        }
        else bags.put(bag,num);
    }

    public void addBag(Bag bag) {

        bags.put(bag, 0);
    }

    public boolean canContainShinyGold() {

        if (name.equals("shiny gold"))
            return true;

        return bags.keySet().stream().map(Bag::canContainShinyGold)
                .reduce(false, (a, b) -> a || b);
    }

    public int getCapacity() {

        int count = 0;
        for (Bag b : bags.keySet()) {

            int instances = bags.get(b);
            count += instances * b.getCapacity();
        }
        return count + 1;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Bag bag = (Bag) o;
        return Objects.equals(name, bag.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name);
    }
}
