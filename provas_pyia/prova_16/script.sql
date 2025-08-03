CREATE DATABASE loja;
USE loja;
CREATE TABLE produtos(
  ProdutoID INT PRIMARY KEY AUTOINCREMENT,
  NomeProduto VARCHAR(255),
  Quantidade INT,
  Preco DECIMAL,
  );

INSERT INTO produtos (NomeProduto, Quantidade, Preco)
VALUES 
  ('Mouse',5,199.99),
  ('Teclado',10,250.00),
  ('Monitor', 1,500.00);
