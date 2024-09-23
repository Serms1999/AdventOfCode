package day8;

import IO.ReadFile;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day8Problem1 {

    private static final byte INST_ACC = 1;
    private static final byte INST_JMP = 2;
    private static final byte INST_NOP = 3;

    private static final String RE_INSTR = "(acc|jmp|nop) ([+|-])(\\d\\d*)";
    private static final Map<String, Byte> instruction = new HashMap<String, Byte>() {{

        put("acc", INST_ACC);
        put("jmp", INST_JMP);
        put("nop", INST_NOP);
    }};

    public static void main(String[] args) {

        List<String> instructions = ReadFile.readFile("day8_input.in");

        Boolean[] execInst = new Boolean[instructions.size()];
        Arrays.fill(execInst, Boolean.FALSE);

        Pattern patInst = Pattern.compile(RE_INSTR);
        Matcher matInst;

        int argument;
        boolean loop = false;
        int accumulator = 0;
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
        System.out.println(accumulator);
    }
}
