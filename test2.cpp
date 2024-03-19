/*Write a program segment that defines a file stream object named employees.
The file should be opened for both input and output (in binary mode). 
If the file fails to open, the program segment should display an error message.
*/

#include <iostream>
#include <fstream>
using namespace std;

int main() {
    fstream employees; 
    employees.open("test.bin", fstream::in | fstream::out | fstream::binary);

    if (!employees.is_open()) {
        cout << "Error: File failed to open!";
    }
}