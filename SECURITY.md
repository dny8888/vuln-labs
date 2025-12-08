# 🔒 Política de Segurança

## 📋 Visão Geral

Este documento descreve as políticas de segurança para o **Vuln-Labs**, um ambiente educacional de pentesting. Embora o projeto contenha vulnerabilidades **intencionais** para fins de aprendizado, levamos a segurança do código base e infraestrutura a sério.

---

## ⚠️ Contexto Importante

### Sobre Este Projeto

**Vuln-Labs é um ambiente de TREINAMENTO que contém vulnerabilidades INTENCIONAIS.**

Estas vulnerabilidades são:
- ✅ **Documentadas** e propositais
- ✅ **Isoladas** em containers Docker
- ✅ **Educacionais** - não devem ser usadas em produção
- ✅ **Controladas** - apenas em ambiente local

### O Que NÃO Reportar

**Não reportamos como vulnerabilidades de segurança:**

- ❌ Vulnerabilidades documentadas nos serviços do lab (são intencionais)
- ❌ Configurações "inseguras" dos containers (são propositais)
- ❌ Senhas fracas nos serviços (são parte do treinamento)
- ❌ Falta de autenticação em serviços (é o objetivo do lab)

**Exemplos de vulnerabilidades INTENCIONAIS:**
- Command injection no `vuln_service`
- Autenticação fraca (senha `admin123`)
- Services sem autenticação (Redis, MySQL)
- Configurações default dos web servers

---

## 🛡️ Versões Suportadas

Apenas a versão mais recente é ativamente mantida:

| Versão | Suportada          |
| ------ | ------------------ |
| 1.x    | ✅ Sim             |
| < 1.0  | ❌ Não             |

---

## 🚨 Reportando Vulnerabilidades de Segurança

### O Que Reportar

**Por favor reporte vulnerabilidades LEGÍTIMAS como:**

#### 1. Vulnerabilidades na Infraestrutura do Projeto

- Escape de container não intencional
- Acesso ao host a partir dos containers
- Exposição não intencional de portas para internet
- Problemas de isolamento de rede

#### 2. Vulnerabilidades no Código Base

- Injeção de código nos scripts de automação
- Path traversal nos scripts Python/Bash
- Execução arbitrária de código fora do contexto do lab
- Problemas de segurança no `docker-compose.yaml`

#### 3. Problemas de Supply Chain

- Dependências vulneráveis críticas
- Imagens Docker comprometidas
- Malware em dependências

#### 4. Configurações Perigosas

- Configurações que permitem acesso externo não intencional
- Volumes montados incorretamente
- Privilégios excessivos não documentados

### Como Reportar

**⚠️ NÃO abra issues públicas para vulnerabilidades de segurança!**

Para reportar vulnerabilidades de segurança LEGÍTIMAS:

1. **Email Privado:**
   - [dny8888@gmail.com]

2. **GitHub Security Advisory:**
   - Vá para a aba "Security" do repositório
   - Clique em "Report a vulnerability"
   - Preencha o formulário privado

### Informações a Incluir

Por favor, inclua:

```markdown
**Tipo de Vulnerabilidade:**
[Container escape / Code injection / etc.]

**Componente Afetado:**
[Script específico / Container / docker-compose.yaml]

**Severidade Estimada:**
[Crítica / Alta / Média / Baixa]

**Descrição:**
Descrição detalhada da vulnerabilidade

**Passos para Reproduzir:**
1. ...
2. ...
3. ...

**Impacto Potencial:**
O que um atacante poderia fazer

**Proof of Concept:**
```bash
# Comandos ou código demonstrando o problema
```

**Sugestão de Correção (opcional):**
Se você tiver ideias de como corrigir

**Ambiente:**
- OS: [Ubuntu 22.04]
- Docker: [24.0.6]
- Docker Compose: [2.21.0]
```

---

## 📞 Processo de Resposta

### Timeline de Resposta

- **24-48 horas**: Confirmação inicial do recebimento
- **1 semana**: Avaliação inicial da vulnerabilidade
- **2-4 semanas**: Desenvolvimento e teste da correção
- **Após correção**: Divulgação coordenada

### Classificação de Severidade

Usamos CVSS 3.1 como base:

| Score | Severidade | Tempo de Resposta |
|-------|------------|-------------------|
| 9.0-10.0 | 🔴 Crítica | 24-48 horas |
| 7.0-8.9 | 🟠 Alta | 1 semana |
| 4.0-6.9 | 🟡 Média | 2-3 semanas |
| 0.1-3.9 | 🟢 Baixa | 4+ semanas |

### Divulgação Coordenada

1. **Vulnerabilidade confirmada**: Notificamos você privadamente
2. **Correção desenvolvida**: Criamos patch em branch privada
3. **Testing**: Validamos a correção
4. **Release**: Publicamos versão corrigida
5. **Advisory**: Publicamos security advisory (após 7 dias)
6. **Créditos**: Creditamos o descobridor (se desejado)

---

## 🏆 Programa de Reconhecimento

### O Que Oferecemos

- ✅ Reconhecimento público (se desejado)
- ✅ Menção nos release notes
- ❌ Não oferecemos recompensas financeiras (projeto open source)

---

## 🔐 Melhores Práticas de Uso

### Para Usuários do Lab

#### ✅ FAÇA:

