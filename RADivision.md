# Division in Relational Algebra
Division R/S is expressed in terms of projection, selection, set difference, and cross product.

  R = (A1,...,An,B1,...,Bm)

  S = (B1,...,Bm)
  - need to find combinations in R where every value occurs in S

T1 = πA1,...,An(R) x S
  - all possible combinations of (A1,...,An) tuples with S tuples
  - need to find complement

T2 = πA1,...,An(T1 - R)
  - all (A1,...,An) tuples that are __not__ associated with __every__ B value in R, those are the ones that should not be in the answer of the division

R/S = πA1,...,An(R-T2)
    = πA1,...,An(R - πA1,...,An(πA1,...,An(R) x S) - R)
