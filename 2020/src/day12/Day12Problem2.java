package day12;

import IO.ReadFile;

import java.util.ArrayList;
import java.util.List;

public class Day12Problem2 {

    public static void main(String[] args) {

        List<Move> moves = new ArrayList<>();
        for (String line : ReadFile.readFile("day12_input.in"))
            moves.add(new Move(line));

        int WPHor = 10;
        int WPVer = 1;
        int ShipHor = 0;
        int ShipVer = 0;

        for (Move m : moves) {

            switch (m.getDir()) {

                case 'N': {
                    WPVer += m.getNum();
                    break;
                }
                case 'S': {
                    WPVer -= m.getNum();
                    break;
                }
                case 'E': {
                    WPHor += m.getNum();
                    break;
                }
                case 'W': {
                    WPHor -= m.getNum();
                    break;
                }
                case 'L': {
                    int cos = (int) Math.cos(Math.toRadians(m.getNum()));
                    int sin = (int) Math.sin(Math.toRadians(m.getNum()));
                    int aux = WPHor;
                    WPHor = WPHor * cos - WPVer * sin;
                    WPVer = aux * sin + WPVer * cos;
                    break;
                }
                case 'R': {
                    int cos = (int) Math.cos(Math.toRadians(-m.getNum()));
                    int sin = (int) Math.sin(Math.toRadians(-m.getNum()));
                    int aux = WPHor;
                    WPHor = WPHor * cos - WPVer * sin;
                    WPVer = aux * sin + WPVer * cos;
                    break;
                }
                case 'F': {
                    ShipHor += m.getNum() * WPHor;
                    ShipVer += m.getNum() * WPVer;
                    break;
                }
            }
            System.out.println("Waypoint: " + WPHor + ", " + WPVer);
            System.out.println("Ship: " + ShipHor + ", " + ShipVer);
        }
        int dist = Math.abs(ShipHor) + Math.abs(ShipVer);
        System.out.println("Manhattan distance: " + dist);
    }
}
