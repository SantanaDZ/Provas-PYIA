CREATE DATEBASE loja;
USE loja;
CREATE TABLE Estoque(
  EstoqueID INT PRIMARY KEY AUTO_INCREMENT,
  ProdutoID INT,
  FornecedorID INT,
  Quantidade INT,
  DataEntrada DATE
  FOREIGN KEY(ProdutoID) REFERENCES Produtos(ProdutosID)
  FOREIGN KEY(FornecedorID) REFERENCES Fornecedores(FornecedorID)
  
);  

SELECT Produtos.NomeProduto, Estoque.Quantidade, Estoque.DataEntrada, Fornecedores.NomeFornecedor
FROM Estoque
FULL OUTER JOIN Produtos ON Estoque.ProdutoID = Produtos.ProdutoID
FULL OUTER JOIN Fornecedores ON Estoque.FornecedorID = Fornecedores.FornecedorID;

SELECT Produtos.NomeProduto, SUM(Estoque.Quantidade) AS TotalEstoque
FROM Estoque
JOIN Produtos ON Estoque.ProdutoID = Produtos.ProdutoID
GROUP BY Produtos.NomeProduto;

ALTER TABLE Estoque
ADD COLUMN PrecoCompra DECIMAL(10, 2);

ALTER TABLE Estoque
MODIFY COLUMN Quantidade BIGINT;

