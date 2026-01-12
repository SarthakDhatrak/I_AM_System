CREATE DATABASE iam_db;
USE iam_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(255),
    role VARCHAR(20)
);

CREATE TABLE permissions (
    role VARCHAR(20),
    permission VARCHAR(50)
);

INSERT INTO users (username, password, role) VALUES
('admin', 'admin123', 'ADMIN'),
('analyst', 'analyst123', 'ANALYST');

INSERT INTO permissions VALUES
('ADMIN', 'VIEW_DASHBOARD'),
('ADMIN', 'MANAGE_USERS'),
('ANALYST', 'VIEW_DASHBOARD');
