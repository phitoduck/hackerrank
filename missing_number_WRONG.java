import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the missingNumbers function below.
    static int[] missingNumbers(int[] arr, int[] brr) {

        // create tree maps of the form { number : frequency }
        TreeMap<Integer, Integer> bmap = new TreeMap<>();
        for (Integer i : brr) {
            if (bmap.keySet().contains(i)) {
                bmap.put(i, bmap.get(i) + 1);
            } else {
                bmap.put(i, 1);
            }
        }
        
        TreeMap<Integer, Integer> amap = new TreeMap<>();
        for (Integer i : arr) {
            if (amap.keySet().contains(i)) {
                amap.put(i, amap.get(i) + 1);
            } else {
                amap.put(i, 1);
            }
        }
        
        // temp
        System.out.println(amap.toString());
        System.out.println(bmap.toString());
        
        // find the missing numbers
        Set<Integer> missing = new HashSet<>();
        Set<Integer> keySet = bmap.keySet();
        for (Integer i : keySet) {
            
            // check if amap has the value
            if (amap.keySet().contains(i)) {
                
                // check that numbers have same frequencies
                if (amap.get(i) != bmap.get(i)) {
                    missing.add(i);
                }
                
            } else {
                missing.add(i);
            }
            
        }
        
        // convert sorted set to array
        int[] toReturn = new int[missing.size()];
        int i = 0;
        for (Integer num : missing)
            toReturn[i++] = num;
        
        Arrays.sort(toReturn);
        
        return toReturn;

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] arr = new int[n];

        String[] arrItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int arrItem = Integer.parseInt(arrItems[i]);
            arr[i] = arrItem;
        }

        int m = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] brr = new int[m];

        String[] brrItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < m; i++) {
            int brrItem = Integer.parseInt(brrItems[i]);
            brr[i] = brrItem;
        }

        int[] result = missingNumbers(arr, brr);

        for (int i = 0; i < result.length; i++) {
            bufferedWriter.write(String.valueOf(result[i]));

            if (i != result.length - 1) {
                bufferedWriter.write(" ");
            }
        }

        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}


