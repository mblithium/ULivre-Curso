> Documento em formato markdown onde guardo minhas anotações de estudos do curso de git e github hospedado em https://www.youtube.com/playlist?list=PLlAbYrWSYTiPA2iEiQ2PF_A9j__C4hi0A

# 01/30 - Introdução - Git e Github para Iniciantes
07/02/2022

- Aprender o que é um Controle de Versão;
- Como lidar com o Git e seus comandos;
- Como subir código no Github.

## Requisitos Básicos
- Windows, Linux ou OSX;
- Conhecimento básico de terminal ou prompt de comando;
- Vontade de aprender.

# 02/30 - O que é controle de versão
07/02/2022

## Sem controle de versão
- Cópias e mais cópias de um projeto. 
- Apagar aquivo importante e não tem como recuperar.

## Controle de versão
Sistema com a finalidade de gerenciar diferentes versões de um documento.

**Sistema Git**: Snapshot dos estados dos arquivos.

# 03/30 - História do Git
07/02/2022

Linux era versionado no BitKeeper. Houve uma quebra no contrato com a Linux Foundation, onde teria que pagar para ter direito de usar a ferramenta. O Linux Torvalds então não aceitou, pois não era um sistema muito bom, assim criando o Git com melhorias.

- Velocidade;
- Design Simples;
- Suporte robusto a desenvolvimento não linear (milhares de banrches paralelos);
- Totalmente distribuído;
- Capaz de lidar eficientemente com grandes projetos como o kernel do Linux.

# 04/30 - O que é Github
07/02/2022

Serviço web compartilhado para projetos que utilizam o Git para versionamento, servidor para armazenar os repositórios. Git é diferente de Github.

# 05/30 - Instalando o Git
07/02/2022

- Instalação em https://git-scm.com/download
  
# 06/30 - Configurando o Git
07/02/2022

git-config

```bash
# Nome
git config --global user.name "Meu Nome"

# Email do usuário
git config --global user.email "user@email.com"

# Editor padrão de código
git config --global core.editor code

# Ver valores
git config user.name
git config user.email
git config --list
```

# 07/30 - Inicializando um repositório
07/02/2022

## Criar pastas
mkdir git-course

## Entrar
cd git-course

## Inicializar repositório no diretório atual
git init

# 08/30 - Utilizando editores no terminal
07/02/2022

## Vim

vi ou vim [nome do arquivo]
i = entra no modo de inserção
esc = sai do modo de inserção
:w = Salvar "write"
:q = Sair "quit"
:wq = Salvar e sair.

# 09/30 - Ciclo de vida dos arquivos
07/02/2022

## Ciclo de vida dos status dos arquivos
- **Untracked**: Não marcado, o momento que foi adicionado no diretório mas não foi marcado para ser visto no git.
- **Unmodified**: Depois de adicionado, existe no git mas está sem modificações,
- **Modified**: Quando modificado.
- **Staged**: Momento que a versão for fechada.

```bash
# Mostra o status dos arquivos no repositório.
git status

# Adiciona o arquivo ao git
git add nomedoarquivo

# Cria um snapshot
git commit -m "digitar o que foi modificado"
```

# 10/30 - Visualizando logs
07/02/2022

```bash
# Logs dos commits
git log
git log --decorate

# Filtra por nome de autor. 
git log --author="Math"

# Mostra os autores em ordem alfabética, junto com quantos commits fizeram e seus arquivos alterados.
git shortlog

# Filtrar só por nome de contribuidores e quantos commits fizeram.
git shortlog -sn

# Mostra de forma gráfica os branchs e versões.
git log graph

# Mostra o que foi alterado no commite com a seguinte hash.
git show [hash]
```

# 11/30 - Visualizando diferença entre versões

```bash
# Mostra as modificações
git diff

# Somente o nome dos arquivos alterados
git diff --name-only

# Quando os arquivos já foram adicionados pelo menos uma vez
git commit -am "Descrição de o que foi alterado aqui"
```

# 12/30 - Desfazendo coisas com o reset
08/02/2022

Resetar ou voltar para uma versão do arquivo.

```bash
# Reseta o arquivo para antes da edição.
git checkout nomedoarquivo

# Reseta um arquivo do staged
git reset HEAD nomedoarquivo

# Resetando alterações quando feito o commit.
git reset --option [hash]
# --soft: Voltar o commit.
# --mixed: Voltar o commit e volta os arquivos para antes do staged.
# --hard ignora a existencia do commit e tudo que foi feito nele.
# Altera o histórico, tomar cuidado para usar somente no repositório local para não ter problemas.
```

