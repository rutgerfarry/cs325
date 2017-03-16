# assignment3
- Rhea Mae Edwards **(edwardrh)**, Miles Curry **(currymi)** & Rutger Farry **(farryr)**
- CS 325
- Dr. Xiaoli Fern
- 15 March 2016

## Warm-up question: Least squares isn't good enough for me
**Write summary here**
The goal of this question was to determine the line of best fit using linear
program. Given the set of points, `(x1, y1), (x2,y2), ... (xN, yN)`. find values of `a` and `b` to minimize: ![Prob 1 Objective
Function](docs/prob1OF.png "Objective Function").

### Linear program description
**TODO**
To turn this into a linear program, the variable `m` was created to represent as
the objective function to be  *minimized*. With values: `(1,3), (2,5), (3,7),
(5,11), (7,14), (8,15), (10, 19)`.

    * Objective: `Min m`
    
    Such that:

    * `a * x + b - y <= m`
    * `-a * x - b + y <= m'
    * For all points `(x1, y1), (x2, y2), ... (xN, yN)`.

### Running the code
**TODO**
The script was built in Python 2 and uses [PuLP] as its linear program solver as
well as numpy Before running the script, PuLP will need to be installed.

```bash
pip install -y requirements.txt     # Install PuLP
python warm_up.py                   # Run the Script
```
### Solution
**TODO**
The best values of `a` and `b`, given the set of points: `(1,3), (2,5), (3,7),
(5,11), (7,14), (8,15), (10, 19)` found by the script is:

    * `a: 1.7142857`
    * `b: 1.8571492`

And the output of PuLP confirmed it was an optimal solution:

```bash
Status: Optimal
a: 1.7142857
b: 1.8571492
```
### Plot
**TODO**



## Warming-up question: Local temperature change
**Write summary here**

### Running the code
**TODO**
### Linear program description
**TODO**
### Solution
**TODO**
include variables, final equation, and output of GuLP, showing it was an optimal solution
### Plot
**TODO**
- raw data plotted as points in 2-d (with d as the x-axis and T as the y-axis),
- best fit curve, and
- linear part of the curve x0 + x1 · d.
### Reflection
**TODO**
Discuss whether or not Corvallis' temperature is rising (per day and per century) and whether these findings fit with other climate models

## Meta
If you're reading the PDF version of this file, we generated it from `README.md` using pandoc. You can update it from the README file using:
```bash
pandoc README.md --latex-engine=xelatex -o writeup.pdf
