-- Creates table unique_id with UNIQUE constraint
-- Prevents duplicate id entries
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
