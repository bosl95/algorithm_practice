package ARRAY.backjoon_10807;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.valueOf(br.readLine());
        String[] str = br.readLine().split(" ");
        int v = Integer.valueOf(br.readLine());

        int result = 0;
        for (int i=0; i<N; i++) {
            if (v == Integer.valueOf(str[i])) {
                result++;
            }
        }
        System.out.print(result);
    }
}
