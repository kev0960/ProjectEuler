#include <iostream>
#include <string>

using ll = long long;
int gcd(ll a, ll b) {
  if (b > a) return gcd(b, a);
  // assume a > b
  while (true) {
    a = a % b;
    if (a == 0) {
      return b;
    }
    ll t = a;
    a = b;
    b = t;
  }
}
int main() {
  ll cur = 1;
  for (int i = 1; i <= 20; i ++) {
    int g = gcd(i, cur);
    cur = (i * cur) / g;
  }
  std::cout << "lcm : " << cur;
}
