CREATE TABLE IF NOT EXISTS users (
    id                  INTEGER         PRIMARY KEY AUTOINCREMENT,
    username            TEXT            NOT NULL UNIQUE,
    password            TEXT            NOT NULL,
    email               TEXT            NOT NULL UNIQUE,
    avatar              BLOB            DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS dictionaries (
    id                  INTEGER                     PRIMARY KEY AUTOINCREMENT,
    title               TEXT                        NOT NULL,
    dictionary_slug     TEXT                        NOT NULL,
    created_at          TIMESTAMP                   DEFAULT CURRENT_TIMESTAMP,
    updated_at          TIMESTAMP                   DEFAULT CURRENT_TIMESTAMP,
    user_id             INTEGER                     NOT NULL,
    FOREIGN KEY         (user_id)                   REFERENCES users(id),
    UNIQUE              (dictionary_slug, user_id)
);


CREATE TABLE IF NOT EXISTS words (
    id                  INTEGER         PRIMARY KEY AUTOINCREMENT,
    original            TEXT            NOT NULL,
    translate           TEXT            NOT NULL,
    dictionary_id       INTEGER         NOT NULL,
    user_id             INTEGER         NOT NULL,
    FOREIGN KEY         (dictionary_id) REFERENCES dictionaries(id),
    FOREIGN KEY         (user_id)       REFERENCES users(id)
) ;

CREATE TABLE IF NOT EXISTS games (
    id                  INTEGER         PRIMARY KEY AUTOINCREMENT,
    title               TEXT            NOT NULL,
    created_at          TIMESTAMP       DEFAULT CURRENT_TIMESTAMP,
    updated_at          TIMESTAMP       DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS game_words (
    id                  INTEGER         PRIMARY KEY AUTOINCREMENT,
    game_id             INTEGER         NOT NULL,
    word_id             INTEGER         NOT NULL,
    point               INTEGER         DEFAULT 0,
    FOREIGN KEY         (game_id)       REFERENCES games(id),
    FOREIGN KEY         (word_id)       REFERENCES words(id)
);
