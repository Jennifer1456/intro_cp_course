#include <iostream>

int main()
{
    for (int i = 0; i < 14; i++)
    {
        for (int j = 0; j < (13 - i); j++)
        {
            std::cout << " ";
        }
        for (int j = 0; j < (i); j++)
        {
            std::cout << "* ";
        }
        std::cout << "\n";
    }

    // std::cout << "             *"
    //           << "\n";
    // std::cout << "            * *"
    //           << "\n";
    // std::cout << "           * * *"
    //           << "\n";
    // std::cout << "          * * * *"
    //           << "\n";
    // std::cout << "         * * * * *"
    //           << "\n";
    // std::cout << "        * * * * * *"
    //           << "\n";
    // std::cout << "       * * * * * * *"
    //           << "\n";
    // std::cout << "      * * * * * * * *"
    //           << "\n";
    // std::cout << "     * * * * * * * * *"
    //           << "\n";
    // std::cout << "    * * * * * * * * * *"
    //           << "\n";
    // std::cout << "   * * * * * * * * * * *"
    //           << "\n";
    // std::cout << "  * * * * * * * * * * * *"
    //           << "\n";
    // std::cout << " * * * * * * * * * * * * *"
    //           << "\n";
    // std::cout << "* * * * * * * * * * * * * *"
    //           << "\n";
}