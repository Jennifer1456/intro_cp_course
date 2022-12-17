#include <iostream>

int multi_calculator(int A, int B, std::string O)
{
    int ret_value = 0;
    /// START YOUR CODE HERE ///

    if (O == "add")
        ret_value = A + B;
    if (O == "sub")
        ret_value = A - B;
    if (O == "mul")
        ret_value = A * B;
    if (O == "div" && B != 0)
    {
        int ans = static_cast<double>(A) / B;
        ret_value = A / B;
        if (ans - ret_value > 0.5)
        {
            ++ret_value;
        }
    }
    if (O == "mod")
        ret_value = A % B;
    if (O == "pow")
    {
        ret_value = A;
        for (int i = 0; i < (B - 1); i++)
        {
            ret_value = ret_value * A;
        }
    }

    if (O == "or")
        ret_value = A | B;
    if (O == "and")
        ret_value = A & B;
    if (O == "xor")
        ret_value = A ^ B;
    if (O == "lshift")
        ret_value = A << B;
    if (O == "rshift")
        ret_value = A >> B;

    //// END YOUR CODE HERE ////
    return ret_value;
}
