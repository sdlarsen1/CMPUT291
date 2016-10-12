# Review
## ER Diagrams
  - Basics
    - entities: objects
    - attributes: used to describe/identify entities
    - relationships: how two (or more) entities connect
  - Role: the function of an entity set in a relationship set
    - *role labels* are needed whenever an entity set has multiple functions in a relationship set

[Many-to-Many Relationships](https://github.com/sdlarsen1/CMPUT291/blob/master/images/many-to-many.png)
  - no constraints
    - eg. many employees can be in relationships with many projects and vice versa

[Many-to-One](https://github.com/sdlarsen1/CMPUT291/blob/master/images/many-to-one.png)
  - constraint: each employee works in at most one department
    - given an employee, we can uniquely identify the department they work in

[Participation Constraints](https://github.com/sdlarsen1/CMPUT291/blob/master/images/participation.png)
  - represented by a **bold** line
  - eg. every project *must* have a supervisor
    - every pid value in projects must appear in an element of the supervises relationship

[Set-Value Attributes](https://github.com/sdlarsen1/CMPUT291/blob/master/images/set-value.png)
  -  eg. each employee can have more than 1 hobby
    - attribute value can be a set: (1111, John, (stamps, coins))

[Weak Entities](https://github.com/sdlarsen1/CMPUT291/blob/master/images/weakentity.png)
  - identified uniquely only by considering **primary key** of another (owner) entity
    - owner entity and weak identity must participate in a 1-1 relationship
    - weak entity must have total participation in identifying relationship
    - weak entities have a **weak key**

[ISA Hierarchies](https://github.com/sdlarsen1/CMPUT291/blob/master/images/isa.png)
  - forms a new entity set as a union of two or more entity sets, or
  - forms a derived entity set by taking a subset of a given entity set
    - attributes common to all lower-level entities are represented a the higher-level entity

## Mapping ER Diagrams to Tables
Entity Sets to Tables
  ```sql
  CREATE TABLE employees (
    sin CHAR,
    name CHAR,
    PRIMARY KEY (sin)
  )
  ```

Relationship Sets to Tables
  - attributes of relationship with no constraints
    - key of every participating entity set
    - all descriptive attributes
```sql
CREATE TABLE Works_on (
  sin char(11),
  pid integer,
  since date,
  primary key (sin, pid),
  foreign key constraint(...)
)
```

Relationships with Key Constraints
  - better to combine tables for one-to-many relationships
  - generally has a single **PRIMARY KEY**
  - relations with participation restraints
    - use a **NOT NULL**
  ```sql
  CREATE TABLE emp_works (
    sin CHAR,
    name CHAR,
    did CHAR,
    since DATE,
    PRIMARY KEY sin,
    FOREIGN KEY (did) REFERENCES Departments
  )
  ```

Set-Value Attributes
  - cannot store more than one value in a field
  - same problem arises when mapping a relationship with a set-value attribute
  - combination of (sin, hobby) becomes primary key
  ```sql
  CREATE TABLE Employees (
    sin CHAR,
    name CHAR,
    hobby CHAR,
    PRIMARY KEY (sin, hobby)
  )
  ```

Multi-value Attributes and Many-to-Many Relationships
  - primary key must be tuple across relationships
  - does not include primary key of employee table (belongs to only that table)

Weak Entities
  - weak entity set and identifying relationship set are translated into a single table
  ```sql
  CREATE TABLE foo(
    ....
    ON DELETE CASCADE
  )
  ```

ISA hierarchies
  - general approach: 3 relations
  ```sql
  CREATE TABLE Contract_Emps(
    sin CHAR NOT NULL,
    ....
    FOREIGN KEY sin REFERENCES Employees
    ON DELETE CASCADE
  )
  ```
  - alternate approach: split into types of ISAs, provided the relationship covers

## SQL
Basic queries
  ```sql
  SELECT <columns>
  FROM R1 r1, R2 r2,... -- implicit join
  WHERE C;
  ```
  - _tuple_ variables r1, r2,..., rn range over rows of R1, R2,..., Rn, respectively
  - is conceptually equivalent to
      πTargetList(σCondition(R1xR2x...xRn))
  - conceptual evaluation strategy
    - __FROM__ produces a Cartesian product of listed tables
    - __WHERE__ selects only those (combined) rows from the Cartesian product that satisfy condition C
    - __SELECT__ retains the desired columns

Duplicates
  - duplicate rows not allowed in a relation
  - duplicate elimination from a query is expensive and not automatically done:
    - use **SELECT DISTINCT**

Operations Over Strings
  - equality and comparison operators apply to strings (based on lexical ordering)
  ```sql
    WHERE cname < 'P'
  ```
  - concatenate operator applies to strings
  ```sql
    WHERE bname ||'--'|| address = ...
  ```
  - expressions can also be used in __SELECT__ clause
  ```sql
  SELECT bname ||'--'|| address AS NameAdd
  FROM branch
  ```

Expressions Using Strings
  - expression for string matching
    - col-name [__NOT__] __LIKE__ pattern
  - pattern may include wildcard characters
    - % matching any string
    - _ matches any single character
    ```sql
    SELECT *
    FROM customer
    WHERE name LIKE '%John%'
    ```

Queries over multiple relations
  - join conditions

Nested structures
  - **IN** operator
  - **EXISTS** operator

Group By
  - groups rows by attributes mentioned in **GROUP BY**
  - creates single output line that repeats the attributes given by **GROUP BY** condition
    - plus whatever you want to do now for the whole group
  ```sql
  SELECT b.city, COUNT(b.name), AVG(b.assets)
  FROM branch b
  GROUP BY b.city;
  ```
  - **HAVING** clause
    - group condition, excludes certain groups
    - allows you to add **aggregates**
  - proper usage
    - every attribute that occurs in **select** clause must also occur in **group by** or it must be an aggregate
    - *aggregates* cannot be applied to a select statement, only the result of the select statement

## NULL
Null is not a constant, it is a truth-value

## Left Outer Join
Only matches tuples that can be matched
  - places null values in places that have no match

## Relational Algebra
Up to and not including division
