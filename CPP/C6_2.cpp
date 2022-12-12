#include <cmath>

double evaluate_equation(double x, double y, double t)
{
    double ret_value(1.);
    /// START YOUR CODE HERE ///
    for (int n = 1; n <= 4; n++)
    {
        ret_value *= (cos(n * M_PI * t / 2) * cosh(x) + sin(n * M_PI * t / 2) * sinh(y));
    }

    //// END YOUR CODE HERE ////
    return ret_value;
}
