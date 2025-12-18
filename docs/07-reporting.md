# 07 - Reporting

## 📋 Visão Geral

Um pentest sem relatório é trabalho perdido. Este guia ensina a documentar achados de forma clara, profissional e acionável.

**Tempo:** 20-30 minutos | **Nível:** Todos

---

## 🎯 Objetivos

- Estruturar relatórios profissionais
- Classificar vulnerabilidades (CVSS)
- Documentar evidências adequadamente
- Prover recomendações acionáveis

---

## 📊 Estrutura de Um Relatório

### Componentes Essenciais

1. **Executive Summary** - Para gestores (não-técnico)
2. **Technical Summary** - Para equipe técnica
3. **Methodology** - Como foi feito o teste
4. **Findings** - Vulnerabilidades encontradas
5. **Recommendations** - Como corrigir
6. **Appendix** - Evidências detalhadas

---

### 📄 [Template: Executive Summary](docs/07.1-template-executive-summary.md)

### 🔍 [Template: Finding Individual](docs/07.2-template-finding-individual.md)

###  [Template de Recomendação](docs/07.3-template-recomendacao.md)
---

## 📊 Classificação CVSS

### Calculadora Simplificada

```text
Base Score Metrics:

Attack Vector (AV):
  Network (N) = 0.85
  Adjacent (A) = 0.62
  Local (L) = 0.55
  Physical (P) = 0.2

Attack Complexity (AC):
  Low (L) = 0.77
  High (H) = 0.44

Privileges Required (PR):
  None (N) = 0.85
  Low (L) = 0.62
  High (H) = 0.27

User Interaction (UI):
  None (N) = 0.85
  Required (R) = 0.62

Scope (S):
  Unchanged (U) = Impact sem alteração
  Changed (C) = Impact além do componente

Impact:
  High (H) = 0.56
  Low (L) = 0.22
  None (N) = 0

Score Range:
  0.0 = None
  0.1-3.9 = Low
  4.0-6.9 = Medium
  7.0-8.9 = High
  9.0-10.0 = Critical
```

### Exemplos de Classificação

| Vulnerabilidade | CVSS | Severidade |
|-----------------|------|------------|
| Command Injection (autenticado) | 8.8 | 🟠 Alta |
| Command Injection (não autenticado) | 9.8 | 🔴 Crítica |
| Senha fraca (SSH) | 7.5 | 🟠 Alta |
| Information Disclosure (banner) | 5.3 | 🟡 Média |
| Serviço sem autenticação (Redis) | 7.5 | 🟠 Alta |
| Anonymous SMB access | 6.5 | 🟡 Média |

---

## 📸 Documentando Evidências

### Screenshots Efetivos

**Incluir:**
- Comando executado (visível)
- Output completo
- Timestamp
- IP/hostname do alvo

**Exemplo de legenda:**
```text
Figura 1: Command injection confirmada via metacharacter ';'
Comando: ping 127.0.0.1; id
Data: 09/12/2024 23:45
Alvo: lab_vuln (10.89.0.12:9999)
```

### Logs e Outputs

```bash
# Sempre salvar outputs
nmap -sV lab_vuln -oA scan_vuln_$(date +%Y%m%d_%H%M%S)

# Logs de exploração
script -c "nc lab_vuln 9999" exploitation_log_$(date +%Y%m%d).txt

# Capturas de rede (se relevante)
tcpdump -i eth0 -w capture.pcap host 10.89.0.12
```

---

## 📋 Checklist de Qualidade

### Antes de Entregar o Relatório

- [ ] Executive summary claro para não-técnicos
- [ ] Todos os findings documentados
- [ ] CVSS calculado para cada vulnerabilidade
- [ ] Screenshots claros e legíveis
- [ ] Proofs of concept reproduzíveis
- [ ] Recomendações específicas e acionáveis
- [ ] Prazo para cada correção definido
- [ ] Referências técnicas incluídas
- [ ] Revisão ortográfica e gramatical
- [ ] Índice e numeração de páginas
- [ ] Controle de versão do documento
- [ ] Classificação de confidencialidade

---

## 🎓 Exercício: Relatório Completo

### Criar Relatório do Lab

```markdown
# 1. Coletar todas as evidências
cd /root/nmap_results
ls -la

# 2. Organizar findings
# - Host discovery
# - Port scanning  
# - Service enumeration
# - Vulnerability assessment
# - Exploitation

# 3. Documentar cada finding usando template

# 4. Calcular CVSS para cada vulnerabilidade

# 5. Criar executive summary

# 6. Adicionar recomendações

# 7. Revisar e entregar
```

### Estrutura de Diretórios

```text
pentest_report/
├── report.md
├── executive_summary.md
├── findings/
│   ├── 001_command_injection.md
│   ├── 002_weak_auth.md
│   ├── 003_info_disclosure.md
│   └── ...
├── evidences/
│   ├── screenshots/
│   ├── logs/
│   └── pcaps/
└── recommendations/
    └── remediation_plan.md
```

---

## ⚠️ Boas Práticas

### ✅ Faça

- Use linguagem clara e objetiva
- Inclua sempre prova de conceito
- Classifique corretamente (CVSS)
- Forneça recomendações específicas
- Revise antes de entregar
- Mantenha confidencialidade

### ❌ Não Faça

- Incluir informações desnecessárias
- Usar jargões sem explicar
- Omitir vulnerabilidades "pequenas"
- Fazer recomendações genéricas
- Entregar sem revisão
- Compartilhar sem autorização

---

## 🔗 Recursos Adicionais

- [CVSS Calculator](https://www.first.org/cvss/calculator/3.1)
- [CWE List](https://cwe.mitre.org/)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [PTES Reporting](http://www.pentest-standard.org/index.php/Reporting)
- [SANS Pentest Report Template](https://www.sans.org/)