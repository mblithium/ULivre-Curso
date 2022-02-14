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