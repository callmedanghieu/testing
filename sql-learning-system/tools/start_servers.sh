#!/usr/bin/env bash
# Start throwaway MariaDB (MySQL-compatible) and PostgreSQL servers for tests/test_servers.py.
# Data lives in /tmp/sqlsrv; nothing here is needed for the SQLite-based practice.
set -e
BASE=${SQLSRV_DIR:-/tmp/sqlsrv}
mkdir -p "$BASE"
if ! mysqladmin --socket="$BASE/mysql.sock" -uroot ping >/dev/null 2>&1; then
  if [ ! -d "$BASE/mysql" ]; then
    mariadb-install-db --user="$(whoami)" --datadir="$BASE/mysql" --auth-root-authentication-method=normal >/dev/null
  fi
  (mariadbd --user="$(whoami)" --datadir="$BASE/mysql" --socket="$BASE/mysql.sock" --port=3307 \
     --bind-address=127.0.0.1 --pid-file="$BASE/mysql.pid" >"$BASE/mysql.log" 2>&1 &)
  for i in $(seq 30); do mysqladmin --socket="$BASE/mysql.sock" -uroot ping >/dev/null 2>&1 && break; sleep 1; done
fi
PGBIN=$(ls -d /usr/lib/postgresql/*/bin | tail -1)
if ! "$PGBIN/pg_isready" -h "$BASE" -p 5433 >/dev/null 2>&1; then
  chown -R postgres "$BASE" 2>/dev/null || true
  if [ ! -d "$BASE/pg" ]; then su postgres -c "$PGBIN/initdb -D $BASE/pg -A trust" >/dev/null; fi
  su postgres -c "$PGBIN/pg_ctl -D $BASE/pg -o '-p 5433 -k $BASE -c listen_addresses=' -l $BASE/pg.log start" >/dev/null
  for i in $(seq 30); do "$PGBIN/pg_isready" -h "$BASE" -p 5433 >/dev/null 2>&1 && break; sleep 1; done
fi
echo "MariaDB socket: $BASE/mysql.sock   PostgreSQL: -h $BASE -p 5433"
