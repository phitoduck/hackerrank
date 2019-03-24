import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {
    
    static void print_grid(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.printf(" " + matrix[i][j]);
            }
            System.out.printf("\n");
        }
        System.out.println();
    }
    
    static void print_stack(ArrayList< int[] > stack) {
        for (int[] move : stack) {
            System.out.printf("(%d, %d)", move[0], move[1]);
        }
        System.out.println();
    }
    
    static boolean is_valid_move(int[] move, int[][] matrix) {
        
        int m = matrix.length;
        int n = matrix[0].length;
        
        if (move[0] < 0 || move[1] < 0)
            return false;
        else if (move[0] >= m || move[1] >= n)
            return false;
        
        return true;
        
    }
    
    static int depth_search(int[][] matrix, int i, int j) {
        
        int[][] moves = {
             {0, 1}, 
             {1, 0}, 
             {0, -1}, 
             {-1, 0},
             {1, 1},
             {1, -1},
             {-1, 1},
             {-1, -1}
        };
        
        ArrayList< int[] > stack = new ArrayList<>();
        int[] first_move = {i, j};
        stack.add(first_move);
        
        int island_size = 0;
        while (stack.size() > 0) {
            
            // pop off the top of the "stack"
            int[] loc = stack.get( stack.size() - 1 );
            stack.remove( stack.size() - 1 );
            
            // set current location to 0
            matrix[loc[0]][loc[1]] = 0;
            island_size++;
            
            // print_grid(matrix);
            // print_stack(stack);
                
            // loop over all moves
            for (int m_index = 0; m_index < moves.length; m_index++) {
                
                // calculate next move
                int[] move = moves[m_index];
                int[] next_move = { loc[0] + move[0], loc[1] + move[1] };
                
                if (is_valid_move(next_move, matrix) && matrix[next_move[0]][next_move[1]] != 0) {
                    matrix[next_move[0]][next_move[1]] = 0;
                    stack.add(next_move);
                }
                
            }
            
        }
        
        return island_size;
        
    }

    // Complete the connectedCell function below.
    static int connectedCell(int[][] matrix) {
        
        
        
        ArrayList<Integer> island_sizes = new ArrayList<>();
        island_sizes.add(0);
        
        // iterate over all grid values
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                
                // perform depth first search on nonzero entries
                if (matrix[i][j] != 0) {
                    island_sizes.add( depth_search(matrix, i, j) );    
                    // print_grid(matrix);
                }
                
            }
        }
        
        return Collections.max(island_sizes);


    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int m = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[][] matrix = new int[n][m];

        for (int i = 0; i < n; i++) {
            String[] matrixRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < m; j++) {
                int matrixItem = Integer.parseInt(matrixRowItems[j]);
                matrix[i][j] = matrixItem;
            }
        }

        int result = connectedCell(matrix);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}


