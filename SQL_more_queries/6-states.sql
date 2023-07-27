-- Script that creates the database hbtn_0d_usa and the table states on your MySQL server.

CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL);
