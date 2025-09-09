# Sistema de Reuniões

## Descrição

O **Sistema de Reuniões** é uma aplicação simples e eficaz para agendamento de reuniões. Com ele, os usuários podem facilmente criar novas reuniões, visualizar os detalhes da reunião agendada e receber uma confirmação de agendamento. Este sistema pode ser utilizado por empresas ou equipes que precisam de uma solução ágil para gerenciar compromissos e reuniões.

## Imagens

![ilustração](./img/tela.jpg)

## Funcionalidades

- **Agendamento de Reuniões**: Permite que os usuários agendem reuniões, fornecendo informações como nome da reunião, data e horário.
- **Página de Confirmação**: Após o agendamento, o sistema exibe uma página de confirmação com os detalhes da reunião.
- **Armazenamento em JSON**: As reuniões são armazenadas em um arquivo JSON, permitindo o fácil acesso e manutenção dos dados.
- **Design Responsivo**: A interface foi projetada para ser simples e acessível em dispositivos móveis e desktops.

## Como Funciona

1. **Página de Agendamento**: O usuário preenche um formulário com as informações da reunião (nome, data, horário).
2. **Confirmação**: Após o envio do formulário, o sistema exibe uma página de confirmação, mostrando os detalhes da reunião agendada.
3. **Armazenamento de Dados**: As informações da reunião são armazenadas em um arquivo JSON, que pode ser acessado posteriormente.

## Tecnologias Usadas

- **Backend**: [Flask](https://flask.palletsprojects.com/) (framework web Python)
- **Frontend**: HTML5, CSS3 (com o framework de estilo [Google Fonts](https://fonts.google.com/))
- **Armazenamento de Dados**: [JSON](https://www.json.org/json-pt.html)
- **Estilização**: [CSS](https://www.w3.org/Style/CSS/)

## Como Rodar o Projeto

### 1. Clonar o Repositório

```bash
git clone https://github.com/shakarpg/sistema_reunioes.git
````

### 2. Instalar Dependências

Para rodar o sistema, você precisa ter o Python instalado. Instale as dependências com o `pip`:

```bash
pip install -r requirements.txt
```

### 3. Rodar o Servidor

Com tudo configurado, inicie o servidor:

```bash
python app.py
```

### 4. Acessar a Aplicação

Abra o navegador e acesse a aplicação:

```bash
http://localhost:5000
```

## Como Contribuir

1. Faça um fork deste repositório.
2. Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`).
3. Realize suas modificações e faça commit (`git commit -am 'Adiciona nova funcionalidade'`).
4. Envie para o repositório remoto (`git push origin feature/nova-funcionalidade`).
5. Abra um pull request para revisão.

## Licença

Este projeto está licenciado sob a **MIT License** - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Como o Sistema Pode Ajudar

* **Gestão de Reuniões Simplificada**: Ajuda organizações a manterem o controle sobre os compromissos, sem complicações.
* **Praticidade**: Qualquer usuário pode facilmente agendar reuniões sem a necessidade de ferramentas complexas.
* **Acessibilidade**: A interface é simples e direta, acessível para pessoas com diferentes níveis de conhecimento técnico.
* **Armazenamento Simples**: O uso de JSON para armazenar dados torna o sistema fácil de manter e adaptar conforme necessário.

```
