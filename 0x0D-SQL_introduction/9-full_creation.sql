-- create a table second_table in hbtn_0c_0
-- add multiple rows
CREATE TABLE IF NOT EXISTS second_table (
        id INT AUTO_INCREMENT,
        name VARCHAR(256),
	score INT,
        PRIMARY KEY(id)
);

INSERT INTO second_table(name, score) VALUES('John', 10);
INSERT INTO second_table(name, score) VALUES('Alex', 3);
INSERT INTO second_table(name, score) VALUES('Bob', 14);
INSERT INTO second_table(name, score) VALUES('George', 8);
