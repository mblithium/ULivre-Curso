> Notas do curso de Introdução à Ciência da Computação com Python I da USP. [Coursera - USP - Introdução à Ciência da Computação com Python PARTE 1](https://www.coursera.org/learn/ciencia-computacao-python-conceitos)

# SEMANA 1

11/02/2022

## Visão Geral do Curso
- Visão Geral do Curso;
- A quem se destina este curso;
- Como aproveitar este curso ao máximo;
- IMPORTANTE: O Código de Honra do Coursera.

## Introdução: O que é Ciência da Computação?

Uma nova ciência, surgida em meados do século 20
Engloba aspectos de várias áreas do conhecimento humano:
- Matemática;
- Engenharia;
- Ciências Naturais;
- Arte (o uso dessa habilidade nos diversos campos do pensamento e do conhecimento humano);

**Habilidades:** Capacidade de resolver problemas do mundo real computacionalmente. 

**Habilidades básicas**

- Formular um problema do mundo real em termos computacionais;
- Elaborar uma solução para esse problema em termos computacionais. "Algoritmo";
- Escrever um programa em uma linguagem de programação que implemente esse algoritmo;
- Testar o problema para verificar se ele realmente resolve o problema de forma correta.

**Habilidades mais avançadas**

- Gerenciar software de grande porte composto por muitos programas, vários deles de grande porte;
- Construir software para lidar com grandes quantidades de dados: Big Data, Mineração de Dados, Aprendizagem de Máquina, etc;
- Gerenciar equipes de desenvolvimento de software; 
- Comunicar-se com clientes e usuários para entender seus problemas, dificuldades e necessidades.

**Neste curso**

- **Habilidades de solucionar problemas:** formular questões, pensar criativamente, expressar a solução de forma clara e precisa
- **Aprender a programar**

### Algoritmo
> "Uma lista de instruções passo-a-passo para resolver um determinado problema". Pense como uma receita de bolo, uma sequência para resolver o problema.

**Simplificadamente, em Computação o que fazemos é:**

- Analisar o problema;
- Criar um algoritmo genérico que resolva esse problema;
- Escrever um programa que implemente esse algoritmo;
- Testar o programa para verificar que ele realmente funciona.

### Linguagens de Programação

Linguagens formais, precisas e cujas instruções podem ser executadas por um computador.

- Linguagem de baixo nível: Linguagem de máquina, lingagem de montagem (Assembly);
- Linguagem de auto nível: Python, Java, Ruby, C/C++, Javascript e muitas outras.

**Linguagens Interpretadas**

Código Fonte -> Interpretador -> Saída (Processador)

- **Código Fonte**: Código escrito pelo programador;
- **Interpretador**: Lê as linhas escritas no código fonte e traduz uma por vez para a saída.

**Linguagens Compiladas**

Código Fonte -> Compilador -> Código Objeto -> Executor -> Saída

- **Código Fonte**: Código escrito pelo programador;
- **Compilador**: Transforma esse programa em código de máquina, ou seja, código objeto;
- **Código objeto**: arquivo já compilado e pronto para ser executado pelo executor. Pode ser salvo no HD ou alguma unidade para posteriormente ser executado, sem necessidade de fazer a compilação toda vez que usar;
- **Executor (sistema operacional)**: Normalmente o Sistema Operacional, que pega o Código Objeto e executa para a saída (máquina).

### Linguagens Interpretadas e Compiladas
Exemplos: Java e Python

1) Antes de iniciar a execução do programa, um compilador traduz o código-fonte para _byteode_ (código em bytes).
2) Ao iniciar a execução do programa, o interpretador lê os _bytecodes_ uma-a-um executando os comandos correspondentes.


### Por onde começar?

**Um bom jeito de iniciar o aprendizado em Computação:**

- aprender a escrever códigos simples numa linguagem de alto nível;
- executar pequenos programas;
- aprender novos conceitos incrementalmente e;
- aumentar a sofisticação e o tamanho dos programas progressivamente.


# Introdução ao Python

```python
1 + 1
123874 + 342
5 - 8
8 * 6

# Divisão /
8 / 2

# Multiplicação *
2 + 5 * 2
(2 + 5) * 2

# Potenciação **
2 ** 3
10 ** 6

# Comparação
# < Menor que
2 < 20
20 < 50

# > Maior que
10 > 5
10 > 100

# >= Maior ou igual a
10 >= 20

# <= Menor ou igual a
5 <= 5

# == é igual a
9 ** 2 == 80 + 1

# != é diferente de
20 != 30
5 != 4 + 1
20 ** 2 != 400
```

# Variáveis e Primeiro Programa
14/02/2022

