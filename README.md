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
![Processsando](https://github.com/DeyvidJLira/fiap-iadev-project-fase2/blob/main/screenshots/screenshot_1.jpg)
![Processamento finalizado](https://github.com/DeyvidJLira/fiap-iadev-project-fase2/blob/main/screenshots/screenshot_2.jpg)
![Testando outro modelo](https://github.com/DeyvidJLira/fiap-iadev-project-fase2/blob/main/screenshots/screenshot_3.jpg)

## Testes e Resultados
**Foi considerado os seguintes hiper parametros possíveis:**
```
population_sizes = [3, 5, 7]
n_generations_list = [50, 100, 150]
crossover_methods = [CrossoverMethod.OX1, CrossoverMethod.OX2, CrossoverMethod.CX]
mutation_methods = [MutateMethod.SWAP, MutateMethod.INSERTION, MutateMethod.INVERSION, MutateMethod.SHUFFLE]
mutation_probabilities = [0.05, 0.1, 0.2]
```

**Criado dois métodos para ser possível comparar**
```
# Identifica a melhor solução dados os paramêtros
def get_winner_genetic_algorithm(
        population_size: int,
        n_generations: int,
        crossover_method: CrossoverMethod,
        mutation_method: MutateMethod, 
        mutation_probability: float) -> dict:
    ...

# Monta uma tabela com o resultado de vencedores conforme diversas combinações dos hiper parametros
def grid_search_genetic_algorithm():
    ...
```

![Tabela de resultado](https://github.com/DeyvidJLira/fiap-iadev-project-fase2/blob/main/screenshots/result_table.jpg)


**Gráfico visual das melhores soluções encontradas ao longo das gerações**
![Gráfico](https://github.com/DeyvidJLira/fiap-iadev-project-fase2/blob/main/screenshots/picture_about_best_fitness_x_generation_x_crossover.png)

**Ordenando pela melhor aptidão e menor número de gerações necessários para alcançar**
![Gráfico](https://github.com/DeyvidJLira/fiap-iadev-project-fase2/blob/main/screenshots/result_table_ordered.jpg)


## Créditos
Copyright (C) by Deyvid Jaguaribe
