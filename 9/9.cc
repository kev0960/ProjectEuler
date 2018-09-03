#include <iostream>
#include <unordered_map>

int main() {
    std::unordered_map<int, int> squares;
    for (int i = 1; i < 1000; i ++) {
        squares[i * i] = i;
    }

    for (int a = 1; a < 1000; a ++) {
        for (int b = a; b < 1000; b ++) {
            auto itr = squares.find(a * a + b * b);
            if (itr != squares.end()) {
                if (a  + b + itr->second == 1000) {
                    std::cout << a << "," << b << "," << itr->second;
                    std::cout << "\n" << a * b * itr->second;
                }
            }
        }
    }
}