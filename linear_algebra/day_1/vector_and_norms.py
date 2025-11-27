import math

def dot(a, b):
    """
    Compute dot product of two vectors (lists/tuples of numbers).
    """
    assert len(a) == len(b), "Vectors must be same length"
    return sum(x * y for x, y in zip(a, b))


def l2_norm(a):
    """
    Compute L2 norm (Euclidean length) of a vector.
    """
    return math.sqrt(sum(x * x for x in a))


def cosine_similarity(a, b):
    """
    Compute cosine similarity between two vectors.
    cos(theta) = (a · b) / (||a|| * ||b||)
    """
    denom = l2_norm(a) * l2_norm(b)
    if denom == 0:
        raise ValueError("Zero-length vector not allowed for cosine similarity")
    return dot(a, b) / denom


if __name__ == "__main__":
    # Basic tests
    a = [1, 2, 3]
    b = [4, 5, 6]
    print("a:", a)
    print("b:", b)
    print("Dot(a, b):", dot(a, b))          # Expected: 32
    print("||a|| (L2):", l2_norm(a))        # Expected: sqrt(14) ≈ 3.741657
    print("Cosine similarity:", cosine_similarity(a, b))

    # Orthogonal vectors example
    u = [1, 0]
    v = [0, 1]
    print("\nOrthogonal example:")
    print("u:", u)
    print("v:", v)
    print("Dot(u, v):", dot(u, v))          # Expected: 0
    print("Cosine similarity:", cosine_similarity(u, v))  # Expected: 0.0

    # Simple 3-4-5 vector norm check
    w = [3, 4]
    print("\nVector w:", w)
    print("||w|| (L2):", l2_norm(w))        # Expected: 5.0
