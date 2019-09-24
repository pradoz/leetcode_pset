#include <iostream>

/*
n=1
***
* * - n-1 indents, n spaces at 1st block, n+1 stars
*** -- 2n+1 = 2(1)+1 = 2+1 = 3
----------
n=2
 ***
 * *
***** -- 2n+1 = 2(2)+1 = 4+1 = 5
* * * - n-level indents
*****
n=3
  ***
  * *
 *****
 * * *
*******
* * * *
******* -- 2n+1 = 2(3)+1 = 6+1 = 7
*/

/* Al Gore Rythym
1. Get the number of indents on the current line, note that we repeat indented
    cases twice.
2. Check if we are on a line of all stars, or a line of stars and spaces
    alternating.
3. Print the result of (2) on the current line
4. Move to the next level and check if we are done
5. If we are done, then exit. If we are not done, continue to next block.
*/


void indent_block(int level);
void outer_block(int level);
void inner_block(int level);
void finish_pyramid(int n, int level);
void create_inner_block(int n, int level);



int main() {
    // Get the number of blocks in the bottom layer of the pyramid
    int n = 3;

    // Create top of first block
    for (int level = 1; level <= n; ++level) {

        // Start the base case (top of the pyramid)
        indent_block(n - level);
        outer_block(level);

        // If we are still inside the pyramid, then create an inner block
        if (level != n) {
            create_inner_block(n, level);
        }
        else { // Else, finish of the pyramid base
            finish_pyramid(n, level);
        }
    }

    return 0;
}


// indent_block() indents the current line before placing stars and spaces.
void indent_block(int level) {
    for (int i = 0; i < (level); ++i) {
        std::cout << ' ';
    }
}


// outer_block() prints a '*' character for every index remaining on the
// current line.
void outer_block(int level) {
    const int size = (2 * level + 1);
    for (int i = 0; i < size; ++i) {
        std::cout << '*';
    }
    std::cout << '\n';
}


// inner_block() alternates printing a space for every even index, and a
// '*' character for every odd index remaining on the current line.
void inner_block(int level) {
    const int size = (2 * level + 1);
    for (int i = 0; i < size; ++i) {
        i % 2 == 0
        ? std::cout << '*'
        : std::cout << ' ';
    }
    std::cout << '\n';
}


// create_inner_block() indents and prints the inner pyramid block.
void create_inner_block(int n, int level) {
    indent_block(n - level);
    inner_block(level);
}


// finish_pyramid() prints the bottom row of the pyramid.
void finish_pyramid(int n, int level) {
    inner_block(level);
    indent_block(n - level);
    outer_block(level);
}