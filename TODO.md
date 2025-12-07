## 📋 **PLANO DE AÇÃO**

### **🔥 Correções Críticas**

- [x] Corrigir `dnsmasq.hosts` com IPs corretos
- [x] Adicionar IPs fixos no `docker-compose.yaml`
- [x] Testar resolução de nomes DNS
- [x] Substituir `vuln_server.py` pela versão melhorada
- [ ] Atualizar container SSH para versão moderna
- [ ] Adicionar pelo menos 2 usuários com senhas fracas
- [ ] Testar força bruta SSH (hydra)
- [ ] Testar todas as vulnerabilidades manualmente
- [ ] Documentar exploração - write-up

---

### **📚 Semana 2: Documentação Modular**

- [ ] Criar diretório `docs/`
- [ ] Dividir README em 7 documentos menores
- [ ] Criar índice navegável
- [ ] Escrever `CHALLENGES.md` completo
- [ ] Adicionar sistema de pontuação
- [ ] Criar templates de write-up
- [ ] Criar `CONTRIBUTING.md` para colaboradores
- [ ] Adicionar `LICENSE` (MIT)
- [ ] Melhorar README principal (overview + quickstart)

---

### **🤖 Automação**

- [ ] Implementar `scripts/auto_scan.sh`
- [ ] Testar script em todos os cenários
- [ ] Documentar uso do script
- [ ] Implementar `scripts/analyze_results.py`
- [ ] Testar análise de resultados
- [ ] Adicionar exportação JSON
- [ ] Implementar `scripts/setup_lab.sh` (automação de deploy)
- [ ] Script para reset completo do lab

---

### **🎯 Gamificação e Publicação**

- [ ] Implementar todos os 10 desafios CTF
- [ ] Testar cada desafio
- [ ] Criar gabarito de respostas (arquivo separado)
- [ ] Adicionar badges no README (Docker, License, etc)
- [ ] Criar diagrama de rede visual (draw.io)
- [ ] Screenshots dos serviços

---

## 🎯 **MELHORIAS FUTURAS (Backlog)**

### **Fase 2 :**
- [ ] Adicionar Metasploitable 2/3 como target
- [ ] Container Windows Server com AD vulnerável
- [ ] Sistema de logging com ELK Stack
- [ ] Dashboard Grafana para métricas
- [ ] Integração com OWASP ZAP

### **Fase 3:**
- [ ] CI/CD para testes automatizados
- [ ] Docker Hub para distribuição fácil
- [ ] Documentação em vídeo (YouTube)
- [ ] Versão "hard mode" com IDS/IPS
- [ ] Write-ups oficiais publicados
