### Designing databases

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



