#include <iostream>
double sum_of_series(int N)
{
    double ret_value(0.);
    /// START YOUR CODE HERE ///
    for (int i = 1; i <= N; i++)
    {
        if (i % 2 == 0)
        {
            ret_value -= 1. / i;
        }
        else
        {
            ret_value += 1. / i;
        }
    }

    //// END YOUR CODE HERE ////
    return ret_value;
}

int main()
{
    double aa = sum_of_series(11);
    std::cout << aa;
}