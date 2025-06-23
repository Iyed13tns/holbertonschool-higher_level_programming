-- This SQL query retrieves the name and creation statement of a specific table named 'first_table' in the current database.
SELECT 
    TABLE_NAME AS 'Table',
    CREATE_TABLE AS 'Create Table'
FROM 
    INFORMATION_SCHEMA.TABLES
WHERE 
    TABLE_SCHEMA = DATABASE() 
    AND TABLE_NAME = 'first_table';