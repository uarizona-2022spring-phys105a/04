You may accept this assignment in GitHub Classroom using this link:

    https://classroom.github.com/a/kvmaNFBm

## Assignment 04: compute pi using random number

In this assignment, you are going to develop a Python program to
compute pi using a Monte Carlo method.
You are going to write this program from scratch.
But don't worry!
The material you learned from the last assignment will be useful.

### The Problem

The idea of using Monte Carlo to compute `pi` is very simple.
We use the facts that

* The area of a circle is `A = pi r**2`.

Given that a quater circle with radius `r` fits inside a `r * r` box,
the *ratio* between the red area in the following square provides:

* `pi = 4 A_quater / A_box`

For simplicity, we will use unit circle in this calculation.

### Goal

You will write a python script `pi.py` that takes exactly one argument
`n`, which is the number of sampling points to compute `pi`.

This repository also contain two extra files `plot.py` and `run.sh`.
`plot.py` is a plotting script that reads in a text file and plot the
result using matplotlib.
`run.sh` is a "driver" script that runs *YOUR* `pi.py` many times in
order to generate the input of `plot.py`.

### Computational Thinking: Breaking the Problem into Smaller Pieces

We suggest breaking the problem into 4 steps:

1. Develop a python function `random_point()` to randomly generate a
   two-dimensional point `(x, y)` in the domain `[0,1) x [0,1)`.

2. Given a two-dimension point `(x, y)`, develop another python
   function `inside(x, y)` to test if the point is inside the quater
   circle.

3. Write a for loop to sample `n` random points, test if each of them
   is inside the quater circle, and use `n_inside / n_total` as an
   approximation of `pi`.

4. Finally, use python's standard `argparse` to read in a command line
   argumentment and the computation of `pi`.
   The assignment from last week will be useful:

       https://github.com/uarizona-2022spring-phys105a/03/blob/main/quadratic_explained.py#L266
