# Introdução
Projeto destinado ao **Desafio da Fase 2*** do curso de pós graduação "AI para devs" na FIAP.

[Documentação do código fonte](https://github.com/DeyvidJLira/fiap-iadev-project-fase2/wiki/Documenta%C3%A7%C3%A3o)

## Desafio 
O desafio consiste em projetar, implementar e testar um sistema que  utilize Algoritmos Genéticos para otimizar uma função ou resolver um problema complexo de otimização. Você pode escolher problemas como otimização de rotas, alocação de recursos e design de redes neurais. 

## Problema a ser resolvido
Uma empresa de turismo deseja fornecer para os clientes um roteiro que esteja de acordo com o orçamento que eles possuem para viajar. Este roteiro deve ser o mais agradável possível para o cliente, se baseando na pontuação daquele evento e que tenha o menor deslocamento de um evento para outro. 

Existe alguns requisitos que precisam serem atendidos:
- O roteiro não pode ter um destino repetido;
- Quanto menor a distância total pecorrida do roteiro, melhor;
- O custo total do roteiro a ser proposto tem que estar abaixo do orçamento do cliente;
- Quando maior o total de pontuação dos eventos juntos, melhor.

## Screenshots
![Processsando](https://github.com/DeyvidJLira/fiap-iadev-project-fase2/blob/main/static/images/screenshot_1.jpg)
![Processamento finalizado](https://github.com/DeyvidJLira/fiap-iadev-project-fase2/blob/main/static/images/screenshot_2.jpg)
![Testando outro modelo](https://github.com/DeyvidJLira/fiap-iadev-project-fase2/blob/main/static/images/screenshot_3.jpg)

## Como estar organizado
O projeto é formado pelas seguintes pastas e arquivos, com os respectivos propósitos:
- /static/images - pasta com todos arquivos de imagens que serão exibidas na execução da aplicação;
- app.py - contém o código da aplicação em si;
- attraction.py - é o modelo da atração;
- draw_functions.py - reúne as funções de desenhar algum tipo de conteúdo na tela;
- main.py - ponto de partida para execução do projeto;
- setup.py - contém várias constantes utilizadas no projeto;
- util.py - contém algumas funções utilitárias, como por exemplo converter geolocalização para pixel.

## Testes e Resultados
Em breve...

## Créditos
Copyright (C) by Deyvid Jaguaribe
