double evaluate_equation(double x)
{
    double ret_value(0.);
    /// START YOUR CODE HERE ///
    ret_value = 1 + x + x * x / 2 + x * x * x / 6 + x * x * x * x / 24;

    //// END YOUR CODE HERE ////
    return ret_value;
}
