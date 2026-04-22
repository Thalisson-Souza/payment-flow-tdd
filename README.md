# Payment Flow TDD

Implementação feita com **TDD (Test-Driven Development)** com Python, que refere a um fluxo de pagamentos.

## Problema
Dado um valor de pagamento, saldo disponível e método de pagamento (`pix`, `crédito`, `débito`),
o sistema deve validar entradas, garantir que o valor seja numérico e maior que zero (não podendo ser zero ou negativo), aplicar taxa de 5% em pagamentos no crédito e impedir processamento
em cenários inválidos (ex.: saldo insuficiente, valor inválido, método de pagamento não suportado).
Quando os dados forem válidos e houver saldo suficiente, o pagamento deve ser processado.


## Objetivo 

Entender o ciclo **Red -> Green -> Refactor** aplicando TDD em regras de negócio necessárias para processamento de pagamentos, com foco em:
- validação de dados de entrada
- proteção de cenários inválidos (edge-cases)
- assegurar comportamento conforme as implementações
- clareza e estruturação das regras de negócio antes das implementações

## Regras de negócios do fluxo
- O valor do pagamento deve ser numérico (`int` ou `float`).
- O saldo disponível deve ser numérico (`int` ou `float`).
- O valor do pagamento deve ser maior que zero.
- Métodos aceitos: `pix`, `crédito`, `débito`.
- Pagamento não pode ser processado com saldo insuficiente.
- Pagamentos em `crédito` recebem taxa de 5%.
- Pagamentos em `pix` e `débito` não possuem taxa.

## Tecnologias

- Python 3.12.3
- `unittest`


## Executar os testes

1. Clone o repositório
```bash
    git clone https://github.com/Thalisson-Souza/payment-flow-tdd
```
2. Entre na pasta do projeto
```bash
    cd payment-flow-tdd
```
3. Execute os testes
```bash
    python3 -m unittest -v
```