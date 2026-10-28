# Plano de desenvolvimento — Website Vieira Creations

> Documento vivo, compartilhado entre **Vinicius** (dono do projeto), **Claude** e **Codex**.
> Objetivo: alinhar o que vamos construir, como, e quem faz o quê, antes de escrever código.
> Status: **rascunho v0.2 (28/10/2026)** — revisão do Claude sobre a v0.1. Pontos marcados com ⚠️ ainda precisam de confirmação do Vinicius (seção 9).

---

## 1. Visão geral

A Vieira Creations é um **estúdio de inteligência criativa**: une criação humana (direção, roteiro, edição) com ferramentas de IA para entregar sites, conteúdo e automação para marcas e pequenos negócios.

O website tem dois trabalhos ao mesmo tempo:

1. **Ser a prova.** O próprio site é o case nº 1 do estúdio. Quem visita precisa sentir, nos primeiros 5 segundos, que este estúdio faz sites e vídeos de nível premiado. Tudo o que vendemos (site, vídeo com IA, agente de IA) deve aparecer *funcionando* no site, não só descrito.
2. **Converter.** Transformar visitas (vindas principalmente de Instagram/TikTok, no celular) em conversas no WhatsApp, reuniões agendadas e e-mails capturados.

**Critério de sucesso do MVP:**
- Site no ar com domínio próprio, em **inglês e português**.
- Pelo menos **4 cases** (ver seção 3.3) com página de detalhe.
- Lead chegando por WhatsApp, formulário e agendamento, com rastreamento de origem (UTM).
- Lighthouse ≥ 90 em todas as categorias **no celular**, mesmo com vídeo no hero (meta: 95+).

## 2. Serviços e público

### 2.1 O que o estúdio vende

| Linha de serviço | Exemplos de entrega |
|---|---|
| **Websites & landing pages** | Site novo, redesign de site existente, landing page de campanha, páginas de venda de infoproduto |
| **Edição de vídeo para redes** | Pacote mensal de Reels/TikTok/Shorts, carrosséis, versões PT→EN de vídeos existentes |
| **Vídeo e séries com IA** | Anúncios com IA, vídeos cinematográficos, personagens de IA (sempre identificados como IA), séries para redes |
| **Automação & agentes de IA** | Funil "comente a palavra → DM → landing page → e-mail", chatbots de atendimento/qualificação, automações de agenda |

### 2.2 Público-alvo

- **Pequenos negócios e profissionais autônomos no Reino Unido** — com forte presença de profissionais brasileiros (estética, beleza, saúde, serviços), mas **sem se limitar a um nicho**.
- Marcas brasileiras que querem conteúdo de nível internacional.
- Chegam pelo celular, via Instagram/TikTok/indicação. Muitos nunca contrataram um estúdio antes: o site precisa ser direto sobre **o que é, quanto custa (a partir de) e como começar**.

## 3. Escopo do MVP

### 3.1 Páginas

| Página | Conteúdo | Prioridade |
|---|---|---|
| **Home** | Hero com filme curto feito pelo estúdio (Higgsfield), frase de posicionamento, slider "antes/depois" (vídeo cru de celular → versão final com IA), cases em destaque, 4 linhas de serviço, prova social, CTA WhatsApp/agendar | P0 |
| **Trabalho (cases)** | Grade filtrável por linha de serviço; página de detalhe por case: desafio → solução → resultado, galeria/vídeo, ferramentas usadas | P0 |
| **Serviços** | Uma landing page por linha de serviço (4), cada uma com processo, entregáveis, **preço "a partir de"**, FAQ e CTA. Servem também como destino de anúncios | P0 |
| **Pacotes** | Comparação simples dos pacotes mensais (ex.: edição para redes) com oferta de lançamento | P0 |
| **Contato / Começar um projeto** | Formulário curto em etapas (tipo de projeto → orçamento → contato), botão WhatsApp, agendamento (Cal.com/Calendly) | P0 |
| **Sobre** | História do estúdio, como trabalhamos com IA de forma responsável, quem está por trás | P1 |
| **Legal** | Política de privacidade e cookies (UK GDPR / LGPD), termos | P0 |
| **Blog / Aprenda IA** | Artigos e bastidores; base para o futuro infoproduto do estúdio | P2 (pós-MVP) |

### 3.2 O "fator uau" (o que torna o site excepcional)

1. **Hero em vídeo cinematográfico** produzido pelo estúdio, otimizado (poster, AV1/H.264, streaming adaptativo), sem derrubar a nota de performance.
2. **Transições entre páginas conectadas** (o elemento clicado "voa" para a próxima página) com View Transitions API + GSAP, e rolagem suave.
3. **Slider antes/depois** de vídeo: demonstra o serviço de IA em segundos.
4. **Agente de IA no site** que conversa com o visitante, entende a necessidade, sugere um pacote e passa o lead qualificado para o WhatsApp/e-mail — é ao mesmo tempo atendimento e demonstração ao vivo do serviço de agentes.
5. **Performance como argumento de venda:** página "como este site foi feito" mostrando as notas do Lighthouse.
6. Acessibilidade de verdade: tudo funciona sem animação (`prefers-reduced-motion`) e por teclado.

