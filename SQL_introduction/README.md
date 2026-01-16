
# SQL - Introduction

This project introduces the basics of SQL and how to use MySQL to manage data in relational databases.

## What is SQL?
SQL (Structured Query Language) is a language used to interact with databases.  
It allows you to create databases, define tables, store data, update information, and retrieve results using queries

### Task 0: List All Databases

In this task, the goal was to write an SQL script that displays all the existing databases in the MySQL server.  
The script must start with a comment explaining its purpose, and all SQL keywords must be written in uppercase.

**File:** `0-list_databases.sql`  
**Purpose:** Show all databases using the `SHOW DATABASES;` command.

Example content:
# sql
-- Script that lists all databases
SHOW DATABASES;

**File:** `1-create_database_if_missing.sql`  
**Content:**
#sql
-- Script that creates the database hbtn_0c_0 if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;

### Task 2: Delete a Database

In this task, the goal was to write an SQL script that deletes the database `hbtn_0c_0` from the MySQL server.  
The script must not fail if the database does not


Task 3: List All Tables
In this task, the goal was to write a script that lists all the tables inside the current database.
The script must use only the SHOW TABLES; command, start with a comment, and all SQL keywords must be uppercase.
The database name will be passed as an argument when calling the mysql command.
File: 3-list_tables.sql
Content:
SQL-- Script that lists all tables in the current databaseSHOW TABLES;إظهار 

Task 4: First Table
In this task, the goal was to create a table named first_table in the currently selected database.
The table must contain two columns:

id (INT)
name (VARCHAR(256))

The script must not fail if the table already exists, so CREATE TABLE IF NOT EXISTS must be used.
SQL keywords must be uppercase and the script must begin with a comment describing the task.
You are not allowed to use SELECT or SHOW.
File: 4-first_table.sql
Content:
SQL-- Script that creates the table `first_table` if it does not already exist-- The table has: id INT, name VARCHAR(256)CREATE TABLE IF NOT EXISTS first_table (    id INT,    name VARCHAR(256));

---

### Task 5: Full Description

In this task, the goal was to write an SQL script that prints the full description of the table `first_table` from the database `hbtn_0c_0`.  
The script must not use `DESCRIBE` or `EXPLAIN`, so instead we use the command:
