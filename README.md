# ⚔️ Defensores de OOP - Arena RPG

Este repositório contém a evolução de um projeto inicial de Programação Orientada a Objetos (OOP) em Python. O que começou como uma estrutura básica de classes no terminal foi reescrito e expandido para se tornar um simulador de batalhas de RPG completo por turnos, apresentando uma interface gráfica moderna e mecânicas avançadas de jogo.

## 🚀 O que eu desenvolvi (Minhas implementações)

Peguei a base de herança simples e apliquei os seguintes upgrades no projeto:

* **Interface Gráfica (GUI) Moderna:** Substituição das saídas de texto no terminal por uma interface visual construída com `CustomTkinter`, incluindo telas de seleção de personagens, barras de progresso dinâmicas para Vida (HP) e botões de ação iterativos.
* **Refatoração e Arquitetura Limpa:** Separação da lógica de negócios e da interface gráfica em arquivos modulares (`personagem.py`, `heroi.py`, `vilao.py`, `gui.py` e `main.py`), respeitando princípios de responsabilidade e facilitando a expansão do código.
* **Novas Mecânicas de Combate:**
  * **Sistema de Energia/Mana:** Habilidades especiais agora consomem energia, exigindo gerenciamento de recursos.
  * **Agilidade e Esquiva:** Inclusão de um status de agilidade que dá aos personagens uma chance percentual de desviar de ataques.
  * **Magia Elemental:** Adição de ataques mágicos que ignoram parcialmente a esquiva do inimigo, ao custo de alta energia.
  * **Inventário de Itens:** Uso de dicionários Python para criar um inventário de Poções de Cura e de Mana, com quantidades limitadas.
* **Inteligência Artificial (IA) Inimiga Aprimorada:** Os vilões agora possuem um "Modo Fúria" passivo, ativado quando estão com pouca vida, o que aumenta seus atributos e libera golpes de roubo de vida.
* **Expansão do Catálogo de Personagens:** Criação de classes especializadas (Guerreiro, Maga, Arqueiro, Paladino, etc.) e chefões, cada um com balanceamento próprio de atributos.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **CustomTkinter** (Biblioteca para a interface gráfica baseada no Tkinter)

## 🎮 Como executar o jogo na sua máquina

Siga os passos abaixo para testar o jogo localmente:

git clone [https://github.com/Samuel-SI/jogo-desafio.git](https://github.com/Samuel-SI/jogo-desafio.git)
Acesse a pasta do projeto:

Bash
cd jogo-desafio
Instale a dependência da Interface Gráfica:

Bash
pip install customtkinter
Inicie a Batalha:

Bash
python main.py

1. **Clone este repositório:**
   ```bash
   git clone [https://github.com/Samuel-SI/jogo-desafio.git](https://github.com/Samuel-SI/jogo-desafio.git)
