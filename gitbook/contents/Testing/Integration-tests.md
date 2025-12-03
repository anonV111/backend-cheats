### Integration tests

[Integration testing](https://en.wikipedia.org/wiki/Integration_testing) involves testing individual modules (components) in conjunction with others (that is, in integration). What was covered by a stub during Unit testing is now an actual component or an entire module.

-   Why it's needed?
    > Integration tests are the next step after units. Having tested each component individually, we cannot yet say that the basic functionality of the program works without errors. Potentially, there may still be many problems that will only surface after the different parts of the program interact with each other.
-   Strategies for writing integration tests
    > -   **Big Bang**: Most of the modules developed are connected together to form either the whole system or most of it. If everything works, you can save a lot of time this way.
    > -   **incremental approach**: By connecting two or more logically connected modules and then gradually adding more and more modules until the whole system is tested.
    > -   **Bottom-up approach**: each module at lower levels is tested with the modules of the next higher level until all modules have been tested.

<details>
<summary>🔗 <b>References</b></summary>

1. 📺 [**Unit testing vs. integration testing** – YouTube](https://youtu.be/pf6Zhm-PDfQ)
2. 📺 [**PyTest REST API Integration Testing with Python** – YouTube](https://youtu.be/7dgQRVqF1N0)
3. 📄 [**Integration Testing – Software testing fundamentals**](https://softwaretestingfundamentals.com/integration-testing/)
 </details>


