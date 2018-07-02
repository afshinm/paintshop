# Paintshop

Paint shop problem in Python


## Problem

You own a paint factory. There are N different colors you can mix, and each color can be prepared "matte" or "glossy". So, you can make 2N different types of paint.

Each of your customers has a set of paint types they like, and they will be satisfied if you have at least one of those types prepared. At most one of the types a customer likes will be a "matte".

You want to make N batches of paint, so that:

There is exactly one batch for each color of paint, and it is either matte or glossy. For each customer, you make at least one paint type that they like. The minimum possible number of batches are matte (since matte is more expensive to make). Find whether it is possible to satisfy all your customers given these constraints, and if it is, what paint types you should make. If it is possible to satisfy all your customers, there will be only one answer which minimizes the number of matte batches.

### Input

One line containing an integer C, the number of test cases in the input file. For each test case, there will be: One line containing the integer N, the number of paint colors. One line containing the integer M, the number of customers. M lines, one for each customer, each containing: An integer T >= 1, the number of paint types the customer likes, followed by T pairs of integers "X Y", one for each type the customer likes, where X is the paint color between 1 and N inclusive, and Y is either 0 to indicate glossy, or 1 to indicated matte. Note that: No pair will occur more than once for a single customer. Each customer will have at least one color that they like (T >= 1). Each customer will like at most one matte color. (At most one pair for each customer has Y = 1). All of these numbers are separated by single spaces.

### Output

C lines, one for each test case in the order they occur in the input file, each containing the string "Case #X: " where X is the number of the test case, starting from 1, followed by: The string "IMPOSSIBLE", if the customers' preferences cannot be satisfied; OR N space-separated integers, one for each color from 1 to N, which are 0 if the corresponding paint should be prepared glossy, and 1 if it should be matte. Limits

Small dataset

```
C = 100
1 <= N <= 10
1 <= M <= 100 
```

Large dataset

```
C = 5
1 <= N <= 2000
1 <= M <= 2000 
```

The sum of all the T values for the customers in a test case will not exceed 3000.Sample

Input 2
5
3
1 1 1
2 1 0 2 0
1 5 0
1
2
1 1 0
1 1 1

Output Case #1: 1 0 0 0 0
Case #2: IMPOSSIBLE

In the first case, you must make color #1 matte, to satisfy the first customer. Every other paint type can be glossy. The second customer is satisfied by getting color #2 glossy, and the third customer is satisfied by getting color #5 glossy.

In the second case, there is only one color. One of your customers wants it matte and one wants it glossy. You cannot satisfy them both.


## Algorithm

This is my answer to the problem, although there are different ways to attack the problem (for example, using strongly connected components)

- Sorting the customers choices so that we have customers with least choices first and then sort each choice so that first item is glossy (least cost)
- Create a path of choices and backtrack if we cannot satisfy all the customers (of the current path)
- Fail if we have tried all the options

## License

MIT
