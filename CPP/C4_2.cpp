double evaluate_equation(double x, double y)
{
    double ret_value(0.);
    /// START YOUR CODE HERE ///

    ret_value = sqrt(pow(x, y) + pow(y, x)) / (sqrt(pow(x, y)) + sqrt(pow(y, x)));

    //// END YOUR CODE HERE ////
    return ret_value;
}
