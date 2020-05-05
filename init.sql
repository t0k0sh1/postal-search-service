DROP DATABASE IF EXISTS sample;
DROP USER IF EXISTS 'user'@'localhost';

-- create new database
CREATE DATABASE sample DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- create new user
CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';

-- grand all privileges on created database to created user
GRANT ALL PRIVILEGES ON sample.* TO 'user'@'localhost';

-- flush privileges
FLUSH PRIVILEGES;

-- change database
USE sample;

-- create address table
CREATE TABLE address (
    id INT NOT NULL PRIMARY KEY COMMENT 'ID',
    zipcode CHAR(7) NOT NULL COMMENT '郵便番号（7桁）',
    pref_name VARCHAR(255) COMMENT '都道府県名',
    pref_name_kana VARCHAR(255) COMMENT '都道府県名（カナ）',
    city_name VARCHAR(255) COMMENT '市区町村名',
    city_name_kana VARCHAR(255) COMMENT '市区町村名（カナ）',
    town_name VARCHAR(255) COMMENT '町域名',
    town_name_kana VARCHAR(255) COMMENT '町域名（カナ）',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '作成日時',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新日時'
);
