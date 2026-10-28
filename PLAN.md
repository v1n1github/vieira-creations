# Plano de desenvolvimento — Website Vieira Creations

> Documento vivo, compartilhado entre **Vinicius** (dono do projeto), **Claude** e **Codex**.
> Objetivo: alinhar o que vamos construir, como, e quem faz o quê, antes de escrever código.
> Status: **rascunho v0.1 (28/10/2026)** — aguardando respostas da seção 9.

---

## 1. Visão geral

A Vieira Creations é um studio criativo. O website deve:

1. Apresentar o studio e o seu trabalho (portfólio) com qualidade visual alta.
2. Gerar contatos e pedidos de orçamento (leads).
3. Ser rápido, responsivo (mobile first), acessível e bem posicionado no Google.
4. Ser fácil de atualizar (novos projetos, textos, imagens) sem mexer em código.

**Critério de sucesso do MVP:** site no ar com domínio próprio, portfólio com pelo menos 6 projetos, formulário de contato funcionando, Lighthouse ≥ 90 em todas as categorias.

## 2. Público-alvo (hipótese, a confirmar)

- Marcas e pequenas/médias empresas que procuram conteúdo criativo (design, vídeo, foto, IA criativa).
- Visitantes chegando principalmente por Instagram/TikTok no celular.

## 3. Escopo do MVP

### Páginas

| Página | Conteúdo | Prioridade |
|---|---|---|
| Home | Hero com vídeo/imagem de impacto, frase de posicionamento, destaques do portfólio, serviços resumidos, CTA de contato | P0 |
| Portfólio | Grade filtrável por categoria; página de detalhe por projeto (galeria, vídeo, descrição, cliente, resultado) | P0 |
| Serviços | Lista de serviços com descrição, processo de trabalho e CTA | P0 |
| Sobre | História do studio, equipe, valores | P1 |
| Contato | Formulário (nome, e-mail, empresa, tipo de projeto, orçamento estimado, mensagem), WhatsApp, redes sociais | P0 |
| Legal | Política de privacidade e cookies (UK GDPR / LGPD) | P0 |
| Blog / Novidades | Artigos e bastidores | P2 (pós-MVP) |

### Funcionalidades

- Layout responsivo, modo claro/escuro opcional.
- Vídeos otimizados (lazy loading, poster, formatos modernos).
- Formulário com proteção anti-spam e envio por e-mail.
- SEO: metadados, Open Graph, sitemap.xml, robots.txt, dados estruturados (Organization, CreativeWork).
- Analytics respeitando consentimento de cookies.
- Multi-idioma (PT / EN) — **a decidir**, ver seção 9.

### Fora do escopo do MVP

- Loja / pagamentos online.
- Área de cliente com login.
- Blog (fica para a fase 2).

## 4. Stack proposta (para discussão)

| Camada | Proposta | Alternativas | Por quê |
|---|---|---|---|
| Framework | **Next.js (App Router) + TypeScript** | Astro, SvelteKit | Ecossistema grande, ótimo para SEO e imagens; Codex e Claude dominam bem |
| Estilo | **Tailwind CSS** | CSS Modules | Rápido de iterar, consistente |
| Animações | Framer Motion | GSAP | Transições de portfólio com cara de studio |
| Conteúdo | **MDX/JSON no repositório** no MVP; CMS headless depois | Sanity, Contentful, Payload | Zero custo no início; migrar para CMS se o Vinicius quiser editar sozinho |
| Mídia | Cloudinary ou Mux (vídeo) | Vercel Blob | Vídeo pesado não deve ficar no git |
| Formulário | Route handler + Resend | Formspree | Simples e barato |
| Hospedagem | **Vercel** | Netlify, Cloudflare Pages | Deploy automático por PR com preview |
| Qualidade | ESLint, Prettier, Playwright (smoke tests), Lighthouse CI | — | Garante que nada quebre entre agentes |

> Se o Codex ou o Vinicius preferirem outra stack, registrar a decisão na seção 8.

## 5. Estrutura de repositório sugerida

