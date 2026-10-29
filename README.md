# 📱 Sistema de Gerenciamento de Ordens de Serviço (OS)

Este é um **trabalho acadêmico** desenvolvido para fins de estudo e avaliação. Trata-se de um sistema via terminal (CLI) projetado para gerenciar o fluxo de atendimento, registro de ordens de serviço (OS) e fechamento de caixa diário para uma assistência técnica de dispositivos móveis.

## ⚙️ Funcionalidades do Sistema

O sistema possui um menu interativo que permite ao usuário realizar as seguintes operações:

- **Abertura de OS (Ordem de Serviço):**
  - Cadastro de dados do cliente (Nome, Modelo do Aparelho, Telefone).
  - Seleção do tipo de serviço (Tela, Bateria, Conector, Software).
- **Cálculo de Taxa de Urgência:** 
  - Acréscimo automático de 30% sobre o valor base do serviço (exceto para serviços de Software).
- **Simulação e Cálculo de Pagamento:**
  - Pagamento à vista (1 parcela) com 5% de desconto.
  - Pagamento em 2x ou 3x sem juros.
  - Pagamento em 4x a 6x com acréscimo de 10%.
- **Resumo da OS:**
  - Exibição de um "cupom" contendo todos os dados do cliente, valor total, quantidade e valor das parcelas.
- **Fechamento do Dia (Resumo Diário):**
  - Contabilização da quantidade total de OS registradas.
  - Cálculo do faturamento total e ticket médio (valor médio por OS).
  - Identificação da OS de maior valor.
  - Contagem de estatísticas específicas (quantidade de trocas de tela e serviços de urgência).
  - Listagem de todos os clientes atendidos no dia.

## 💻 Linguagem e Tecnologias

- **Linguagem:** Python

## 🧠 Estruturas de Dados e Tipagens Utilizadas

O código utiliza diversos conceitos fundamentais de programação:

- **Variáveis Primitivas:** Manipulação de números inteiros (`int`) para parcelas/telefones e números de ponto flutuante (`float`) implícitos para cálculos financeiros.
- **Strings (`str`):** Utilização massiva de cadeias de caracteres (`str`) para capturar textos de input do usuário (como nomes e modelo de aparelhos), formatação de mensagens no console e concatenação de textos e valores (ex: `str(valor_final)`).
- **F-Strings:** Uso de formatação de strings `f"{variavel:.2f}"` para limitar a exibição de valores monetários a duas casas decimais.
- **Listas (Arrays):** Uso da estrutura de dados lista (`clientes = []`) para armazenar e recuperar o nome de todos os clientes atendidos durante o dia.

## 🔄 Estruturas de Controle de Fluxo

O algoritmo baseia-se fortemente em estruturas de controle para guiar a lógica do usuário:

1. **Estruturas de Repetição (Laços / Loops):**
   - `while True:` Utilizado para criar o laço principal do programa (menu) e para validação de entrada de dados (garantindo que o usuário só avance se digitar opções válidas).
   - `for cliente in clientes:` Laço de iteração utilizado no encerramento do dia para percorrer a lista de clientes cadastrados e imprimi-los na tela.
2. **Estruturas Condicionais:**
   - `if`, `elif` e `else`: Utilizados para tomadas de decisão, como direcionamento de menus, aplicação de taxas, cálculo de juros/descontos baseados no número de parcelas, e identificação do maior valor de OS.
3. **Controle de Interrupção:**
   - `break`: Utilizado estrategicamente para interromper os laços `while` infinitos assim que uma entrada válida é processada com sucesso ou quando o usuário decide sair do programa.

## DESENVOLVEDOR:
** 👨‍💻Henrique fernandes**
[Github — Henriquefernandes](https://github.com/luizhenriquelopesfernandes01-lab)