1. **Execute apenas em ambiente isolado**
   ```bash
   # Verifique isolamento
   docker network inspect docker-lab_labnet
   ```

2. **Use máquina virtual dedicada**
   - Preferencialmente em VM (VirtualBox, VMware)
   - Ou em host dedicado de testes

3. **Mantenha o lab atualizado**
   ```bash
   git pull origin main
   docker compose pull
   docker compose up -d --build
   ```

4. **Monitore logs regularmente**
   ```bash
   docker compose logs -f
   ```

5. **Destrua o lab quando não estiver usando**
   ```bash
   docker compose down --volumes
   ```

#### ❌ NÃO FAÇA:

1. **Nunca exponha serviços para internet**
   ```yaml
   # ERRADO - NÃO FAÇA ISSO:
   ports:
     - "0.0.0.0:9999:9999"  # Expõe para internet!
   
   # CORRETO - Apenas rede interna:
   # Sem seção "ports" = apenas comunicação intra-container
   ```

2. **Não use em rede corporativa**
   - Pode acionar IDS/IPS
   - Pode violar políticas de segurança
   - Use apenas em redes isoladas

3. **Não modifique para uso em produção**
   - Este lab NÃO é hardened
   - Configurações são inseguras por design
   - Nunca adapte para uso real

4. **Não desabilite isolamento do Docker**
   ```bash
   # ERRADO - NUNCA USE:
   docker run --privileged  # Perigoso!
   docker run --net=host    # Remove isolamento!
   ```

### Para Desenvolvedores/Contribuidores

#### Segurança no Código

1. **Validação de Input**
   ```python
   # BOM
   import shlex
   safe_arg = shlex.quote(user_input)
   
   # RUIM - nos scripts do lab (não nos serviços vulneráveis)
   os.system(f"command {user_input}")  # Command injection!
   ```

2. **Gestão de Secrets**
   ```bash
   # NUNCA commite:
   - Credenciais reais
   - Chaves privadas
   - Tokens de API
   - Senhas pessoais
   
   # Use no .gitignore:
   secrets/
   *.key
   *.pem
   .env
   ```

3. **Dependências Seguras**
   ```bash
   # Verificar vulnerabilidades
   docker scout cves attacker/
   
   # Manter imagens atualizadas
   docker compose pull
   ```

4. **Code Review**
   - Todo PR deve ser revisado
   - Scripts de automação devem ser seguros
   - Verificar injection em variáveis de ambiente

---

## 🛠️ Ferramentas de Segurança

### Scanning de Containers

```bash
# Usando Docker Scout
docker scout cves kalilinux/kali-rolling:latest

# Usando Trivy
trivy image --severity HIGH,CRITICAL python:3.11-alpine

# Usando Grype
grype kalilinux/kali-rolling:latest
```

### Linting de Dockerfiles

```bash
# Hadolint
docker run --rm -i hadolint/hadolint < attacker/Dockerfile

# Dockle
dockle attacker:latest
```

### Verificação de Secrets

```bash
# Gitleaks
gitleaks detect --source . --verbose

# TruffleHog
trufflehog filesystem --directory .
```

---

## 🔍 Auditoria e Compliance

### Checklist de Segurança

Para maintainers antes de cada release:

- [ ] Scan de vulnerabilidades em todas as imagens
- [ ] Revisão de PRs com foco em segurança
- [ ] Verificação de secrets commitados
- [ ] Teste de isolamento de rede
- [ ] Validação de permissões de containers
- [ ] Review do docker-compose.yaml
- [ ] Atualização de dependências
- [ ] Teste em ambiente limpo

### Logs de Auditoria

```bash
# Verificar eventos de segurança
docker events --filter 'type=container' --filter 'event=start'

# Logs de tentativas de escape (exemplo)
docker compose logs | grep -i "error\|permission\|denied"
```

---

## ⚖️ Responsabilidade Legal

### Disclaimer

Este laboratório é fornecido "como está" para fins educacionais. Os mantenedores:

- ❌ NÃO são responsáveis por uso indevido
- ❌ NÃO garantem segurança absoluta
- ❌ NÃO endossam atividades ilegais
- ✅ Encorajam uso ético e legal

### Uso Responsável

**Você é responsável por:**
- Garantir uso legal em sua jurisdição
- Obter autorizações necessárias
- Seguir leis de privacidade e cibersegurança
- Usar apenas em ambientes controlados

**Este lab NÃO deve ser usado para:**
- Ataques reais a sistemas
- Testes não autorizados
- Atividades maliciosas
- Violação de leis locais

---

## 📜 Histórico de Segurança

### Vulnerabilidades Corrigidas

Veja [CHANGELOG.md](CHANGELOG.md) para histórico completo.

#### v1.0.1 (2024-XX-XX)
- Nenhuma vulnerabilidade de segurança corrigida ainda

---

## 🙏 Agradecimentos

Agradecemos a todos os pesquisadores de segurança que reportam vulnerabilidades responsavelmente.

Security Hall of Fame: [SECURITY_HALL_OF_FAME.md](SECURITY_HALL_OF_FAME.md)

---

<p align="center">
  <b>Segurança é responsabilidade de todos! 🔒</b>
</p>

<p align="center">
  Se você viu algo, diga algo - reporte responsavelmente.
</p>

---

**Última atualização:** 2025-12-07  
**Versão deste documento:** 1.0