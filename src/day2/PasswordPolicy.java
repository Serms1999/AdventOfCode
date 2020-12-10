package day2;

public class PasswordPolicy {

    private int minValue;
    private int maxValue;
    private char letter;
    private String password;

    public PasswordPolicy(int minValue, int maxValue, char letter, String password) {

        this.minValue = minValue;
        this.maxValue = maxValue;
        this.letter = letter;
        this.password = password;
    }

    public int getMinValue() {
        return minValue;
    }

    public int getMaxValue() {
        return maxValue;
    }

    public char getLetter() {
        return letter;
    }

    public String getPassword() {
        return password;
    }

    public int getLetterApparencesPassword() {

        int count = 0;
        for (int i = 0; i < password.length(); i++) {

            if (password.CharAt(i).equals(letter)) {

                count++;
            }
        }
        return count;
    }
}
