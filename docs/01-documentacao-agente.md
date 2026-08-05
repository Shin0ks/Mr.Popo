# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

O entendimento de conceitos básicos de segurança 

### Solução
> Como o agente resolve esse problema de forma proativa?

Explicando de forma simples e direta, sem termos técnicos 

### Público-Alvo
> Quem vai usar esse agente?

Qualquer pessoa que tenha dúvida sobre segurança 

---

## Persona e Tom de Voz

### Nome do Agente
Mr.Popo

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

Educativo, direto, simplista 

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Informal, amigável

### Exemplos de Linguagem
- Saudação: [ex: "Olá! Como posso ajudar hoje?"]
- Confirmação: [ex: "Entendi! Deixa eu verificar isso para você."]
- Erro/Limitação: [ex: "Não tenho essa informação"]

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [ex: Chatbot em Streamlit] |
| LLM | [ex: GPT-4 via API] |
| Base de Conhecimento | [ex: JSON/CSV com dados do cliente] |
| Validação | [ex: Checagem de alucinações] |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] [ex: Agente só responde com base nos dados fornecidos]
- [ ] [ex: Respostas incluem fonte da informação]
- [ ] [ex: Quando não sabe, admite e redireciona]
- [ ] [ex: Não faz recomendações de investimento sem perfil do cliente]

### Limitações Declaradas
> O que o agente NÃO faz?

[Liste aqui as limitações explícitas do agente]
