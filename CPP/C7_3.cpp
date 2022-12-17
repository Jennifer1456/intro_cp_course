#include <iostream>
#include <bits/stdc++.h>
std::string rotate_characters(std::string input)
{
    std::string output(input);
    /// START YOUR CODE HERE ///
    char arr[input.length() + 1];
    char ans[input.length() + 1];

    for (int x = 0; x < sizeof(arr); x++)
    {
        arr[x] = input[x];
        int num = static_cast<char>(arr[x]);
        char O;
        if (num == 90)
        {
            O = static_cast<char>(65);
        }
        else if (num == 122)
        {
            O = static_cast<char>(97);
        }
        else
        {
            O = static_cast<char>(num + 1);
        }
        ans[x] = O;
        output[x] = ans[x];
    }

    //// END YOUR CODE HERE ////
    return output;
}

int main()
{
    std::string cat = "banana";

    std::cout << rotate_characters(cat);

    return 0;
    /*
        std::string output(input);
    /// START YOUR CODE HERE ///
    
    for (int i=0; i<input.length(); i++) {
        if (output[i] >= 'a') {
        	output[i] = ((output[i]-'a'+1)%26)+'a';
        } else {
            output[i] = ((output[i]-'A'+1)%26)+'A';
        }
    }
    
    */
}
