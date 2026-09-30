# Desafio de Automacao Digital: Gestao de Pecas, Qualidade e Armazenamento

## 1. Explicacao do Funcionamento
Este projeto consiste em um sistema desenvolvido em Python para automatizar a inspecao de qualidade e o controle de armazenamento de pecas em uma linha de montagem industrial.

O sistema recebe os dados de cada peca produzida (ID, peso, cor e comprimento) e realiza a validacao automatica segundo os seguintes criterios de qualidade:
- **Peso:** entre 95g e 105g (inclusive).
- **Cor:** azul ou verde.
- **Comprimento:** entre 10cm e 20cm (inclusive).

### Regras de Negocio e Armazenamento:
1. As pecas que atendem a todos os criterios sao classificadas como **APROVADAS** e armazenadas automaticamente em caixas com capacidade maxima de **10 pecas por caixa**.
2. Quando uma caixa atinge 10 pecas, ela e fechada automaticamente e uma nova caixa e iniciada para as proximas pecas aprovadas.
3. As pecas que falham em um ou mais criterios sao classificadas como **REPROVADAS**, nao ocupam espaco nas caixas e tem seus motivos de reprovacao registrados detalhadamente.
4. O operador conta com um menu interativo contendo 5 funcionalidades principais: cadastrar peca, listar pecas aprovadas/reprovadas, remover peca cadastrada, listar caixas fechadas e gerar relatorio consolidado.

---

## 2. Como Rodar o Programa (Passo a Passo)

### Pre-requisitos
- Ter o **Python 3** instalado no computador (versao 3.8 ou superior recomendada).

### Passo a Passo para Executar
1. Baixe ou clone este repositorio no seu computador:
   ```bash
   git clone SEU_LINK_DO_REPOSITORIO_AQUI
   ```
2. Acesse a pasta do projeto pelo terminal (Prompt de Comando, PowerShell ou Terminal):
   ```bash
   cd nome-da-pasta-do-repositorio
   ```
3. Execute o arquivo principal com o comando:
   ```bash
   python main.py
   ```
   *(Caso utilize Linux ou macOS, pode ser necessario utilizar `python3 main.py`)*.

---

## 3. Exemplos de Entradas e Saidas

### Exemplo 1: Cadastro de Peca Aprovada (Opcao 1)
**Entrada:**
```text
Escolha uma opcao: 1
Digite o ID da peca: P001
Digite o peso da peca (em gramas, ex: 100): 100
Digite a cor da peca (azul ou verde): azul
Digite o comprimento da peca (em cm, ex: 15): 15
```
**Saida:**
```text
Resultado: Peca 'P001' APROVADA.
Armazenamento: Peca alocada na Caixa 1 (1/10 pecas).
```

### Exemplo 2: Cadastro de Peca Reprovada (Opcao 1)
**Entrada:**
```text
Escolha uma opcao: 1
Digite o ID da peca: P002
Digite o peso da peca (em gramas, ex: 100): 110
Digite a cor da peca (azul ou verde): vermelha
Digite o comprimento da peca (em cm, ex: 15): 15
```
**Saida:**
```text
Resultado: Peca 'P002' REPROVADA.
Motivo(s) da reprovacao:
 - Peso fora do padrao (110.0g - exigido entre 95g e 105g)
 - Cor invalida ('vermelha' - exigido azul ou verde)
```

### Exemplo 3: Geracao do Relatorio Final (Opcao 5)
**Saida:**
```text
==================================================
        RELATORIO CONSOLIDADO DE PRODUCAO         
==================================================
Total de pecas produzidas/analisadas : 2
Total de pecas APROVADAS             : 1
Total de pecas REPROVADAS            : 1
Quantidade de caixas utilizadas      : 1
 - Caixas fechadas (10/10 pecas)     : 0
 - Caixa em aberto (1/10 pecas)      : 1

DETALHAMENTO DE REPROVACOES:
 - Peca ID 'P002':
    * Peso fora do padrao (110.0g - exigido entre 95g e 105g)
    * Cor invalida ('vermelha' - exigido azul ou verde)
==================================================
```
