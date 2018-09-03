#include <iostream>
using ull = unsigned long long;
int main() {
 int bef = 1, cur = 2;
 ull sum = 0;
 while (cur < 4000000) {
   if (cur % 2 == 0) {
     sum += cur;
   }
   int t = cur;
   cur = cur + bef;
   bef = t;
 } 
 std::cout << "sum : " << sum;
}
