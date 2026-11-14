-- CREATE TABLE users(
--     id SERIAL NOT NULL PRIMARY KEY,
--     first_name VARCHAR(100) NOT NULL,
--     second_name VARCHAR(100),
--     last_name VARCHAR(100) NOT NULL,
--     id_number VARCHAR(13) NOT NULL UNIQUE,
--     email VARCHAR(150) NOT NULL UNIQUE,
--     cellphone VARCHAR(10) NOT NULL UNIQUE,
--     password TEXT NOT NULL, 
--     create_at TIMESTAMP NOT NULL DEFAULT NOW(),
--     status VARCHAR(10) NOT NULL DEFAULT 'Pending',
--     first_active TIMESTAMP
-- );

-- CREATE TABLE products(
--     product_id SERIAL NOT NULL PRIMARY KEY,
--     product_name VARCHAR(200) NOT NULL,
--     product_description TEXT NOT NULL,
--     quantity INT NOT NULL DEFAULT 0,
--     price DECIMAL(4, 2) NOT NULL,
--     product_image TEXT NOT NULL,
--     user_id INT REFERENCES users(id)
-- );


-- INSERT INTO users(first_name, second_name, last_name, id_number, email, cellphone, password)
-- VALUES ('TestUser2', 'Secondname', 'UsersSurname', '0987654321234', 'test_user2@devs.com', '0612345789', 'password_123');
SELECT * FROM users;