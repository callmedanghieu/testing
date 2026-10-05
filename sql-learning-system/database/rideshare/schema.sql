-- rideshare: Lecture 4 L863-968 (views for security) and Lecture 6 L1840-1900 (access control)
CREATE TABLE "rides" (
    "id" INTEGER,
    "origin" TEXT NOT NULL,
    "destination" TEXT NOT NULL,
    "rider" TEXT NOT NULL,
    PRIMARY KEY("id")
);
