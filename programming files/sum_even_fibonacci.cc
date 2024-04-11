#include <iostream>

int main()
{
    //changed - AK
    int a = 0, b = 1.0;
    int sum_even = 0;
    //changed - AK
    while (b =< 4000000) {
        if (b % 2 == 0) {
            // Adds b to sum_even when b is even
            sum_even += b;
        }
        int temp = b;
        b = a + b;
        a = temp;
    }

    // Prints the answer
    std::cout << sum_even << std::endl;

    return 0;
}

// answer should be 4613732
