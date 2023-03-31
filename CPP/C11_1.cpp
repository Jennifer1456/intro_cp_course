#include <string>
#include <iostream>
std::string Number2Text(int N)
{
    std::string text;
    /// START YOUR CODE HERE ///
    

        //// END YOUR CODE HERE ////
        return text;
}
enum numm
    {
        zero,
        one,
        two,
        three,
        four,
        five,
        six,
        seven,
        eight,
        nine,
        ten,
        eleven,
        twelve,
        thirteen,
        fourteen,
        fifteen,
        sixteen,
        seventeen,
        eighteen,
        nineteen,
        twenty
    };
int Text2Number(std::string text)
{
    int N(0);
    /// START YOUR CODE HERE ///
    
    int N_list[20];
    for (int i = 0; i < 21; i++)
    {
        N_list[i] = i;
    }
    N =static_cast<numm>(text);
    //// END YOUR CODE HERE ////
    return N;
}

int main(){
    std::cout<<Text2Number("zero");

}
