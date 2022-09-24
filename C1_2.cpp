#include <iostream>

int main()
{
    int num_comb(0);
    /// START YOUR CODE HERE ///

    // 100!/(4!96!)
    int a = 1;
    int i = 97;
    while (i <= 100)
    {
        a = a * i;
        i = i + 1;
    }
    i = 1;
    while (i <= 4)

    {
        a = a / i;
        i = i + 1;
    }
    num_comb = a;

    //// END YOUR CODE HERE ////
    std::cout << "# of combinations is " << num_comb << "\n";

    return 0;
}