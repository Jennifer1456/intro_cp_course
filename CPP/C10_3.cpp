#include <string>
#include <iostream>
std::string password_generator()
{
    std::string password;
    /// START YOUR CODE HERE ///

    // password = "hi";
    password = "asdfghjklo";
    /// START YOUR CODE HERE ///
    for (int i = 0; i < 10; i++)
    {
        int j = (rand() % 62);
        if (j < 26)
        {
            password[i] = j + 'a';
        }
        else if (j < 52)
        {
            password[i] = j - 26 + 'A';
        }
        else
        {
            password[i] = j - 52 + '0';
        }
    }
    //// END YOUR CODE HERE ////
    return password;
}
int main()
{
    // std::string aa[2];
    // aa[0] = (rand() %52+'A');
    // aa[1] = (rand() %52+'A');
    std::string aa = password_generator();
    // std::cout << aa;

    std::cout << static_cast<int>('A');
    // std::cout << aa;

    return 0;
}
