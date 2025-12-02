## Databases

[Databases (DB)](https://en.wikipedia.org/wiki/Database) – a set of data that are organized according to certain rules (for example, a library is a database for books).

[Database management system (DBMS)](https://en.wikipedia.org/wiki/Database#Database_management_system) is a software that allows you to create a database and manipulate it conveniently (perform various operations on the data). An example of a DBMS is a librarian. He can easily and efficiently work with the books in the library: give out requested books, take them back, add new ones, etc.

-   ### Database classification

    Databases can differ significantly from each other and therefore have different areas of application. To understand what database is suitable for this or that task, it is necessary to understand the classification.

    -   [Relational DB](https://en.wikipedia.org/wiki/Relational_model)
        > These are repositories where data is organized as a set of tables (with rows and columns). Interactions between data are organized on the basis of links between these tables. This type of database provides fast and efficient access to structured information.
    -   [Object-oriented DB](https://en.wikipedia.org/wiki/Object_database)
        > Here data is represented as objects with a set of attributes and methods. Suitable for cases where you need high-performance processing of data with a complex structure.
    -   [Distributed DB](https://en.wikipedia.org/wiki/Distributed_database)
        > Composed of several parts located on different computers (servers). Such databases may completely exclude information duplication, or completely duplicate it in each distributed copy (for example, as [Blockchain](https://en.wikipedia.org/wiki/Blockchain)).
    -   [NoSQL](https://en.wikipedia.org/wiki/NoSQL)
        > Stores and processes unstructured or weakly structured data. This type of database is subdivided into subtypes:
        >
        > -   [Key–value DB](https://en.wikipedia.org/wiki/Key%E2%80%93value_database) <br>
        > -   [Column family DB](https://en.wikipedia.org/wiki/Column_family) <br>
        > -   [Document-oriented DB](https://en.wikipedia.org/wiki/Document-oriented_database) (store data as a hierarchy of documents) <br>
        > -   [Graph DB](https://en.wikipedia.org/wiki/Graph_database) (are used for data with a large number of links)

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**Comparing database types: how database types evolved to meet different needs**](https://www.prisma.io/dataguide/intro/comparing-database-types)
2. 📄 [**SQL vs. NoSQL Database – A Complete Comparison**](https://backendless.com/sql-vs-nosql-database-a-complete-comparison/)
3. 📺 [**7 Database Paradigms** – YouTube](https://youtu.be/W2Z7fbCLSTw)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Relational database

    The most popular relational databases: [MySQL](https://en.wikipedia.org/wiki/MySQL), [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL), [MariaDB](https://en.wikipedia.org/wiki/MariaDB), [Oracle](https://en.wikipedia.org/wiki/Oracle_Database). A special language [SQL (Structured Query Language)](https://postgrespro.com/docs/postgresql/14/sql) is used to work with these databases. It is quite simple and intuitive.

    -   [SQL basics](https://github.com/cheatsnake/sql-by-example/blob/master/README.md)
        > Learn the basic cycle of creating/receiving/updating/deleting data. Everything else as needed.
    -   Merging tables
        -   Querying data from multiple tables
            > Operator `JOIN`; Combinations with other operators; `JOIN` types.
        -   Relationships between tables
            > References from one table to another; foreign keys.
    -   [Subquery Expressions](https://postgrespro.com/docs/postgresql/14/functions-subquery)
        > Query inside another SQL query.
    -   [Indexes](https://postgrespro.com/docs/postgresql/14/indexes-intro)
        > Data structure that allows you to quickly determine the position of the data of interest in the database.
    -   [Transactions](https://postgrespro.com/docs/postgresql/14/tutorial-transactions)
        > Sequences of commands that must be executed completely, or not executed at all.
        -   Command `START TRANSACTION`
        -   Commands `COMMIT` and `ROLLBACK`
    -   Working with a programming language
        > To do this, you need to install a database driver (adapter) for your language. (For example [psycopg2](https://github.com/psycopg/psycopg2) for Python, [node-postgres](https://github.com/brianc/node-postgres) for Node.js, [pgx](https://github.com/jackc/pgx) for Go)
    -   [ORM (Object-Relational Mapping)](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping) libraries
        > Writing SQL queries in code is difficult. It's easy to make mistakes and typos in them, because they are just strings that are not validated in any way. To solve this problem, there are so-called ORM libraries, which allow you to execute SQL queries as if you were simply calling methods on an object. Unfortunately, even with them all is not so smooth, because "under the hood" queries that are generated by these libraries are not the most optimal in terms of performance (so be prepared to work with ORM, as well as with pure SQL). <br> Popular ORMs: [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) for Python, [Prisma](https://github.com/prisma/prisma) for Node.js, [GORM](https://github.com/go-gorm/gorm) for Go.
    -   [Optimization and performance](https://postgrespro.ru/docs/postgresql/14/performance-tips)

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**SQL Crash Course - Beginner to Intermediate** – YouTube](https://youtu.be/nWeW3sCmD2k)
2. 📺 [**SQL Tutorial for Beginners (and Technical Interview Questions Solved)** – YouTube](https://youtu.be/-fW2X7fh7Yg)
3. 📺 [**SQL Tutorial - Full Database Course for Beginners** – YouTube](https://youtu.be/HXV3zeQKqGY)
4. 📺 [**MySQL - The Basics. Learn SQL in 23 Easy Steps** – YouTube](https://youtu.be/Cz3WcZLRaWc)
5. 📄 [**MySQL command-line client commands**](https://www.mysqltutorial.org/mysql-cheat-sheet.aspx)
6. 📺 [**Learn PostgreSQL Tutorial - Full Course for Beginners** – YouTube](https://youtu.be/qw--VYLpxG4)
7. 📄 [**Postgres Cheat Sheet**](https://postgrescheatsheet.com)
8. 📺 [**Database Indexing Explained (with PostgreSQL)** – YouTube](https://youtu.be/-qNSXK7s7_w)
9. 📄 [**SQL Indexing and Tuning e-Book**](https://use-the-index-luke.com/)
10. 📺 [**What is a Database transaction?** – YouTube](https://youtu.be/P80Js_qClUE)
11. 📺 [**SQL Server Performance Essentials – Full Course** – YouTube](https://youtu.be/HvxmF0FUwrM)
12. 📺 [**ORM: The Good, the Great, and the Ugly** – YouTube](https://youtu.be/3EvhK7-DlZA)
13. 📺 [**I Would Never Use an ORM, by Matteo Collina** – YouTube](https://youtu.be/qfRQ5zhYuJE)
14. 📄 [**Awesome SQL** – GitHub](https://github.com/danhuss/awesome-sql)
</details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### MongoDB

    [MongoDB](https://en.wikipedia.org/wiki/MongoDB) is a popular [NoSQL](https://en.wikipedia.org/wiki/NoSQL) database that stores data in flexible, JSON-like documents, allowing for dynamic and scalable data structures. It offers high performance, horizontal scalability, and a powerful query language, making it a preferred choice for modern web applications.

    -   [Basic commands](https://www.mongodb.com/developer/products/mongodb/cheat-sheet/)
        > Learn the basic cycle of creating/reading/updating/deleting data. Everything else as needed.
    -   [Aggregations](https://www.mongodb.com/docs/manual/aggregation)
        > MongoDB provides a powerful aggregation framework for performing complex queries and calculations. Learn how to use aggregation pipelines.
    -   Working with [Indexes](https://www.mongodb.com/docs/manual/indexes)
        > Indexing is an important concept in MongoDB for improving performance.
    -   Working with a programming language
        > For this you need to install [MongoDB driver](https://www.mongodb.com/docs/drivers) for your language.
    -   [Best practices](https://www.mongodb.com/developer/products/mongodb/mongodb-schema-design-best-practices/)
        > Learn best practices for schema design, indexing, and query optimization. Read up on these to ensure your applications are performant and scalable.
    -   [Scaling](https://www.mongodb.com/basics/scaling)
        > Learn about scaling to handle large datasets and high traffic. MongoDB provides sharding and replica sets for scaling horizontally and vertically.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**MongoDB in 100 Seconds** – YouTube](https://youtu.be/-bt_y4Loofg)
2. 📺 [**MongoDB Crash Course 2022** – YouTube](https://youtu.be/2QQGWYe7IDU)
3. 📄 [**MongoDB — Complete Guide**](https://faun.pub/mongodb-com-50d2f3016c2b)
4. 📄 [**MongoDB Cheat Sheet**](https://www.mongodb.com/developer/products/mongodb/cheat-sheet/)
5. 📺 [**MongoDB Tutorial For Beginners (playlist)** – YouTube](https://youtube.com/playlist?list=PLp50dWW_m40UWFSV6PTgYzciZJIxgHy7Q)
6. 📄 [**Awesome MongoDB** – GitHub](https://github.com/ramnes/awesome-mongodb)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Redis

    [Redis](https://redis.io/) is a fast data storage working with _key-value_ structures. It can be used as a database, cache, message broker or queue.

    -   Data types
        > String / Bitmap / Bitfield / List / Set / Hash / Sorted sets / Geospatial / Hyperlog / Stream
    -   Basic operations
        ```bash
        SET key "value" # setting the key with the value "value"
        GET key # retrieve a value from the specified key
        SETNX key "data" # setting the value / creation of a key
        MSET key1 "1" key2 "2" key3 "3" # setting multiple keys
        MGET key1 key2 key3 # getting values for several keys at once
        DEL key # remove the key-value pair
        INCR someNumber # increase the numeric value by 1
        DECR someNumber # decrease the numeric value by 1
        EXPIRE key 1000 # set a key life timer of 1000 seconds
        TTL key # get information about the lifetime of the key-value pair
            # -1 the key exists, but has no expiration date
            # -2 the key does not exist
            # <another number> key lifetime in seconds
        SETEX key 1000 "value" # consolidation of commands SET and EXPIRE
        ```
    -   Transactions
        > `MULTI` — start recording commands for the transaction. <br> `EXEC` — execute the recorded commands. <br> `DISCARD` — delete all recorded commands. <br> `WATCH` — command that provides execution only if other clients have not changed the value of the variable. Otherwise, EXEC will not execute the written commands.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**Redis in 100 Seconds** – YouTube](https://youtu.be/G1rOthIU-uo)
2. 📺 [**Redis In-Memory Database Crash Course** – YouTube](https://youtu.be/V7FPk4J10KI)
3. 📺 [**Redis Course - In-Memory Database Tutorial** – YouTube](https://youtu.be/XCsS_NVAa1g)
4. 📺 [**Redis Crash Course - Transactions** – YouTube](https://youtu.be/5seIrOGYHPo)
5. 📺 [**Python and Redis Tutorial - Caching API Responses** – YouTube](https://youtu.be/_8lJ5lp8P0U)
6. 📺 [**Top 5 Redis Use Cases** – YouTube](https://youtu.be/a4yX7RUgTxI)
7. 📄 [**How To Run Transactions in Redis** – Digital Ocean](https://www.digitalocean.com/community/cheatsheets/how-to-run-transactions-in-redis)
8. 📄 [**Redis cheatsheet** – QuickRef](https://quickref.me/redis)
9. 📄 [**Awesome Redis** – GitHub](https://github.com/JamzyWang/awesome-redis)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### ACID Requirements

    [ACID](https://en.wikipedia.org/wiki/ACID) is an acronym consisting of the names of the four main properties that guarantee the reliability of transactions in the database.

    -   [Atomicity](<https://en.wikipedia.org/wiki/Atomicity_(database_systems)>)
        > Guarantees that the transaction will be executed completely or not executed at all.
    -   [Consistency](<https://en.wikipedia.org/wiki/Consistency_(database_systems)>)
        > Ensures that each successful transaction captures only valid results (any inconsistencies are excluded).
    -   [Isolation](<https://en.wikipedia.org/wiki/Isolation_(database_systems)>)
        > Guarantees that one transaction cannot affect the other in any way.
    -   [Durability](<https://en.wikipedia.org/wiki/Durability_(database_systems)>)
        > Guarantees that the changes made by the transaction are saved.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**ACID Transactions (Explained by Example)** – YouTube](https://youtu.be/pomxJOFVcQs)
2. 📺 [**Relational Database Atomicity Explained By Example** – YouTube](https://youtu.be/6vqzOjfZDco)
3. 📺 [**ACID Properties in DBMS With Examples | In-depth Explanation** – YouTube](https://youtu.be/clPPKgYJC10)
4. 📄 [**How SQLite Helps You Do ACID**](https://fly.io/blog/sqlite-internals-rollback-journal/)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Designing databases

    [Database design](https://en.wikipedia.org/wiki/Database_design) is a very important topic that is often overlooked. A well-designed database will ensure long-term scalability and ease of data maintenance. There are several basic steps in database design:

    - Definition of entities
        > An entity is an object, concept, or event that has its own set of attributes. For example, if you're designing a database for a library, entities might include books, authors, publishers, and borrowers.
    - Define the attributes to each entity
        > Each entity has a set of specific attributes. For example, attributes of a book might include its title, author, ISBN, and publication date. Each attribute has a specific data type, be it a string, an integer, a boolaen, and so on.
    - Add constraints
        > Attribute values may have certain limitations. For example, strings can only be unique or have a limit on the maximum number of characters.
    - Define relationships
        > Entities can be linked to one another by one type of relationship: [one to one](https://vertabelo.com/blog/one-to-one-relationship-in-database/), [one to many](https://vertabelo.com/blog/one-to-many-relationship/) or [many to many](https://vertabelo.com/blog/many-to-many-relationship/). For example, a book might have one or more authors, and an author might write one or more books. You can represent these relationships by creating a foreign key in one table that references the primary key in another table.
    - [Normalization](https://en.wikipedia.org/wiki/Database_normalization)
        > It is the process of separating data into separate related tables. Normalization eliminates [data redundancy](https://en.wikipedia.org/wiki/Data_redundancy) and thus avoids data integrity violations when data changes.
    - Optimize for performance
        > Create indexes on frequently queried columns, tune the database configuration, and optimize the queries that you use to access the data.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**How to Create a Database Design From an Idea** – YouTube](https://youtu.be/5RpUmDEsn1k)
2. 📺 [**Database Design Course - Learn how to design and plan a database for beginners** – YouTube](https://youtu.be/ztHopE5Wnpc)
3. 📺 [**7 Database Design Mistakes to Avoid (With Solutions)** – YouTube](https://youtu.be/s6m8Aby2at8)
4. 📄 [**Dbdiagram – simple tool to draw ER diagrams**](https://dbdiagram.io/home)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

