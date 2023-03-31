#include <iostream>
enum Color : short { 
 kRed, 
 kGreen, 
 kBlue 
}; 
int main() 
{ 
 short color_code = kGreen; 
 Color paint = 
 static_cast<Color>(color_code);
 std::cout<<color_code<<"\n"<<paint<<kGreen<<kBlue;
}