import os
import json
from flask import Flask, render_template, request, redirect, url_for

# Cria uma instância do aplicativo Flask
app = Flask(__name__)

# Define o nome do arquivo onde as reuniões serão salvas
ARQUIVO_DADOS = 'reunioes.json'

# --- Função de Rota Principal (Página Inicial) ---
# A rota '/' corresponde à página inicial do site.
@app.route('/')
def index():
    # Renderiza o template 'index.html', que contém o formulário de agendamento.
    return render_template('index.html')

# --- Função de Rota para Processar o Formulário ---
# A rota '/agendar' é acionada quando o formulário é enviado (método POST).
@app.route('/agendar', methods=['POST'])
def agendar():
    # Pega os dados enviados pelo formulário HTML usando request.form
    nome = request.form['nome_reuniao']
    data = request.form['data_reuniao']
    horario = request.form['horario_reuniao']

    # Cria um dicionário com os dados da nova reunião
    nova_reuniao = {
        'nome': nome,
        'data': data,
        'horario': horario
    }

    # --- Lógica para salvar os dados no arquivo JSON ---
    reunioes = []
    # Verifica se o arquivo de dados já existe
    if os.path.exists(ARQUIVO_DADOS):
        # Se existir, abre o arquivo para leitura e carrega os dados existentes
        with open(ARQUIVO_DADOS, 'r') as f:
            # Tenta carregar os dados. Se o arquivo estiver vazio, inicia com uma lista vazia.
            try:
                reunioes = json.load(f)
            except json.JSONDecodeError:
                reunioes = []

    # Adiciona a nova reunião à lista de reuniões
    reunioes.append(nova_reuniao)

    # Abre o arquivo de dados em modo de escrita ('w') e salva a lista atualizada
    with open(ARQUIVO_DADOS, 'w') as f:
        # Salva a lista de reuniões no arquivo JSON com identação para melhor visualização
        json.dump(reunioes, f, indent=4)

    # --- Redirecionamento para a página de confirmação ---
    # Redireciona o usuário para a rota '/confirmacao', passando os dados da reunião
    # como parâmetros na URL (query string).
    return redirect(url_for('confirmacao',
                            nome=nova_reuniao['nome'],
                            data=nova_reuniao['data'],
                            horario=nova_reuniao['horario']))

# --- Função de Rota para a Página de Confirmação ---
# A rota '/confirmacao' recebe os dados da URL e os exibe para o usuário.
@app.route('/confirmacao')
def confirmacao():
    # Pega os dados passados na URL usando request.args
    nome = request.args.get('nome')
    data = request.args.get('data')
    horario = request.args.get('horario')
    
    # Renderiza o template 'confirmacao.html' e passa os dados para serem exibidos.
    return render_template('confirmacao.html', nome=nome, data=data, horario=horario)

# --- Inicia o Servidor Flask ---
if __name__ == '__main__':
    # O comando app.run() inicia o servidor web.
    # debug=True permite que o servidor reinicie automaticamente a cada mudança no código.
    app.run(debug=True)