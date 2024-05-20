# Sistema Bancário

Este é um simples sistema bancário em Python que permite realizar operações de depósito, saque e exibir extrato.

## Funcionalidades

- **Depósito:** Adiciona um valor ao saldo atual.
- **Saque:** Retira um valor do saldo, respeitando os limites diários e máximos de saque.
- **Extrato:** Exibe todas as transações realizadas e o saldo atual.

## Como usar

1. Clone este repositório:
   ```
   git clone <URL_DO_REPOSITORIO>
   cd <nome-do-repositorio>
   python sistema_bancario.py
   ```

2. Siga as instruções no menu para realizar as operações desejadas.

## Exemplo de uso
```
================================
   Menu - Sistema Bancário
================================

[1] - Depósito
[2] - Saque
[3] - Extrato
[0] - Sair

Entre com a opção: 1

================================
   Depósito
================================

Valor a depositar: R$ 1000.00

Depósito realizado com sucesso!
Saldo: R$1,000.00
Extrato: 
------
[DEPÓSITO] - R$1,000.00
------
```
## Limitações:
- Limite de saques diários: 3
- Valor máximo por saque: R$500,00

## Licença
Este projeto está licenciado sob a MIT License.