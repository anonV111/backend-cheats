### Redis

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


