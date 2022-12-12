#include <string>
#include <iostream>

namespace bank
{
    double amount(0.);
    std::string base_currency("TWD");
    double c(0.);
    void deposit(std::string currency, double cash)
    {
        /// START YOUR CODE HERE ///
        if (currency == "USD")
        {
            amount += cash * 30;
        }
        else if (currency == "EUR")
        {
            amount += cash * 35;
        }
        else
        {
            amount += cash;
        }
        //// END YOUR CODE HERE ////
    }
    double draw(std::string currency, double cash)
    {
        if (currency == "USD")
        {
            c = cash * 30;
        }
        else if (currency == "EUR")
        {
            c = cash * 35;
        }
        else
        {
            c = cash;
        }

        if (c <= amount)
        {
            amount -= c;
            return cash;
        }
        else
        {
            int aa = amount;
            amount = 0;
            if (currency == "USD")
            {
                aa = aa * 30;
            }
            else if (currency == "EUR")
            {
                aa = aa * 35;
            }
            else
            {
                aa = aa;
            }
            return aa;
        }

        /// START YOUR CODE HERE ///

        //// END YOUR CODE HERE ////
    }
    double check_balance(std::string currency)
    {
        /// START YOUR CODE HERE ///

        return amount;
        //// END YOUR CODE HERE ////
    }
}

int main()
{
    bank::deposit("TWD", 12.);
    std::cout << "balance in TWD: " << bank::check_balance("TWD") << "\n";

    bank::draw("USD", 67.6);
    std::cout << "balance in TWD: " << bank::check_balance("TWD") << "\n";
}
