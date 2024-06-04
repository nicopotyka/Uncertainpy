# Uncertainpy

Uncertainpy is a Python library for computational argumentation. It currently mainly supports
- **Gradual (Quantitative) Argumentation** [(src/uncertainpy/gradual)](src/uncertainpy/gradual)
  
but also contains some preliminary modules that can help with 
- Probabilistic Argumentation [(src/uncertainpy/probability)](src/uncertainpy/probability).

## Getting Started (Gradual Argumentation)

The best way to get started is to go through the example notebook [(examples/gradual/gradual_argumentation_examples.ipynb)](examples/gradual/gradual_argumentation_examples.ipynb). 
The notebook explains 
- how to create gradual/quantitative bipolar argumentation graphs (BAGs) either from bag-files or programmatically,
- how to declare the argumentation semantics,
- how to compute strength values.

Roughly speaking, there are four steps involved in solving a gradual argumentation problem:
1. choose a semantics `model = grad.semantics.QuadraticEnergyModel()`,
2. choose an algorithm to compute strength values `model.approximator = grad.algorithms.RK4(model)`,
3. choose the BAG `model.BAG = grad.BAG("stock_example.bag")`,
4. compute strength values of arguments `model.solve(delta=10e-2, epsilon=10e-4, verbose=True, generate_plot=False)`.


## Semantics

Most gradual argumentation semantics are defined by an iterative procedure that initializes the strength values of arguments with their base score (aka initial strength)
and repeatedly updates the strength values with an update function until the values converge. 
The update function can typically be decomposed into 
- an **aggregation function** that aggregates the strength values of an argument's attackers and supporters and
- an **influence function** that adapts the argument's initial strength based on the aggregate.

Intuitively, attackers decrease the aggregate proportional to their strength while supporters increase it accordingly. An overall positive
aggregate (the supporters dominate the attackers) will result in an increased strength, while a negative aggregate (the attackers dominate the supporters) will result
in a decreased strength in the next iteration. 

Uncertainpy allows using high-level implementations of semantics [(src/uncertainpy/gradual/semantics)](src/uncertainpy/gradual/semantics)
or defining semantics from implementations of aggregation and influence function [(src/uncertainpy/gradual/semantics/modular)](src/uncertainpy/gradual/semantics/modular).


## Approximators

### General BAGs

Algorithms for computing strength values for general BAGs are called **approximators** in Uncertainpy. 

`model.approximator = grad.algorithms.RK4(model)`

The reason for this name is that strength values have to be computed iteratively in cyclic graphs.
If a well-defined limit exists, the approximator will converge to this limit (approximate the limit). However, it can happen that the strength values start oscillating
and that no well-defined limit exists. Approximators have two parameters that can influence the convergence/termination behaviour of the implementation.

`model.solve(delta=10e-2, epsilon=10e-4, verbose=True, generate_plot=False)`

- **delta** is a step size parameter of the algorithm. Intuitively, a smaller step size will result in more accuracy but will increase runtime. If the step size is chosen
too large, the algorithm may fail to converge to the limit even if it exists theoretically. delta=10e-2 usually works well for RK4.
- **epsilon** is the termination condition. The algorithm stops when the strength values in the last two iterations do not differ by more than epsilon. Again, a small
epsilon will improve accuracy but increase runtime. If the step size is chosen too large, the algorithm may stop too early with strength values that are far away from the
true strength values in the limit. epsilon=10e-4 usually works well for RK4, that is, the algorithm converges quickly and the computed strength values are close to the real
strength values.

Another way to think about epsilon is the following: if the limit exists, it is guaranteed to be a fixed-point of the update function. That is, if we actually reached the limit
the difference between the current and the next strength values are guaranteed to be 0. So, theoretically, we should set epsilon to 0. However, the strength values may never reach
the limit either for theoretical (the limit may not exist or cannot be reached in finite time) or for numerical reasons (rounding errors due to floating-point arithmetic). 
By setting epsilon to a small value, we make sure that the computed solution is almost a fixed-point. 


### Acyclic BAGs

In acyclic graphs, the limit of the strength values is always well-defined and can be computed by a simple forward pass. In this case, the _computeStrengthValues_ function from the 
[(src/uncertainpy/gradual/algorithms/Acyclic.py)](src/uncertainpy/gradual/algorithms/Acyclic.py) can be used to compute strength values more efficiently.

`strength_values = grad.algorithms.computeStrengthValues(bag, agg_f, inf_f)`

The algorithm has a simplified interface and directly takes a BAG and the semantics as input. The inputs are
- a BAG object,
- the aggregation function of the semantics,
- the influence functions of the semantics.
