# 📋 TODO - Docker Lab Project

**Última atualização:** 2025-12-07  
**Versão atual:** 1.0.0  
**Próximo release:** 1.1.0 (previsto para Jan/2026)

---

## 🎯 Legenda de Prioridades

| Símbolo | Prioridade | Descrição |
|---------|------------|-----------|
| 🔴 | **CRÍTICA** | Bloqueia funcionalidades essenciais |
| 🟠 | **ALTA** | Importante para qualidade geral |
| 🟡 | **MÉDIA** | Melhoria significativa |
| 🟢 | **BAIXA** | Nice to have |
| 🔵 | **FUTURO** | Backlog para versões futuras |

---

## ✅ Concluído (v1.0)

- [x] 🔴 Corrigir `dnsmasq.hosts` com IPs corretos
- [x] 🔴 Adicionar IPs fixos no `docker-compose.yaml`
- [x] 🔴 Testar resolução de nomes DNS
- [x] 🔴 Substituir `vuln_server.py` pela versão melhorada
- [x] 🟠 Atualizar container SSH para versão moderna
- [x] 🟠 Adicionar pelo menos 2 usuários com senhas fracas (SSH)
- [x] 🟡 Criar README.md com badges e estrutura profissional
- [x] 🟡 Criar estrutura de diretórios `docs/`

---

## 🚧 Em Progresso

### 🔴 Prioridade CRÍTICA

- [ ] **Testar todas as vulnerabilidades manualmente**  
  - [ ] Command injection (vuln_service)
  - [ ] Weak authentication (vuln_service)
  - [ ] SSH brute force (lab_ssh)
  - [ ] MySQL root access (lab_mysql)
  - [ ] Redis no auth (lab_redis)
  - *Prazo:* Esta semana

- [ ] **Documentar exploração - write-up modelo**  
  - [x] Criar template de write-up
  - [ ] Escrever write-up do vuln_service
  - [ ] Adicionar screenshots
  - *Prazo:* Esta semana

### 🟠 Prioridade ALTA

- [ ] **Melhorar README.md principal**  
  - [x] ~~Remover conteúdo duplicado~~
  - [ ] Adicionar diagrama visual da rede
  - [ ] Criar seção de FAQ
  - [ ] Adicionar GIFs demonstrativos
  - *Prazo:* Próxima semana

- [ ] **Completar documentação modular (docs/)**  
  - [x] ~~01-setup.md (completo)~~
  - [ ] 02-host-discovery.md (expandir com exemplos)
  - [ ] 03-port-scanning.md (expandir com exemplos)
  - [ ] 04-service-enumeration.md (expandir)
  - [ ] 05-nse-scripts.md (listar scripts úteis)
  - [ ] 06-exploitation-guide.md (step-by-step)
  - [ ] 07-reporting.md (templates)
  - *Prazo:* 2 semanas

### 🟡 Prioridade MÉDIA

- [ ] **Criar CHALLENGES.md completo**  
  - [ ] 3 desafios nível iniciante
  - [ ] 3 desafios nível intermediário
  - [ ] 3 desafios nível avançado
  - [ ] 1 desafio bônus
  - [ ] Sistema de pontuação
  - [ ] Gabarito (arquivo separado)
  - *Prazo:* 3 semanas

- [ ] **Adicionar sistema de badges/pontuação**  
  - [ ] Definir critérios de avaliação
  - [ ] Criar badges visuais
  - [ ] Implementar tracking (opcional)
  - *Prazo:* 1 mês

### 🟢 Prioridade BAIXA

- [ ] **Criar CONTRIBUTING.md**
  - [ ] Guidelines de contribuição
  - [ ] Code of conduct
  - [ ] Como reportar bugs
  - [ ] Como sugerir features
  - *Prazo:* 1 mês

- [ ] **Adicionar LICENSE (MIT)**
  - [ ] Arquivo LICENSE
  - [ ] Atualizar headers dos scripts
  - *Prazo:* 1 mês

---

## 🤖 Automação (v1.1)

### Scripts Planejados

- [ ] 🟠 **auto_scan.sh** - Scan automatizado completo
  - [ ] Host discovery
  - [ ] Port scanning (comum + full)
  - [ ] Service enumeration
  - [ ] Vulnerability scanning
  - [ ] NSE scripts específicos
  - [ ] Geração de relatório resumido
  - *Prazo:* 2 semanas

- [ ] 🟠 **analyze_results.py** - Análise de resultados
  - [ ] Parser de arquivos .nmap
  - [ ] Parser de arquivos .gnmap
  - [ ] Parser de arquivos .xml
  - [ ] Extração de CVEs
  - [ ] Geração de relatório estruturado
  - [ ] Export para JSON
  - [ ] Export para HTML
  - *Prazo:* 2 semanas

- [ ] 🟡 **setup_lab.sh** - Deploy automatizado
  - [ ] Verificação de requisitos
  - [ ] Build automático
  - [ ] Verificação de saúde
  - [ ] Testes de conectividade
  - *Prazo:* 3 semanas

- [ ] 🟡 **reset_lab.sh** - Reset do ambiente
  - [ ] Parar containers
  - [ ] Limpar volumes
  - [ ] Rebuild
  - [ ] Restart
  - *Prazo:* 3 semanas

