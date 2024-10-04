use employees;
CREATE TABLE employee (
    Employee_ID INT AUTO_INCREMENT PRIMARY KEY,
    lastname VARCHAR(50) NOT NULL,
    firstname VARCHAR(50) NOT NULL,
    DOB DATE,
    gender VARCHAR(10),
    hireDate DATE
);

INSERT INTO employee (lastname, firstname, DOB, gender, hireDate)
VALUES 
('Nguyen', 'An', '1990-05-10', 'Male', '2023-01-15'),
('Tran', 'Binh', '1985-03-22', 'Male', '2022-10-10'),
('Le', 'Lan', '1992-07-30', 'Female', '2021-05-25');


select * from employee

ALTER TABLE employee
MODIFY COLUMN DOB DATE;

