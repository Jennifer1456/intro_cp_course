#include <iostream>

std::string rotate_characters(std::string input)
{
    std::string output(input);

    /// START YOUR CODE HERE ///

    int num = static_cast<int>(in);
    char O;
    if (num = 90)
    {
        O = static_cast<char>(65) + 1;
    }
    else if (num = 122)
    {
        O = static_cast<char>(97) + 1;
    }
    else
    {
        O = static_cast<char>(num + 1);
    }
    output = O;
    //// END YOUR CODE HERE ////
    return output;
}

int main()
{
    rotate_characters("v");
}
