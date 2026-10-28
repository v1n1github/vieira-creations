# Plano de desenvolvimento — Website Vieira Creations

> Documento vivo, compartilhado entre **Vinicius** (dono do projeto), **Claude** e **Codex**.
> Objetivo: alinhar o que vamos construir, como, e quem faz o quê, antes de escrever código.
> Status: **rascunho v0.3 (28/10/2026)** — incorpora a revisão do Codex (Issue #1 e comentário no PR #2), a identidade VI e a divisão dos serviços em 6 peças. Itens marcados com ⚠️ aguardam o Vinicius (seção 9).

---

## 1. Visão geral

A Vieira Creations é um **estúdio de inteligência criativa**: une criação (direção, roteiro, design, edição) com tecnologia e IA para entregar marca, conteúdo, sites e automação para marcas e pequenos negócios.

O website tem dois trabalhos ao mesmo tempo:

1. **Ser a prova.** O próprio site é o case nº 1. É uma **experiência imersiva e cinematográfica**, conduzida pelo scroll, que demonstra a capacidade do estúdio enquanto o visitante navega.
2. **Converter.** Transformar visitas (principalmente do Instagram/TikTok, no celular) em conversas no WhatsApp e reuniões agendadas. A experiência nunca impede o acesso direto a "Trabalho" e "Contato".

**Critério de sucesso do lançamento:**
- Site no ar com domínio próprio.
- Viagem imersiva completa, com alternativa para movimento reduzido e sem WebGL.
- Pelo menos 4 cases com página de detalhe.
- Lead chegando por WhatsApp, formulário e agendamento, com origem (UTM).
- Performance medida em aparelhos de referência (ver seção 4.2), além do Lighthouse ≥ 90 no celular.

## 2. Marca

### 2.1 Identidade VI (registrada)

- **Nome:** Vieira Creations — ⚠️ provisório até confirmação final.
- **Símbolo VI:** **Vi**eira + "**vi**" (de enxergar) + **VI** romano (seis).
- **Seis peças:** o V tem 3 (braço esquerdo, braço direito, base) e o I tem 3 blocos.
- **Paleta:** preto `#0B0B0B`, marfim `#F4EFE6`, laranja `#FF4D24` como acento único.
- **Versão "REC":** bloco de cima do I em laranja, como a luz de gravação de uma câmera. Proposta como assinatura digital (site, redes, vídeos); a versão toda em marfim fica para usos formais.
- **Master vetorial:** `brand/` (PR #3), com logo, símbolo, versão pequena, ícones e guia de uso.
- **Pendente:** aprovação final da animação de 5 s com som.

### 2.2 V = Visão, I = Inteligência

A divisão do símbolo explica o negócio:

- **V — Visão:** o lado criativo.
- **I — Inteligência:** o lado técnico.
- Juntos: **inteligência criativa**.

## 3. Serviços — um por peça do VI

| Peça | Grupo | Serviço | Exemplos de entrega | Lançamento |
|---|---|---|---|---|
| V · braço esquerdo | Visão | **Identidade & Marca** | Logo, paleta, guia de marca, kit para redes | Complemento |
| V · braço direito | Visão | **Vídeo com IA** | Anúncios com IA, vídeos cinematográficos, séries e personagens de IA (sempre identificados como IA) | ⭐ Carro-chefe |
| V · base | Visão | **Conteúdo para Redes** | Pacote mensal de Reels/TikTok/Shorts, carrosséis, versões PT→EN | ⭐ Carro-chefe |
| I · bloco 1 | Inteligência | **Websites & Landing Pages** | Site novo, redesign, landing page de campanha | ⭐ Carro-chefe |
| I · bloco 2 | Inteligência | **Automação & Funis** | "Comente a palavra → DM → página → e-mail", agendamentos automáticos | Complemento |
| I · bloco 3 | Inteligência | **Agentes de IA** | Atendimento e qualificação de clientes 24h | Complemento |

- **Carro-chefe:** destaque no site, pacotes com preço "a partir de" e oferta de lançamento.
- **Complemento:** aparece no site com a mesma qualidade, mas é vendido junto de um carro-chefe até o estúdio ter estrutura para entregá-lo sozinho.
- ⚠️ A ordem das peças (qual serviço fica em qual posição) é uma proposta para discussão.

### 3.1 Público-alvo

- Pequenos negócios e profissionais autônomos no Reino Unido, com forte presença de profissionais brasileiros (estética, beleza, saúde, serviços), **sem se limitar a um nicho**.
- Marcas brasileiras que querem conteúdo de nível internacional.
- Muitos nunca contrataram um estúdio: o site precisa deixar claro **o que é, quanto custa (a partir de) e como começar**.

## 4. A experiência

### 4.1 A viagem pelo scroll

Narrativa (hipótese criativa, a validar no storyboard):

**VI se monta** → **câmera** → **entra pela lente** → **set / mundos de IA** → **interface de um site** → **automação conectando tudo** → **volta ao VI**.

Princípios:
- **A viagem é o menu de serviços.** Cada capítulo apresenta serviços do VI, com um ponto de leitura curto e um CTA. As 6 peças podem virar os 6 capítulos (⚠️ a definir no storyboard).
- **O logo é a navegação.** Um menu em forma de VI: cada peça é um serviço e acende em laranja ao passar o dedo ou o mouse.
- **Ritmo rápido.** Nada de vinheta lenta. Som opcional, nunca automático.
- **Atalhos sempre visíveis:** "Trabalho" e "Contato" fixos; quem não quer a viagem chega ao conteúdo em um toque.
- **Acessível:** conteúdo e navegação existem fora do canvas; alternativa completa com `prefers-reduced-motion` e sem WebGL; teclado e toque.

### 4.2 Abordagem técnica (hipótese para a prova técnica)

Comparar no spike, cena por cena:
- **Híbrida (hipótese principal):** cenas cinematográficas pré-renderizadas, produzidas pelo Vinicius no Higgsfield, controladas pelo scroll (sequência de imagens ou vídeo com scrub). 3D em tempo real só onde a interação é o ponto, como a montagem das 6 peças do VI.
- **3D em tempo real** (Three.js / React Three Fiber) na viagem inteira.

Metas propostas (a acordar, ainda não medidas): 60 fps no desktop de referência e 30 fps estáveis no celular de referência; medir peso, memória e carregamento antes de escalar a narrativa.

### 4.3 Portfólio

| # | Case | Situação |
|---|---|---|
| 1 | O próprio site da Vieira Creations (com página de bastidores) | Este repositório |
| 2 | Site de cliente piloto (estética, Londres) | Versão existente; será finalizado em paralelo |
| 3 | Vídeos/série de redes do cliente piloto | Autorizado; publicar só com a estrutura completa no ar |
| 4–6 | Projetos-conceito para marcas fictícias, um por serviço carro-chefe | Produzir nas fases 1–3; **sempre identificados como "Conceito"** |

Não inventar trabalhos, clientes ou resultados.

## 5. O que entra no lançamento e o que vem depois

### 5.1 Lançamento

- Viagem imersiva com os 6 serviços e o menu VI.
- Cases (seção 4.3).
- Pacotes com preço "a partir de" para os 3 carros-chefe.
- Contato: WhatsApp, formulário curto e agendamento.
- Política de privacidade e cookies (UK GDPR / LGPD).
- SEO base: metadados, Open Graph, sitemap, dados estruturados.
- Estrutura bilíngue preparada; ⚠️ idioma de lançamento (EN, ou EN + PT) a decidir.

### 5.2 Depois (fase 6, em ordem sugerida)

1. Versão em português (se não entrar no lançamento).
2. Agente de IA no site, que qualifica o visitante e sugere um pacote.
3. Captura de e-mail com material gratuito, ligada ao funil das redes.
4. Landing pages separadas por serviço, para anúncios.
5. Blog / "Aprenda IA".
6. Venda de infoprodutos (checkout).

Nada é cortado: só muda a ordem, para o site entrar no ar mais cedo.

## 6. Stack (proposta — decisão #2 só depois da prova técnica)

| Camada | Proposta | Observação |
|---|---|---|
| Framework | Next.js (App Router) + TypeScript | Candidato; confirmar após auditoria do site piloto e spike |
| Estilo | Tailwind CSS + design tokens da marca | |
| 3D | Three.js / React Three Fiber | Só nas cenas que exigirem interação real |
| Timeline de scroll e câmera | GSAP (ScrollTrigger) + Lenis | Motion/CSS só para interações de UI; nunca duas bibliotecas controlando a mesma propriedade |
| Transições entre páginas | View Transitions API | |
| i18n | next-intl | |
| Conteúdo | MDX/JSON no repositório | Edição via Claude/Codex; CMS só se o Vinicius quiser editar sozinho |
| Vídeo | Mux, Cloudinary ou Bunny Stream | Mídia pesada fora do git |
| Formulário | Route handler + Resend + Turnstile | Reaproveitar do site piloto se possível |
| Agendamento | Cal.com (embed) | |
| Hospedagem | Vercel | Preview por PR |
| Qualidade | ESLint, Prettier, Playwright, Lighthouse CI (mobile) | Mais medição de fps em aparelhos reais |

Verificar versões e licenças na documentação oficial antes de adotar dependências.

**Reaproveitamento do site piloto:** formulário, configuração, SEO e estrutura de conteúdo, após auditoria. Layout, composição e navegação são novos, com a identidade do estúdio. A economia de prazo só conta depois da auditoria.

## 7. Fases

| Fase | Entregas | Quem | Estimativa |
|---|---|---|---|
| 0. Inventário e decisões | Assets e cases disponíveis, auditoria do site piloto, idioma de lançamento, domínio, aprovação do logo | Vinicius + Codex/Claude | 1–2 dias |
| 1. Storyboard + animatic | Storyboard desktop/mobile dos capítulos, com pontos de leitura e CTAs; animatic com ritmo | Claude (roteiro, textos, conversão), Vinicius (aprovação e cenas no Higgsfield) | 3–4 dias |
| 2. Prova técnica | Trecho VI → câmera → lente → primeiro mundo navegável; híbrido × 3D; métricas. Em paralelo: fundação (projeto, lint, CI, preview) | Codex (spike e fundação), Claude (revisão de clareza e acessibilidade) | 5–7 dias |
| **Portão de decisão** | Decisão #2 (stack e arquitetura) registrada em `docs/decisions/` | Vinicius | — |
| 3. Construção | Viagem completa, menu VI, cases, pacotes, contato, SEO | Codex + Claude | 1,5–2 semanas |
| 4. Polimento e lançamento | Performance, movimento reduzido, alternativa sem WebGL, testes em celular, domínio, analytics | ambos | 4–5 dias |
| 5. Pós-lançamento | Itens da seção 5.2 | — | contínuo |

Meta: lançamento em cerca de 4 semanas, a confirmar depois da prova técnica e do inventário de assets.

## 8. Como os três vão trabalhar juntos

- **Vinicius** decide: identidade, conteúdo, preços, prioridades e aprovação de cada PR.
- **Claude** e **Codex** implementam via branches + Pull Requests; nada vai direto para `main`.
- Cada tarefa vira uma Issue com critério de aceite; quem assumir comenta "assumindo".
- Revisão cruzada: Claude avalia clareza, conversão e acessibilidade do que o Codex faz; Codex avalia viabilidade técnica e custo dos assets do que o Claude propõe.
- Merge final sempre do Vinicius. Decisões importantes viram arquivo em `docs/decisions/` e linha na seção 10.

## 9. Perguntas em aberto para o Vinicius

1. ⚠️ **Nome:** "Vieira Creations" é final (também para renomear a empresa)? Domínio disponível?
2. ⚠️ **Idioma de lançamento:** só inglês, ou inglês + português?
3. **Serviços:** concorda com os 6 serviços, a ordem das peças e os 3 carros-chefe?
4. **Preços "a partir de"** dos carros-chefe e oferta de lançamento.
5. **Inventário:** o que já existe pronto para mostrar (vídeos, imagens, site piloto)?
6. **Código do site piloto:** em que stack foi feito e onde está?
7. **Referências:** 2–3 sites que você admira, e o que gosta neles.
8. **Orçamento mensal** para serviços pagos (hospedagem, vídeo, e-mail).
9. **Repositório público:** tornar privado até o lançamento?

## 10. Registro de decisões

| # | Data | Decisão | Quem decidiu |
|---|---|---|---|
| 1 | 28/10/2026 | Repositório `vieira-creations` com este plano | Vinicius |
| 2 | — | Stack e arquitetura (após prova técnica) | pendente |
| 3 | — | Nome final e domínio | pendente ⚠️ |
| 4 | 28/10/2026 | Reaproveitar infraestrutura do site do cliente piloto, sem limitar o desenho | Vinicius |
| 5 | 28/10/2026 | Experiência imersiva pelo scroll é o centro do site | Vinicius (via Codex) |
| 6 | 28/10/2026 | Logo VI de 6 peças, versão 2 (marfim, blocos retos), master vetorial no PR #3 | Vinicius |
| 7 | — | 6 serviços mapeados nas 6 peças do VI (V = Visão, I = Inteligência) | proposto (v0.3) |
| 8 | — | Lançamento enxuto + fase 6 (seção 5) | proposto (v0.3) |

## 11. Próximos passos imediatos

1. Vinicius discute a v0.3 com o Codex e responde a seção 9.
2. Vinicius aprova o logo (merge do PR #3).
3. Fechamos as decisões #3, #7 e #8 e abrimos as Issues das fases 0 e 1.
