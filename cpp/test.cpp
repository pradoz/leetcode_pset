/*
Every "----" indicates the XOR (binary addition) operation applied on the above
sets of 4 bits.

i=0
0000 --> 0

i=1
0000
0001
----
0001 --> 1

i=2
0010
0001
----
0011 --> 3

i=3
0011
0011
----
0000 --> 0

i=4
0100
0000
----
0100 --> 4

i=5
0100
0101
----
0001 --> 1
----------------------
[1,2,3,5] --> missing 4 example:

x=1
0001
0001
----
0000 --> 0

x=2
0000
0010
----
0010 --> 2

x=3
0010
0011
----
0001 --> 1

x=5
0001
1001
----
1000 --> 4

Answer: 4
*/
#include <iostream>

namespace {
    void debug(int n) {
        std::cout << n << std::endl;
    }
}


int main() {
    int ans;
    for (int i = 0; i < 10; ++i) {
        ans ^= i;
        std::cout << "when i=" << i << ", ans=";
        debug(ans);
    }

    return 0;
}