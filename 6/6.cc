#include <iostream>
#include <string>

using ull = unsigned long long;

int main() {
  ull n = 100;
  ull s = n * n / 4  * (n + 1) * (n + 1);
  ull s2 = n * (2 * n + 1) / 6 * (n + 1);
  std::cout << s - s2;

}
