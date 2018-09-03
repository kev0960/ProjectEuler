#include <iostream>
#include <string>
bool isPalindrome(int x) {
  std::string s = std::to_string(x);
  for (int i = 0; i < s.length(); i ++) {
    if (s[i] != s[s.length() - i - 1]) return false;
  }
  return true;
}

int main() {
  int largest = 0;
  for (int i = 100; i <= 999; i ++) {
    for (int j = i; j < 999; j ++) {
      if (isPalindrome(i * j) && i * j > largest) {
        largest = i * j;
      }
    }
  }
  std::cout << "Largest : " << largest;

}
