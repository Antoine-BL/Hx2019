use DBO

CREATE TABLE [user]
(
    user_id INT PRIMARY KEY NOT NULL IDENTITY,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    level INT,
    password VARCHAR(255) NOT NULL
)
CREATE UNIQUE INDEX user_user_id_uindex ON [user] (user_id)

CREATE TABLE [group]
(
    group_id INT PRIMARY KEY NOT NULL IDENTITY,
    date DATETIME NOT NULL,
    level INT,
    maxUser INT
)
CREATE UNIQUE INDEX group_group_id_uindex ON [group] (group_id)

CREATE TABLE [groupUser]
(
    group_id INT NOT NULL,
	user_id INT NOT NULL,
    date DATETIME NOT NULL,

	primary key (group_id, user_id),
	FOREIGN KEY (user_id) REFERENCES [user](user_id),
	FOREIGN KEY (group_id) REFERENCES [group](group_id)
)