```
vieira-creations/
├── AGENTS.md            # instruções para agentes (Codex, Claude)
├── PLAN.md              # este documento
├── docs/
│   └── decisions/       # ADRs curtos: 0001-stack.md, 0002-cms.md...
├── content/
│   └── projects/        # um .mdx por projeto do portfólio
├── public/              # imagens leves, favicon, og-image
└── src/
    ├── app/             # rotas: /, /portfolio, /portfolio/[slug], /servicos, /sobre, /contato
    ├── components/
    └── lib/
```

## 6. Fases e marcos

| Fase | Entregas | Estimativa |
|---|---|---|
| 0. Descoberta | Respostas da seção 9, referências visuais, logo e paleta, lista de projetos do portfólio | 2–3 dias |
| 1. Fundação | Setup Next.js + Tailwind + lint + CI + deploy de preview na Vercel; design tokens (cores, tipografia) | 1–2 dias |
| 2. Design | Wireframes da Home, Portfólio e Contato; aprovação do Vinicius | 3–5 dias |
| 3. Construção | Páginas P0, conteúdo real, formulário, SEO | 1–2 semanas |
| 4. Polimento | Animações, performance, acessibilidade (WCAG 2.1 AA), testes em celular | 3–5 dias |
| 5. Lançamento | Domínio, analytics, política de privacidade, checklist final | 1 dia |
| 6. Pós-lançamento | Blog, CMS, PT/EN, melhorias por dados | contínuo |

## 7. Como os três vão trabalhar juntos

- **Vinicius** decide: identidade visual, conteúdo, prioridades, aprovação de cada PR.
- **Claude** e **Codex** implementam via **branches + Pull Requests**; nada vai direto para `main`.
- Cada tarefa vira uma **Issue** no GitHub com critério de aceite. O agente que pegar a issue comenta "assumindo" para evitar trabalho duplicado.
- Um agente pode revisar o PR do outro; o merge final é sempre do Vinicius.
- Decisões importantes viram um arquivo curto em `docs/decisions/` e uma linha na seção 8.

**Proposta inicial de divisão (a discutir):**
- Codex: setup da fundação (fase 1) e componentes base.
- Claude: estrutura de conteúdo do portfólio, SEO, textos e revisão de acessibilidade.

## 8. Registro de decisões

| # | Data | Decisão | Quem decidiu |
|---|---|---|---|
| 1 | 28/10/2026 | Repositório `vieira-creations` no GitHub do Vinicius com este plano | Vinicius |
| 2 | — | Stack (seção 4) | pendente |

## 9. Perguntas em aberto para o Vinicius

1. **O que o studio faz exatamente?** (design gráfico, vídeo, fotografia, conteúdo com IA, branding, social media…?)
2. **Onde estão os clientes?** Reino Unido, Brasil ou ambos? Isso define idioma (PT/EN/ambos) e moeda.
3. **Já existe identidade visual?** Logo, cores, fontes. Se não, criamos junto?
4. **Referências:** 2–3 sites de que você gosta (e o que gosta neles).
5. **Portfólio:** quantos projetos temos prontos para mostrar, e em que formato (vídeos, fotos)?
6. **Domínio:** já tem (ex.: vieiracreations.com)? Onde está registrado?
7. **Contato:** o lead deve chegar por e-mail, WhatsApp, ou ambos? Quer agenda de reunião (Calendly)?
8. **Edição de conteúdo:** você quer editar textos/projetos sozinho por um painel (CMS) já no MVP?
9. **Prazo e orçamento** para hospedagem/serviços pagos.
10. **Stack:** alguma preferência ou restrição (ex.: já usar Higgsfield/Webflow/WordPress)?

## 10. Próximos passos imediatos

1. Vinicius responde a seção 9 (pode ser direto neste arquivo, numa Issue ou no chat).
2. Codex lê este plano e o `AGENTS.md` e comenta: concorda com a stack? propõe mudanças?
3. Fechamos a decisão #2 (stack) e abrimos as Issues da fase 1.
