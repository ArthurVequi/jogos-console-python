import os
import random

ARQUIVO_DADOS = 'palavras.txt'

class GerenciadorDados:
    # Gerencia a leitura e gravação no arquivo palavras.txt
    
    @staticmethod
    def carregar_dados():
        # Retorna o saldo de moedas e a lista de palavras cadastrada
        try:
            with open(ARQUIVO_DADOS, "r") as arquivo:
                linhas = arquivo.readlines()
                if not linhas:
                    return 100, ["ABOBORA", "ABACAXI"]
                moedas = int(linhas[0].strip())
                palavras = [linha.strip() for linha in linhas[1:] if linha.strip()]
                return moedas, palavras
        except FileNotFoundError:
            return 100, ["ABOBORA", "ABACAXI"]

    @staticmethod
    def salvar_saldo(saldo):
        # Atualiza a primeira linha do arquivo com o saldo atual de moedas
        try:
            linhas = []
            try:
                with open(ARQUIVO_DADOS, "r") as arquivo:
                    linhas = arquivo.readlines()
            except FileNotFoundError:
                pass
            
            if not linhas:
                linhas = [f"{saldo}\n"]
            else:
                linhas[0] = f'{saldo}\n'
                
            with open(ARQUIVO_DADOS, "w") as arquivo:
                arquivo.writelines(linhas)
        except Exception as e:
            print(f"Erro ao salvar saldo: {e}")

class CassinoUCL:
    # Jogo de Caça-Níquel baseado em sorteio de 3 números

    def _sortear_numeros(self):
        # Retorna 3 números aleatórios entre 1 e 9
        return [random.randint(1, 9) for _ in range(3)]

    def _sequencia(self, sorteio):
        # Verifica se os três números estão em ordem sequencial (ex: 3, 4, 5)
        lst = sorted(sorteio)
        return lst[1] == lst[0] + 1 and lst[2] == lst[1] + 1

    def _iguais(self, sorteio):
        # Verifica se os três números são iguais (ex: 7, 7, 7)
        return sorteio[0] == sorteio[1] == sorteio[2]

    def jogar(self):
        # Executa o loop principal de apostas do Caça-Níquel
        print('\n\033[35mBem Vindo ao Cassino UCL!\033[m')
        saldo, _ = GerenciadorDados.carregar_dados()
        
        while saldo > 0:
            aposta_str = input(f'\nSeu saldo atual é de \033[31m{saldo}\033[m moedas!\nQuantas deseja apostar (0 ou vazio para sair): ')

            if not aposta_str or aposta_str == '0':
                print('\nVolte Sempre!')
                break

            try:
                aposta = int(aposta_str)
            except ValueError:
                print('\nValor Inválido!')
                continue

            if aposta > saldo or aposta < 0:
                print('\nSaldo insuficiente ou Inválido!')
                continue

            sorteio = self._sortear_numeros()
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'\n[{sorteio[0]}] [{sorteio[1]}] [{sorteio[2]}]')

            if self._sequencia(sorteio):
                media = sum(sorteio) // 3
                premio = (aposta * 2) + media
                saldo += premio
                print('\n\033[92mPARABÉNS, VOCÊ ACERTOU UMA SEQUÊNCIA!\033[m')
            elif self._iguais(sorteio):
                premio = aposta + sorteio[0]
                saldo += premio
                print('\n\033[92mPARABÉNS, VOCÊ ACERTOU UMA COMBINAÇÃO!\033[m')
            else:
                saldo -= aposta
                print('\n\033[31mInfelizmente nenhuma combinação foi obtida, mas não desista!\033[m')
            
            GerenciadorDados.salvar_saldo(saldo)

            if saldo <= 0:
                print('\n\033[mAparentemente você está sem saldo!')
                print('Fim de Jogo!')
                GerenciadorDados.salvar_saldo(100) # Reinicia o saldo para a próxima vez

class JogoForca:
    def _palavra_aleatoria(self, palavras):
        # Escolhe uma palavra aleatória do arquivo em maiúsculo
        if not palavras:
            return "DEFAULT"
        return random.choice(palavras).upper()

    def jogar(self, tipo):
        # Controla as tentativas, digitação e exibição da palavra oculta
        _, palavras = GerenciadorDados.carregar_dados()
        
        if tipo == 'defina':
            palavra = input('Entre com a palavra que vai ser descoberta: ').upper()
        else:
            palavra = self._palavra_aleatoria(palavras)
            
        mysL = ['_'] * len(palavra)
        erros = []
        tentativas = 10
        
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            misterio = ' '.join(mysL)
            erradas = ', '.join(erros)
            
            print('JOGO DA FORCA')
            print(f'Numero de Tentativas: {tentativas}')
            print(f'Letras Erradas: {erradas}')
            print(f'Palavra: {misterio}')
            
            escolha = input('\nEntre com uma Letra: ').upper()
            
            if len(escolha) != 1 or escolha == ' ' or not escolha.isalpha():
                continue
                
            if escolha in mysL or escolha in erros:
                continue
                
            acertou = False
            for i, letra in enumerate(palavra):
                if escolha == letra:
                    mysL[i] = escolha
                    acertou = True
                    
            if not acertou:
                tentativas -= 1
                erros.append(escolha)
                
            if tentativas <= 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'JOGO DA FORCA\nVocê Perdeu!\nA palavra era "{palavra}"')
                input('\nPressione Enter para continuar...')
                break
                
            if '_' not in mysL:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'JOGO DA FORCA\nParabéns você ganhou!\nA palavra era "{palavra}"')
                input('\nPressione Enter para continuar...')
                break

class SistemaJogos:
    # Gerencia a inicialização e transição entre os jogos do menu

    def __init__(self):
        self.forca = JogoForca()
        self.cassino = CassinoUCL()

    def iniciar(self):
        # Loop do menu principal de navegação do usuário
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            escolha = input('\033[mMENU\nEscolha o Jogo:\n1 - Jogo da Forca\n2 - Caça Níquel\n0 - Sair\n> ')
            
            if escolha == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                tipo_forca = input('MENU\nQual Forca?:\n1 - Defina a palavra\n2 - Palavra Aleatoria\n> ')
                if tipo_forca == '1':
                    self.forca.jogar('defina')
                elif tipo_forca == '2':
                    self.forca.jogar('aleatoria')
            elif escolha == '2':
                self.cassino.jogar()
                input('\nPressione Enter para voltar ao menu...')
            elif escolha == '0':
                print("Saindo...")
                break

if __name__ == "__main__":
    sistema = SistemaJogos()
    sistema.iniciar()