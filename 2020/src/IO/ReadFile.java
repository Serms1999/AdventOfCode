package IO;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class ReadFile {

    private static final String pathInput = System.getProperty("user.dir") + "/inputs/";

    public static List<String> readFile(String file) {

        File input;
        FileReader fr = null;
        BufferedReader br;
        List<String> lines = new ArrayList<>();

        try {
            input = new File(pathInput + file);
            fr = new FileReader(input);
            br = new BufferedReader(fr);

            String line;
            while ((line = br.readLine()) != null) {

                lines.add(line);
            }

        } catch (Exception e) {

            e.printStackTrace();
        } finally {

            try {
                if (fr != null) {
                    fr.close();
                }
            } catch (Exception e2) {
                e2.printStackTrace();
            }
        }
        return Collections.unmodifiableList(lines);
    }
}
