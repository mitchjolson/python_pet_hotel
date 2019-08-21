CREATE TABLE owner
(
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR
);
​
CREATE TABLE pet
(
    "id" SERIAL PRIMARY KEY,
    "owner_id" INT,
    "name" VARCHAR,
    "breed" VARCHAR,
    "color" VARCHAR,
    "checked_in" VARCHAR
);
​
ALTER TABLE "pet" ADD FOREIGN KEY ("owner_id") REFERENCES "owner" ("id");
​
​
INSERT INTO owner
    ("name")
VALUES
    ('Molly');
​
INSERT INTO owner
    ("name")
VALUES
    ('Mitch');
​
​
INSERT INTO owner
    ("name")
VALUES
    ('Mark');
​
INSERT INTO pet
    ("owner_id", "name", "breed", "color", "checked_in")
VALUES
    ('1', 'Pallu', 'Alaskan Malamute', 'Ginger', '08/21/2019');
​
INSERT INTO pet
    ("owner_id", "name", "breed", "color", "checked_in")
VALUES
    ('2', 'Leon', 'Annoying', 'Tabby', '08/21/2019');
​
INSERT INTO pet
    ("owner_id", "name", "breed", "color", "checked_in")
VALUES
    ('3', 'Tobi', 'Mutt', 'Cow', '08/21/2019');
    
INSERT INTO pet
    ("owner_id", "name", "breed", "color", "checked_in")
VALUES
    ('1', 'Kitty', 'Puke Princess', 'White', '08/19/2019');