CREATE DATABASE lesson_30;

CREATE TABLE IF NOT EXISTS book (
                                    id SERIAL PRIMARY KEY,
                                    name VARCHAR(256) NOT NULL,
    author VARCHAR(256) NOT NULL,
    genre VARCHAR(256) NOT NULL,
    pages INTEGER NOT NULL,
    writing_date DATE,
    publisher VARCHAR(256) NOT NULL,
    publication_year INTEGER NOT NULL,
    book_code VARCHAR(30) UNIQUE NOT NULL
    );

DROP TABLE IF EXISTS book;

INSERT INTO book (name , author, genre, pages, writing_date, publisher, publication_year, book_code)
VALUES ('Kobzar', 'T.G.Shevchenko', 'Poesion', 576, '1840-03-12', 'Shkola', 2022, '978-966-429-192-4');

SELECT
    name,
    author,
    book_code
FROM book;

DELETE FROM book
WHERE author = 'T.G.Shevchenko';

UPDATE book
SET publication_year = 2000
WHERE author = 'T.G.Shevchenko';

UPDATE book
SET genre = 'Poetry'
WHERE genre = 'Poesion';

SELECT * FROM book;
