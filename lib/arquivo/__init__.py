from Sistema_Cadastro.lib.interface import cabecalho

def verifica_arquivo(nome_arquivo):
    """
    Verifica se o arquivo .txt existe. Se não existir, cria um novo arquivo vazio.
    """
    try:
        with open(nome_arquivo, 'r') as arquivo:
            print(f'O arquivo "{nome_arquivo}" já existe.')
    except FileNotFoundError:
        with open(nome_arquivo, 'w') as arquivo:
            print(f'Arquivo "{nome_arquivo}" criado com sucesso.')


def ler_arquivo(nome_arquivo):
    """
    Lê o conteúdo de um arquivo .txt existente.
    """
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.readlines()
        for linha in conteudo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0].ljust(30)}R${dado[1].rjust(4)}')
    except FileNotFoundError:
        print(f'O arquivo "{nome_arquivo}" não foi encontrado.')

def inserir_dados_arquivo(nome_arquivo, nome='desconhecido', salario=float):
    """
    Insere dados no arquivo .txt existente.
    """
    try:
        with open(nome_arquivo, 'a') as arquivo:
            arquivo.write(f'{nome};{salario:.2f}\n')
            print(f'Novo registro de {nome} adicionado.')
    except:
        print('Erro no cadastro!')


def deletar_dados_por_nome(nome_arquivo, nome):
    """
    Deleta dados do arquivo .txt existente com base no nome.
    """
    try:
        with open(nome_arquivo, 'r') as arquivo_leitura:
            linhas = arquivo_leitura.readlines()

        with open(nome_arquivo, 'w') as arquivo:
            for linha in linhas:
                dados = linha.strip().split(';')
                if nome not in linha:
                    arquivo.write(linha)
            print(f'Registros com o nome {nome} deletados, se existirem.')
    except Exception as e:
        print(f'Erro ao deletar dados por nome: {e}')