#include <iostream>

int main()
{
    int A(0), B(0), C(0);
    /// START YOUR CODE HERE ///
    int m;
    m = 42;

    A = m * (m + 1) / 2;
    B = m * (m + 1) * (2 * m + 1) / 6;
    C = A * A;
    //// END YOUR CODE HERE ////
    std::cout << "A = sum_{k=1}^m k = " << A << "\n";
    std::cout << "B = sum_{k=1}^m k^2 = " << B << "\n";
    std::cout << "C = sum_{k=1}^m k^3 = " << C << "\n";
    return 0;
}