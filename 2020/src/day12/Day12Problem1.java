package day12;

import IO.ReadFile;

import java.util.ArrayList;
import java.util.List;

public class Day12Problem1 {

    private enum direction {east, south, west, north}

    public static void main(String[] args) {

        List<Move> moves = new ArrayList<>();
        for (String line : ReadFile.readFile("day12_input.in"))
            moves.add(new Move(line));

        direction dir = direction.east;
        int hor = 0;
        int ver = 0;

        for (Move m : moves) {

            switch (m.getDir()) {

                case 'N': {
                    ver += m.getNum();
                    break;
                }
                case 'S': {
                    ver -= m.getNum();
                    break;
                }
                case 'E': {
                    hor += m.getNum();
                    break;
                }
                case 'W': {
                    hor -= m.getNum();
                    break;
                }
                case 'L': {
                    int newDir = Math.floorMod(dir.ordinal() - (m.getNum() / 90), direction.values().length);
                    dir = direction.values()[newDir];
                    break;
                }
                case 'R': {
                    int newDir = Math.floorMod(dir.ordinal() + (m.getNum() / 90), direction.values().length);
                    dir = direction.values()[newDir];
                    break;
                }
                case 'F': {
                    switch (dir) {
                        case north: {
                            ver += m.getNum();
                            break;
                        }
                        case south: {
                            ver -= m.getNum();
                            break;
                        }
                        case east: {
                            hor += m.getNum();
                            break;
                        }
                        case west: {
                            hor -= m.getNum();
                            break;
                        }
                    }
                    break;
                }
            }
        }
        int dist = Math.abs(hor) + Math.abs(ver);
        System.out.println("Manhattan distance: " + dist);
    }
}
