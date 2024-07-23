#include <stdio.h>  
   
int main() {  
    int octalDigitToBinary[8] = {0, 1, 10, 11, 100, 101, 110, 111};  
    long long octalNumber, binaryNumber = 0, position;  
    int digit;  
       
    /* Take an Octal Number as input from user */ 
    printf("Enter an Octal Number\n");  
    scanf("%ld", &octalNumber); 
   
    position = 1;  
    /* Convert Octal Number to Binary Number */ 
    while(octalNumber != 0) {
        digit = octalNumber % 10;
        binaryNumber = (octalDigitToBinary[digit] * position) + binaryNumber;  
        octalNumber /= 10;  
        position *= 1000;  
    }
 
    printf("%ld", binaryNumber);
     
    return 0;
}