### 3.3 Portfólio — estratégia para não depender de clientes antigos

O estúdio está começando, então a meta de "6 projetos prontos" da v0.1 é o maior risco do plano. Proposta:

| # | Case | Situação |
|---|---|---|
| 1 | **O próprio site da Vieira Creations** (com página de bastidores) | Construído neste repositório |
| 2 | **Site de cliente piloto (estética, Londres)** — redesign com transições e funil de infoproduto | Já existe uma versão; será finalizado em paralelo |
| 3 | **Vídeos/série de redes sociais do cliente piloto** | Autorização obtida; publicar só quando a estrutura completa estiver no ar |
| 4–6 | **Projetos-conceito** para marcas fictícias (ex.: marca de produto de luxo, restaurante, app), cada um mostrando uma linha de serviço | Produzir na fase 2–3; **sempre identificados como "Conceito"** |

Projetos-conceito são prática comum em estúdios novos e são honestos desde que rotulados.

### 3.4 Funcionalidades

- Mobile first, tema escuro como padrão (combina com vídeo), claro opcional.
- **Bilíngue desde o início (EN padrão + PT)** com rotas `/en` e `/pt`, `hreflang` e textos separados — adicionar idioma depois dá muito retrabalho.
- Vídeos fora do git, servidos por plataforma de vídeo (lazy loading, poster, formatos modernos).
- Formulário com anti-spam (Turnstile) e envio por e-mail; lead também gravado (planilha/DB simples) com UTM de origem.
- Captura de e-mail com isca (ex.: guia gratuito) para alimentar o funil das redes sociais.
- SEO: metadados, Open Graph por página, sitemap.xml, robots.txt, dados estruturados (Organization, LocalBusiness, Service, CreativeWork, FAQPage).
- Analytics respeitando consentimento de cookies (Plausible ou GA4 com banner).

### 3.5 Fora do escopo do MVP

- Loja / pagamento online (a venda de infoprodutos fica para a fase 6).
- Área de cliente com login.
- Blog (fase 2).

## 4. Stack proposta (para discussão)

| Camada | Proposta | Alternativas | Por quê |
|---|---|---|---|
| Framework | **Next.js (App Router) + TypeScript** | Astro | Ecossistema grande, ótimo para SEO, imagens e rotas de API (agente, formulário); Codex e Claude dominam bem |
| Estilo | **Tailwind CSS** + design tokens | CSS Modules | Rápido de iterar, consistente |
| Animações | **GSAP (ScrollTrigger) + Lenis + View Transitions API** | Framer Motion | GSAP é o padrão de sites premiados e hoje é gratuito, incluindo plugins; dá controle fino de timeline para transições cinematográficas |
| i18n | `next-intl` | — | Rotas por idioma e mensagens tipadas |
| Conteúdo | **MDX/JSON no repositório** no MVP | Sanity, Payload | Zero custo; o Claude/Codex editam a pedido do Vinicius. CMS só se ele quiser editar sozinho |
| Vídeo | **Mux** ou Cloudinary | Bunny Stream | Streaming adaptativo, poster automático; vídeo pesado não fica no git |
| Formulário / e-mail | Route handler + Resend + Turnstile | Formspree | Simples e barato |
| Agente de IA | Route handler chamando a API do Claude, com prompt fixo sobre serviços e pacotes, limite de uso | — | Demonstra o serviço de agentes; custo controlado |
| Agendamento | Cal.com (embed) | Calendly | Gratuito, bonito, embutível |
| Hospedagem | **Vercel** | Netlify, Cloudflare Pages | Deploy automático por PR com preview |
| Qualidade | ESLint, Prettier, Playwright (smoke tests), Lighthouse CI (mobile) | — | Garante que nada quebre entre agentes |

> A stack final depende também da auditoria do site do cliente piloto (seção 6): se ele já usa uma stack sólida, vale adotá-la para reaproveitar mais.
> Se o Codex ou o Vinicius preferirem outra stack, registrar a decisão na seção 8.

## 5. Estrutura de repositório sugerida

```
vieira-creations/
├── AGENTS.md            # instruções para agentes (Codex, Claude)
├── PLAN.md              # este documento
├── docs/
│   └── decisions/       # ADRs curtos: 0001-stack.md, 0002-i18n.md...
├── content/
│   ├── cases/           # um .mdx por case, com versões en/pt
│   └── services/        # um .mdx por linha de serviço
├── messages/            # textos de interface: en.json, pt.json
├── public/              # imagens leves, favicon, og-image
└── src/
    ├── app/[locale]/    # rotas: /, /work, /work/[slug], /services/[slug], /pricing, /about, /contact
    ├── components/
    └── lib/
```

## 6. Fases e marcos

O prazo da v0.1 (4–6 semanas) é longo para um estúdio que precisa começar a gerar clientes. Proposta mais curta, com o site do cliente piloto avançando em paralelo.

