# 🤝 Guia de Contribuição

Obrigado por considerar contribuir com o Vuln-Labs! 🎉

Este documento fornece diretrizes para contribuir com o projeto. Seguir estas diretrizes ajuda a comunicar que você respeita o tempo dos desenvolvedores que gerenciam e desenvolvem este projeto open source.

---

## 📋 Índice

- [Código de Conduta](#código-de-conduta)
- [Como Posso Contribuir?](#como-posso-contribuir)
- [Diretrizes de Desenvolvimento](#diretrizes-de-desenvolvimento)
- [Processo de Pull Request](#processo-de-pull-request)
- [Convenções de Código](#convenções-de-código)
- [Reportando Bugs](#reportando-bugs)
- [Sugerindo Melhorias](#sugerindo-melhorias)

---

## 📜 Código de Conduta

Este projeto adere a um Código de Conduta. Ao participar, espera-se que você mantenha este código.

### Nossos Padrões

**Comportamentos aceitáveis:**
- ✅ Usar linguagem acolhedora e inclusiva
- ✅ Respeitar pontos de vista e experiências diferentes
- ✅ Aceitar críticas construtivas com elegância
- ✅ Focar no que é melhor para a comunidade
- ✅ Mostrar empatia com outros membros

**Comportamentos inaceitáveis:**
- ❌ Uso de linguagem ou imagens sexualizadas
- ❌ Trolling, comentários insultuosos ou depreciativos
- ❌ Assédio público ou privado
- ❌ Publicar informações privadas de outros sem permissão
- ❌ Conduta não profissional ou inadequada

---

## 🚀 Como Posso Contribuir?

### 1. Reportar Bugs 🐛

Bugs são rastreados como [GitHub Issues](https://github.com/dny8888/vuln-labs/issues). Antes de criar um bug report:

- **Verifique se já não existe** uma issue sobre o problema
- **Use a busca** para ver se alguém já reportou
- Se encontrar uma issue similar, adicione um 👍 ou comente

**Ao criar um bug report, inclua:**
- Título claro e descritivo
- Passos exatos para reproduzir o problema
- Comportamento esperado vs comportamento atual
- Screenshots (se aplicável)
- Versões: Docker, Docker Compose, SO
- Logs relevantes

### 2. Sugerir Melhorias 💡

Melhorias também são rastreadas como Issues. Ao sugerir:

- Use título claro descrevendo a melhoria
- Explique **por que** isso seria útil
- Forneça exemplos de uso
- Mencione se você pode implementar

### 3. Contribuir com Código 💻

#### Áreas que Precisam de Ajuda

Procure issues com as labels:
- `good first issue` - Bom para iniciantes
- `help wanted` - Ajuda externa bem-vinda
- `documentation` - Melhorias em docs
- `enhancement` - Novas features

#### Tipos de Contribuição Bem-vindas

- 📝 **Documentação**: Corrigir typos, adicionar exemplos, melhorar clareza
- 🐛 **Bug Fixes**: Corrigir problemas existentes
- ✨ **Features**: Adicionar novos serviços vulneráveis, desafios CTF
- 🧪 **Testes**: Adicionar validação automatizada
- 🤖 **Automação**: Scripts de setup, análise, etc.
- 🎨 **Design**: Diagramas, badges, screenshots
- 🌐 **Tradução**: Documentação em outros idiomas

---

## 🛠️ Diretrizes de Desenvolvimento

### Setup do Ambiente de Desenvolvimento

```bash
# 1. Fork o repositório
# 2. Clone seu fork
git clone https://github.com/seu-usuario/vuln-labs.git
cd docker-lab

# 3. Adicione o upstream remote
git remote add upstream https://github.com/dny8888/vuln-labs.git

# 4. Crie uma branch para sua feature
git checkout -b feature/minha-feature

# 5. Faça suas alterações
# 6. Teste localmente
docker compose up -d --build
docker exec -it lab_attacker bash
# ... testar funcionalidade

# 7. Commit suas mudanças
git add .
git commit -m "feat: adiciona nova vulnerabilidade XSS"

# 8. Push para seu fork
git push origin feature/minha-feature

# 9. Abra um Pull Request
```

### Mantendo seu Fork Atualizado

```bash
# Buscar mudanças do upstream
git fetch upstream

# Merge com sua branch main
git checkout main
git merge upstream/main

# Push para seu fork
git push origin main
```

---

## 📤 Processo de Pull Request

### Checklist Antes de Submeter

- [ ] Código segue as [convenções do projeto](#convenções-de-código)
- [ ] Documentação foi atualizada (se necessário)
- [ ] Testei localmente e tudo funciona
- [ ] Commits seguem o padrão [Conventional Commits](#mensagens-de-commit)
- [ ] Adicionei meu nome ao [CONTRIBUTORS.md](CONTRIBUTORS.md) (se primeira contribuição)

### Template de Pull Request

```markdown
## Descrição
Breve descrição das mudanças

## Tipo de Mudança
- [ ] Bug fix (non-breaking change)
- [ ] Nova feature (non-breaking change)
- [ ] Breaking change (fix ou feature que quebraria funcionalidade existente)
- [ ] Documentação

## Motivação e Contexto
Por que essa mudança é necessária? Qual problema resolve?

## Como Foi Testado?
Descreva os testes realizados

## Screenshots (se aplicável)
Adicione screenshots das mudanças

## Checklist
- [ ] Meu código segue o style guide do projeto
- [ ] Realizei self-review do código
- [ ] Comentei código complexo
- [ ] Atualizei a documentação
- [ ] Minhas mudanças não geram novos warnings
- [ ] Testei localmente e funciona
```

### Processo de Review

1. **Submeta o PR** com descrição clara
2. **Aguarde review** (normalmente 2-5 dias)
3. **Responda a comentários** construtivamente
4. **Faça alterações** se solicitadas
5. **Aguarde aprovação** de pelo menos 1 maintainer
6. **Merge** será feito por um maintainer

---

## 📝 Convenções de Código

### Estrutura de Diretórios

```
docker-lab/
├── docs/              # Documentação
├── scripts/           # Scripts de automação
├── attacker/          # Dockerfile do atacante
├── vuln_service/      # Serviço vulnerável customizado
├── [service_name]/    # Outros serviços
└── docker-compose.yaml
```

### Docker Compose

```yaml
services:
  nome_servico:
    image: imagem:tag  # Sempre especifique tags
    container_name: lab_nome  # Prefixo "lab_"
    networks:
      labnet:
        ipv4_address: 10.89.0.X  # IPs sequenciais
    # Sempre adicione comentários explicativos
    environment:
      - VAR=valor  # Explicar se não for óbvio
```

### Python (Scripts)

```python
#!/usr/bin/env python3
"""
Docstring descrevendo o propósito do script
"""
import os
import sys

# Constantes em UPPER_CASE
DEFAULT_PORT = 9999

# Funções com docstrings
def minha_funcao(parametro):
    """Descrição da função.
    
    Args:
        parametro (str): Descrição do parâmetro
        
    Returns:
        bool: Descrição do retorno
    """
    pass

# Sempre incluir main guard
if __name__ == "__main__":
    main()
```

### Bash (Scripts)

```bash
#!/bin/bash
###############################################################################
# Script Name: script.sh
# Description: Breve descrição
# Usage: ./script.sh [args]
###############################################################################

set -euo pipefail  # Exit on error, undefined vars, pipe failures

# Constantes em UPPER_CASE
readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Funções com comentários
function setup() {
    # Descrição do que a função faz
    echo "[+] Setting up..."
}

# Main
main() {
    setup
}

main "$@"
```

### Markdown (Documentação)

- Use headers hierárquicos (# ## ### ####)
- Adicione índice para docs longos
- Use blocos de código com syntax highlighting
- Inclua exemplos práticos
- Use emojis com moderação para melhorar legibilidade

### Mensagens de Commit

Seguimos [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: Nova feature
- `fix`: Bug fix
- `docs`: Apenas documentação
- `style`: Formatação (não afeta código)
- `refactor`: Refatoração de código
- `test`: Adicionar testes
- `chore`: Manutenção (build, deps)

**Exemplos:**

```bash
feat(vuln): adiciona vulnerabilidade SQL injection
fix(docker): corrige problema de DNS resolution
docs(readme): atualiza instruções de instalação
chore(deps): atualiza imagem do Kali Linux
```

---

## 🐛 Reportando Bugs

### Antes de Reportar

1. **Atualize** para a última versão
2. **Procure** issues existentes
3. **Teste** em ambiente limpo
4. **Colete** informações do sistema

### Template de Bug Report

```markdown
**Descrição do Bug**
Descrição clara e concisa do problema

**Passos para Reproduzir**
1. Vá para '...'
2. Execute '...'
3. Observe '...'

**Comportamento Esperado**
O que deveria acontecer

**Comportamento Atual**
O que realmente acontece

**Screenshots**
Se aplicável, adicione screenshots

**Ambiente:**
 - OS: [e.g. Ubuntu 22.04]
 - Docker Version: [e.g. 24.0.6]
 - Docker Compose Version: [e.g. 2.21.0]

**Logs**
```
Cole logs relevantes aqui
```

**Contexto Adicional**
Qualquer outra informação relevante
```

---

## 💡 Sugerindo Melhorias

### Template de Feature Request

```markdown
**O problema que sua feature resolve**
Descrição clara do problema ou necessidade

**Solução Proposta**
Como você imagina que funcionaria

**Alternativas Consideradas**
Outras soluções que você pensou

**Contexto Adicional**
Screenshots, mockups, referências
```

---

## 🎯 Prioridades do Projeto

Atualmente focamos em:

1. 🔴 **Alta**: Estabilidade e correção de bugs
2. 🟠 **Média**: Documentação e usabilidade
3. 🟡 **Baixa**: Novas features e melhorias
4. 🟢 **Futuro**: Automação avançada e integração

Veja [TODO.md](TODO.md) para roadmap detalhado.

---

## 📚 Recursos Úteis

### Aprendendo Docker
- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)

### Aprendendo Git
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)

### Segurança em Labs
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Nmap Reference Guide](https://nmap.org/book/man.html)

---

## 🙏 Reconhecimento

Contribuidores são listados em [CONTRIBUTORS.md](CONTRIBUTORS.md).

Agradecemos especialmente contribuições de:
- 📝 Documentação
- 🐛 Bug reports detalhados
- 💡 Sugestões construtivas
- 🤝 Apoio à comunidade

---

## ❓ Dúvidas?

- 💬 Abra uma [Discussion](https://github.com/dny8888/vuln-labs/discussions)
- 📧 Entre em contato via [email](mailto:dny8888@gmail.com)
- 💭 Comente em issues existentes

---

## 📄 Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas sob a [MIT License](LICENSE).

---

<p align="center">
  <b>Obrigado por contribuir! 🎉</b>
</p>

<p align="center">
  Toda contribuição, não importa o tamanho, é valorizada e faz diferença!
</p>