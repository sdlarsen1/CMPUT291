Updates - Bulk Insert

emp(sin, name, phone, city)
Edmonton_phonebook(name, phone)
```sql
INSERT INTO Edmonton_phonebook
SELECT name, phone
FROM emp
WHERE city = 'Edmonton'
```


Update Examples
------------
Insert a new customer record for John Smith
```sql
INSERT INTO customer
VALUES ('John', '345 Jasper Ave','Edmonton')
```

Delete all customer who have less than $1000 in their accounts
```sql
DELETE FROM customer
WHERE cname IN (SELECT cname
                FROM desposit
                WHERE balance < 1000)
```

Increase by 5% the balance of every customer who lives in Edmonton and has a balance of more than $5000
```sql
UPDATE desposit
SET balance = balance * 1.05
WHERE balance > 5000
AND cname IN (SELECT cname
              FROM customer
              WHERE city = 'Edmonton')
```

View Definition Examples
------------
Create a view of customers who live in Jasper and name the view jasper_customers
```sql
CREATE VIEW jasper_customers
AS SELECT *
FROM customer
WHERE city = 'Jasper'
```

List the name of all customers in Jasper
```sql
SELECT cname
FROM jasper_customers
```
In queries, a view is exactly like a base table.

Create a view called cust_info which gives for each customer the name, city, number of deposit accounts owned and the total balance.
```sql
CREATE VIEW cust_info(Name, city, Num, Total)
AS SELECT c.name, city, COUNT(accno), SUM(balance)
FROM deposit d, customer c
WHERE d.cname = c.cname
GROUP BY c.name, city
```

Create a view called deposit_holders which includes the name and the city of every deposit account holder
```sql
CREATE VIEW desposit_holders(Name, city)
AS SELECT distinct c.cname, city
FROM deposit d, customer c
WHERE d.cname = c.cname
```

Views Summary
-------------
- behave like a table
- derived table whose definition, not the table itself is stored
- degree of data independence
- SQLite does not support updateable(?) views, but could be achieved with triggers


Unknown Values - NULL
--------------
- useful when we don't know a column value
```sql
SELECT cname FROM customer WHERE city IS NOT NULL
```
- predicate city='Edmonton' evaluates to UNKNOWN when city is NULL
- What if the WHERE clause consists of several predicates?
    eg. city='Edmonton' OR street LIKE '100%'
    - use 3-value logic: values TRUE, FALSE, UNKNOWN

Set Operations
-------------
- Operations: UNION, INTERSECT, EXCEPT
- Duplicates are removed from union results by default

Constraint Examples
--------------
```sql
CREATE TABLE branch (
  bname CHAR(15) NOT NULL,
  address VARCHAR(20),
  city CHAR(9),
  assets DECIMAL(10,2) DEFAULT 0.00)
  CHECK (assets >= 0)
  CHECK (cname = 'Bill Clinton' OR
          balance > 100000);
```
- Every row must satisfy first check
- Second check is examined every time tuples are inserted/updated


RELATIONAL ALGEBRA
------------------
- "Under the hood" of SQL, procedural

What is an algebra?
  - Language based on operators and a domain D
  - operators map values in D into other values in D
    - an expression involving operators and arguments produces a value
    that is again in D --> changing of operators

Relational Algebra:
  - domain: set of relations
  - basic operators: select, project, union, set difference
  - derived operators: set intersection, division, join
  - procedural; relation expression specifies query by describing an algorithm for determining the result of an expression
  - expression referred to as query

Operations on Tables
  - operations on one table: pick some rows, pick some columns
  - operations on two tables: join, etc.
  - no duplicate data allowed, assumed to be sets

Select Operator
  - represented by σ
  - select rows that satisfy a specific condition

Selection Conditions
  - simple selection condition:
    <attribute> operator <constant>
    <attribute> operator <attribute>
  - <condition> OPERATOR <condition>:
    OPERATOR = and, or, not, etc.

Project Operator
  - represented by π
  - produces relation obtained from the argument relation by dropping all attributes *not* mentioned in the *attribute list*
    - ie. only keeps attributes in the attribute list

Union Compatible Relations
  - two relations are **union compatible** if:
    - both have same number of columns
    - names of attributes are the same in both
    - attributes with the same name in both relations have the same domain
  - can be combined using union, intersection, difference

Cartesian Product
  - if R and S are two relations, R x S is the set of concatenated tuples <x,y>, where x is a tuple in R and y is a tuple is S
    - (R & S need to be union compatible)
  - R x S is expensive to compute
    - factor of two in the size of each row
    - quadratic in the number of rows
    - R x S = {<a,b>| a ∈ R and b ∈ S}
    - set theory: <<ab>, <cd>>
    - rel. algebra: <a, b, c, d>

Renaming
  - result of an expression is a relation
  - attributes (columns) of a relation must have distinct names
    - not guaranteed with the Cartesian product
  - **renaming operator** solves this problem
    - use expr[A1,...,An]

Join Operator
  - θ, the join condition, is a conjunction of terms:
      Ai op Bi
    in which Ai is a n attribute of R; Bi is an attribute of S; and op is an operator

Equijoin
  - join condition is a conjunction of equalities

Natural Join
  - special case of equijoin:
    - join condition equates all and *only* those attributes with the same name
    - duplicate columns eliminated from result

Division
  - goal is to produce the tuples in one relation, r, that match *all* tuples in another relation, s
    - r(A1, A2,...,An)
    - s(B1, B2,..., Bn)
    - r/s with attributes A1,...,An is the set of all tuples <a> such that for every tuple <b> in s, <a,b> is in r
  - **more info in bookmarked webpages**

