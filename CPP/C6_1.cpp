#include <cmath>

double evaluate_equation(double x)
{
    double ret_value(0.);
    /// START YOUR CODE HERE ///
    for (int m = 1; m <= 4; m++)
    {
        for (int n = 1; n <= 4; n++)
        {
            ret_value += m * exp(n * M_PI * x);
        }
    }
    ret_value = log(ret_value);

    //// END YOUR CODE HERE ////
    return ret_value;
}
