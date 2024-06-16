-- schema.sql

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20)
);

CREATE TABLE interactions (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    type VARCHAR(50) NOT NULL,
    details TEXT,
    interaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
