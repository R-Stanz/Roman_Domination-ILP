Roman_Domination-ILP
===

General Description
---
This repository is made thinking on analyzing the solving of the roman domination problem with integer linear programming and mixed integer linear programming approaches. 
<p>
In order to achieve it, we are going to use the Google OR tools on python 3 to solve the linear models generated that will help to analyze the performance of the selected approaches.



Technologies
---

It's been used the following technologies:

|Name|Version|
|---|---|
|Jupyter Notebook|7.1.1|
|MatPlotLib|3.8.2|
|NetworkX|3.3|
|OR-Tools|9.10.4067|
|Pandas|2.2.1|
|Python 3|3.10.12|


Theoretical Approaches
---

For the integer linear programming it's been used the ReVelle and Rosing formulation. [^1]

For the mixed integer linear programming it's been used the improved version proposed by Marija Ivanovic. [^2]


Implementations Approaches
---

The implementation tool required create the solutions for solve the system of equations was the google OR-tools. 

If needed both the rr and the rr improved implementations could be almost the same thing, exchanging just one variable instead of been a IntVar been a NumVar.

But instead that, I chose the CP-SAT solver for the rr implementation, because it been the default solver for integer programming [^3], and the pywrappl SAT for the rr improved implementation, a flexible solver [^4].


Repository Organization
---

The code used to develop the solutions was thought to divide the code in 4 parts - one part in a python notebook with the rr implementation, another one with the rr improved implementation, some complementary functions (to help reduce the code written on the notebooks) on a python file named handlers and the rest of the code on a python notebook with the benchmark data analysis.

The benchmark data is stored in the data directory. Currently the benchmark data is not up to date with the code on the repository, it needs to be processed by the codes on the rr implementation and rr improved implementation. 


FootNotes
---

[^1]: C.S. ReVelle, K.E. Rosing, *Defendens imperium romanum: a classical problem in military strategy*, Am. Math. Mon. **107**(7) (2000), 585-594.

[^2]: M. Ivanovic, *Improved mixed integer linear programming formulations for roman domination problem*.

[^3]: Google OR-Tools, CP-SAT: https://developers.google.com/optimization/cp

[^4]: Google OR-Tools, Linear Solver: https://developers.google.com/optimization/lp