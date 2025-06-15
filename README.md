## Exercise VII. 

* It is commonly said that one human year is equivalent to 7 dog years. However this simple conversion fails to recognize that dogs reach adulthood in approximately two years. As a result, some people believe that it is better to count each of the first two human years as 10.5 dog years, and then count each additional human year as 4 dog years.
Write a program that implements the conversion from human years to dog years described in the previous paragraph. Ensure that your program works correctly for conversions of less than two human years and for conversions of two or more human years. Your program should display an appropriate error message if the user enters a negative number.

## Exercise VIII. 

* A univariate quadratic function has the form f(x) = ax2 + bx + c, where a, b and c are constants, and a is non-zero. The roots of a quadratic function can be found by finding the values of x that satisfy the quadratic equation ax2 + bx + c = 0. A quadratic function may have 0, 1 or 2 real roots. These roots can be computed using the quadratic formula:
√
root= −b± b2 −4ac
2a
The portion of the expression under the square root sign is called the dis- criminant. If the discriminant is negative then the quadratic equation does not have any real roots. If the discriminant is 0, then the equation has one real root. Otherwise the equation has two real roots, and the expression must be evaluated twice, once using a plus sign, and once using a minus sign, when computing the numerator.
Write a program that computes the real roots of a quadratic function. Your program should begin by prompting the user for the values of a, b and c. Then it should display a message indicating the number of real roots, along with the values of the real roots (if any).

## Exercise IX. 

* The edit distance between two strings is a measure of their simi- larity—the smaller the edit distance, the more similar the strings are with regard to the minimum number of insert, delete and substitute operations needed to transform one string into the other.
Consider the strings kitten and sitting. The first string can be transformed into the second string with the following operations: Substitute the k with an s, substitute the e with an i, and insert a g at the end of the string. This is the smallest number of operations that can be performed to transform kitten into sitting. As a result, the edit distance is 3.
Write a recursive function that computes the edit distance between two strings. Use the following algorithm:
Let s and t be the strings
If the length of s is 0 then
    Return the length of t
Else if the length of t is 0 then
    Return the length of s
Else
    Set cost to 0
    If the last character in s does not equal the last character in t then
        Set cost to 1
    Set d1 equal to the edit distance between all characters \
       except the last one in s, and all characters in t, plus 1
    Set d2 equal to the edit distance between all characters in s, \
       and all characters except the last one in t, plus 1
    Set d3 equal to the edit distance between all characters \
       except the last one in s, and all characters \
       except the last one in t, plus cost
    Return the minimum of d1, d2 and d3
Use your recursive function to write a program that reads two strings from the user and displays the edit distance between them.

## Exercise X. Follow the steps:
• Create a class, Triangle. Its init () method should take self, angle1, angle2, and angle3 as arguments. Make sure to set these appropriately in the body of the init () method.
• Create a variable named number of sides and set it equal to 3.
• Create a method named check angles. The sum of a triangle’s three angles is It should return True if the sum of self.angle1, self.angle2, and self.angle3 is equal 180, and False otherwise.
• Create a variable named my triangle and set it equal to a new instance of your Triangle class. Pass it three angles that sum to 180 (e.g. 90, 30, 60).
• Print out my triangle.number of sides and print out my triangle.check angles().