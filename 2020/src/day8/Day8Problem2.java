package day8;

import IO.ReadFile;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day8Problem2 {

    private static final byte INST_ACC = 1;
    private static final byte INST_JMP = 2;
    private static final byte INST_NOP = 3;

    private static final String RE_INSTR = "(acc|jmp|nop) ([+|-])(\\d\\d*)";
    private static final Map<String, Byte> instruction = new HashMap<String, Byte>() {{

        put("acc", INST_ACC);
        put("jmp", INST_JMP);
        put("nop", INST_NOP);
    }};

    private static int lastInstChanged = -1;

    private static void switchNopJmp(List<String> instructions) {

        Iterator<String> it = instructions.iterator();
        int i;
        boolean found = false;

        Pattern patInst = Pattern.compile(RE_INSTR);
        Matcher matInst;


        for (i = 0; i < lastInstChanged + 1; i++)
            it.next();
        while (it.hasNext() && !found) {

            String inst = it.next();
            matInst = patInst.matcher(inst);
            if (matInst.find()) {

                String type = matInst.group(1);
                String sign = matInst.group(2);
                String argument = matInst.group(3);
                switch (instruction.get(type)) {

                    case INST_NOP: {
                        instructions.set(i, String.format("jmp %s%s", sign, argument));
                        found = true;
                        break;
                    }
                    case INST_JMP: {
                        instructions.set(i, String.format("nop %s%s", sign, argument));
                        found = true;
                        break;
                    }
                }
            }
            if (!found) i++;
        }
        lastInstChanged = i;
    }

    public static void main(String[] args) {

        List<String> lines = ReadFile.readFile("day8_input.in");
        List<String> instructions;

        Pattern patInst = Pattern.compile(RE_INSTR);
        Matcher matInst;
        int accumulator;
        boolean loop;

        do {

            instructions = new ArrayList<>(lines);
            switchNopJmp(instructions);

            Boolean[] execInst = new Boolean[instructions.size()];
            Arrays.fill(execInst, Boolean.FALSE);

            int argument;
            loop = false;
            accumulator = 0;
            for (int i = 0; i < instructions.size() && !loop; i++) {

                if (!execInst[i]) {

                    matInst = patInst.matcher(instructions.get(i));
                    if (matInst.find()) {

                        execInst[i] = true;
                        argument = Integer.parseInt(matInst.group(3));
                        if (matInst.group(2).equals("-"))
                            argument = -argument;
                        switch (instruction.get(matInst.group(1))) {

                            case INST_ACC: {
                                accumulator += argument;
                                break;
                            }
                            case INST_JMP: {
                                i += argument - 1;
                                break;
                            }
                        }
                    }
                } else loop = true;
            }
        } while (loop);
        System.out.println(accumulator);
    }
}
