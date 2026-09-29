# 📘 Atividade: Jogo da Forca em Python

## 🎯 Objetivo

Criar um jogo de adivinhação de palavras em Python usando strings, laços, condicionais e entrada de dados do usuário. Nesta atividade, o aluno pratica organização do estado do jogo, seleção aleatória de palavras e controle do fluxo da partida.

## 📝 Tarefas

### 🛠️ Configurar a palavra secreta e o estado do jogo

#### Descrição
Defina a lista de palavras possíveis e inicialize as variáveis necessárias para acompanhar o progresso do jogador durante a partida.

#### Requisitos
O programa concluído deve:

- Definir uma lista de palavras e escolher uma aleatoriamente com `random.choice()`.
- Criar variáveis para armazenar a palavra secreta, as letras chutadas, as tentativas restantes e a palavra oculta atual.
- Exibir o estado inicial do jogo com underscores para representar letras ainda não reveladas.
- Atualizar o estado do jogo após cada tentativa do jogador.

### 🛠️ Implementar o loop de chutes e as condições de vitória/derrota

#### Descrição
Construa o loop principal do jogo para que o jogador possa inserir letras até descobrir a palavra ou esgotar as tentativas permitidas.

#### Requisitos
O programa concluído deve:

- Solicitar uma letra por vez ao jogador.
- Verificar se a letra está na palavra secreta e atualizar a palavra visível conforme o resultado.
- Contar as tentativas erradas e reduzir as chances restantes.
- Exibir mensagens de feedback para acertos e erros.
- Encerrar a partida quando o jogador vencer ou perder e mostrar o resultado final.