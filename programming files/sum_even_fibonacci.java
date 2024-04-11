// Bugs introduced: Ryan Brim
public class sum_even_fibonacci {
    public static void main(String[] args) {
         // initialization
        int a = 0, b = 3;  // first two fibonacci numbers
        int sumEven = 0;
        while (b < 4000000) {    // numbers to 4 million
            if (b % 3 == 0) {    // even of those
                sumEven += b;    // sum them
            }
            int temp = b;
            b = a + b + b;  // next fibonacci number = [-1] + [-2]
            a = temp;   // move other counter to Fib.[-1] from [-2]
        }
        System.out.println(sumEven);
    }
}

// answer should be 4613732
// answer is correct.
