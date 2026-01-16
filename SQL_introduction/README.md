
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
```sql
-- Script that lists all databases
SHOW DATABASES;

**File:** `1-create_database_if_missing.sql`  
**Content:**
```sql
-- Script that creates the database hbtn_0c_0 if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;

