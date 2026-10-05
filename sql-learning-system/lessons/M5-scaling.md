# M5 · Scaling
*Source: lecture6 (Week 6 · Scaling). MySQL scripts: `database/scaling/mysql/`, PostgreSQL: `database/scaling/postgres/`. All executed on MariaDB 10.11 / PostgreSQL 16 by `tests/test_servers.py`.*

Story: SQLite is an *embedded* database (a file). MySQL and PostgreSQL are *servers* with users, stricter types, procedures, replication and access control. The lecture re-implements MBTA (types), MFA (procedures), rideshare (permissions) and bank (injection) on them.

---

## C5.1 Database servers and their command-line clients
*Source: lecture6 L40-156, L159-352, L1329-1490*

**Level 1.** A server runs on its own machine. You connect over the network as a **user**, and one server holds many databases.

**Level 2.**

| Task | SQLite | MySQL | PostgreSQL |
|---|---|---|---|
| connect | `sqlite3 mbta.db` | `mysql -u root -h 127.0.0.1 -P 3306 -p` | `psql -U postgres` |
| list databases | n/a | `SHOW DATABASES;` | `\l` |
| create / use db | n/a | `CREATE DATABASE \`mbta\`; USE \`mbta\`;` | `CREATE DATABASE "mbta";` `\c mbta` |
| list tables | `.tables` | `SHOW TABLES;` | `\dt` |
| describe table | `.schema t` | `DESCRIBE t;` | `\d t` |
| quit | `.quit` | `quit` | `\q` |
| identifier quotes | `"x"` | `` `x` `` | `"x"` |

**Level 3.** Servers can keep data in RAM and offer replication and sharding (L48-53). The price is operating a server, with users, passwords and network access.

---

## C5.2 MySQL types
*Source: lecture6 L183-852*

**Integers** (signed range; `UNSIGNED` shifts the range to 0…):

| Type | Bytes | Max (signed) |
|---|---|---|
| TINYINT | 1 | 127 |
| SMALLINT | 2 | 32,767 |
| MEDIUMINT | 3 | 8,388,607 |
| INT | 4 | 2,147,483,647 (unsigned about 4.29 billion) |
| BIGINT | 8 | 2⁶³−1 |

