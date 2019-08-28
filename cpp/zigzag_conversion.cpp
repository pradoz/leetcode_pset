/********************************************************************

    * File: zigzag-conversion.cpp
    * Author: Zachary Prado
    * E-mail: zacharyprado@yahoo.com
    * Last Update: 12/8/2018 

 *******************************************************************/

class Solution {
public:
    string convert(string s, int num_rows) {
        // length of string 
        int len = s.length(); 

        // Create an array of strings for all num_rows 
        string arr[num_rows]; 
    
        // Initialize index for array of strings arr[] 
        int row = 0; 
        bool down; // True if we are moving down in rows, else false
    
        // Travers through given string 
        for (int i = 0; i < len; ++i) {
            // append current character to current row
            arr[row].push_back(s[i]);
    
            // If last row is reached, change direction to 'up'
            if (row == num_rows-1)
              down = false;
    
            // If 1st row is reached, change direction to 'down'
            else if (row == 0)
              down = true;
    
            // If direction is down, increment, else decrement
            (down) ? row++ : row--;
        }
      
        // Print concatenation of all rows
        for (int i = 0; i < num_rows; ++i)
            cout << arr[i]; 
    return s;
    }
};