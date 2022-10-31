CREATE TABLE IF NOT EXISTS departments (
	did INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS employee_model ( 
	employee_id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(20),
	age INT,
	position VARCHAR(30),
	fk_did INT,
	FOREIGN KEY (fk_did) REFERENCES departments(did)
);
