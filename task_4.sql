-- Use the alx_book_store database
USE alx_book_store;

-- Query the information_schema to get the full description of the books table
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, EXTRA
FROM information_schema.columns
WHERE table_name = 'Books'
AND table_schema = 'alx_book_store';
