# Sistema Bancário em Python

Este é um simples sistema bancário desenvolvido em Python. O sistema permite que os usuários realizem operações básicas como depósito, saque e visualização de extrato, além de gerenciar o cadastro de clientes.

## Funcionalidades

- **Cadastro de Cliente**: Possibilidade de cadastrar novos clientes com informações pessoais.
- **Login de Cliente**: Permite que clientes existentes façam login.
- **Depósito**: Realização de depósitos na conta do cliente.
- **Saque**: Realização de saques na conta do cliente, com limite de quantidade e valor.
- **Extrato**: Visualização do extrato bancário, mostrando todas as transações realizadas.

## Como Usar

1. **Clone o repositório**:
    ```sh
    git clone https://github.com/seu-usuario/sistema-bancario.git
    cd sistema-bancario
    ```

2. **Execute o programa**:
    ```sh
    python sistema_bancario.py
    ```

## Estrutura do Código

- **menu_opcoes**: Função para exibir o menu principal e capturar a opção escolhida pelo usuário.
- **menu_cadastro**: Função para exibir o menu de cadastro e capturar a opção escolhida pelo usuário.
- **deposito**: Função para realizar depósitos, atualizando o saldo e o extrato do cliente.
- **saque**: Função para realizar saques, respeitando os limites de quantidade e valor de saque.
- **imprimir_extrato**: Função para imprimir o extrato do cliente.
- **criar_conta**: Função para criar uma nova conta corrente.
- **cadastrar**: Função para cadastrar um novo cliente.
- **login**: Função para realizar o login de um cliente existente.

## Constantes

- **LIMITE_SAQUE**: Número máximo de saques permitidos por dia.
- **LIMITE_VALOR_SAQUE**: Valor máximo permitido por saque.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma _issue_ ou enviar um _pull request_.

1. **Fork o repositório**:
    ```sh
    git fork https://github.com/tvrocha/sistema-bancario.git
    ```

2. **Crie uma _branch_ para sua feature**:
    ```sh
    git checkout -b minha-feature
    ```

3. **Faça o _commit_ de suas alterações**:
    ```sh
    git commit -m 'Adiciona minha feature'
    ```

4. **Envie para o repositório remoto**:
    ```sh
    git push origin minha-feature
    ```

5. **Abra um _pull request_**.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

**Nota**: Este é um projeto educativo desenvolvido para fins de aprendizado. Não é recomendado para uso em produção sem devidas melhorias e validações de segurança.