# 13/30 - Criando repositório remoto
08/02/2022

Trabalhando com repositório remoto.
Github

# 14/30 - Ligando o repositório local com remoto
08/02/2022

```bash
git remote add origin https://github.com/mblithium/github-course.git
git remote origin
git remote -v
git branch -M main
git push -u origin main
```

# 15/30 - Criando chave SSH
08/02/2022

SSH é um protocolo para autenticar um usuário remoto a um servidor.

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Os arquivos de chaves ficam em /home/.ssh/

# 16/30 - Enviando mudanças para o remoto
09/02/2022

```bash
# git push remoto branch
git push origin main
```

# 17/30 - Clonando um repositório
09/02/2022

```bash
git clone endereçossh.git escolhernomedoclone
```

# 18/30 - Fazendo um fork de um projeto
09/02/2022

Botão "Fork" no repositório. Ele faz uma cópia de algum repositório. Pode ser usado para trabalhar em modificações e depois enviar para ser aceito no repositório oficial.

# 19/30 - O que é um branch e por que usar
09/02/2022

## O que é um branch?

É um ponteiro móvel que leva a um commit.

São ramificações do código.

## Por que usar?

Vantagens

- Poder modificar sem alterar o local principal (master);
- Facilmente removível e manipulável;
- Múltiplas pessoas trabalhando;
- Evita conflitos

# 20/30 - Criando um branch
09/02/2022

```bash
# checkout muda para outro branch.
# -b cria um novo branch
git checkout -b testing

# Ver em qual branch está trabalhando.
git branch
```

# 21/30 - Movendo entre branches e deletando
09/02/2022

```bash
# Move entre ramificações (branches)
git checkout nomedobranch

# Deleta uma ramificação
git branch -D testing
```

# 22/30 - Entendendo o Merge
09/02/2022 (ver novamente)

## Unindo branches

### Merge
Cria um novo branch no branch que será mesclado.

Pro
- Operação não destrutiva;


Contra
- Commit extra
- Histórico poluído

# 23/30 - Entendendo o Rebase
09/02/2022

### Rebase
Aplica todas as mudanças para frente da fila/histórico do branch.

Pro
- Evita commits extras
- Histórico linear
    
Contra
- Perde ordem cronológica
  
git pull --rebase

# 24/30 - Merge e Rebase na prática
10/02/2022

MERGE
```bash
git merge nomedabranchparamesclar
```

```bash
got rebase nomedabranchparamesclar
```

Em caso de adição normal enquanto desenvolvendo, usar o rebase. Porém quando for adição de nova feature ou pull request, usar o merge para identificar que foi feito a mesclagem.

# 25/30 - Criando um .gitignore
10/02/2022

Arquivo ".gitignore" para o git não monitorar nem subir aqueles arquivos especificados neste arquivo.

```bash
# Ignora todos os arquivos com a extensão json
*.json

# Ignora um arquivo específico, no caso o db.xls
db.xls
```
## Padrões de arquivos que são ocultos em vários projetos.
[Gitignore](https://github.com/github/gitignore)

# 26/30 - Git stash é lindo
10/02/2022

Git stash é responsável por guardar as modificações que ainda não foram commitadas. Ele guarda as modificações.

```bash
# Guarda as mudanças
git stash

# Aplica as mudanças guardadas
git stash apply

# Mostra a lista de rascunhos
git stash list

# Limpa todos os rascunhos
git stash clear
```

# 27/30 - Criando alias
10/02/2022

Aliases são atalhos para comandos.
Exemplo: git status = git s

```bash
git config --global alias.s status
```

# 28/30 - Criando tags
10/02/2022

Para criar um ponto no código onde diz que finaliza uma versão.

```bash
# -a (com alguma notação) -m (mensagem)
git tag -a 1.0.0 -m "Readme finalizado"
```

# 29/30 - Salvando sua sexta com git revert
10/02/2022

**Revert:** reverter mudanças, coloca o código anterior no lugar, mas continua com a modificações no local.
**Reset:** Reset apaga tudo que foi feito e retorna para o estado anterior.

```bash
git revert hashdocommitparareverter
```

# 30/30 - Apagando tags e branches remotos
10/02/2022

```bash
# Deleta tag local
git tag -d 1.0.1

# Apaga uma tag do repositório remoto.
git push origin :1.0.0

# Apaga um branch
git push origin test
```