**Variáveis**: Uma parte da memória onde podemos guardar valores para ser modificado ou usado posteriormente. 

```py
x = 5
print(x)
# Resultado: 5

y = 10 * 32 + x
print(y)
# Resultado: 325

print(x)
# Resultado: 5

x = 345
print(x)
# Resultado: 345

x = x + 10
print(x)
# Resultado: 355

soma = x + y
print(soma)
# Resultado: 680

peso = 78
altura = 183


```
```py
# Strings

frase = "A massa ainda comerá do fino biscoito que fabrico"
print(frase)
# Resultado: "A massa ainda comerá do fino biscoito que fabrico"


```

# Quatro maneiras de rodar python
14/02/2022

- Idle
- Prompt de comando
- Executar arquivos .py
- Editor de texto do Idle

# Software Livre
14/02/2022

## Computação

**Simplificadamente, em Computação o que fazemos é**

- Analisar o problema;
- Criar um algoritmo genérico que resolva esse problema;
- Escrever um programa que implemente esse algoritmo;
- Testar o programa para verificar que ele realmente funciona.

## Programas são peculiares

- Um livro contém **conhecimento**
  - Pode ser sobre ferramentas
- Uma ferramenta (um martelo ou máquina) tem uma **utilidade**.
  - Mas o conhecimento que a gerou não é acessível diretamente.
- Um programa de computador é **as duas coisas**.
  - Ele contém o conhecimento sobre o problema e sua solução, descritos na linguagem de programação.
  - Ele é uma ferramenta para solucionar o problema quando é executado.
- Programas podem ser muito facilmente **copiados**.
- Programas podem ser **modificados** para incorporar melhorias ou resolver problemas novos.
- **A mesma ferramenta pode ser usada e adaptada por várias pessoas!**
- **O conhecimento pode ser acessado por todos!**

Mas...

- Do ponto de vista legal, programas são protegidos por direitos de autor (copyright)
  - Metáfora pelo qual são "comprados" e "vendidos" como se fossem objetos.
- O uso da ferramenta tem restrições
  - É preciso pagar pelo uso, alguns tipos de uso podem ser retritos, etc
- O conhecimento não pode ser mais usado por todos
  - E muitas vezes o código fonte é secreto. Compiladas e não revelado o código-fonte. Somente código objeto.

## O software livre

O software pode e deve ser compartilhado.

- "Se eu posso ajudar meu amigo (oferecendo uma cópia de um programa), por que não fazê-lo?"
- "Se meu amigo pode aprender com meu trabalho (analisando o código-fonte de um programa), por que impedi-lo?"
- "Se eu e meu amigo trabalharmos juntos, vamos criar mais facilmente um programa que resolva tanto os problemas dele quanto os meus!"
  
E não precisa nem ser meu amigo, pode ser uma comunidade com pessoas, empresas, governos, universidades...

## Definição

Um programa é Software Livre se oferecer as 4 liberdades seguintes:

- Liberdade para **executar** o programa;
- Liberdade para **estudar e modificar** o programa;
- Liberdade para **redistribuir** o programa;
- Liberdade para melhorar e **redistribuir as melhorias** ao programa.

## Vantagens

O Software Livre oferece diversas vantagens:
- Redução do **custo** e do **risco** de desenvolvimento
  - Não depende de uma única equipe paga por uma única empresa
- **Qualidade** potencialmente maior
  - Mais desenvolvedores trabalhando no programa
  - Mais usuários reportando falhas
  - Orgulho pessoal dos desenvolvedores
- Permite ao usuário **escolher** seu fornecedor
  - Qualquer um com acesso ao código-fonte pode prestar serviços

## Software Livre e você

- Várias linguagens de programação amplamente usadas, como **Java**, **Ruby** e **Python**, são Software Livre.
  - E várias delas são usadas em cursos introdutórios à programação por sua excelente qualidade, clareza e popularidade.
- Várias ferramentas que você conhece, como navegador **Firefox** e quase todo o sistema **Android**, além de partes fundamentais da infraestrutura de grandes sítios web, como servidor web **Apache** e o banco de dados **MySQL**, são Software Livre.

# Tipos de Dados
14/02/2022
```py
type(10)
# Resultado: <class 'int'>

type("tudo bem?")
# Resultado: <class 'str'>

type(5/2)
# Resultado: <class 'float'>

print(10 // 3)
# Divisão inteira. Resultado: 3

print(10 % 3)
# Resto da divisão. Resultado: 1

peso = 78
altura = 1.83
IMC = peso / (altura ** 2)
print(IMC)
# Resultado: 23.291229...

IMCInteiro = int(IMC)
print(IMCInteiro)
# Converte para inteiro. Resultado: 23

texto = "bom dia, tudo bem?"
print(len(texto))
# Conta quantos caracteres, comprimento. Resultado: 18

print(len(str(IMC)))
# Converte para string a variável IMC, conta quantos caracteres tem e exibe o valor na tela.
```

