# Rato em Busca do Queijo

Jogo 2D simples feito em Python com Pygame para atividade acadêmica.

O objetivo é controlar um rato com as setas do teclado e encontrar o queijo.
Quando o rato encosta no queijo, ele aparece em outra posição aleatória.

## Requisitos

- Python 3.10 ou superior
- Pygame (neste projeto usamos `pygame-ce`, compatível com Python 3.14)

> Observação: o pacote clássico `pygame` ainda não possui wheel pronto para Python 3.14 no Windows.
> Por isso foi instalado o `pygame-ce`, que usa o mesmo `import pygame` e a mesma API ensinada em aula.

## Instalação

No PowerShell, dentro da pasta do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Como executar

```powershell
.\.venv\Scripts\Activate.ps1
python main.py
```

Controles: setas do teclado (cima, baixo, esquerda e direita).
Feche a janela para encerrar o jogo.

## Fontes das imagens

### Rato (`assets/rato.png`)

- Nome: Mouse / Rato em pixel art
- Autor: allen yatsura (Allen)
- Fonte: https://opengameart.org/content/mouse-0
- Licença: CC0
- Observação: o arquivo original veio em GIF; foi convertido para PNG para uso no Pygame.

### Queijo (`assets/queijo.png`)

- Nome: Pixel Platformer Food Expansion
- Autor: Kenney
- Fonte: https://kenney.nl/assets/pixel-platformer-food-expansion
- Licença: CC0 1.0 Universal
- Observação: foi utilizado um sprite individual de queijo do pacote (tile com furos), redimensionado para melhor visualização.
