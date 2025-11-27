# Day 1 – Linear Algebra Basics (Vectors & Matrices)

## Vectors

- A vector is an ordered list of numbers that can represent many things: position, direction, features of a word, etc.
- In the geometric view, a vector is like an arrow from the origin to a point in space.
- Vectors can be added and scaled. These operations correspond to moving and stretching arrows.

## Matrices

- A matrix is a rectangular array of numbers.
- A matrix can be seen as a **linear transformation**: it takes in a vector and outputs another vector.
- Examples of transformations:
  - Scaling (making vectors longer/shorter)
  - Rotations
  - Shearing (slanting shapes)
- Solving a system of equations like `Ax = b` means finding which input vector `x` maps to output `b` under the transformation defined by `A`.

## Matrix–Vector Multiplication

- If `A` is an m×n matrix and `x` is an n-dimensional vector, `Ax` is an m-dimensional vector.
- Each entry of `Ax` is a dot product between a row of `A` and the vector `x`.
- In Transformers, lots of operations are just huge matrix–vector or matrix–matrix multiplies.

## Span and Linear Combinations

- A **linear combination** of vectors is a sum of scaled versions of them, like  
  `a*v1 + b*v2 + c*v3`.
- The **span** of a set of vectors is the set of all possible linear combinations of those vectors.
- If we say vectors span a space, it means we can reach any point in that space using those vectors and scalar weights.
- In embedding spaces, we are effectively operating in a high-dimensional vector space whose basis and span define what can be represented.

## Key Insights I Noted

- A system of linear equations is not just numbers and symbols—it is about whether a vector `b` lies in the column space (span of columns) of `A`.
- Thinking visually about vectors and matrices (transformations of space) makes the algebra much easier to remember.
- Almost everything in deep learning boils down to “multiply a matrix by a vector (or another matrix) many, many times.”