## Entrada de dados

```py
# temperaturaFahrenheit
temperaturaF = float(input('Digite um valor F: '))

temperaturaC = ((temperaturaF - 32) * 5) / 9

print(f"A temperatura em celcios é {temperaturaF}")
```

# Expressões Booleanas
15/02/2022

> Expressões booleanas vem de George Boole, que criou a álgebra booleana, valores que tem apenas dois tipos de coisas, como ligado e desligado, 1 e 2, verdadeiro e falso, etc.

```py
5 > 3
# True

18 == 9 * 2
# True

x = 12312
x < 0
# False

type(False)
# <class 'bool'>
```

**And, Or e outros operadores**
```py
# Usa-se "and" (e) para comparar se os valores comparados são verdadeiros. Se um deles ser falso, imprime False.
x = 12312
x > 0 and x ** 2 > 100
# True

x < 0 and x == 12312
# False

# Usa-se "or" (ou) para comparar se um valor é verdadeiro. Se pelo menos um dos valores for verdadeiro, imprime True, ao contrário, será False
x < 0 or x == 12312
# True

# O operador booleano "Not" inverte o valor booleano.
not x > 0
# False
not True
# False
not False
True
not not True
# True

```

### Tabela Verdade

| Operator | True | False  |
|---|---|---|
| and | True | False  |
| True | True  | False |
| False  | False  | False |
|---|---|---|
| or | True  | False  |
| True | True | True  |
| False | True | False |
|---|---|---|
| not | False  | True  |
|   |   |   |


### Ordem de Operadores Aritméticos

| Nível | Categoria | Operadores |
|---|---|---|
| 7 (auto) | Exponenciação | ** |
| 6 | Multiplicação | *, /, //, % |
| 5 | Adição e Subtração | +, -
| 4 | Relacional | ==, !=, <=, >=, >, < |
| 3 | Lógico | not |
| 2 | Lógico | and |
| 1 (baixo) | Lógico | or |
| | | | | |

```py
x = 12312
y = 50

x > 0 and not y == 50 or x + y == 150
# False
((x > 0) and (not y == 50)) or (x + y == 150)
# Melhora a visibilidade/entendimento ao usar parênteses.
```

## Execução Condicional

Escrever determinado trecho do código que só é executada caso uma condição for verdadeiro.

```py
temperatura = 102
if temperatura > 100:
  aguaFerve = True
print(aguaFerve)
```

```py 
if condição:
  comando
  comando
  comando...
else:
  comando
  comando
# If (se) e Else (se não)
```

```py
import math

# Modulo que alcula a raiz quadrada.
math.sqrt(8)
```

# Repetição - While
16/02/2022

"Laço" ou "Loop" de repetição de blocos de comandos.

```py
while (expressão/condição booleana verdadeira):
  comando1
  comando2
  ...
comando3
```
```py
i = 0
while (i <= 17):
  print(2 ** i)
  i+
print("Acabou")
```
## Variáveis booleanas - Indicadores de passagem

Indicadores de passagem para indicar se uma determinada condição passou a ser verdadeira ou não.

```py
decrescente = True

valor = 1
anterior = int(input("Digite o primeiro número da sequência: "))
while (valor != 0 and decrescente):
  valor = int(input("Digite o próximo número da sequência: "))
  if valor > anterior:
    decrescente = False
  anterior = valor

if decrescente:
  print("A sequência está em ordem decrescente!")
else:
  print("A sequência não está em ordem decrescente! ")
```

```py
meuCartao = int(input("Digite o número do cartão de crédito: "))

cartaoLido = 1
encontreiMeuCartaoNaLista = False

while cartaoLido != 0 and not encontreiMeuCartaoNaLista:
  cartaoLido = int(input("Digite o número do próximo cartão de crédito: "))
  if cartaoLido == meuCartao:
    encontreiMeuCartaoNaLista = True

if encontreiMeuCartaoNaLista:
  print("Eba! Meu cartão está lá!")
else:
  print("Xii, meu cartão não está lá...")
```

## Debugger
19/02/2022

Depurador é um programa que nos ajuda a identificar erros no programa, executando ele passo por passo.

- Breakpoints (pontos de parada)

# Funções
19/02/2022
(Semana 5)

São pedaços de código organizados em blocos, que recebe ou não parâmetros, retorna ou não algo e pode ser chamada ao decorrer do programa.

```py
def soma (x, y):
  return x + y 

```

- Exemplo com Coeficientes Binomiais