**Atalho decidido pelo Vinicius:** o site da Vieira Creations será construído **reaproveitando a estrutura do site do cliente piloto** (componentes, layout, formulário, SEO, configuração) no que for possível. O visual e a identidade serão próprios do estúdio. Isso também cria uma **base reutilizável** para os próximos sites de clientes — cada projeto deixa o seguinte mais rápido.

| Fase | Entregas | Estimativa |
|---|---|---|
| 0. Descoberta | Auditoria do código do site do cliente piloto (stack, o que reaproveitar, o que refazer), respostas da seção 9, nome/domínio confirmados, 3 referências visuais, paleta e tipografia | 1–2 dias |
| 1. Fundação | Importar a estrutura reaproveitável do site do cliente piloto; Next.js + Tailwind + i18n + lint + CI + preview na Vercel; design tokens; layout base com transições | 2 dias |
| 2. Home + Contato | Home completa (hero de vídeo pode começar com placeholder), contato com WhatsApp e agendamento — **já dá para divulgar** | 4–5 dias |
| 3. Serviços + Cases | 4 landing pages de serviço, página de pacotes, cases 1–2, primeiro projeto-conceito | 1 semana |
| 4. Uau + Polimento | Agente de IA, slider antes/depois, vídeo final do hero, performance, acessibilidade (WCAG 2.1 AA), testes em celular | 4–5 dias |
| 5. Lançamento | Domínio, analytics, política de privacidade, checklist final | 1 dia |
| 6. Pós-lançamento | Blog, mais cases, infoproduto/checkout, CMS se necessário, melhorias por dados | contínuo |

## 7. Como os três vão trabalhar juntos

- **Vinicius** decide: identidade visual, conteúdo, preços, prioridades, aprovação de cada PR.
- **Claude** e **Codex** implementam via **branches + Pull Requests**; nada vai direto para `main`.
- Cada tarefa vira uma **Issue** no GitHub com critério de aceite. O agente que pegar a issue comenta "assumindo" para evitar trabalho duplicado.
- Um agente pode revisar o PR do outro; o merge final é sempre do Vinicius.
- Decisões importantes viram um arquivo curto em `docs/decisions/` e uma linha na seção 8.

**Proposta de divisão (a discutir):**
- **Codex:** fundação (fase 1), componentes base, CI e deploy.
- **Claude:** sistema de animação/transições, textos EN/PT e SEO, estrutura de conteúdo dos cases e serviços, agente de IA, revisão de acessibilidade e performance.

## 8. Registro de decisões

| # | Data | Decisão | Quem decidiu |
|---|---|---|---|
| 1 | 28/10/2026 | Repositório `vieira-creations` no GitHub do Vinicius com este plano | Vinicius |
| 2 | — | Stack (seção 4) | pendente |
| 3 | — | Nome final do estúdio e domínio | pendente ⚠️ |
| 4 | — | Bilíngue EN/PT no MVP | proposto (v0.2) |
| 5 | 28/10/2026 | Reaproveitar a estrutura do site do cliente piloto para acelerar o site do estúdio | Vinicius |

## 9. Perguntas em aberto para o Vinicius

Já respondidas (v0.2, a partir das conversas com o Vinicius — confirmar):

- ✅ **O que o estúdio faz:** sites e landing pages, edição de vídeo para redes, vídeo e séries com IA, automação e agentes de IA.
- ✅ **Onde estão os clientes:** Reino Unido (muitos brasileiros) e Brasil → site em EN e PT, preços em £.
- ✅ **Contato:** WhatsApp como canal principal, mais formulário e agendamento.
- ✅ **Edição de conteúdo:** no MVP, por pedido ao Claude/Codex; CMS só depois.

Ainda em aberto:

1. ⚠️ **Nome:** "Vieira Creations" é o nome final do estúdio (e da empresa a ser renomeada)? O domínio está disponível/registrado?
2. **Identidade visual:** já existe logo, cores, fontes? Se não, criamos na fase 0.
3. **Referências:** 2–3 sites de que você gosta (e o que gosta neles).
4. **Preços "a partir de"** que podem aparecer no site para cada linha de serviço, e qual a oferta de lançamento.
5. **Agente de IA no site:** ok ter um custo pequeno e variável de API por conversa?
6. **Orçamento mensal** para serviços pagos (hospedagem, vídeo, e-mail).
7. **Código do site do cliente piloto:** em que stack ele foi feito e onde está (pasta no Mac / outro repositório)? Precisamos dele no repo (ou acessível) para a auditoria da fase 0. Se a stack for diferente de Next.js, decidimos se migramos ou se adotamos a stack dele.
8. **Privacidade do repositório:** o repo está **público**. Como você ainda não quer divulgar o estúdio, sugerimos torná-lo privado até o lançamento.

## 10. Próximos passos imediatos

1. Vinicius revisa este PR e responde a seção 9 (no arquivo, numa Issue ou no chat).
2. Codex lê o plano e o `AGENTS.md` e comenta: concorda com a stack? propõe mudanças?
3. Fechamos as decisões #2 e #3 e abrimos as Issues da fase 1.
