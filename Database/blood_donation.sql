CREATE TABLE donors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    blood_group VARCHAR(5) NOT NULL,
    phone VARCHAR(15) UNIQUE NOT NULL,
    city VARCHAR(50),
    last_donation_date DATE,
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE blood_banks (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100),
    contact_number VARCHAR(15),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE blood_inventory (
    id SERIAL PRIMARY KEY,
    blood_bank_id INT REFERENCES blood_banks(id),
    blood_group VARCHAR(5) NOT NULL,
    units_available INT DEFAULT 0,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE donations (
    id SERIAL PRIMARY KEY,
    donor_id INT REFERENCES donors(id),
    blood_bank_id INT REFERENCES blood_banks(id),
    blood_group VARCHAR(5),
    units_donated INT,
    donation_date DATE DEFAULT CURRENT_DATE
);

CREATE TABLE blood_requests (
    id SERIAL PRIMARY KEY,
    hospital_id INT REFERENCES blood_banks(id),
    blood_group VARCHAR(5),
    units_required INT,
    status VARCHAR(20) DEFAULT 'OPEN',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO donors
(name, blood_group, phone, city, last_donation_date, is_available)
VALUES
('Ravi Kumar', 'O+', '9000000001', 'Hyderabad', '2025-12-10', TRUE),
('Anil Reddy', 'A+', '9000000002', 'Hyderabad', '2025-11-15', TRUE),
('Suresh Kumar', 'B+', '9000000003', 'Vijayawada', '2025-10-20', FALSE),
('Rahul Sharma', 'O+', '9000000004', 'Hyderabad', '2025-09-12', TRUE),
('Kiran Patel', 'AB+', '9000000005', 'Guntur', '2025-08-05', TRUE);

SELECT * FROM donors;

SELECT name, blood_group, phone, city
FROM donors
WHERE blood_group = 'O+'
AND city = 'Hyderabad'
AND is_available = TRUE;

SELECT * FROM donors
WHERE blood_group = 'O+'
LIMIT 10;

CREATE INDEX idx_donor_search
ON donors (blood_group, city, is_available);
