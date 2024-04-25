const express = require('express');
const { Pool } = require('pg');

const app = express();
const port = 3000;

// Configurar a conexão com o banco de dados
const pool = new Pool({
  user: 'seu_usuario',
  host: 'localhost',
  database: 'seu_banco_de_dados',
  password: 'sua_senha',
  port: 5432,
});

app.get('/', (req, res) => {
  // Consultar o banco de dados
  pool.query('SELECT * FROM sua_tabela', (error, results) => {
    if (error) {
      throw error;
    }
    res.send('Bem-vindo ao backend!' + JSON.stringify(results.rows));
  });
});

app.listen(port, () => {
  console.log(`Backend rodando na porta ${port}`);
});