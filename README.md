# Jumping Cube

Jogo 2D de plataforma em rolagem automática (auto-runner), feito em Python com Pygame. Um cubo é empurrado da esquerda para a direita por uma "câmera" que avança sozinha, e o jogador precisa pular na hora certa para não cair nos buracos e não encostar nos espinhos.

## Estrutura do projeto

```
.
├── main.py       # loop principal do jogo (game loop)
├── game.py       # classe Game: carrega a fase e orquestra update/draw
├── player.py     # classe Player: física, colisão e input
├── tile.py       # classes Tile e HalfTile: blocos do cenário
├── spike.py      # classe Spike: obstáculo que mata o jogador
├── setup.py      # inicialização do Pygame, constantes globais e tela
└── levels/
    └── level1.txt  # matriz da fase, uma linha de texto por linha do mapa
```

Não existe um arquivo de dependências (`requirements.txt`) no projeto atual. A única dependência externa é o `pygame`.

## Como rodar

```bash
pip install pygame
python main.py
```

O arquivo `levels/level1.txt` precisa existir relativo ao diretório de onde o `main.py` é executado, já que `game.py` abre `'levels/' + self.level + '.txt'` com caminho relativo.

## Controles

- `ESPAÇO` ou `SETA PARA CIMA`: pular (só funciona se o cubo estiver no chão)
- Fechar a janela: encerra o jogo

## Como o jogo funciona

- O `Player` tem posição, velocidade e aceleração (gravidade fixa de `3500` px/s²). A cada frame a gravidade é aplicada, a posição vertical é atualizada, e então o jogo testa colisão contra a lista de tiles e a lista de spikes.
- Quem se move de verdade é o cenário: `Tile`, `HalfTile` e `Spike` recebem `camera_speed` em `update()` e sobem a posição X deles para a esquerda. O `Player` não anda no eixo X, ele fica fixo horizontalmente; a ilusão de avanço vem do cenário deslizando.
- Colisão é feita por AABB simples (`colliding`), sem uso do sistema de sprites/rects do Pygame.
- Encostar em qualquer spike mata o jogador (`PLAYER_DEAD`), assim como colidir com um tile pela lateral ou por baixo (só a colisão vindo de cima, caindo sobre o tile, é tratada como "pousar").
- O nível termina (`COMMAND_WIN`) quando o último tile carregado já passou 200px à esquerda da posição do jogador, ou seja, quando o cenário "acabou" de passar pela tela.
- Ao morrer, `main.py` incrementa o contador `ATTEMPTS` (definido em `setup.py`) e recria a `Game` do zero, reiniciando a fase.

## Formato do arquivo de nível (`level1.txt`)

Cada linha do `.txt` é uma linha do mapa, e cada linha é uma sequência de números separados por vírgula. Cada número vira um tile de `50x50` (ou `50x25` para meio-bloco) na posição `(coluna * 50, linha * 50)`:

| Código | Significado                                  |
|--------|-----------------------------------------------|
| `0`    | vazio, nada é desenhado                        |
| `1`    | `Tile` — bloco sólido inteiro                  |
| `2`    | `HalfTile` — bloco sólido de meia altura       |
| `3`    | `Spike` virado para cima (ângulo 0)            |
| `4`    | `Spike` virado para baixo (ângulo 180)         |

Vale reparar que o ângulo do `Spike` (`self.angle`) é guardado mas não é usado em nenhum lugar do desenho (`draw` sempre desenha o mesmo triângulo apontando para cima) nem na colisão — então hoje, visualmente, spikes de código `3` e `4` são idênticos.

## Status do projeto

O projeto está em desenvolvimento. O núcleo do jogo já funciona (movimento, gravidade, colisão, spikes, câmera, vitória e derrota), mas ainda há partes em aberto ou pensadas para evoluir mais para a frente:

- Em `setup.py`, `dimensions = pygame.Vector2(SCREEN_WIDTH, SCREEN_WIDTH)` ainda não usa `SCREEN_HEIGHT` no segundo termo. Essa variável também ainda não é consumida em nenhum outro arquivo — provavelmente entra em uso em uma próxima etapa.
- `jump_cooldown_amount` está zerado por enquanto, então o cooldown de pulo ainda não está ativo de fato. É um gancho já preparado na classe `Player` para quando o balanceamento do pulo for ajustado.
- Em `player.py`, a checagem `if tile.__class__.__name__ == 'Spike'` dentro do laço de tiles é resquício de uma versão em que spikes e tiles estavam na mesma lista; hoje os spikes já têm lista própria (`self.spikes`), então esse trecho pode ser limpo numa próxima passada de refatoração.
- `Game.import_level` ainda não trata arquivo de nível ausente nem códigos de tile desconhecidos — hoje qualquer valor fora de `0,1,2,3,4` é ignorado silenciosamente. Validação e mensagens de erro são um próximo passo natural.
- A rotação do `Spike` (`self.angle`, vindo dos códigos `3` e `4` do nível) já é lida e guardada, mas o desenho e a colisão ainda não diferenciam spike voltado para cima do voltado para baixo — isso é algo a implementar.
- A tela de vitória hoje é só o texto `"FASE CONCLUÍDA!"` sobre o cenário congelado, sem transição de fase ou menu — um ponto natural para expandir quando houver mais de um nível.

## Possíveis próximos passos

- Adicionar mais níveis e uma forma de escolher/encadear fases (hoje o nome do nível está fixo como `'level1'` em `main.py`).
- Guardar recorde de tentativas ou tempo de conclusão.
- Adicionar som e um menu inicial.
- Fazer a rotação do `Spike` (`self.angle`) realmente afetar desenho e colisão, já que hoje ela é lida do arquivo de nível mas não muda nada visualmente.
