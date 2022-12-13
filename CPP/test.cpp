#include <iostream>

int main() 
{ 
 char ch; 
 std::cout << "Input a character: "; 
 std::cin >> ch; 
 std::cout << ch << " has ASCII code " << static_cast<int>(ch) << "\n"; 
}