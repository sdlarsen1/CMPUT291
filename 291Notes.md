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
