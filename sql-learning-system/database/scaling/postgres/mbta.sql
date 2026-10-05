-- PostgreSQL translation of the MBTA schema (sources/lecture6.txt L1288-1477).
-- Run: createdb mbta && psql -d mbta -f mbta.sql
CREATE TABLE "cards" (
    "id" SERIAL,
    PRIMARY KEY("id")
);

CREATE TABLE "stations" (
    "id" SERIAL,
    "name" VARCHAR(32) NOT NULL UNIQUE,
    "line" VARCHAR(32) NOT NULL,
    PRIMARY KEY("id")
);

CREATE TYPE "swipe_type" AS ENUM('enter', 'exit', 'deposit');

CREATE TABLE "swipes" (
    "id" SERIAL,
    "card_id" INT,
    "station_id" INT,
    "type" "swipe_type" NOT NULL,
    "datetime" TIMESTAMP NOT NULL DEFAULT now(),
    "amount" NUMERIC(5,2) NOT NULL CHECK("amount" != 0),
    PRIMARY KEY("id"),
    FOREIGN KEY("card_id") REFERENCES "cards"("id"),
    FOREIGN KEY("station_id") REFERENCES "stations"("id")
);

INSERT INTO "cards" DEFAULT VALUES;
INSERT INTO "stations" ("name", "line") VALUES ('Harvard', 'red');
INSERT INTO "swipes" ("card_id", "station_id", "type", "amount") VALUES (1, 1, 'deposit', 20), (1, 1, 'enter', -2.40);
SELECT "type", "amount", "datetime" IS NOT NULL AS "has_time" FROM "swipes";
