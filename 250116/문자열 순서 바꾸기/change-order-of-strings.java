import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String s, t, temp;

        s = sc.next();
        t = sc.next();
        
        temp = s;
        s = t;
        t = temp;

        System.out.printf(s + "\n" + t);
    }
}