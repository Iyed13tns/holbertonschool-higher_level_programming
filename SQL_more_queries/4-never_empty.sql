-- Script that creates a table 'id_not_null' with id and name columns
-- The id column cannot be null and has a default value of 1
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);