- [ ] 🟢 **exploit_vuln.py** - Exploit automatizado (demo)
  - [ ] Conectar ao vuln_service
  - [ ] Autenticar automaticamente
  - [ ] Explorar command injection
  - [ ] Capturar flag
  - *Prazo:* 1 mês

---

## 📚 Documentação Adicional

- [ ] 🟡 **Criar nmap-cheatsheet.md**
  - [ ] Comandos essenciais
  - [ ] Flags comuns explicadas
  - [ ] Exemplos práticos
  - [ ] NSE scripts úteis
  - *Prazo:* 2 semanas

- [ ] 🟡 **Criar vulnerabilities.md**
  - [ ] Listar todas vulnerabilidades do lab
  - [ ] CVSSv3 score estimado
  - [ ] Impacto e exploração
  - [ ] Mitigação
  - *Prazo:* 3 semanas

- [ ] 🟡 **Criar troubleshooting.md**
  - [ ] Problemas comuns e soluções
  - [ ] Erros do Docker
  - [ ] Problemas de rede
  - [ ] Performance issues
  - *Prazo:* 3 semanas

- [ ] 🟢 **Criar FAQ.md**
  - [ ] Perguntas frequentes
  - [ ] Melhores práticas
  - [ ] Dicas de performance
  - *Prazo:* 1 mês

---

## 🎨 Melhorias Visuais

- [ ] 🟠 **Diagrama de rede**
  - [ ] Criar no draw.io
  - [ ] Export para PNG/SVG
  - [ ] Adicionar ao README
  - *Prazo:* 1 semana

- [ ] 🟡 **Screenshots dos serviços**
  - [ ] Capturar cada serviço funcionando
  - [ ] Adicionar às docs
  - [ ] Criar galeria
  - *Prazo:* 2 semanas

- [ ] 🟡 **GIFs/Vídeos demonstrativos**
  - [ ] GIF do quick start
  - [ ] GIF de exploração
  - [ ] Vídeo completo (YouTube)
  - *Prazo:* 3 semanas

- [ ] 🟢 **Logo do projeto**
  - [ ] Criar logo simples
  - [ ] Adicionar ao README
  - *Prazo:* 1 mês

---

## 🧪 Testes e Qualidade

- [ ] 🟠 **Testes manuais completos**
  - [x] ~~Setup inicial~~
  - [ ] Todos os serviços funcionando
  - [ ] DNS resolution
  - [ ] Scans básicos
  - [ ] Exploração de vulnerabilidades
  - *Prazo:* Esta semana

- [ ] 🟡 **Script de validação automática**
  - [ ] Verificar containers ativos
  - [ ] Verificar conectividade
  - [ ] Verificar portas abertas
  - [ ] Smoke tests básicos
  - *Prazo:* 2 semanas

- [ ] 🟢 **CI/CD básico**
  - [ ] GitHub Actions
  - [ ] Build automático
  - [ ] Testes de integração
  - *Prazo:* Futuro (v2.0)

---

## 🔮 Backlog (Versões Futuras)

### v1.2 (Fev-Mar/2026)

- [ ] 🔵 Adicionar Metasploitable 2 como target
- [ ] 🔵 Container com aplicação web vulnerável (DVWA ou similar)
- [ ] 🔵 Integração com OWASP ZAP
- [ ] 🔵 Wordlists customizadas

### v2.0 (Abr-Jun/2026)

- [ ] 🔵 Container Windows Server com Active Directory
- [ ] 🔵 Ataques em AD (Kerberoasting, Pass-the-Hash)
- [ ] 🔵 Sistema de logging com ELK Stack
- [ ] 🔵 Dashboard Grafana para métricas
- [ ] 🔵 IDS/IPS (Suricata) em modo "hard"

### v3.0 (Jul-Dez/2026)

- [ ] 🔵 Docker Hub para distribuição
- [ ] 🔵 Versão "cloud" (AWS/Azure/GCP)
- [ ] 🔵 Documentação em vídeo completa
- [ ] 🔵 Certificado de conclusão automatizado
- [ ] 🔵 Integração com plataformas CTF

---

## 📊 Métricas de Progresso

### v1.0 → v1.1

**Concluído:** 8/45 tarefas (17.8%)

**Por prioridade:**
- 🔴 Crítica: 4/6 (66.7%)
- 🟠 Alta: 4/12 (33.3%)
- 🟡 Média: 0/15 (0%)
- 🟢 Baixa: 0/12 (0%)

---


## 📅 Timeline Estimado

```
Dez/2024  ████████░░░░░░░░░░░░  v1.0 Release
Jan/2025  ░░░░░░░░████████░░░░  v1.1 Dev (automação)
Fev/2025  ░░░░░░░░░░░░░░██░░░░  v1.1 Release
Mar/2025  ░░░░░░░░░░░░░░░░████  v1.2 Dev
```

---

## 📝 Notas de Desenvolvimento

### Decisões Técnicas

- **Por que Python 3.11 no vuln_service?**  
  Versão estável, moderna, com boas libs de rede

- **Por que Kali como atacante?**  
  Já vem com todas as ferramentas necessárias

- **Por que não exponho portas no host?**  
  Segurança - lab deve ser isolado

### Lições Aprendidas

- Docker Compose v2 tem sintaxe diferente do v1
- DNS interno do Docker é excelente para labs
- IPs fixos evitam muitos problemas
- Documentação modular > README gigante

---