**Text.** `CHAR(M)` has a fixed width (e.g. state codes 'MA'). `VARCHAR(M)` is variable, up to M characters. `TEXT` (TINY/MEDIUM/LONG) is for long passages. `BLOB` is binary.
**Choices.** `ENUM('a','b')` allows exactly one of the listed values, and `SET(...)` allows several (movie genres).
**Time.** `DATE`, `TIME`, `DATETIME`, `TIMESTAMP`, `YEAR`. TIME, DATETIME and TIMESTAMP accept `(fsp)` fractional-second digits up to 6.
**Real numbers.** `FLOAT` (4 bytes) and `DOUBLE PRECISION` (8 bytes) are approximate. **`DECIMAL(M,D)`** is exact, with M total digits and D after the point: `DECIMAL(5,2)` holds −999.99…999.99 (the lecture's "5 comma 1" is a slip, errata #7).

```sql
CREATE TABLE `swipes` (
    `id` INT AUTO_INCREMENT,
    `card_id` INT, `station_id` INT,
    `type` ENUM('enter', 'exit', 'deposit') NOT NULL,
    `datetime` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `amount` DECIMAL(5,2) NOT NULL CHECK(`amount` != 0),
    PRIMARY KEY(`id`),
    FOREIGN KEY(`card_id`) REFERENCES `cards`(`id`),
    FOREIGN KEY(`station_id`) REFERENCES `stations`(`id`)
);
```

**Level 3**
* Choose the smallest type that will *safely* fit. INT for card ids, because fewer than 4 billion people exist (L264-273).
* MySQL is **strict** (it rejects mismatched values by default), unlike SQLite's affinities (L839-852).
* `DESCRIBE` shows Key = `PRI` (primary), `UNI` (unique) and `MUL` (non-unique index, which foreign keys get, errata #10).
* VARCHAR stores the actual length, so over-sizing doesn't waste disk per row as the lecture suggests (errata #9). Still size thoughtfully. You can widen later with MODIFY.

---

## C5.3 ALTER TABLE … MODIFY (MySQL)
*Source: lecture6 L853-923*

```sql
ALTER TABLE `stations` MODIFY `line` ENUM('blue', 'green', 'orange', 'red', 'silver') NOT NULL;
ALTER TABLE `collections` ADD COLUMN `deleted` TINYINT DEFAULT 0;
```
MODIFY replaces the whole column definition, so repeat every old ENUM value and constraint. SQLite has no equivalent.

---

## C5.4 Stored procedures (MySQL)
*Source: lecture6 L947-1278*

**Level 1.** A named, saved sequence of statements on the server that you can `CALL` again and again, optionally with inputs.

**Level 2.**
```sql
DELIMITER //
CREATE PROCEDURE `sell`(IN `sold_id` INT)
BEGIN
    UPDATE `collections` SET `deleted` = 1 WHERE `id` = `sold_id`;
    INSERT INTO `transactions` (`title`, `action`)
    VALUES ((SELECT `title` FROM `collections` WHERE `id` = `sold_id`), 'sold');
END//
DELIMITER ;
CALL `sell`(2);
```
* `DELIMITER //` lets the body contain `;` (D5-02).
* Several parameters are separated by commas, and procedures can call procedures (L1110-1118, L1250-1256).
* Control flow exists (IF / ELSEIF / ELSE, loops). The lecture leaves using it to you (M5-E06).

**Level 3.** Procedures vs triggers vs views: a view is a *read* abstraction, a trigger *reacts* automatically to writes, and a procedure is an *action* you invoke explicitly. Calling `sell(2)` twice logs two sales unless you guard against it.

---

## C5.5 PostgreSQL types
*Source: lecture6 L1293-1477*

* Integers: `SMALLINT`, `INT`, `BIGINT`. Auto-increment: **`SERIAL`** (SMALLSERIAL, BIGSERIAL).
* An enum is declared once as a type: `CREATE TYPE "swipe_type" AS ENUM('enter', 'exit', 'deposit');`, then used as `"type" "swipe_type" NOT NULL`.
* Time: `TIMESTAMP`, `DATE`, `TIME`, `INTERVAL` (a duration), with precision. The default "now" is `now()`.
* Exact numbers: `NUMERIC(precision, scale)`. Also `MONEY` (currency-formatted, locale-dependent).

---

## C5.6 Scaling strategies
*Source: lecture6 L1494-1785*

**Vertical scaling** means a more powerful single server. **Horizontal scaling** means more servers.

**Replication** keeps copies on several servers:
* *Single-leader*: all writes go to the leader, which forwards them to followers. Reads can go to any server, and a follower used only for reads is a **read replica**.
* *Multi-leader* and *leaderless* exist too, and are much more complex.
* **Synchronous**: the leader waits for the follower's OK before answering the client. This is safe but slower, which suits finance and healthcare.
* **Asynchronous**: the leader answers immediately. This is faster, but an acknowledged write can be lost if the follower fails, which is acceptable for social media.

**Sharding** splits one huge data set across servers (names A-I / J-R / S-Z, or id ranges). Watch out for **hotspots** (one shard gets most of the traffic) and the **single point of failure** (a shard without replicas goes down). Combine sharding with replication.

---

## C5.7 Access control
*Source: lecture6 L1786-1920*

```sql
CREATE USER 'carter' IDENTIFIED BY 'password';          -- demo password only!
GRANT SELECT ON `rideshare`.`analysis` TO 'carter';     -- read the view only
REVOKE SELECT ON `rideshare`.`analysis` FROM 'carter';
```
This finally makes the M3 "secure view" real: carter can read `analysis` but gets a permission error on `rides`. Grant several privileges with commas (`SELECT, INSERT`). Avoid `GRANT ALL ON *.*` outside a sandbox.

---

## C5.8 SQL injection and prepared statements
*Source: lecture6 L1921-2148*

**Level 1.** If an application pastes user input into SQL text, the user can write SQL.

**Level 2: Attacks from the lecture.**
```sql
-- password field:  ' OR 1=1           →  … AND "password" = '' OR 1=1 …
-- account id:      1 UNION SELECT * FROM accounts
SELECT * FROM accounts WHERE id = 1 UNION SELECT * FROM accounts;
```
**Defence: prepared statements (bound parameters).**
```sql
PREPARE `balance_check` FROM 'SELECT * FROM `accounts` WHERE `id` = ?';
SET @id = '1 UNION SELECT * FROM accounts';
EXECUTE `balance_check` USING @id;      -- returns only Alice
```

**Level 3.** The bound value is **never parsed as SQL**. The lecture calls this escaping, but it is really binding (errata #8). MySQL returned Alice because it converted `'1 UNION …'` to the number 1 when comparing it with the INT column. SQLite returns no row for the same input. In application code, never build SQL with f-strings or concatenation. Use the driver's placeholders (`?`, `%s`). `python3 tools/labs.py injection` shows both versions.

**Practice:** M5-E01 … M5-E10 · **Debug:** D5-01, D5-02 · **Review deck:** R5
