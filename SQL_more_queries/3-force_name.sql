-- Script that creates a table 'force_name' with id and name columns
-- The name column cannot be null
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);