# 🧪 Aula 17 - Integração Contínua e Qualidade

---

## 🔹 1. Repositório da Atividade

| Item                | Descrição                                                         |
| ------------------- | ----------------------------------------------------------------- |
| Nome do repositório | Local-Eats-3-Qualidade-De-software                                |
| Link do repositório | https://github.com/GabrielSbruzzi/Local-Eats-3-Qualidade-De-software.git |

### 📁 Estrutura de diretórios

```
Local-Eats-3-Qualidade-De-software/
├── tests/
│   └── test_login.py
├── .github/
│   └── workflows/
│       └── quality.yml
├── login.py
└── requirements.txt
```

---

## 🔹 2. Planejamento da Funcionalidade

| Item                       | Descrição                                                                  |
| -------------------------- | -------------------------------------------------------------------------- |
| Título da Issue            | Implementar funcionalidade de login simples                                |
| Objetivo da funcionalidade | Validar usuário e senha para permitir acesso ao sistema                    |
| Link da Issue              | https://github.com/GabrielSbruzzi/Local-Eats-3-Qualidade-De-software/issues/1 |

---

## 🔹 3. Teste Automatizado

| Item                         | Descrição                                                                                       |
| ---------------------------- | ----------------------------------------------------------------------------------------------- |
| Tipo de teste                | Unitário                                                                                        |
| Objetivo do teste            | Verificar se a função login retorna verdadeiro para credenciais corretas e falso para inválidas |
| Link para o arquivo do teste | https://github.com/GabrielSbruzzi/Local-Eats-3-Qualidade-De-software/blob/4bd52a0c6b874c4e6a917079652a9f0d1b58166a/tests/test_login.py |

### 💻 Código do teste

```python
from login import login

def test_login_sucesso():
    assert login("admin", "123") == True

def test_login_falha():
    assert login("user", "errado") == False
```

---

## 🔹 4. Pipeline de Integração Contínua

| Item                             | Descrição                                                                                                 |
| -------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Nome do workflow                 | Qualidade CI                                                                                              |
| Evento que dispara a execução    | push na branch main                                                                                       |
| Link para o arquivo do workflow  | https://github.com/SEU_USUARIO/Local-Eats-3-Qualidade-De-software/blob/main/.github/workflows/quality.yml |
| Link de uma execução do workflow | https://github.com/GabrielSbruzzi/Local-Eats-3-Qualidade-De-software/actions                                 |

### ⚙️ Código do workflow

```yaml
name: Qualidade CI

on:
  push:
    branches: [ main ]

jobs:
  testes:
    runs-on: ubuntu-latest

    steps:
      - name: Baixar código
        uses: actions/checkout@v3

      - name: Configurar Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Instalar dependências
        run: pip install -r requirements.txt

      - name: Rodar testes
        run: pytest
```

---

## 🔹 5. Indicadores de Qualidade

| Indicador                       | Valor     |
| ------------------------------- | --------- |
| Quantidade de testes executados | 2         |
| Quantidade de testes aprovados  | 2         |
| Quantidade de testes com falha  | 0         |
| Status final do pipeline        | Sucesso ✅ |

---

## 🔹 6. Registro de Defeito

| Item              | Descrição                                                                  |
| ----------------- | -------------------------------------------------------------------------- |
| Título do defeito | Erro ao importar módulo login                                              |
| Severidade        | Alta                                                                       |
| Link da Issue     | https://github.com/GabrielSbruzzi/Local-Eats-3-Qualidade-De-software/issues/2 |

### 🐞 Descrição do defeito

O sistema apresentou erro ao executar os testes devido ao módulo `login` não ser encontrado.
O problema foi identificado durante a execução da pipeline no GitHub Actions.
A causa foi a estrutura incorreta do projeto e ausência do arquivo na raiz.
A correção foi mover o arquivo `login.py` para a raiz do repositório e ajustar a estrutura.

---

## 📦 Conclusão

A atividade permitiu aplicar conceitos de integração contínua, automação de testes e organização de projetos.
A pipeline foi configurada com sucesso e validou automaticamente a execução dos testes.

---
