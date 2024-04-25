<?php
   
   $nome = $_POST['nome'];
   $usuario = $_POST['usuario'];
   $senha = $_POST['senha'];
   $confirmar_senha = $_POST['Confirmar senha'];
   $data_atual = date('d/m/Y');
   $hora_atual = date('H.i.s')

   // Configurações de credenciais
   $server = 'localhost';
   $usuario = 'root';
   $senha = '';
   $banco = 'Teste_do_banco';

   $conn = new mysqli('localhost','root','','teste_do_banco');

   if($conn->connect_error){
        die("Falha ao se comunicar com o banco de dados:" .$conn->connect_error);
   }

   $smtp = $conn->prepare("INSERT INTO mensagem (nome , email, mensagem,data,hora) VAlUES (?,?,?,?,?)");
   $smtp->bind_pram("sssss",$nome,$usuario,$senha,$confirmar_senha,$data_atual,$hora_atual)
   if($smtp->execeute()){
    echo "Mensagem enviada com sucesso! ";
   }else{
      echo "Erro no envio da mensagem:".$smtp->error;
   }

   $smtp->close();
   $conn->close();

