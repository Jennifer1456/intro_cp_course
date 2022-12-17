#include <stdlib.h>
#include <iostream>
#include <ctime>
#include <bits/stdc++.h>
std::string g_picked = "";

int randint()
{
    int min = 1;
    int max = 42;
    srand(time(NULL));
    int a = rand() % (max - min + 1) + min;
    // std::cout << a;
    return a;
}

int lottery_function(bool reset = false)
{
    int pick(0);
    if (reset)
    {
        g_picked = "";
        pick = 0;
        //std::cout << g_picked;
    }
    else
    {
        bool redraw = true;
        //while (redraw)
        for (int j = 0; j<3; j++)
        {
            redraw = false;
            pick = randint();
            /// START YOUR CODE HERE ///
            for (int i = 0; i < g_picked.length() + 1; i++)
            {
                if (pick == static_cast<int>(g_picked[i]))
                {
                    redraw = true;
                    break;
                }
                
            }
            g_picked[j] = static_cast<char>(pick);
        }
        std::cout << g_picked;
        //// END YOUR CODE HERE ////
    }
    return pick;
}

int main()
{
    int pp = lottery_function(false);
    std::cout << " The number you drawed:" << pp << "\n";
    // pp = lottery_function();
    // std::cout << " The second:" << pp;
    return 0;
}
