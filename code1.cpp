
#include <iostream>
using namespace std;

void func(int a, int b = 10) {
    cout << a << " " << b << endl;
}

int main() {
    func(1);
    return 0;
}
