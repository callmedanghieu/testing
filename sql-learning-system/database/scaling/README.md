# Scaling scripts (Lecture 6)

Complete, runnable versions of what Lecture 6 builds on database servers. `tests/test_servers.py` executes all of them on MariaDB 10.11 (MySQL-compatible) and PostgreSQL 16.

| File | Lecture lines | What it shows |
|---|---|---|
| `mysql/mbta.sql` | lecture6 L159-923 | INT / AUTO_INCREMENT, VARCHAR, ENUM, DATETIME, DECIMAL(5,2), ALTER TABLE … MODIFY |
| `mysql/mfa_procedures.sql` | lecture6 L947-1278 | DELIMITER, CREATE PROCEDURE, IN parameters, CALL |
| `mysql/rideshare_access.sql` | lecture6 L1786-1920 | CREATE USER, GRANT, REVOKE |
| `mysql/bank_injection.sql` | lecture6 L1921-2148 | UNION injection vs PREPARE / EXECUTE … USING |
| `postgres/mbta.sql` | lecture6 L1288-1477 | SERIAL, CREATE TYPE … AS ENUM, TIMESTAMP DEFAULT now(), NUMERIC |

To try them yourself:
```bash
tools/start_servers.sh                                   # throwaway local servers (or use your own)
mysql --socket=/tmp/sqlsrv/mysql.sock -uroot -e 'CREATE DATABASE `mbta`'
mysql --socket=/tmp/sqlsrv/mysql.sock -uroot mbta < database/scaling/mysql/mbta.sql
psql -h /tmp/sqlsrv -p 5433 -U postgres -c 'CREATE DATABASE mbta'
psql -h /tmp/sqlsrv -p 5433 -U postgres -d mbta -f database/scaling/postgres/mbta.sql
```