# Rational Normalization Theory
Limitations of Relational Database Designs
  - provides set of guidelines, does not result in unique schema
  - pitfalls:
    - repetition of information
    - inability to represent certain information
    - loss of information
  - normalization theory provides a mechanism for analyzing and refining the schema produced by an ER design

Redundancy
  - dependencies between attributes cause redundancy
    - eg. all addresses in the same town have the same zip code
  - set-value attributes in the ER diagram result in multiple rows in corresponding table
    - eg. Person(SSN, name, address, hobby)
    - person with multiple hobbies yields multiple rows in table Person
      - the association between name and address for the same person is stored redundantly
      - hobby cannot be __null__ because it is part of the _primary key_

Anomalies
  - __update anomaly__: a change in address must be made in several places
  - __deletion anomaly__: suppose a person gives up all hobbies
    - set hobby attribute to null?
      - no, since hobby is part of key
    - delete entire row?
      - no, since we lose other information in the row
  - __insertion anomaly__: hobby value must be supplied for any inserted row since hobby is part of key

Decomposition
  - Solution: use two relations to store Person information
    - Person1(SSN, name, address)
    - Hobbies(SSN, hobby)
  - decomposition is more general: people with hobbies can now be described
  - no update anomalies:
    - name and address stored once
    - a hobby can be separately supplied or deleted

Functional Dependencies
--
  - Definition: a __functional dependency__ (FD) on a relation schema R is a _constraint_ X -> Y, where X and Y are subsets of attributes of R
  - Definition: a __constraint__ on a relation schema R i a condition that has to be satisfied in every allowable instance of ref
  - Definition: an FD X->Y is __satisfied__ in an instance r of R is for every pair of tuples, t and s: if t and s agree on all attributes in X then they must agree on all attributes in Y

Notation/Conventions
  - capital letters from the beginning of the alphabet denote __single__ attributes
    - eg. A, B, C
  - capital letters from the end of the alphabet denote __sets__ of attributes
    - eg. X, Y, Z
  - string ABC denotes the {A,B,C}
  - string XY denotes X + Y
  - string XA denotes X + {A}

Functional Dependencies Cont'd
  - FD must be identified base on semantics of application
  - given a particular allowable instance r1 of R, we can check if it violates some FD f, but we cannot tell if f holds over the schema r
  - a key constraint is a special kind of functional dependency: all attributes of the relation occur in the right side of the FD
    - SSN -> SSN, name, address
    - Address -> ZipCode
    - VIN -> Manufacturer, Engine Type, etc.

Entailment, Closure, Equivalence
  - Definition: if _F_ is a set of FDs on schema _R_ and _f_ is another FD on _R_, then _F_ __entails__ _f_ if every instance _r_ of _R_ that satisfies every FD in _F_ also satisfies _f_
  - Eg. F = {A → B, B → C}, and f is A → C
    - if StreetAddr → Town and Town → Zip, then StreetAddr → Zip
  - Definition: the __closure__ of _F_, denoted _F+_, is the set of all FDs entailed by _F_
  - Definition: _F_ and _G_ are __equivalent__ if _F_ entails _G_ and _G_ entails _F_

Entailment Cont'd
  - satisfaction, entailment, and equivalence are _semantic_ concepts - defined in terms of the actual relations in the "real world"
    - they define _what these notions are_, not how to compute them
  - how to check if _F_ entails _f_ or if _F_ and _G_ are equivalent?
    - Solution: find algorithmic, _syntactic_ ways to compute these notions

Armstrong's Axioms for FD
  - __Reflexivity__: If Y subset X, the X → Y (trivial FD)
    - Name, address → Name
  - __Augmentations__: if X → Y then XZ → YZ
    - if Town → Zip, then Town, Name → Zip, Name
  - __Transitivity__: if X → Y and Y → Z, then X → Z
  - __Union__: if X → Y and X → Z, then X → YZ
  - __Decomposition__: if X → YZ, then X → Y and X → Z

## BCNF
  - __Definition__: a relation schema R = (R, F) is in _BCNF_ if for every FD → Y associated with R either
    - Y is a subset of X (ie., the FD is trivial)
    - X is a superkey of R
  - Example: Person1(SSN, Name, Address)
    - the only non-trivial FD is SSN → Name, Address
    - since SSN is a key, Person1 is in BCNF

Decomposition into BCNF
  - Consider relation R with FDs F
  - if X → Y violates BCNF (and X intersect Y ≠ emptyset),
    decompose R into XY and R - Y
    - repeated application of this idea will give us a collection of relations that are in BCNF and guaranteed to terminate
      - eg. CSJDPQV, key C, JP → C, SD → P, J → S
        - to deal with SD → P, decompose into SDP, CSJDQV
        - to deal with J → S, decompose CSJDQV into JS and CDJQV
  - in general, several dependencies may cause violations of BCNF. The order in which we "deal with" them could lead to very different relations

## Third Normal Form (3NF)
  - a relational schema R is in 3NF if for every FD X → Y associated with R either
    - Y is a subset of X (ie, the FD is trivial)
    - X is a superkey of R
    - every A ∈ Y is part of some key of R
  - 3NF is weaker than BCNF
    - every schema in BCNF is also in 3NF
  - see slides for example

## Minimal Cover
  - a minimal cover of set dependencies, T, is a set of dependencies, U, s.t.
    - U is equivalent to T
    - all FDs in U have the form X → A where A is a single attribute
    - it is not possible to make U smaller by
      - deleting an FD
      - deleting an attribute from an FD
  - FDs and attributes that can be deleted in this way are called _redundant_
  - see slides for example on computing Minimal Cover
