# Tamagotchi

Um aplicativo em Python que simula um bichinho virtual Tamagotchi, usando Pygame. O jogador cuida de um bichinho, gerenciando seus atributos de fome, felicidade e saúde por meio de ações como alimentar, brincar e curar, enquanto observa animações e barras de progresso.

## Criador
- **Nome**: Leonardo de Moura Fuseti
- **Email**: mourafuseti@hotmail.com

## Funcionalidades
- **Bichinho Virtual**: Um personagem animado (círculo com olhos e boca, significativamente aumentado para alta visibilidade com raio de 160 pixels) que pisca e muda de expressão com base em seus atributos (feliz, triste, doente).
- **Atributos**:
  - Fome: Diminui com o tempo, aumentada ao alimentar.
  - Felicidade: Diminui com o tempo, aumentada ao brincar.
  - Saúde: Diminui se fome ou felicidade estiverem baixas, aumentada ao curar.
- **Ações**: Botões interativos para alimentar, brincar e curar, com efeito de hover.
- **Interface Gráfica**:
  - Bichinho no centro da tela, agora muito maior para melhor visualização.
  - Barras de atributos (fome, felicidade, saúde) à esquerda.
  - Botões abaixo do bichinho.
  - Título "Tamagotchi" no topo.
- **Fim de Jogo**: Se a saúde chegar a zero, o jogo exibe uma mensagem de fim.

## Requisitos
- Python 3.7+
- Biblioteca Python:
  - `pygame`
- Para execução no Pyodide (navegador), nenhuma biblioteca adicional é necessária além do Pygame.

## Instalação
1. Clone o repositório ou baixe o arquivo `tamagotchi.py`.
2. Instale a dependência:
   ```bash
   pip install pygame
   ```
3. Execute o script:
   ```bash
   python tamagotchi.py
   ```

## Como Usar
1. Execute o programa (`python tamagotchi.py`).
2. A interface mostra:
   - Bichinho no centro, muito maior, com animações (piscar, expressões).
   - Barras de fome, felicidade e saúde à esquerda.
   - Botões "Alimentar", "Brincar" e "Curar" abaixo do bichinho.
   - Título "Tamagotchi" no topo.
3. Clique nos botões para interagir:
   - **Alimentar**: Aumenta fome em 20.
   - **Brincar**: Aumenta felicidade em 15.
   - **Curar**: Aumenta saúde em 25.
4. Monitore os atributos:
   - Fome e felicidade diminuem com o tempo.
   - Saúde diminui se fome ou felicidade estiverem abaixo de 30.
5. Se a saúde chegar a 0, o jogo exibe "Game Over: Seu Tamagotchi morreu!".

## Notas
- **Pyodide**: O jogo funciona em navegadores com Pyodide, usando apenas Pygame.
- **Personalização**: Ajuste cores, posições ou taxas de diminuição no código para personalizar.
- **Animações**: O bichinho pisca a cada 2 segundos e muda de expressão com base nos atributos.

## Licença
Este projeto é licenciado sob a Licença MIT. Veja o arquivo [LICENSE](#) para detalhes.

---

Desenvolvido por Leonardo de Moura Fuseti (mourafuseti@hotmail.com).