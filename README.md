# advancedProg.optimization
Several Python projects containing Earth's Mover Distance image detector, PuLP optimization 


### opProblem 1

# Part 1:
Solve the following program:

       min 122x + 143y
       subject to:
         x ≥ -10
         y ≤  10
         3x +  2y ≤  10
         12x + 14y ≥ -12.5
         2x +  3y ≥   3
         5x -  6y ≥-100
Your program should find the optimal solution, determine its objective value, and identify the tight constraints.
# Part 2:
Find an optimal mixed strategy of the following game: Both players choose independently a single integer from 1 to 6. Then, the numbers are compared:

If they are equal, there is a draw
If they differ by 1, the player who played the smaller number gets 2EUR from the other player
If they differ by ≥2, the player who played the larger number gets 1EUR from the other player
Note that the game is symmetric and the same strategy is optimal for both players.
Required output example:

x1: 0.2 x2: 0.1 x3: 0.2 x4: 0.1 x5: 0.2 x6: 0.2
# Part 3:
On some imaginary island, there are 69 companies and there are bilateral contracts between them. The monarch of the island would like to inspect validity of each of these contracts during a single large event. The monarch requires two representatives to represent each contract relationship (they can be both from the same party of the contract or each from a different one). This is of course satisfied by each company sending a single representative, which would require involvement of 69 representatives in total. However, the companies want to find a solution which minimizes the total number of representatives who need to attend the event.

Input file hw1-03.txt contains information about the contracts. Each line corresponds to a single contract and contains identifiers (1-69) of both involved parties separated by a space.

Example output:

representatives from company 1: 1.0
representatives from company 2: 2.0
representatives from company 3: 1.0
...
representatives from company 69: 1.0
Total number of representatives involved: 58
Important: It is not possible to send an arbitrary fraction of a representative. However, it is enough to solve the LP relaxation since it already gives an integral solution. Reasons for this will be explained later in the class.

# opProblem 2

Consider a set of pictures from 360° camera mounted inside a merry-go-round. They were taken at night and only one seat is visible which emits light – the seat in the shape of a jelly fish. We know that the merry-go-round rotates clockwise and that all the pictures were taken during a single cycle of merry-go-round. Given that the first picture is P1, your task is to sort the rest in the chronological order. Assume that the move of jelly fish is monotonous in horizontal direction, i.e., it always moves in clockwise direction, never backwards.

Input files: text files, each of them with 10 rows and 80 columns representing the brightness level in the given parts of the picture. Jelly fish can be recognized by high brightness (value 1 to 9) on a black background (value 0).

