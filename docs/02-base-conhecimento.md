
# Base de Conhecimento - Mr.Popo(Assistente de Cibersegurança)

## Dados Utilizados

Abaixo estão listados os arquivos localizados no diretório `data/` que compõem a base de conhecimento do assistente:

| Arquivo | Formato | Utilização no Agente |
| :--- | :--- | :--- |
| `glossario_ciberseguranca.json` | JSON | Fornecer conceitos, definições simples e analogias do cotidiano (ex: Phishing, Vírus, MFA). |
| `politica_senhas_exemplos.csv` | CSV | Base de regras para o "Avaliador de Senhas" e exemplos de senhas fortes vs. fracos. |
| `templates_phishing.json` | JSON | Alimentar a dinâmica interativa "É Phishing ou Real?" com exemplos reais e falsos. |
| `cenarios_engenharia_social.csv` | CSV | Casos práticos e simulações de ataques baseados em personificação (ex: Falso suporte da TI). |

> **Dica:** Você pode expandir esta base utilizando frameworks como o **NIST Cybersecurity Framework** ou manuais da **OWASP**, adaptando os conceitos para uma linguagem leiga e didática.

---

## Adaptações nos Dados

Os dados técnicos foram intencionalmente traduzidos e adaptados para o contexto corporativo leigo:

- **Linguagem Descomplicada:** Remoção de jargões técnicos excessivos (ex: substituído "Ataque Man-in-the-Middle" por "Intermediário Espião").
- **Uso de Analogias:** Cada conceito técnico possui uma analogia correspondente no mundo físico (ex: *Senha = Cadeado da porta*; *MFA = Chave + Biometria*; *Firewall = Muro com Porteiro*).
- **Contextualização Corporativa:** Exemplos focados no dia a dia da empresa (e-mails corporativos, mensagens em chats internos, solicitações falsas de credenciais).

---

## Estratégia de Integração

### Como os dados são carregados?
Os arquivos JSON e CSV armazenados na pasta `data/` são lidos no início da sessão do assistente. O sistema carrega as regras de validação de senhas e os cenários de simulação em memória para consulta rápida.

### Como os dados são usados no prompt?
- **System Prompt:** Contém a persona fixa (*Guardião Digital*), diretrizes de tom (empático, paciente) e a estrutura pedagógica do treinamento.
- **Injeção Dinâmica de Contexto:** Sempre que o usuário seleciona um tópico ou aceita um desafio (ex: *"Avaliador de Senhas"* ou *"Desafio de Phishing"*), o backend busca dinamicamente o cenário/exemplo correspondente na base e insere no contexto da mensagem enviada ao modelo (LLM).

---

## Exemplo de Contexto Montado

```text
[SISTEMA - PERSONA]:
Você é o "Guardião Digital", um assistente empático e didático focado em conscientização de cibersegurança para funcionários leigos.

[BASE DE CONHECIMENTO CARREGADA - TÓPICO: PHISHING]:
- Item do Dataset: ID #04 (E-mail Falso do Suporte)
- Remetente Falso: "suporte-ti@empresa-suporte-update.com"
- Assunto: "URGENTE: Atualize sua senha do e-mail corporativo em 15 minutos ou perderá o acesso"
- Sinais de Alerta: Senso de urgência extrema, domínio do remetente desconhecido, link externo mascarado.
- Analogia Sugerida: "Carta falsa de cobrança bancária com código de barras adulterado".

[ESTADO DO USUÁRIO]:
- Nome: Ana Silva
- Módulo Atual: "Desafio É Phishing ou Real?"
- Histórico: Respondeu corretamente 1 de 2 testes anteriores.

[INSTRUÇÃO PARA A IA]:
Apresente o e-mail fictício acima para a Ana de forma amigável. Pergunte se ela considera a mensagem suspeita e peça para ela indicar o motivo da escolha.
