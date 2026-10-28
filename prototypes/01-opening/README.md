# Protótipo 01 — Abertura (VI → REC → câmera → lente)

Protótipo de direção, não código de produção. Arquivo único (HTML + CSS + JS, sem dependências além de Google Fonts).

**O que demonstra (storyboard v0.2, capítulos 01–03):**
- Primeiro estado utilizável: VI montado, título, menu dos 6 serviços, atalhos Services/Work/Contact.
- Passar o mouse/foco num serviço acende a peça correspondente do VI.
- Scroll: peças se separam em profundidade → bloco REC acende → VI encolhe e vira a luz de gravação (tally) → câmera se desenha → push-in na lente → "Every story starts with a look."
- HUD de visor com timecode a 24 fps enquanto "grava".
- `prefers-reduced-motion`: sem viagem fixada; hero estático.

**Para o Codex:** a geometria do VI é a mesma de `brand/tools/build_logo.py`. A câmera é desenho de linha provisório; na versão final entram as cenas pré-renderizadas (Higgsfield) da hipótese híbrida. Distribuição do scroll e timings ficam no `render(p)`.

Para abrir: basta abrir `index.html` no navegador.
