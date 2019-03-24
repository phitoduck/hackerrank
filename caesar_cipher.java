import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    public static char rotateUpper(char letter, int k) {
        int val = (int) letter + k;
        val -= 65;
        val %= 26;
        val += 65;
        return (char) val;
    }
    
    public static char rotateLower(char letter, int k) {
        int val = (int) letter + k;
        val -= 97;
        val %= 26;
        val += 97;
        return (char) val;
    }
    
    // Complete the caesarCipher function below.
    static String caesarCipher(String s, int k) {
        
        StringBuilder result = new StringBuilder();
        for (Character c : s.toCharArray()) {
            if (Character.isLetter(c) && c.equals(Character.toLowerCase(c))) {
                result.append(rotateLower(c, k));
            } else if (Character.isLetter(c) && !c.equals(Character.toLowerCase(c))) {
                result.append(rotateUpper(c, k));
            } else {
                result.append(c);
            }
        }
        
        return result.toString();

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        String s = scanner.nextLine();

        int k = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        String result = caesarCipher(s, k);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
