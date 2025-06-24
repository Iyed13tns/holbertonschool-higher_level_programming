-- file: 5-full_table.sql
SELECT 
    TABLE_NAME AS 'Table',
    CREATE_TABLE AS 'Create Table'
FROM 
    INFORMATION_SCHEMA.TABLES
WHERE 
    TABLE_SCHEMA = DATABASE()
    AND TABLE_NAME = 'first_table';