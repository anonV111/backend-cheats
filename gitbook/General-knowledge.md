## General knowledge

-   ### Numeral systems

    [Numeral system](https://en.wikipedia.org/wiki/Numeral_system) is a set of symbols and rules for denoting numbers. In computer science, it is customary to distinguish four main number systems: binary, octal, decimal, and hexadecimal. It is connected, first of all, with their use in various branches of programming.

    -   [Binary number](https://en.wikipedia.org/wiki/Binary_number)
        > The most important system for computing technology. Its use is justified by the fact that the logic of the processor is based on only two states (on/off, open/closed, high/low, true/false, yes/no, high/low).

    <p align="center"><img src="./files/common/binary.png" alt="Binary"/></p>

    -   [Octal](https://en.wikipedia.org/wiki/Octal)
        > It is used e.g., on Linux systems to grant access rights.

    <p align="center"><img src="./files/common/octal.png" alt="Octal"/></p>

    -   [Decimal](https://en.wikipedia.org/wiki/Decimal)
        > A system that is easy to understand for most people.
    -   [Hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal)
        > The letters A, B, C, D, E, F are additionally used for recording. It is widely used in low-level programming and computer documentation because the minimum addressable memory unit is an 8-bit byte, the values of which are conveniently written in two hexadecimal digits.

    <p align="center"><img src="./files/common/hex.png" alt="Hex"/></p>

    -   Translation between different number systems
        > You can try [online converter](https://cheatsnake.github.io/NSConverter/) for a better understanding.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**Number Systems Introduction - Decimal, Binary, Octal & Hexadecimal** – YouTube](https://youtu.be/FFDMzbrEXaE)
1. 📄 [**Number System in Maths** – GeeksGorGeeks](https://www.geeksforgeeks.org/number-system-in-maths/)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Logical connective

    [Logical connective](https://en.wikipedia.org/wiki/Logical_connective) are widely used in programming to handle boolean types (true/false or 1/0). The result of a boolean expression is also a value of a boolean type.

    <table>
    <tr><td width=33% valign=top>

    AND
    | a | b | a AND b |
    |---|---|:-------:|
    | 0 | 0 | 0       |
    | 0 | 1 | 0       |
    | 1 | 0 | 0       |
    | 1 | 1 | 1       |

    </td><td width=33% valign=top>

    OR
    | a | b | a OR b |
    |---|---|:-------:|
    | 0 | 0 | 0       |
    | 0 | 1 | 1       |
    | 1 | 0 | 1       |
    | 1 | 1 | 1       |
    </td><td valign=top>

    XOR
    | a | b | a XOR b |
    |---|---|:-------:|
    | 0 | 0 | 0       |
    | 0 | 1 | 1       |
    | 1 | 0 | 1       |
    | 1 | 1 | 0       |
    </td></tr>
    </table>

    -   Basic logical operations
        > They are the basis of other all kinds of operations. <br>
        > There are three in total: [Operation AND (&&, Conjunction)](https://en.wikipedia.org/wiki/Logical_conjunction), [operation OR (||, Disjunction)](https://en.wikipedia.org/wiki/Logical_disjunction), [operation NOT (!, Negation)](https://en.wikipedia.org/wiki/Negation).
    -   Operation [Exclusive OR (XOR, Modulo 2 Addition)](https://en.wikipedia.org/wiki/Exclusive_or)
        > An important operation that is fundamental to coding theory and computer networks.
    -   [Truth Tables](https://en.wikipedia.org/wiki/Truth_table)
        > For logical operations, there are special tables that describe the input data and the return result.
    -   Priority of operations
        > The `NOT` operator has the highest priority, followed by the `AND` operator, and then the `OR` operator. You can change this behavior using round brackets.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**Logical Operators − Negation, Conjunction & Disjunction** – YouTube](https://youtu.be/6kYngPvoGxU)
2. 📺 [**Logical Operators − Exclusive OR** – YouTube](https://youtu.be/m2mf6I3g2-c)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Data structures

    [Data structures](https://en.wikipedia.org/wiki/Data_structure) are containers in which data is stored according to certain rules. Depending on these rules, the data structure will be effective in some tasks and ineffective in others. Therefore, it is necessary to understand when and where to use this or that structure.

    -   [Array](<https://en.wikipedia.org/wiki/Array_(data_structure)>)
        > A data structure that allows you to store data of the same type, where each element is assigned a different sequence number.

    <p align="center"><img src="./files/common/array_eng.png" alt="Array"/></p>

    -   [Linked list](https://en.wikipedia.org/wiki/Linked_list)
        > A data structure where all elements, in addition to the data, contain references to the next and/or previous element. There are 3 varieties:
        >
        > -   A [singly linked list](https://en.wikipedia.org/wiki/Linked_list#Singly_linked_list) is a list where each element stores a link to the next element only (one direction).
        > -   A [doubly linked list](https://en.wikipedia.org/wiki/Doubly_linked_list) is a list where the items contain links to both the next item and the previous one (two directions).
        > -   A [circular linked list](https://en.wikipedia.org/wiki/Linked_list#Circular_linked_list) is a kind of bilaterally linked list, where the last element of the ring list contains a pointer to the first and the first to the last.

    <p align="center"><img src="./files/common/linked-list.png" alt="Linked list"/></p>

    -   [Stack](<https://en.wikipedia.org/wiki/Stack_(abstract_data_type)>)
        > Structure where data storage works on the principle of _last in - first out_ (LIFO).

    <p align="center"><img src="./files/common/stack_eng.png" alt="Stack"/></p>

    -   [Queue](<https://en.wikipedia.org/wiki/Queue_(abstract_data_type)>)
        > Structure where data storage is based on the principle of _first in - first out_ (FIFO).

    <p align="center"><img src="./files/common/queue.gif" alt="Queue"/></p>

    -   [Hash table](https://en.wikipedia.org/wiki/Hash_table)
        > In other words, it is an associative array. Here, each of the elements is accessed with a corresponding key value, which is calculated using [hash function](https://en.wikipedia.org/wiki/Hash_function) according to a certain algorithm.

    <p align="center"><img src="./files/common/hash-table_eng.png" alt="Hash Table"/></p>

    -   [Tree](<https://en.wikipedia.org/wiki/Tree_(data_structure)>)
        > Structure with a hierarchical model, as a set of related elements, usually not ordered in any way.

    <p align="center"><img src="./files/common/tree.png" alt="Tree"/></p>

    -   [Heap](<https://en.wikipedia.org/wiki/Heap_(data_structure)>)
        > Similar to the tree, but in the heap, the items with the largest key is the root node (max-heap). But it may be the other way around, then it is a min heap.

    <p align="center"><img src="./files/common/heap_eng.png" alt="Heap"/></p>

    -   [Graph](<https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)>)
        > A structure that is designed to work with a large number of links.

    <p align="center"><img src="./files/common/graph_eng.png" alt="Graph"/></p>

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**10 Key Data Structures We Use Every Day** – YouTube](https://youtu.be/ouipSd_5ivQ)
2. 📺 [**CS50 2022 - Lecture about Data Structures** – YouTube](https://youtu.be/X8h4dq9Hzq8)
3. 📺 [**Data Structures Easy to Advanced Course** – YouTube](https://youtu.be/RBSGKlAvoiM)
4. 📄 [**Free courses to learn data structures and algorithms in depth** – freeCodeCamp](https://www.freecodecamp.org/news/these-are-the-best-free-courses-to-learn-data-structures-and-algorithms-in-depth-4d52f0d6b35a/)
5. 📄 [**Data Structures: collection of topics** – GeeksForGeeks](https://www.geeksforgeeks.org/data-structures/)
6. 📄 [**JavaScript Data Structures and Algorithms** – GitHub](https://github.com/trekhleb/javascript-algorithms)
7. 📄 [**Go Data Structures** – GitHub](https://github.com/emirpasic/gods)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Basic algorithms

    [Algorithms](https://de.wikipedia.org/wiki/Algorithmus) refer to sets of sequential instructions (steps) that lead to the solution of a given problem. Throughout human history, a huge number of algorithms have been invented to solve certain problems in the most efficient way. Accordingly, the correct choice of algorithms in programming will allow you to create the fastest and most resource-intensive solutions.

    > There is a very good book about algorithms for beginners – [Grokking algorithms](https://edu.anarcho-copy.org/Algorithm/grokking-algorithms-illustrated-programmers-curious.pdf). You can start [learning a programming language](#programming-language) in parallel with reading it.

    -   [Binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm)
        > Maximum efficient search algorithm for sorted lists.
    -   [Selection sort](https://en.wikipedia.org/wiki/Selection_sort)
        > At each step of the algorithm, the minimum element is searched for and then swapped with the current iteration element.
    -   [Recursion](https://en.wikipedia.org/wiki/Recursion)
        > When a function can call itself and so on to infinity. On the one hand, recursion-based solutions look very elegant, but on the other hand, this approach quickly leads to Stack Overflow and is recommended to be avoided.
    -   [Bubble sort](https://en.wikipedia.org/wiki/Bubble_sort)
        > At each iteration neighboring elements are sequentially compared, and if the order of the pair is wrong, the elements are swapped.
    -   [Quicksort](https://en.wikipedia.org/wiki/Quicksort)
        > Improved bubble sorting method.
    -   [Breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search)
        > Allows finding all shortest paths from a given vertex of the graph.
    -   [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
        > Finds the shortest paths between all vertices of a graph and their length.
    -   [Greedy algorithm](https://en.wikipedia.org/wiki/Greedy_algorithm)
        > An algorithm that at each step makes locally the best choice in the hope that the final solution will be optimal.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**Code for the book Grokking Algorithms** – GitHub](https://github.com/egonSchiele/grokking_algorithms)
2. 📺 [**Algorithms and Data Structures Tutorial** – YouTube](https://youtu.be/8hly31xKli0)
3. 📄 [**Largest open-source algorithm library**](https://the-algorithms.com/)
4. 📺 [**Sorting Algorithms Explained Visually** – YouTube](https://youtu.be/RfXt_qHDEPw)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Algorithm complexity

    <p align="center"><img src="./files/common/BigO_eng.png" alt="BigO"/></p>

    In the world of programming there is a special unit of measure [Big O notation](https://en.m.wikipedia.org/wiki/Big_O_notation). It describes how the complexity of an algorithm increases with the amount of input data. Big O estimates how many actions (steps/iterations) it takes to execute the algorithm, while always showing the worst case scenario.

    -   Main types of complexity
        > -   Constant O(1) – the fastest. <br>
        > -   Linear O(n) <br>
        > -   Logarithmic O(log n) <br>
        > -   Linearimetric O(n \* log n) <br>
        > -   Quadratic O(n^2) <br>
        > -   Stepwise O(2^n) <br>
        > -   Factorial O(n!) – the slowest. <br>
    -   [Time complexity](https://en.wikipedia.org/wiki/Time_complexity)
        > When you know in advance on which machine the algorithm will be executed, you can measure the execution time of the algorithm. Again, on very good hardware the execution time of the algorithm can be quite acceptable, but the same algorithm on a weaker hardware can run for hundreds of milliseconds or even a few seconds. Such delays will be very sensitive if your application handles user requests over the network.
    -   [Space complexity](https://en.wikipedia.org/wiki/Space_complexity)
        > In addition to time, you need to consider how much memory is spent on the work of an algorithm. It is important when you're working with limited memory resources.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📄 [**Big O Algorithm Complexity cheatsheet**](https://www.bigocheatsheet.com/)
2. 📺 [**Big O Notation - Full Course** – YouTube](https://youtu.be/Mo4vesaut8g)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Data storage formats

    Different file formats can be used to store and transfer data over the network. Text files are human-readable, so they are used for configuration files, for example. But transferring data in text formats over the network is not always rational, because they weigh more than their corresponding binary files.

    -   Text formats

        -   [JSON (JavaScript Object Notation)](https://en.wikipedia.org/wiki/JSON)
            > Represents an object in which data is stored as key-value pairs.
        -   [XML (eXtensible Markup Language)](https://en.wikipedia.org/wiki/XML)
            > The format is closer to HTML. Here the data is wrapped in opening and closing tags.
        -   [YAML (Yet Another Markup Language)](https://en.wikipedia.org/wiki/YAML)
            > The format is close to markup languages like HTML. Minimalist, because it has no opening or closing tags. Easy to edit.
        -   [TOML (Tom's Obvious Minimal Language)](https://en.wikipedia.org/wiki/TOML)
            > A minimal configuration file format that's easy to read due to obvious semantics. TOML is designed to map unambiguously to a hash table. TOML should be easy to parse into data structures in a wide variety of languages.

    -   Binary formats
        -   [Message Pack](https://msgpack.org/)
            > Binary analog of JSON. Allows you to pack data 15-20% more efficiently.
        -   [BSON (Binary JavaScript Object Notation)](https://en.wikipedia.org/wiki/BSON)
            > It is a superset of JSON, including additionally regular expressions, binary data and dates.
        -   [ProtoBuf (Protocol Buffers)](https://en.wikipedia.org/wiki/Protocol_Buffers)
            > Binary alternative to XML text format. Simpler, more compact and faster.

    -   Image formats
        -   [JPEG (Joint Photographic Experts Group)](https://en.wikipedia.org/wiki/JPEG)
            > It is best suited for photographs and complex images with a wide range of colors. JPEG images can achieve high compression ratios while maintaining good image quality, but repeated editing and saving can result in loss of image fidelity.
        -   [PNG (Portable Network Graphics)](https://en.wikipedia.org/wiki/PNG)
            > It is a lossless compression format that supports transparency. It is commonly used for images with sharp edges, logos, icons, and images that require transparency. PNG images can have a higher file size compared to JPEG, but they retain excellent quality without degradation during repeated saves.
        -   [GIF (Graphics Interchange Format)](https://en.wikipedia.org/wiki/GIF)
            > Used for simple animations and low-resolution images with limited colors. It supports transparency and can be animated by displaying a sequence of frames.
        -   [SVG (Scalable Vector Graphics)](https://en.wikipedia.org/wiki/SVG)
            > XML-based vector image format defined by mathematical equations rather than pixels. SVG images can be scaled to any size without losing quality and are well-suited for logos, icons, and graphical elements.
        -   [WebP](https://en.wikipedia.org/wiki/WebP)
            > Modern image format developed by Google. It supports both lossy and lossless compression, providing good image quality with smaller file sizes compared to JPEG and PNG. WebP images are optimized for web use and can include transparency and animation.

    -   Video formats
        -   [MP4 (MPEG-4 Part 14)](https://en.wikipedia.org/wiki/MP4_file_format)
            > Widely used video format that supports high-quality video compression, making it suitable for streaming and storing videos. MP4 files can contain both video and audio.
        -   [AVI (Audio Video Interleave)](https://en.wikipedia.org/wiki/Audio_Video_Interleave)
            > Is a multimedia container format developed by Microsoft. It can store audio and video data in a single file, allowing for synchronized playback. However, they tend to have larger file sizes compared to more modern formats.
        -   [MOV (QuickTime Movie)](https://www.adobe.com/creativecloud/video/hub/guides/what-is-an-mov-video.html)
            > Is a video format developed by Apple for use with their QuickTime media player. It is widely used with Mac and iOS devices. MOV files can contain both video and audio, and they offer good compression and quality, making them suitable for editing and professional use.
        -   [WEBM](https://en.wikipedia.org/wiki/WebM)
            > Best for videos embedded on your personal or business website. It is lightweight, load quickly and stream easily.

    -   Audio formats
        -   [MP3 (MPEG-1 Audio Layer 3)](https://en.wikipedia.org/wiki/MP3)
            > The most popular audio format known for its high compression and small file sizes. It achieves this by removing some of the audio data that may be less perceptible to the human ear. Suitable for music storage, streaming, and sharing.
        -   [WAV (Waveform Audio File Format)](https://en.wikipedia.org/wiki/WAV)
            > Is an uncompressed audio format that stores audio data in a lossless manner, resulting in high-quality sound reproduction. WAV files are commonly used in professional audio production and editing due to their accuracy and fidelity. However, they tend to have larger file sizes compared to compressed formats.
        -   [AAC (Advanced Audio Coding)](https://en.wikipedia.org/wiki/Advanced_Audio_Coding)
            > Is a widely used audio format known for its efficient compression and good sound quality. It offers better sound reproduction at lower bit rates compared to MP3. AAC files are commonly used for streaming music, online radio, and mobile devices, as they deliver good audio quality while conserving bandwidth and storage.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**Data Formats: XML, JSON, and YAML** – YouTube](https://youtu.be/JQO-x8rzNVI)
2. 📺 [**Serialization formats: JSON and Protobuf** – YouTube](https://youtu.be/uGYZn6xk-hA)
3. 📺 [**Protocol Buffers Crash Course** – YouTube](https://youtu.be/46O73On0gyI)
4. 📺 [**Explaining Image File Formats** – YouTube](https://youtu.be/WblPwVq9KnU)
5. 📺 [**What's the difference between a JPEG, PNG, GIF, etc…?** – YouTube](https://youtu.be/ww12lImOJ38)
 </details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

-   ### Text encodings

    Computers work only with numbers, or more precisely, only with 0 and 1. It is already clear how to convert numbers from different number systems to binary. But you can't do that with text. That's why special tables called [encodings](https://en.wikipedia.org/wiki/Character_encoding) were invented, in which text characters are assigned numeric equivalents.

    -   [ASCII (American standard code for information interchange)](https://en.wikipedia.org/wiki/ASCII)
        > The simplest encoding created specifically for the American alphabet. Consists of 128 characters.
    -   [Unicode](https://en.wikipedia.org/wiki/Unicode)
        > This is an international character table that, in addition to the English alphabet, contains the alphabets of almost all countries. It can hold more than a million different characters (the table is currently incomplete).
    -   [UTF-8 (Unicode Transformation Format)](https://en.wikipedia.org/wiki/UTF-8)
        > UTF-8 is a variable-length encoding that can be used to represent any Unicode character.
    -   [UTF-16](https://en.wikipedia.org/wiki/UTF-16)
        > Its main difference from UTF-8 is that its structural unit is not one but two bytes. That is, in UTF-16 any Unicode character can be encoded by either two or four bytes.

<details>
    <summary>🔗 <b>References</b></summary>

1. 📺 [**Unicode, in friendly terms: ASCII, UTF-8 and more** – YouTube](https://youtu.be/ut74oHojxqo)
2. 📄 [**Understanding the ASCII Table**](https://linuxhandbook.com/ascii-table/)
3. 📺 [**Unicode Encoding! UTF-32, UCS-2, UTF-16, & UTF-8!** – YouTube](https://youtu.be/uTJoJtNYcaQ)
</details>

<div align="right"><a href="#top">Contents ⬆️</a></div>

