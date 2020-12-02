CREATE TABLE IF NOT EXISTS missions(
    mission_id INTEGER NOT NULL AUTO_INCREMENT,
    dossier_num  VARCHAR(63) NOT NULL,
    mission_obj  VARCHAR(63) NOT NULL,
    mission_trgt VARCHAR(63) NOT NULL,
    PRIMARY KEY (mission_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;