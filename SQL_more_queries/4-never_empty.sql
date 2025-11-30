-- Table yaradılır (əgər artıq mövcuddursa, xətaya düşmür)
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
