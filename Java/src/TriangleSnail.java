import java.util.ArrayList;
import java.util.Arrays;

public class TriangleSnail {
    public static void main(String[] args) throws Exception {
        System.out.println(Arrays.toString(solution(5)));
    }

    public static int[] solution(int n) {
        int[][] arr = new int[n][];
        for (int i = 0; i < n; i++) {
            arr[i] = new int[i + 1];
        }
        int[][] d = { { 1, 0 }, { 0, 1 }, { -1, -1 } };
        int x = 0;
        int y = 0;
        int status = 0;
        int maxNum = 0;
        for (int i = 1; i <= n; i++) {
            maxNum += i;
        }
        for (int i = 1; i < maxNum + 1; i++) {
            arr[x][y] = i;
            int status_ = status % 3;
            int nx = x + d[status_][0];
            int ny = y + d[status_][1];
            if (0 <= nx && nx < n && 0 <= ny && ny <= nx && arr[nx][ny] == 0) {
                x = nx;
                y = ny;
            } else {
                status++;
                status_ = status % 3;
                x = x + d[status_][0];
                y = y + d[status_][1];
            }
        }
        ArrayList<Integer> answer = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                answer.add(arr[i][j]);
            }
        }
        int[] ans = answer.stream().mapToInt(Integer::intValue).toArray();
        return ans;
    }
}