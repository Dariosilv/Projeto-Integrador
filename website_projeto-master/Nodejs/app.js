async function cadastrar() {
    const nome = document.getElementById('nome').value;
    const usuario = document.getElementById('usuario').value;
    const senha = document.getElementById('senha').value;
    const confirmSenha = document.getElementById('confirmSenha').value;
  
    const response = await fetch('http://localhost:5500/cadastrar', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ nome, usuario, senha, confirmSenha }),
    });
  
    if (response.ok) {
      document.getElementById('msgSuccess').textContent =
        'Usuário cadastrado com sucesso';
    } else {
      const { error } = await response.json();
      document.getElementById('msgError').textContent = error;
    }
  }