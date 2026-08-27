CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    embedding VECTOR(1024) NOT NULL
);

CREATE INDEX ON documents USING hnsw (embedding vector_cosine_ops);
