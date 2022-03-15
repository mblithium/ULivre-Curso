# Desenvolvimento Web

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

Vários tamanhos de imagem que são carrecagados dinamicamente.

## Imagens
300x300 - Resolução 80x80 - Texto: "P" centralizado 150px tamanho opacidade de 50% - Fundo #fbe9d1;
700x700 - Resolução 80x80 - Texto: "M" centralizado 150px tamanho opacidade de 50% - Fundo: #f4d9c2;
1000x1000 - Resolução 80x80 - Texto: "G" centralizado 150px tamanho opacidade de 50% - Fundo: #abc7ab; 

# Capítulo 11 - Aula 02 - Imagens que se adaptam sozinhas

```html
<picture>
    <source media="(max-width: 750px)" srcset="./imagens/foto-p.png" type="image/png">
    <source media="(max-width: 1050px)" srcset="./imagens/foto-m.png" type="image/png">

    <!--Imagem que será carregada se nenhuma das anteriores for atendida. -->
    <img src="imagens/foto-g.png" alt="Imagem flexível">
</picture>
```

# Capítulo 11 - Áudio em HTML5

Cuidado com direitos autorais nas músicas/áudios.

