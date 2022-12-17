#include <stdlib.h>
#include <iostream>
#include <ctime>
#include <bits/stdc++.h>

char stay[];

int randint()
{
    int min = 1;
    int max = 42;
    srand(time(NULL));
    int a = rand() % (max - min + 1) + min;
    // std::cout << a;
    return a;
}
int main()
{
    int ans = randint();
    stay = static_cast<char>(ans);
    // std::cout << "first draw:" << ans << "\n";
    std::cout << ans << stay;

    // ans = randint();
    // if (ans == stay[0])
    // {
    //     std::cout << "oh no! It's same with stay = ";
    //     std::cout << stay << "\n";
    // }
    // else
    // {
    //     std::cout << "second draw: " << ans << "\n";
    //     std::cout << "with stay: " << stay << "\n";
    // }
    // ans = randint();
    // if (ans == stay[1])
    // {
    //     std::cout << "oh no! It's same with stay = " << stay << "\n";
    // }
    return 0;
}