# Dynamic Programming Refresher

A number of coding interview problems solved using dynamic programming.

## DP Styles:
1. Memoization = Recursion (Algorithm) + Dictionary (Data Structure)
    - Draw a tree:
        1. The nodes are the inputs.
        2. The edges are the transtions, reductions, or shirnking of the problem.
        3. The leaves are the base case.
2. Tabulation = Iteration (Algorithm) + List (Data Structure)
    - Draw a table:
        1. The size of the table is the size of the inputs + 1.
        2. For an input of 3 and 3, have a 4 x 4 table/array. 

## Memoization Recipe:
1. Draw a tree. The nodes are the input. The edges are the transition/reduction. The leaves are the base case.
2. Write the recursion algorithm which is the brute force solution.
3. Code it.
4. Improve the performance by adding a memo which will improve the time complexity by sacrificing some space.
    1. Add a memo dictionary with default value None which you then intialize as an empty dictionary.
    2. Add a memo base case checking if the solution is already in the memo and if so, just return it.
    3. If not solve it recursively. Save the result in the memo, then return it.

## Tabulation Recipe:
1. Create a table. It's size is the input + 1.
2. Initialize all values with the default value of the base case.
3. Seed the table with the base case.
4. Iterative over the table/list. Use the current location/item to calculate the next/future location.
5. Return the last item in the table/list.

## Types of Dynamic Programming Questions:
1. Is there a way?
2. What's one way?
3. What the best way?
4. How many ways are there?
5. What are all the ways?

## Problems and Questions:
1. **Fibonacci Number:**
    1. What's the nth Fibonacci number?
2. **Travel in Grid:**
    1. How many ways to travel in a grid of m x n from start to end?
3. **Making the Sum out of Numbers | Making the Change out of Coins:**
    1. Can you make sum using the following number categories?
    2. What's one way to make the sum using these number categories?
    3. What's the shortest way to make the sum using these number categories?
4. **String Construction:**
    1. Can you construct this target string by concatenating elements from this array of strings?
    2. How many ways can you construct this target string by concatenating elements from this array of strings?
    3. What are all the ways can you construct this target string by concatenating elements from this array of strings?

