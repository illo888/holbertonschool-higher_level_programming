-- Creates table id_not_null with default value
-- Sets default id to 1 when not specified
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
