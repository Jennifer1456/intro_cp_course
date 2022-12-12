#include <iostream>
#include <cmath>

int main()
{
    double abs_AxBxC(0.);
    /// START YOUR CODE HERE ///
    abs_AxBxC = sqrt((1 * 1 + 3 * 3)) * sqrt(2 * 2 + 4 * 4) * sqrt(3 * 3 + 6 * 6);
    //// END YOUR CODE HERE ////
    std::cout << "value: " << abs_AxBxC << "\n";
    return 0;
}
