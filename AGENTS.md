# AGENTS.md

Instruções para agentes de IA (Codex, Claude e outros) que trabalham neste repositório.

## Comece aqui

1. Leia o [`PLAN.md`](./PLAN.md) inteiro antes de qualquer alteração. Ele é a fonte da verdade sobre escopo, stack, fases e decisões.
2. Confira a seção **8. Registro de decisões** e a seção **9. Perguntas em aberto**. Não implemente nada que dependa de uma pergunta ainda sem resposta; proponha uma opção e pergunte.

## Regras de trabalho

- O dono do projeto é o **Vinicius** (`@v1n1github`). Ele aprova e faz o merge de todos os PRs.
- Nunca faça commit direto em `main`. Trabalhe em branch (`codex/<tarefa>` ou `claude/<tarefa>`) e abra um Pull Request.
- Cada PR deve referenciar uma Issue e explicar o que muda e como testar.
- Antes de começar uma Issue, comente nela que você está assumindo, para evitar trabalho duplicado com outro agente.
- Mudanças de stack, arquitetura ou escopo exigem atualizar o `PLAN.md` (seção 8) e um arquivo curto em `docs/decisions/`.
- Idioma: documentação e comunicação com o Vinicius em **português**; código, nomes de variáveis e commits em **inglês**.

## Primeira tarefa para o Codex

Leia o `PLAN.md` e abra uma Issue (ou um PR editando o `PLAN.md`) com:
- se concorda com a stack proposta na seção 4, ou o que mudaria e por quê;
- riscos ou lacunas que você vê no plano;
- como prefere dividir as tarefas da fase 1 com o Claude.

## Quando houver código

Esta seção será preenchida após a fase 1 com os comandos de setup, lint, testes e build.
