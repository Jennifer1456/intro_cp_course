#include <iostream>
#include <cmath>

int calculate_sum_of_factors(int N)
{
    int sum_of_factors(0);
    /// START YOUR CODE HERE ///

    for (int i = 2; i <= N; i++)
    {
        if (N % i == 0)
        {
            sum_of_factors += i;
            std::cout << i << " ";
        };
    }
    ///std::cout<< "; with input number " << sum_of_factors<<"\n";

    //// END YOUR CODE HERE ////
    return sum_of_factors;
}

int main(){
calculate_sum_of_factors(549);

}
