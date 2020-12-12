package day10;

public class Node {

    private int value;
    private Node diff1;
    private Node diff2;
    private Node diff3;

    public Node (int value) {

        this.value = value;
        diff1 = null;
        diff2 = null;
        diff3 = null;
    }

    public void addNode(int diff, int value) {

        switch (diff) {
            case 1: {
                diff1 = new Node(value);
                break;
            }
            case 2: {
                diff2 = new Node(value);
                break;
            }
            case 3: {
                diff3 = new Node(value);
                break;
            }
        }
    }

    public int getNumNodes() {

        if (this == null) return 1;
        else
            return 1 + diff1.getNumNodes() +
                    diff2.getNumNodes() +
                    diff3.getNumNodes();
    }
}
