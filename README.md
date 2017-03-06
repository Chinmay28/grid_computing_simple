# grid_computing_simple
--------------------------
Problem Statement
--------------------------
 
 
The task is to create a grid computing server-client architecture where a client is able to perform calculations using specialized computational servers. Each server will be able to perform a single computation as a function of x: f(x). Clients should be able to perform a sequence of computations with the help of these specialized servers. Implement and test both the client and the server against a set of computational sequence inputs provided from a file.
 
For example, say there are 3 servers implementing the following functions:
Server A
f(x) = x^2
Server B
f(x) = 10x
Server C
f(x) = x + 20
 
 
Now you have an input file containing the computational sequence as:
x = 5
A(x) + B(x) + C(x)
 
A(x) + B(x) + C(x) is the computation sequence that needs to be evaluated for x = 5
 
For this example, the computation will look like
x^2 + 10x + (x+20)
 
with the value of x as 5 this will be
5^2 + (10*5) + (5+20) = 100
 
 
For the problem, the following 5 servers with the specific computation of f(x) are to be implemented
A(x) x^2
B(x) 10x
C(x) x+20
D(x) log10 x
E(x) sqrt(x)
 
 
The client should be able to parse and calculate the result for the following example computational sequences:
x = 100
A(x) + B(x) + C(x)
(B(x) * C(x)) + (D(x) * E(x))
A( C(x) * E(x) )
E( B( A(x) ) )
D( A( E(x) + D(x) ) )
 
 
Given these inputs, each server should be able to:
 
1. Accept client request containing the value of 'x' and respond with the result of f(x).
2. The server is responsible for the computation only and no other operation.
3. Server can log input 'x' and output f(x) into a file
 
 
The client should be able to:
 
1. Read in the input file for the value of 'x' and each computation sequence
2. Parse each computation sequence to determine the order of server calls and mathematical operation
3. Send a request to the server to obtain the computation result
4. Output the result of each computation sequence
5. Handle generic computational sequences. The computational sequences in the example above are for reference.
6. Handle error conditions.
7. Handle operator precedence for the computation sequences
 

