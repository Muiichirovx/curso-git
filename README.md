# Como usar o Git no terminal:

1. Criação
Assim que você criar o seu arquivo(py/js/html...)

- Salve o arquivo(Ctrl + s)

// Importante!

Quando você cria um arquivo novo o git não consegue rastrear esse arquivo

2. Edição do arquivo:
Assim que você editar o seu arquivo(py/js/html...)

- Salve o arquivo(Ctrl + s)


3. Status:

Use o comando no terminal para visualizar o status:

git status

Tipo de status dos arquivos:

- Não rastreado
- Modificado
- Pronto para fazer o commit

4. Adicionar:

Use o comando no terminal para adicionar:

git add (Nome do arquivo)
git add .

// Importante!
O comando git add (Nome do arquivo) é usado somente para o arquivo
O comando git add . é usado para todos os arquivos

5. Commit:

O comando commit serve para salvar os arquivos que foram comitados

ex. historico{
    1 commit: alterei o arquivo .py
    2 commit: add um arquivo .js
    3 commit: deletei o arquivo .html
    ...
}

A partir desses commits que foram salvos no git, podemos escolher qual commit enviar para o github

Use o comando no terminal:

git commit -m "Mensagem"
git commit -am "Mensagem" - add + commit

6. Log:

O comando log é usado para visualizar o historico de commits

Use o comando no terminal:

git log
git log --pretty=oneline (é mais simples de visualizar os commits)

7. Diff:

O comando diff serve para verificar as mudanças

Use o comando no terminal:

git diff

(Dê enter ate aparecer END no terminal. Após use : + q)

8. Restore:

Restaurar caminhos especificados na árvore de trabalho

// Importante!

git restore --staged (nome do arquivo)

Vai "ocultar" o arquivo para não ir ao commit

9. Branch:

O comando branch serve para verificar em qual branch estamos

git branch

Para renomear a branch, use o comando:

git branch -M (novo nome)

10. Blame

git blame é usado para expor as ultimas alterações do arquivo

git blame (nome do arquivo.extenção)
