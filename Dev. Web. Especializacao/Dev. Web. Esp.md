# Desenvolvimento Web

> Aqui neste arquivo estão todas as minhas anotações das aulas do curso, além de links internos para pular para conteúdos específicos.

# SUMÁRIO
- Desenvolvimento Web
  - [Capítulo 11 - Aula 01](#cap11-a01) 
  - [Capítulo 11 - Aula 02](#cap11-a02) 
  - [Capítulo 11 - Aula 03](#cap11-a03)

---

# HTML e CSS, Parte 1

## 001 - Conteúdo do Curso

## Capítulo 1 - Aula 0 - O que vamos aprender no módulo 01?

25/02/2022
---

- Como surgiu a internet;
- Como a internet funciona;
- Domínio e hospedagem;
- Backend e frontend;
- Linguagens;
- Organizar ambiente de desenvolvimento;
- Estruturas de documentos HTML;
- Textos, símbolos e emojis;
- Hierarquia de Títulos
- Semântica;
- Links;
- Multimídia;
- Imagens otimizadas;
- Estilos CSS

## Capítulo 1 - Aula 1 - Precisamos fazer um acordo
25/02/2022
---
- **M01** - Primeiros passos HTML + CSS: Conceitos básicos, preparação de ambiente, semântica HTML5, textos, títulos, ligações, multimídia, estilos.
- **M02** - Deixando as coisas mais bonitas: Fundamentos do design, psicologia das cores, tipografia, elementos CSS, modelo de caixas, wireframe, responsabilidade.
- **M03** - Colocando protótipo no ar: Versionamento de software, hospedagem de sites estáticos, tabelas.
- **M04** - Aprofundando os conhecimentos: Quadros em linha, formulários, media queries, mobile first;
- **M05** - Novas tecnologias: Flexbox, Grid Layout, projeto final.

Foco, bastante exercícios e um caderno de anotações.

https://github.com/gustavoguanabara
https://gustavoguanabara.github.io

# Capítulo 1 - Aula 02 - Será que este curso é pra mim?
27/02/2022

## É para mim se:

- Me interesso por aprender a criar sites, mas não sei onde começar;
- Já tentei, mas acho confuso 'decorar' tantos comandos;
- Tenho boa base, mas quero me aprofundar nas especificações;
- Consigo adaptar códigos prontos, mas não sei criar os meus próprios sites.
- Estou tendo essa disciplina e estou com dificuldades;
- Além de aprender a criar sies, quero deixá-los na Internet.

## Não é pra mim se:

- Eu já sei tudo sobre desenvolvimento HTML5 e CSS3;
- Estou procurando por códigos prontos e templates para sites;
- Estou com pressa e preciso aprender em poucas semanas;
- Quero apenas uma lista de comandos sem 'papinho' extra;
- Não consigo esperar o lançamento de aulas semanais;
- Prefiro consultar a documentação oficial das linguagens.

# Capítulo 1 - Aula 3 - Melhores livros para aprender HTML5 e CSS3
27/02/2022

## Bibliografia recomendada

- Material de Apoio;
- HTML5, Flexbox in CSS, CSS, Grid Layout in CSS (O'Reilly);
- HTML5 e CSS3 (Elizabeth Castro e Bruce Hyslop - Alta books);
- HTMLeCSS (Jon Duckett - Alta books);
- Use a cabeça - HTML e CSS (Elisabeth Robson e Eric Freeman);
- Nate Cooper e Kim gen (novatec);
- HTML5 (Mauricio Samy Silva - Novatec);
- CSS3 (Mauricio Samy Silva - Novatec);
- Fundamentos de HTML5 e CSS3 (Mauricio Samy Silva - Novatec);
- CSS Grid Layout (Maurício Samy Silva - Novatec);
- Curso de Design gráfico (David Dabner - GG);
- Bob e Maggie Gordon Design (Senac);
- A psicologia das Cores (Eva Heller - GG);
- Pensar com tipos (Ellen Lupton - GG);
- Flexbox Explained (Jorge Montoya e Stephen Burge - OSTRaining);
- CSS Grid Explained (Jorge Montoya e Stephen Burge - OSTRaining);
- [ Antigos ] Smashing HTML5 (Bill Sanders - Bookman);
- [ Antigos ] Smashing CSS (Eric Meyer - Bookman).

## Referências Online 

- Referência MDN (Mozilla Developper Network);
- W3C Standards (World Wide Web Consortium);
- WHATWG Living Standard (Web Hypertext Application Technology Working Group);
- W3Schools (Defsnes Data).

# Capítulo 1 - Aula 04 - Como a Internet chega na minha casa?
27/02/2022

How does the internet work - https://youtu.be/TNQsmPf24go

# Capítulo 2 - Aula 01 - Como a Internet funciona?

    Para poupar tempo, irei deixar pendente pois já vi esta aula antes de eu reiniciar os estudos. Irei preencher com anotações no futuro.

# Capítulo 2 - Aula 02 - O que é domínio e hospedagem?

    Para poupar tempo, irei deixar pendente pois já vi esta aula antes de eu reiniciar os estudos. Irei preencher com anotações no futuro.

# Capítulo 3 - Aula 01 - A diferença entre HTML, CSS e JavaScript
01/03/2022

- A linguagem HTML;
- As CSSs (folhas de estilo);

- HTML - HyperText Markup Language (Linguagem de Marcação de Hipertexto). Focada em **conteúdo** (textos, imagens, videos, tabelas, etc)
- CSS - Cascading Style Sheets (folhas de estilo em cascata). Focadas em **design/estilos** (cores, sombras, tamanhos, posicionamento).
- JS - JavaScript - Focado em **interatividade** (menus, animações, popups, validações, lógica de programação, etc).

Conteúdo em HTML

- Exemplo de título: <h1></h1>
- Exemplo de parágrafo: <p></p>

```html
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width,initial-scale=1.0">
        <title>Títulos do site</title>
    </head>
    <body>
        <h1>Título</h1>
        <p>Parágrado</p>
    </body>
</html>
```

Conteúdo em CSS

```css
/*Seletor h1 */ 
h1 { 
    /*declarações*/
}
```

# Capítulo 3 - Aula 02 - Front-end, Back-end e Full Stack
01/03/2022

## Front-end e Back-end

**Site estático**: O mesmo site é entregue para todos os clientes.
**Sites dinâmicos**: As informações no site mudam de acordo com o usuário.

**Back-end / Client-side**: Tecnologias como HTML5, CSS3 e JS. Do lado do cliente.
**Front-end / Server-side**: Tecnologias como JavaScript (NodeJS), PHP, C#, Python, Ruby, Java, etc. Do lado do servidor.
**Full stack**: Faz tanto o front-end, quanto o back-end.

# Capítulo 4 - Aula 01 - Instalando todas as ferramentas
01/03/2022

- Navegador WEB (Recomendado Google Chrome);
- Microsoft Visual Studio Code. Com "word wrap": on, "salvar automaticamente", extensões: "Live Server";

# Capítulo 4 - Aula 02 - Seu primeiro código HTML

[**Ex001**](./html-css/exercicios/ex001/index.html)


# Capítulo 5 - Aula 01 - Parágrafos e Quebras de Linha
01/03/2022

```html
<p>Parágrafo</p>
<h1>Títulos</h1>
<br> <!--quebra de linha-->
<hr> <!--linha horizontal-->
```

# Capítulo 5 - Aula 02 - Símbolos e Emoji no seu site
05/03/2022

## Colocando símbolos
```html
    &reg;
    &copy;
    &trade;
    &euro;
    &pound;
    &yen;
    &cent;
    &delta;
    &Delta;
    &uparrow;
    &uarr;
    &downarrow;
    &darr;
```

## Colocando emojis

```html
    &#x1F596;
    &#x1F913;
```

# Capítulo 6 - Aula 01 - Você tem o direito de usar qualquer imagem no seu site?
05/03/2022

- Unsplash
- Pexels

Não é qualquer imagem que se pode usar nos sites. É necessário ficar atento para as licenças de utilização daquela imagem, os direitos autorais, para não ter problemas com isso em um site em produção no futuro.

# Capítulo 6 - Aula 02 - Quais são os formatos de imagens na Web?
05/03/2022

Uma imagem é um conjunto de pontos/pixels que formam a imagem na tela.

- JPG ou JPEG
- PNG
- GIF
- SVG

# Capítulo 6 - Aula 02 - O tamanho das imagens importa para um site?

## Alterando a imagem no GIMP
06/03/2022

1500x1000 já é um bom tamanho de imagem para fundo.
Resolução depende da imagem, mas pode ser uns 50.

Manter backup das imagens "full", que não foi alterada, para futuras alterações.

# Capítulo 6 - Aula 04 - A tag img em HTML5
06/03/2022

CTRL + Espaço - mostra a lista de arquivos.

```html
<!-- Carrega uma imagem no mesmo diretório -->
<img src="./imagem.png" alt="texto alternativo">

<!-- Carrega uma imagem em um sub-diretório -->
<img src="./img/imagem.png" alt="imagem em subpasta">

<!-- Carrega uma imagem da internet -->
<img src="endereçodaimage.com/imagem.png" alt="imagem na internet">

<!-- Carrega uma imagem fora de um diretório -->
<!-- Exemplo: -->
<!-- Projeto -->
<!--   | pages (Estamos aqui) -->
<!--       | index.html -->
<!--   | assets -->
<!--       | char.png -->

<img src="../assets/char.png" alt="imagem em subpasta">


```

# Capítulo 6 - Aula 05 - Como mudar o favicon de um site
07/08/2022

## O que é?
"Favicon" (Favorite Icon) é o ícone de favorito do site, que normalmente aparece na aba do navegador quando a página está carregada e também quando salva o site nos favoritos.

## Sites relacionados
- favicon.cc
- iconarchive.com
- favicon.io

## Como adicionar no HTML

```html
<link rel="shortcut icon" href="./favicon.ico" type="image/x-icon">
```

# Capítulo 7 - Aula 01 - Hierarquia de Títulos
07/08/2022

De H1 até H6. **Não é letra grande ou tamanho**, no HTML5, é semântico, onde o H1 é o primeiro nível, H2 é subtítulo de H1, H3 é subtítulo de H2 e assim por diante.

```html
<!-- Hierarquia -->
<h1></h1>
    <h2></h2>
        <h3></h3>
            <h4></h4>
                <h5></h5>
                    <h6></h6>
```

```html
<h1></h1>
<h2></h2>
<h3></h3>
<h4></h4>
<h5></h5>
<h6></h6>
```

# Capítulo 8 - Aula 01 - Semântica na HTML5 é importante
09/03/2022

Semântica é o significado e o sentido das coisas. No HTML5, tem mais valor o significado do que a forma. HTML5 é conhecido como "o HTML semântico".

- W3C - Obsolete features (HTML5)

```html
<address></address>
```

# Capítulo 8 - Aula 02 - Negrito e Itálico do jeito certo
09/03/2022

[Exercício 8](./html-css/exercicios/ex008/index.html)

CTRL + SHIFT + P - Emmet: Envelope com a abreviatura; Envelopa o texto selecionado com uma tag. "Quebrar linha com abreviação".

```html
<!-- Texto em itálico / ênfase (não semântico)-->
<i>texto</i>

<!-- Texto em itálico / ênfase (semântico) -->
<em>texto</em>

<!-- Texto em Negrito / Destaque (não semântico) -->
<b>texto</b>

<!-- Texto em Negrito / Destaque (semântico) -->
<strong>texto</strong>
```

# Capítulo 8 - Aula 03 - Formatação adicionais em HTML
09/03/2022

[Exercício 8](./html-css/exercicios/ex008/index.html)

```html
<mark>texto marcado</mark>
<small>texto pequeno</small>
<del>texto como excluído</del>
<ins>texto com inserdido</ins>
<u>sublinhado (não semântica)</u>
Texto Sobrescrito: x<sup>20</sup>+3
Texto Subscrito: H<sub>2</sub>O
```

# Capítulo 8 - Aula 04 - Citações de Códigos
11/03/2022

[Exercício 8 - B](./html-css/exercicios/ex008-b/index.html)

- code (indica que é um bloco de código);
- pre (manter pre-formatado, como foi escrito);
- blockquote (bloco de citação);
- abbr (abreviações);
- bdo (direção do texto);

TAB = Acrescenta tabulação
SHIFT + TAB = Remove uma tabulação

# Capítulo 9 - Aula 01 - Listas OL e UL
11/03/2022

[Exercício 9](./html-css/exercicios/ex009/index.html)

- ol = Ordered Lists;
- ul = Unordered Lists;

# Capítulo 9 - Aula 02 - Listas mistas e de definição
11/03/2022

Segurar ALT e clicar em lugares onde quer alterar em massa.

# Capítulo 10 - Aula 01 - Links e Âncoras em HTML5
14/03/2022

[Exercício 10](./html-css/exercicios/ex010/index.html)

- Links na web são importantes para linkar para outras páginas;
- Buscadores rankeiam melhor um site quando é referenciado por outros sites relevantes. SEO - Search Engine Optimization. 

```html
<!-- Abre em nova aba -->
<a href="linkaqui" target="_blank" rel="external"> 

```

# Capítulo 10 - Aula 02 - Links Internos
14/03/2022

```html
<!-- Vai para uma página interna indicando que é a próxima -->
<a href="./linkaqui" rel="next"></a>

<!-- Vai para uma página interna indicando que é uma página anterior. -->
<!-- prev = previous -->
<a href="./linkaqui" rel="prev"></a>

<!-- Indica que é para abrir na mesma aba-->
<a href="./linkaqui" target="_self"></a>

<!-- Indica para o mecanismo de busca que aquela página não é para ser indexada por esse link. nofollow = "não seguir" -->
<a href="https://linkaqui.com" rel="nofollow"></a>


```

# Capítulo 10 - Aula 03 - Links para download
14/03/2022

- mediatypes

# Capítulo 10 - Aula 04 - Desafios Propostos
14/03/2022

[Página de Exercícios Sugeridos](https://github.com/gustavoguanabara/html-css/tree/master/desafios)

> Fazer os exercícios propostos de acordo com os que já está apto a fazer com base no que estudou no módulo 01.

# Capítulo 11 - Aula 01 - Imagens Dinâmicas
15/03/2022
<a id="cap11-a01"></a>

[Exercício 11](html-css/exercicios/ex011/index.html)

Vários tamanhos de imagem que são carrecagados dinamicamente.

## Imagens
```
300x300 - Resolução 80x80 - Texto: "P" centralizado 150px tamanho opacidade de 50% - Fundo #fbe9d1;
700x700 - Resolução 80x80 - Texto: "M" centralizado 150px tamanho opacidade de 50% - Fundo: #f4d9c2;
1000x1000 - Resolução 80x80 - Texto: "G" centralizado 150px tamanho opacidade de 50% - Fundo: #abc7ab; 
```

# Capítulo 11 - Aula 02 - Imagens que se adaptam sozinhas
15/03/2022
<a id="cap11-a02"></a>

[Exercício 11](html-css/exercicios/ex011/index.html)

```html
<picture>
    <source media="(max-width: 750px)" srcset="./imagens/foto-p.png" type="image/png">
    <source media="(max-width: 1050px)" srcset="./imagens/foto-m.png" type="image/png">

    <!--Imagem que será carregada se nenhuma das anteriores for atendida. -->
    <img src="imagens/foto-g.png" alt="Imagem flexível">
</picture>
```

# Capítulo 11 - Aula 02 - Áudio em HTML5
15/03/2022
<a id="cap11-a03"></a>

[Exercício 11](html-css/exercicios/ex011/index.html)

Cuidado com direitos autorais nas músicas/áudios.

```html
<!-- 
Normalmente os navegadores suportam os seguintes formatos:
MP3, WAV e OGG 
-->
<audio src="midia/happy-mistake.mp3" controls loop></audio>
    <audio preload="metadata" controls>
        <source src="midia/guanacast-33.mp3" type="audio/mpeg">
        <source src="midia/guanacast-33.ogg" type="audio/ogg">

        <source src="midia/guanacast-33.wav" type="audio/wav">
        <!-- Evitar WAV por ser muito pesado para o carregamento na web -->
        
        <!-- Irá aparecer o conteúdo a seguir caso o navegador não consiga carregar nenhuma das mídias acima, dentro da tag audio. -->
        <p>Infelizmente seu navegador não consegue reproduzir áudio. <a href="midia/guanacast-33.mp3">clique aqui para baixar o arquivo MP3</a></p>
    </audio>
```

# Capítulo 11 - Aula 4 – Formatos de vídeo para seu site
15/03/2022
<a id="cap11-a04"></a>

- Handbrake para a conversão de arquivos de vídeo.
- mp4, webm, ogv
- Cuidado com custos com uso de banda do provedor. Quanto menos o tamanhos dos arquivos o quanto puder (sem comprometer tanto a qualidade), melhor.

# Capítulo 11 Aula 5 – Vídeos em hospedagem própria
15/03/2022
<a id="cap11-a03"></a>

## Exemplo

```html
<video width="500px" controls loop poster="imagens/thumb.jpeg">
    <source src="midia/meu_video.mp4" type="video/mp4">
    <source src="midia/meu_video.m4v" type="video/mp4">
    <source src="midia/meu_video.webm" type="video/webm">

    <p>Seu navegador não tem compatibilidade com reprodução de vídeos.</p>
</video>
```

# Capítulo 11 - Aula 6 – Incorporação de vídeos externos
16/03/2022

- Youtube
- Vimeo

# Capítulo 11 - Aula 7 – Desafio: um site com vídeos
17/03/2022

[Acessar desafio](https://github.com/gustavoguanabara/html-css/tree/master/desafios/modulo-01/d009)

# Capítulo 12 - Aula 1 – Estilos CSS inline
17/03/2022

Folhas de estilo em cascata

```html
<!-- Não é recomendado. Usado apenas para alterações pontuais e únicas -->
<!-- CSS é embutido na tag com o atributo "style" -->
<h1 style="background-color: white">
```

# Capítulo 12 - Aula 02 - Estilos CSS Internos
17/03/2022

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Estilos Locais / Internos</title>
    <style>
        body {
            background-color: lightsteelblue;
            font-family: Arial, Helvetica, sans-serif;
            font-size: 20px;
        }
    </style>
</head>
<body>
</body>
</html>
```

# Capítulo 13 - Aula 00 – O que vamos aprender no módulo 02?

## Capítulo 13
- Psicologia das Cores;
- Harmonização das Cores;
- Paleta de Cores;

## Capítulo 14
- Tipografia;
- Família de donte com CSS;
- Peso, estilo e shorthand font;
- Google Fontes;
- Fontes externas baixadas;
- Identificando fontes usadas em algum site e dentro de imagens;
- Alinhamento de textos com CSS;

## Capítulo 15
- ID com CSS;
- Diferença entre ID e Class;
- Pseudo-classes com CSS;

## Capitulo 16
- Modelo de Caixas;
- Modelo de Caixas na prática;
- Grouping Tags em HTML5;
- Sombra nas Caixas;
- Caixas com véstices arredondados;
- Bordas decoradas;
  
## Capítulo 17
- Criando projeto a partir do zero;
- Planejando layout;
- Transformando layout em código;
- Organizando conteúdo do site;
- Variáveis em CSS;
- Responsividade;
- Headers e Menus;
- Melhorando formato do conteúdo;
- Rodapé, conteúdo periférico e links;
- Vídeo responsivo

# Capítulo 13 - Aula 01 - Psicologia das Cores
18/03/2022

- Cores expressão certas emoções;
- A decisão de adquirir um produto está relacionada com sua apresentação visual e harmonia.

# Capítulo 13 - Aula 02 - Representando Cores com CSS3
18/03/2022

- As cores são um conjunto de combinações de vermelho, verde e azul. Red/Green/Blue (RGB).
- Representação por Hexadecimal, RGB e HSL.


# Capítulo 13 - Aula 03 - Harmonia de cores
18/03/2022

Harmonia de Cores com CSS3

## Círculo Cromático: Usado para harmonizar as cores.

- Algo cimétrico é mais bonito;
- Cor é importante;

**Cores primárias:** Amarelo, Vermelho e Azul;
**Cores secundárias:** Laranja, Violeta e Verde;
**Cores terciárias:** Misturas das cores primárias e secundárias. Amarelo-esverdeado, Amarelo-alaranjado, Vermelho-alaranjado, Vermelho-arroxeado, Azul-arroxeado, Azul-esverdeado. A primária vem primeiro no nome.

## Temperatura de Cores

**Do verde ao roxo:** Cores frias;
**Do amarelo ao vermelho-arroxeado:** Cores quentes;

## Paleta

- 3 a 5 cores na máxima;
- Conjunto de cores já harmonizadas para o projeto.

## Cores Complementares

- As cores que mais constratam entre sí.
- Normalmente cor imediatamente oposta no círculo cromática.
- 
**Exemplos:** Roxo e Amarelo, Vermelho e Verde, Azul e laranja.

## Cores Análogas

- Cores imediatamente ao lado no círculo cromático;


## Cores Análogas + uma Complementar

- Do ponto principal, cor inversa ao da principal, traçando uma reta para frente.

## Cores Análogas Relacionadas

- 2 Análogas, e a terceira cor pula uma.
**Exemplos:**
Amarelo e Amarelo-alaranjado + Laranja (pula o Amarelo-alaranjado); 
Amarelo e Amarelo-alaranjado + Verde (pula o Amarelo-esverdeado);

## Cores intercaladas

Pula 1 no circúlo cromático toda vez, a partir da cor principal escolhidas.

**Exemplo:**

Amarelo: Laranja, Vermelho, 
Amarelo-esverdeado: Azul-esverdeado, Roxo; 

## Cores Triáticas

Triângulo Equilátero
**Exemplo:** Amarelo, Azul e Vermelho;

## Cores em Quadrado

Pula duas cores

**Exemplo:** Amarelo, Vermelho-Alaranjado, Lilás, Azul-esverdeado;

## Cores Tetráticas

1 principal + 1 análoga, depois outra principal e outra análoga. (traçando um X) que vira um retângulo.

**Exemplo:**
Verde, Vermelho e Azul e Laranja.

## Monocromia

Uma cor, mudando saturação e luminosidade.

# Capítulo 13 - Aula 04 - Paleta de Cores
26/03/2022

- [Adobe Color](https://color.adobe.com/pt/);
- [Paletton](https://paletton.com);
- [Coolors](https://coolors.co);

# Capítulo 13 - Aula 05 - Como capturar cores da tela
28/03/2022

- Extensão "CollorZilla" para navegadores com base Chromium.
- No Firefox, Menu > Ferramentas > Seletor de Cores.

# Capítulo 13 - Aula 06 - Como criar degradê com CSS?
28/03/2022

# Capítulo 13 - Aula 07 - Criando um exemplo real
28/03/2022
[Exercício 16](./html-css/exercicios/ex016/color03.html)

- Juntando os conhecimentos de harmonia de cores e organização da página, para criar um design com HTML5 e CSS3.

# Capítulo 14 - Aula 01 - Primeiros passos em Tipografia
28/03/2022

## Conceitos Fundamentais

- Os livros surgiram no século 15 quando surgiu a imprensa;
- Monges copistas;
- 1450 - Johannes Gutenberg - Criou a prensa mecânica de tipos móveis. Várias peças de metal com letras, que formavam paralavras, que era jogado tinta e a prensa iria nos papeis.
- Letras mais fáceis de ler. Surgiu a Tipografia.
- Týpos = Impressão | graphía = Escrita Estudo de como são escritas as coisas, legibilidade, forma, emoção, etc.

# Capítulo 14 - Aula 02 - Anatomia do tipo
28/03/2022

## Anatomia do tipo
28/03/2022

- Serifa, Sem serifa;
- Tamanho total;
- Tamanho de fonte maiúscula e minúscula;
- Espaço entre letras;

- Letra x minúscula é o ponto de partida para criação da fonte, altura-x;
- Altura das maiúsculas;
- Ascendente (o que vazou para cima);
- Descendente (o que vazou para baixo);
- Todas as alturas é o "corpo"

Serifa é aquela linha ou prolongamento do final de cada letra, para melhorar a leitura da fonte como se criasse uma linha imaginária que o cérebro percebe para se guiar na leitura.

Uma linha na letra se chama de Haste, no caso se tiver servindo para unir duas Hastes ou arcos, se chama de Filete. Arco é a forma arredondada. O elemento que "sustenta" a letra na linha é chamado de "esporão". Vértice é uma ponta na letra, como acontece nas letras "A" e "V". Terminal é uma linha que sai de uma haste mas não se conecta a outra. Braço é um elemento que sai da haste e se conecta com outros elementos direcionado para cima, a perna é direcionada para baixo. A curva da letra "S" é chamada de "Espinha". Dois arcos ou mais juntos é chamado de "Barriga". Área interna ou "buraco" na letra é chamado de "Olho". A "Orelha" é uma parte saindo de um arco de cima e para baixo é chamado de "Cauda".

Conjunto de Glifos são chamadas de Fontes.

## Família tipográfica

São as variações de uma determinada fonte.

**Exemplo:**

- Open Sans
- Open Sans light
- Open Sans normal
- Open Sans semibold
- Open Sans bold
- Open Sans extrabold

## Categoria de Fontes

- **Serifadas:** Que tem aquela linha para facilitar a leitura, como se criassse uma linha imaginária;
- **Sans-serif:** Ou não-serifadas, que é o oposto das serifadas, sem aquele elemento;
- **Monoespaçadas:** Todos os caracteres tem o mesmo espaço;
- **Handwrite/Script:** Simula a escrita feito a mão;
- **Display:** Não tem nenhuma das características acima ou tem poucas, não se preocupam com isso, algo comemorativo ou especial para expressar algo.

# Capítulo 14 - Aula 03 - Famílias de fonte com CSS
31/03/2022

- CSS Web Safe font combination (W3Schools);
- **Declaração genérica:** sans-serif, serif, monospace, cursive, fantasy, etc (o dispositivo seleciona qualquer uma por padrão dele.)

# Capítulo 14 - Aula 04 - Tamanho de fonte e suas medidas
06/04/2022

- Segundo as recomendações do W3C

**Medidas Absolutas**
- cm (centímetro);
- mm (milímetro);
- in (polegadas); 
- px (pixels); 
- pt (pontos); 
- pc (picas/paicas)

**Medidas Relativas**
- em (medida relativa ao tamanho atual da fonte); 
- ex (relativa a altura x de uma fonte); 
- rem (medida relativa ao tamanho da fonte atual do root/body);
- vw (relativo ao tamanho da largura da tela);
- vh (ViewHight, relativo ao tamanho da altura da tela); 
- % (Porcentagem).

16px geralmente é 1em
px e em para fontes é recomendado pela W3C

# Capítulo 14 - Aula 05 - Peso, estilo e shorthand font
06/04/2022

Weight = Peso; Width: Largura; Height = Largura.
Numérica: de 100 a 900.

```css
font-family: 'Work Sans', sans-serif;
font-weight: bolder;
font-size: 3em;
font-size: italic;
```

Com shorthand:

```css
font: italic bolder 3em 'Work Sans', sans-serif;
```

# Capítulo 14 - Aula 06 - Usando Google Fonts
06/04/2022

