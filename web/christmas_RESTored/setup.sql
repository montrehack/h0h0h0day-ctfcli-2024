CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL,
    address TEXT,
    phone TEXT,
    is_naughty BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS presents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    recipient TEXT NOT NULL,
    occasion TEXT DEFAULT 'Christmas',
    price DECIMAL(10, 2),
    is_wrapped BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO presents (name, description, recipient, occasion, price, is_wrapped)
VALUES
    ('Smartphone', 'A new smartphone with all the latest features', 'johndoe', 'Christmas', 799.99, TRUE),
    ('Laptop', 'High performance laptop for work and play', 'janedoe', 'Christmas', 1200.00, FALSE),
    ('Teddy Bear', 'A soft, cuddly teddy bear', 'johndoe', 'Birthday', 25.99, TRUE),
    ('Coffee Maker', 'Automatic coffee machine', 'janedoe', 'Christmas', 150.00, TRUE),
    ('Drone', 'A high-tech drone for outdoor adventures', 'johndoe', 'Christmas', 500.00, FALSE),
    ('Gaming Console', 'Latest generation gaming console', 'janedoe', 'Christmas', 350.00, TRUE),
    ('Bluetooth Headphones', 'Noise-cancelling Bluetooth headphones', 'johndoe', 'Christmas', 120.00, TRUE),
    ('Smartwatch', 'A smartwatch with fitness tracking', 'janedoe', 'Christmas', 199.99, TRUE),
    ('Video Game', 'A popular video game for the new gaming console', 'johndoe', 'Christmas', 59.99, FALSE),
    ('Book Set', 'A set of classic novels', 'janedoe', 'Christmas', 45.00, TRUE),
    ('Gift Card', 'A $100 gift card for online shopping', 'johndoe', 'Christmas', 100.00, FALSE),
    ('VR Headset', 'Virtual reality headset for immersive gaming', 'janedoe', 'Christmas', 350.00, TRUE),
    ('Camera', 'A professional-grade camera for photography enthusiasts', 'johndoe', 'Christmas', 700.00, TRUE);
