Refatoração do trabalho feito no primeiro periodo da faculdade aplicando boas práticas aprendidas

# Jogos de Console em Python

Este repositório contém uma coleção de jogos clássicos em modo de console desenvolvidos em Python.

## Jogos Incluídos

1. **Jogo da Forca (Hangman)**
   - Permite jogar com uma palavra aleatória obtida da base de dados local (`palavras.txt`).
   - Permite que outro jogador defina uma palavra personalizada para ser adivinhada.
   - Limite de 10 tentativas para descobrir a palavra secreta.

2. **Cassino UCL (Caça-Níquel)**
   - Jogo de caça-níquel baseado no sorteio de 3 números (de 1 a 9).
   - Sistema de apostas integrado com saldo persistido.
   - Ganhe prêmios ao obter sequências ou números iguais.

## Persistência de Dados
O saldo de moedas e o dicionário de palavras do Jogo da Forca são salvos no arquivo local `palavras.txt`.

## Como Executar
Certifique-se de ter o Python 3 instalado e execute:
```bash
python TrabalhoN2.py
```
