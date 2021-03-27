DROP TABLE IF EXISTS item;

CREATE TABLE item (
   item_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   item_name TEXT NOT NULL,
   category_id INTEGER NOT NULL 
);

DROP TABLE IF EXISTS list;

CREATE TABLE list (
    list_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    creator_id INTEGER,
    list_name TEXT NOT NULL
);

DROP TABLE IF EXISTS list_items;

CREATE TABLE list_items (
    list_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL
);

DROP TABLE IF EXISTS roll_event;

CREATE TABLE roll_event (
    roll_event_id INTEGER AUTOINCREMENT,
    list_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    datetime_rolled TEXT NOT NULL
);

DROP TABLE IF EXISTS item_categories;

CREATE TABLE item_categories (
    category_id INTEGER NOT NULL,
    category_name TEXT NOT NULL
);




/* Base inserts */

INSERT INTO 
    item_categories(category_id, category_name)
VALUES
    (0, "Unknown"),
    (1, "Movie"),
    (2, "Video Game"),
    (3, "TV Show"),
    (4, "Anime"),
    (5, "Anime Movie");
