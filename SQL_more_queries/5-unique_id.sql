-- Script that creates a table 'unique_id' with id and name columns
-- The id column must be unique and has a default value of 1
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);