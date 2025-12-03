### Unit Tests

The simplest kind of tests. As a rule, about 70-80% of all tests are exactly [unit-tests](https://en.wikipedia.org/wiki/Unit_testing). "Unit" means that not the whole system is tested, but small and separate parts of it (functions, methods, components, etc.) in isolation from others. All dependent external environment is usually covered by [mocks](https://en.wikipedia.org/wiki/Mock_object).

-   What are the benefits of unit tests?
    > To give you an example, let's imagine a car. Its "units" are the engine, brakes, dashboard, etc. You can check them individually before assembly and, if necessary, replace or repair them. But you can assemble the car without having tested the units, and it will not go. You will have to disassemble everything and check every detail.
-   What do I need to start writing unit tests?
    > As a rule, the means of the standard language library are enough to write quality tests. But for more convenient and faster writing of tests, it is better to use third-party tools. For example:
    >
    > -   For , it uses [pytest](https://docs.pytest.org), although the standard [unittest](https://docs.python.org/3/library/unittest.html) is enough to start with.
    > -   For JavaScript/TypeScript, the best choices are [Jest](https://jestjs.io/).
    > -   For Go – [testify](https://github.com/stretchr/testify).
    > -   [And so on...](https://github.com/atinfo/awesome-test-automation#awesome-test-automation)

<details>
<summary>🔗 <b>References</b></summary>

1. 📺 [**Software Testing Explained in 100 Seconds** – YouTube](https://youtu.be/u6QfIXgjwGQ)
2. 📄 [**How to write your first Unit Test** – medium](https://medium.com/geekculture/how-to-write-your-first-unit-test-in-multiple-programming-languages-6d158d362b3d)
3. 📺 [**Testing JavaScript with Cypress – Full Course** – YouTube](https://youtu.be/u8vMu7viCm8?si=wYAoeR87-dPOIRA4)
4. 📺 [**How To Write Unit Tests For Existing Python Code** – YouTube](https://youtu.be/ULxMQ57engo)
5. 📺 [**Learn How to Test your JavaScript Application** – YouTube](https://youtu.be/ajiAl5UNzBU)
6. 📺 [**Golang Unit Testing and Mock Testing Tutorial** – YouTube](https://youtu.be/XQzTUa9LPU8)

 </details>