00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000005950000000000000000000000000000000000000000
00000000000000000000000000000000000009990000000000000000000000000000000000000000
00000000000000000000000000000000000005950000000000000000000000000000000000000000
00000000000000000000000000000000000003930000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000
Directions
In order to capture the movement of the jelly fish between two pictures, use Earth-mover distance, also known as Wasserstein distance. It can be formulated as a min-cost flow problem on a certain network. Use NetworkX package (https://networkx.org) to perform the optimization required to find this flow.

About Earth-mover distance: Consider two distributions over a discrete set of points P: μ in [0,1]^P and λ in [0,1]^P. Since both are distributions and sum of μ(p) over all points in P is 1 (and the same holds for λ), there is surely a way to transform μ into λ: we denote fp,q the probability mass transfered from point p to q for each pair of points p,q from P, in order to transform μ into λ:

For each p in P: μ(p) = Σq fp,q and for each q in P: λ(q) = Σp fp,q.

Note that fp,p denotes the probability mass which remains at the same place.
Let d(p,q) denote the distance between p and q. Then, the cost of the transformation f is

Σp,q d(p,q) fp,q

The earth-mover distance of μ and λ is then the cost of the cheapest transformation between μ and λ.

Technical instructions:
Your code should implement function sort_files() which returns ordered list of the pictures, something like this:

['P1.txt', 'P2.txt', 'P3.txt', 'P10.txt', 'P4.txt', 'P13.txt', 'P14.txt', 'P9.txt',
  'P15.txt', 'P7.txt', 'P12.txt', 'P11.txt', 'P5.txt', 'P6.txt', 'P8.txt']
You should also define and use function comp_dist(file1, file2) which returns the Earth-mover distance between file1 and file2. I may want to access it during the grading process, especially if your output is not completely correct.

Make sure your code never breaks down. If you know that it cannot handle e.g. P10.txt, skip this file and don't include it in the output. This way, you will not get a full score, but you will still get points for the partial solution.

# opProblem 3

Bakery problem
Consider a small bakery with a single oven. It needs to schedule baking of n pastries, each of them having three requirements:

time when the preparations are done and pastry is ready for baking
time needed for baking, i.e., for how long should it remain in the oven
deadline: time when the custommer comes to pick up the pastry
At each moment, only one kind of pastry can be present in the oven.
Use an ILP to find a shortest baking schedule. Schedule, in this context, is a set of starting times s1, ..., sn denoting when should each pastry be put into oven. Note: these times need not be integral. However, integral variables will be useful to enforce that the periods when two different kinds of pastries are in the oven do not overlap.

Let us denote e1, ..., en the ending times of baking of each of the pastries, i.e., ei = si + baking time of pastry i. We need to make sure that for each two pastries i,j, one of the following needs to be true: ei ≤ sj or ej ≤ si. Obviously, they cannot hold at the same time and it depends on the precedence between i and j which one is true. Since we do not know the precedence in advance, which of these constraints should we include in the LP?

Big-M method
This name usually refers to an alternative way how to start the simplex method without knowledge of the initial basic feasible solution. We did not cover this in the class and I do not go into details of this here either. But the other meaning of Big-M is a method for switching someof the constraints on/off depending on the value of some binary variable.

Imagine, we have variable x which should be bounded by 10 if and only if some binary variable z is set to zero. Also, assume that there is no reason to increase x beyound some large number M (e.g., because we are minimizing over x, or we know that no feasible solution can have x > M for some other reasons). Then, we can write x ≤ 10 + M*z: if z is 0, this switches the constraint ON. If z=1, this constraint evaluates to x ≤ 10 + M which, by choice of M is satisfied by any reasonable solution to our LP and this effectively switches the costraint OFF. Usually, due to possible numerical issues, it is recommended to use M as small as possible. You can check the following blog for more discussion of big-M: https://orinanobworld.blogspot.com/2011/07/perils-of-big-m.html.

You may check that there is a suitable choice of M in our problem and use this approach in your solution.

Input
Text file containing a single line for each kind of pastry consisting of four numbers (integers) separated by spaces:

ID PRE DLN BAK
ID denotes the numerical ID of the pastry, PRE the time since midnight since when the pastry is ready for baking, BAK is the time it needs to spend in the oven, and DLN is the deadline when the pastry needs to be surely finished.
All times are in seconds.

Performance
In Mixed ILP, the performance becomes quite an issue and it matters how do you specify your program. In the template file, it is shown how to setup your LP solver to run in parallel in order to use the hardware of vocareum more efficiently. Since there are limits in vocareum on the length of the computation done during grading, your code when run in vocareum should finish within 10 minutes. Please try it before submitting!

Bakery problem visualization 
Use library matplotlib to visualize your solution suitably. I leave to your creativity how to do it, but it should be clear what are the moments when oven needs to be open, what pastry goes out and what should be put in. There are many other things to visualize: expected arrivals of custommers and times when each pastry is ready, critical preparations (which pastry needs special care to be prepared on time, otherwise it would delay the whole schedule, etc). The vizualization should be understandable to a non-expert, e.g. a baker operating the oven. Therefore, the main criterion for evaluation of this will be clarity and information it provides.

Output:
Your program should produce a picture in PNG format and record it to the file
./visualization.png

# opProblem 4

We have a vehicle which needs to pass a known test track. You are given values Preq(t) for each time t=1,...,T which the vehicle's wheels needs to exert in order to successfully pass this test track.

The vehicle has a combustion engine, a motor/generator connected to a battery, and a friction break. Motor/generator can act either as a motor when it uses energy stored in the battery to power the wheels, or as a generator when it extracts the power from the wheels (regenerative breaking) or the engine to store it in the battery.

Preq(t) is positive when the wheels need power, e.g. vehicle is ascending a hill or accelerating: power for the wheels needs to be provided by the combustion engine and/or the motor/generator which extracts the power stored in the battery. When Preq(t) is negative (e.g. because vehicle is descending a hill), the power is extracted by the motor/generator which can store it in the battery and/or by the friction break.

Power is conserved, i.e., at each time t, we have
Preq(t) = Peng(t) + Pmg(t) - Pbr(t)
where 0≤Peng(t)≤Peng_max is power produced by the combustion engine, Pmg_min ≤ Pmg(t) ≤ Pmg_max is power produced by the motor/generator (can be also negative if motor/generator absorbs power to charge the battery) and Pbr(t)≥0 is the power absorbed by the friction break. See data bellow for the definition of the constants.

For every t=1,...,T+1, the energy E(t) in the battery has to be between 0 and Ebatt_max representing the power stored in empty and full battery respectively. Moreover, we need to take into account the charging and discharging of the battery: we have
E(t+1) = E(t) - Pmg(t) - η|Pmg(t)|, for t=1,...,T,
see variable eta in the data. The term with coefficient η represents the energy lost due to the inefficiency of the battery and motor/generator. We also require E(T+1)=E(1) to make a fair comparison with a non-hybrid vehicle which has no battery.

The objective is to minimize the total fuel consumption of the vehicle over time, where the consumption at time t is given by formula Peng(t) + γ(Peng(t))2, i.e., a quadratic function. See data for the value of γ.

Formulating the problem as a convex program
It is almost convex, just one set of constraints is problematic. Hint: Try to relax it, only one inequality is important, but provide an explanation (e.g. in the comments of your code) why your formulation is equivalent.

# Task 1: Solve your convex program with cvxpy library
Link to the library: https://www.cvxpy.org/. It is installed in vocareum. Implement it in function car_with_battery()

# Task 2: comparison with a battery-less car
Change Ebatt_max to 0 and solve your program again to see how does it affect the power consumption. Implement your code in function car_without_battery()

Hint: Maybe you can prepare a single function which takes the value Ebatt_max as a parameter and solves your convex program based on this parameter. You can then call it from both functions (with/without battery) with the desired parameter value.

# Task 3: handle glitches
You may find out that although your program is equivalent, the solution found by the solver does not fulfill all the relaxed constraints with equality. This might happen during long periods of breaking when there is a lot of opportunities to charge the battery and sometimes the solver may decide to waste part of the power available to charge the battery (because it may charge it fully in the following time steps). There are two options how to proceed:

Postprocess the solution to get another solution with the same objective value where the relaxed constraints are preserved with equality. Such solution must exist since your program is equivalent to the original one. Hint: just move all the power from motor/generator to the battery and, if the battery is full, move it to the friction break.
Add a small term to the objective which will discourage such situation: for every t=1,...,T, you can add a term ε·max{0, -Pmg(t)} for some small positive ε in order to discourage absorbing power by the motor/generator if it is not going to be used for charging the battery (because it is cheaper to absorb the power using the friction break)
In case you decide to modify the objective, make sure the power consumption achieved by your program is similar to the power consumption achieved by the program with the original objective (with your choice of ε, they should not differ by more than 0.1).
Data
Template of main.py contains a code which generates data for you. The array Preq contains power requirements in all time steps. Bellow the definition of Preq, there are the bounds specifying the parameters of the engine, motor/generator, capacity of the battery, coefficient eta of the inefficiency of charging/discharging and coefficient gamma in the objective function.




