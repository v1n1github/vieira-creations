# Marca Vieira Creations — logo VI (master vetorial v1)

> Status: **proposta para aprovação do Vinicius**. Nome "Vieira Creations" ainda provisório.

## Conceito

**VI** = **Vi**eira + "**vi**" (de enxergar) + **VI** romano (seis).
O símbolo tem **seis peças**: três formam o **V** (dois braços + base) e três formam o **I**.
Na versão "REC", o bloco de cima do I fica laranja, como a luz de gravação de uma câmera — liga a marca à viagem câmera → lente do site.

## Arquivos (`brand/logo/`)

| Arquivo | Uso |
|---|---|
| `vi-logo-ivory-on-black.svg` | Logo completo, fundo preto (principal) |
| `vi-logo-black-on-ivory.svg` | Logo completo, fundo marfim |
| `vi-logo-rec-ivory-on-black.svg` | Logo completo com o acento laranja (assinatura, hero, vídeos) |
| `vi-logo-*-transparent.svg` | Logo completo sem fundo, para aplicar sobre fotos/vídeos |
| `vi-mark-*.svg` | Só o símbolo (6 peças), sem fundo |
| `vi-mark-rec-*.svg` | Símbolo com o acento laranja |
| `vi-mark-small-*.svg` | Símbolo simplificado (sem cortes) para tamanhos pequenos |
| `vi-icon-black.svg` / `vi-icon-ivory.svg` | Ícone quadrado: favicon, foto de perfil, ícone de app |
| `preview.png` | Prancha de visualização |

## Cores

| Nome | Hex | Papel |
|---|---|---|
| Preto | `#0B0B0B` | Fundo principal |
| Marfim | `#F4EFE6` | Símbolo, texto |
| Laranja REC | `#FF4D24` | Acento único: um bloco do I, botões de ação. Nunca em grandes áreas |

## Regras de uso

- **Tamanho mínimo:** símbolo de 6 peças a partir de 48 px de altura; abaixo disso, use `vi-mark-small` ou `vi-icon`.
- **Área de respiro:** em volta do logo, no mínimo a largura de um braço do V.
- O laranja aparece em **no máximo uma peça** do símbolo.
- Não inclinar, distorcer, trocar a fonte ou mudar as proporções.

## Geometria

- Símbolo: 624 × 400 unidades. Braços do V com 120 de largura horizontal; I com 104 (igual à espessura real do traço diagonal, para peso visual igual).
- Corte do V e espaços do I: 16 unidades, todos iguais.
- Wordmark: Montserrat Medium (OFL), maiúsculas, espaçamento 0,24 em, convertido em curvas.

Para regenerar: `python3 brand/tools/build_logo.py brand/logo <caminho para montserrat-latin-500-normal.woff>` (fonte do pacote npm `@fontsource/montserrat`). Ajustes de geometria ficam nas constantes no topo do script.
