CREATE TABLE mensagem(
    id SERIAL NOT NULL,
    mensagem boolean NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(id)
);