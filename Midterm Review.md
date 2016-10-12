# Review
## ER Diagrams
  - Basics
    - entities: objects
    - attributes: used to describe/identify entities
    - relationships: how two (or more) entities connect
  - Role: the function of an entity set in a relationship set
    - *role labels* are needed whenever an entity set has multiple functions in a relationship set

Many-to-Many relationships
  - no constraints
    - eg. many employees can be in relationships with many projects and vice versa

Many-to-One
  - constraint: each employee works in at most one department
    - given an employee, we can uniquely identify the department they work in

Participation Constraints
  - represented by a **bold** line
  - eg. every project *must* have a supervisor
    - every pid value in projects must appear in an element of the supervises relationship

Set-Value Attributes
  -  eg. each employee can have more than 1 hobby
    - attribute value can be a set: (1111, John, (stamps, coins))

Weak Entities
  - identified uniquely only by considering **primary key** of another (owner) entity
    - owner entity and weak identity must participate in a 1-1 relationship
    - weak entity must have total participation in identifying relationship
    - weak entities have a **weak key**

ISA Hierarchies
  - forms a new entity set as a union of two or more entity sets, or
  - forms a derived entity set by taking a subset of a given entity set
    - attributes common to all lower-level entities are represented a the higher-level entity

## Mapping ER Diagrams to Tables
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
  );
  ```
  - relationships with key constraints
    - better to combine tables for one-to-many relationships
    - generally has a single **PRIMARY KEY**
  - relations with participation restraints
    - use a **NOT NULL**    
  - set-value attributes
    - cannot store more than one value in a field
    - combination of (sin, hobby) becomes primary key        
  - multi-value attributes and many-to-Many relationships
    - primary key must be tuple across relationships
    - does not include primary key of employee table (belongs to only that table)
  - weak entities
    - weak entity set and identifying relationship set are translated into a single table
    ```sql
    CREATE TABLE foo(
      ....
      ON DELETE CASCADE
    );
    ```
  - ISA hierarchies
    - general approach: 3 relations

## SQL
Basic queries
  ```sql
  SELECT <columns>
  FROM R1 r1, R2 r2,...
  WHERE condition;
  ```
  - is conceptually equivalent to
      πTargetList(σCondition(R1xR2x...xRn))

Duplicates
  - use **SELECT DISTINCT**

Expressions using strings
  - pattern may include wildcard characters
    - % matching any string
    - _ matches

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
  select b.city, count(b.name), avg(b.assets)
  from branch b
  group by b.city;
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
