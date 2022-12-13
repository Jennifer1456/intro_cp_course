#include <cmath>
#include <iostream>

int calculate_sum_of_prime_factors(int N)
{
    int sum_of_prime_factors(0);
    /// START YOUR CODE HERE ///
    bool is_prime = true;
    for (int i = 2; i <= N; i++)
    { /// std::cout << i << " ";

        if (N % i == 0)
        { /// std::cout << i << " ";
            bool is_prime = true;
            for (int j = 2; j < i; j++)
            {
                if (i % j == 0)
                {
                    is_prime = false;
                    /// std::cout << i << " N";
                }
                // std::cout << i<<"/"<<j<<":"<<is_prime << " ";
            }
            if (is_prime)
            {
                sum_of_prime_factors += i;

                // std::cout << i << " ";
            }
            else
            {
                // std::cout <<is_prime<< i << " ";
            }
        };
    }
    /// std::cout<< "; with input number " << sum_of_prime_factors<<"\n";

    //// END YOUR CODE HERE ////
    return sum_of_prime_factors;
}

int main()
{
    calculate_sum_of_prime_factors(572);
}
