# Day 1 – Exercises

## Q1 – Vector operations

Given:
- \( a = (1, 2, 3) \)
- \( b = (4, -1, 2) \)

### (a) Dot product \( a \cdot b \)

\[
a \cdot b = 1 \cdot 4 + 2 \cdot (-1) + 3 \cdot 2
          = 4 - 2 + 6
          = 8
\]

**Answer:** \( a \cdot b = 8 \)

---

### (b) L2 norm of \( a \), i.e., \( \|a\| \)

\[
\|a\| = \sqrt{1^2 + 2^2 + 3^2}
      = \sqrt{1 + 4 + 9}
      = \sqrt{14}
\]

Numerically, \( \sqrt{14} \approx 3.7417 \).

**Answer:** \( \|a\| = \sqrt{14} \approx 3.74 \)

---

### (c) Cosine similarity between \( a \) and \( b \)

First compute \( \|b\| \):

\[
\|b\| = \sqrt{4^2 + (-1)^2 + 2^2}
      = \sqrt{16 + 1 + 4}
      = \sqrt{21}
\]

Cosine similarity:

\[
\cos \theta = \frac{a \cdot b}{\|a\|\|b\|}
            = \frac{8}{\sqrt{14} \cdot \sqrt{21}}
            = \frac{8}{\sqrt{294}}
\]

Numerically:

\[
\sqrt{294} \approx 17.146
\]
\[
\cos \theta \approx \frac{8}{17.146} \approx 0.467
\]

**Answer:** \( \cos \theta \approx 0.47 \)

---

## Q2 – Concept: What does a matrix do to a vector?

A matrix can be viewed as a function that transforms vectors. When we multiply a matrix \( A \) by a vector \( x \), we get a new vector \( Ax \). Geometrically, this can represent operations like stretching, squashing, rotating, or shearing space. Each column of the matrix shows where the corresponding basis vector ends up after the transformation. So, instead of thinking of a matrix as “just numbers”, it is more helpful to think of it as a rule that takes input vectors and outputs transformed vectors. In deep learning and LLMs, these matrices are the learned weights that transform input embeddings and hidden states into new representations layer by layer.

---

## Q3 – Matrix–vector multiplication

Given:

\[
A=
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix},
\quad
x=
\begin{bmatrix}
1 \\
-1
\end{bmatrix}
\]

Compute \( Ax \):

\[
Ax =
\begin{bmatrix}
1 \cdot 1 + 2 \cdot (-1) \\
3 \cdot 1 + 4 \cdot (-1)
\end{bmatrix}
=
\begin{bmatrix}
1 - 2 \\
3 - 4
\end{bmatrix}
=
\begin{bmatrix}
-1 \\
-1
\end{bmatrix}
\]

**Answer:** \( Ax = \begin{bmatrix} -1 \\ -1 \end{bmatrix} \)

---

## Q4 – Sentence as a matrix (LLM view)

Suppose a sentence has 4 words, and each word is represented by a 3-dimensional embedding vector. We can stack these word vectors **row-wise** into a matrix of shape \( 4 \times 3 \). Each row corresponds to one word in the sentence, and each column corresponds to one feature dimension of the embedding space.

So if:
- word 1 → \( (e_{11}, e_{12}, e_{13}) \)
- word 2 → \( (e_{21}, e_{22}, e_{23}) \)
- word 3 → \( (e_{31}, e_{32}, e_{33}) \)
- word 4 → \( (e_{41}, e_{42}, e_{43}) \)

Then the sentence matrix is:

\[
S =
\begin{bmatrix}
e_{11} & e_{12} & e_{13} \\
e_{21} & e_{22} & e_{23} \\
e_{31} & e_{32} & e_{33} \\
e_{41} & e_{42} & e_{43}
\end{bmatrix}
\]

In Transformers, this sentence matrix is passed through layers of matrix operations (linear layers, attention, etc.) to produce new representations that encode context and meaning.

**Answer:** The sentence can naturally be seen as a \( 4 \times 3 \) matrix where rows = tokens, columns = embedding dimensions.
