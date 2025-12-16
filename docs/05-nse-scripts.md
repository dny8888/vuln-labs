# 05 - NSE Scripts

## 📋 Visão Geral

NSE (Nmap Scripting Engine) são scripts Lua que automatizam tarefas de enumeração e detecção de vulnerabilidades. É como ter centenas de ferramentas especializadas dentro do Nmap.

**Tempo:** 15-20 minutos | **Nível:** Intermediário

---

## 🎯 Objetivos

- Entender categorias de scripts NSE
- Usar scripts para enumeração avançada
- Detectar vulnerabilidades automaticamente
- Criar combinações eficientes de scripts

---

## 📚 Categorias de Scripts

| Categoria | Descrição | Exemplo |
|-----------|-----------|---------|
| `auth` | Testa autenticação | `ssh-brute`, `http-auth` |
| `broadcast` | Descoberta via broadcast | `dhcp-discover` |
| `brute` | Força bruta | `mysql-brute`, `ftp-brute` |
| `default` | Scripts padrão (-sC) | `http-title`, `ssh-hostkey` |
| `discovery` | Descoberta de recursos | `smb-enum-shares` |
| `dos` | Testes DoS (cuidado!) | `http-slowloris` |
| `exploit` | Exploração (cuidado!) | `smb-vuln-ms17-010` |
| `external` | Consultas externas | `whois-ip` |
| `fuzzer` | Fuzzing | `http-form-fuzzer` |
| `intrusive` | Agressivos | `http-sql-injection` |
| `malware` | Detecta malware | `smtp-strangeport` |
| `safe` | Seguros, não intrusivos | `http-headers` |
| `version` | Detecção de versão | `mysql-info` |
| `vuln` | Vulnerabilidades | `smb-vuln-*`, `ssl-*` |

---

## 🛠️ Uso Básico

### Executar Scripts

```bash
# Script único
nmap --script=http-title lab_nginx

# Múltiplos scripts
nmap --script=ssh-hostkey,ssh-auth-methods lab_ssh

# Categoria inteira
nmap --script=vuln lab_pyserver

# Wildcards
nmap --script=http-* lab_nginx
nmap --script="ssh-*" lab_ssh
```

---

### Combinar com Outras Flags

```bash
# Script + version detection
nmap -sV --script=banner lab_pyserver

# Script + portas específicas
nmap -p 80,443 --script=http-enum lab_nginx

# Scripts padrão (equivale a --script=default)
nmap -sC lab_ssh
```

---

### Ver Informações do Script

```bash
# Help do script
nmap --script-help=http-title

# Listar scripts disponíveis
ls /usr/share/nmap/scripts/ | grep http

# Procurar por keyword
nmap --script-help="*vuln*"

# Atualizar database
sudo nmap --script-updatedb
```

---

## 💻 Scripts Úteis por Serviço

### HTTP/HTTPS (80, 443, 8025)

```bash
# Informações básicas
nmap -p 80 --script=http-title,http-headers,http-server-header lab_nginx

# Enumeração de diretórios
nmap -p 80 --script=http-enum lab_nginx

# Métodos HTTP
nmap -p 80 --script=http-methods lab_apache

# Vulnerabilidades comuns
nmap -p 80 --script=http-sql-injection,http-vuln-* lab_nginx
```

---

### SSH (22)

```bash
# Informações e métodos
nmap -p 22 --script=ssh-hostkey,ssh-auth-methods,ssh2-enum-algos lab_ssh

# Força bruta (cuidado!)
nmap -p 22 --script=ssh-brute --script-args userdb=users.txt,passdb=pass.txt lab_ssh

```

---

### SMB (445)

```bash
# Discovery completo
nmap -p 445 --script=smb-os-discovery,smb-protocols,smb-security-mode lab_smb

# Enumerar shares
nmap -p 445 --script=smb-enum-shares,smb-enum-users lab_smb

# Vulnerabilidades críticas
nmap -p 445 --script=smb-vuln-ms17-010,smb-vuln-* lab_smb
```

---

### MySQL (3306)

```bash
# Informações
nmap -p 3306 --script=mysql-info lab_mysql

# Enumerar databases (se sem auth)
nmap -p 3306 --script=mysql-databases lab_mysql

# Brute force
nmap -p 3306 --script=mysql-brute lab_mysql

# Dump de hashes (se acesso)
nmap -p 3306 --script=mysql-dump-hashes \
     --script-args='username=root,password=rootpass' lab_mysql
```

---

### Redis (6379)

```bash
# Informações
nmap -p 6379 --script=redis-info lab_redis

# Brute force (se auth habilitado)
nmap -p 6379 --script=redis-brute lab_redis
```

---

### FTP (21)

```bash
# Banner e info
nmap -p 21 --script=ftp-anon,ftp-bounce,banner lab_ftp

# Brute force
nmap -p 21 --script=ftp-brute lab_ftp
```

---

### DNS (53)

```bash
# Zone transfer
nmap -p 53 --script=dns-zone-transfer lab_dns

# Brute force de subdomínios
nmap --script=dns-brute --script-args dns-brute.domain=lab lab_dns
```

---

## 🎯 Scripts de Vulnerabilidades

### Scan de Vulnerabilidades Geral

```bash
# Categoria vuln completa
nmap -sV --script=vuln lab_pyserver -oA vuln_scan

# Mais rápido: apenas safe
nmap -sV --script=vuln-safe lab_pyserver

# SSL/TLS vulnerabilities
nmap -p 443 --script=ssl-* lab_nginx
```

---

### Scripts Específicos Importantes

```bash
# Eternal Blue (MS17-010)
nmap -p 445 --script=smb-vuln-ms17-010 lab_smb

# Heartbleed
nmap -p 443 --script=ssl-heartbleed lab_nginx

# SQL Injection
nmap -p 80 --script=http-sql-injection lab_nginx

# XSS
nmap -p 80 --script=http-stored-xss,http-dombased-xss lab_nginx
```

---

## 💻 Exemplos Práticos no Lab

### Exemplo 1: Scan Completo do Vuln Service

```bash
cd /root/nmap_results

# Todos os scripts seguros
nmap -sV -p 9999 --script=safe lab_pyserver -oA 01_vuln_safe

# Scripts de vulnerabilidade
nmap -p 9999 --script=vuln lab_pyserver -oA 02_vuln_vuln

# Banner e info
nmap -p 9999 --script=banner,auth lab_pyserver -oA 03_vuln_info
```

---

### Exemplo 2: Enumeração Web Completa

```bash
# Nginx
nmap -p 80 --script="http-enum,http-headers,http-methods,http-title" \
     lab_nginx -oA 04_nginx_enum

# Apache
nmap -p 80 --script="http-*" --script-args http.useragent="Mozilla/5.0" \
     lab_apache -oA 05_apache_enum
```

---

## 🎓 Exercícios

### Exercício 1: Explorar Scripts HTTP

```bash
# Listar todos scripts HTTP
ls /usr/share/nmap/scripts/ | grep http | wc -l

# Testar 3 scripts diferentes no nginx
nmap -p 80 --script=http-title lab_nginx
nmap -p 80 --script=http-headers lab_nginx
nmap -p 80 --script=http-methods lab_nginx
```

**Pergunta:** Quantos scripts HTTP existem?

---

### Exercício 2: Detectar Vulnerabilidades

```bash
# Scan de vulnerabilidades em múltiplos alvos
nmap -sV --script=vuln -p 22,80,445,3306,9999 \
     lab_ssh lab_nginx lab_smb lab_mysql lab_pyserver \
     -oA ex2_vulns

# Analisar resultados
grep -i "VULNERABLE\|CVE" ex2_vulns.nmap
```

**Objetivo:** Encontrar pelo menos uma vulnerabilidade

---

### Exercício 3: SSH Brute Force Simulado

```bash
# Criar wordlists simples
echo "admin" > users.txt
echo "labuser" >> users.txt
echo "password" > pass.txt
echo "weakpass123" >> pass.txt

# Brute force
nmap -p 2222 --script=ssh-brute \
     --script-args userdb=users.txt,passdb=pass.txt \
     lab_ssh -oA ex3_ssh_brute
```

**Pergunta:** Conseguiu credenciais válidas?

---

## 📝 Scripts Personalizados

### Localização dos Scripts

```bash
# Diretório de scripts
ls /usr/share/nmap/scripts/

# Ver conteúdo de um script
cat /usr/share/nmap/scripts/http-title.nse
```

### Criar Script Simples (Opcional)
```bash
# Diretório de scripts
vim /usr/share/nmap/scripts/custom-banner.nse
```

```lua
-- custom-banner.nse
description = [[
Captura banner de serviço customizado
]]

categories = {"safe", "discovery"}

portrule = function(host, port)
  return port.number == 9999
end

action = function(host, port)
  local socket = nmap.new_socket()
  socket:connect(host, port)
  local status, banner = socket:receive()
  socket:close()
  return banner
end
```

**Usar:** `nmap --script=custom-banner.nse lab_pyserver`

---

## ⚠️ Boas Práticas

### ✅ Faça

```bash
# Use categorias para organizar
nmap --script=safe,discovery lab_pyserver

# Salve sempre os resultados
nmap --script=vuln lab_pyserver -oA vuln_$(date +%Y%m%d)

# Teste scripts individualmente antes
nmap --script=http-title lab_nginx  # OK
# Depois combine
nmap --script=http-* lab_nginx
```

### ❌ Não Faça

```bash
# ❌ Nunca use 'exploit' ou 'dos' em produção
nmap --script=exploit,dos 10.89.0.3

# ❌ Não rode todos scripts sem filtrar
nmap --script=all 10.89.0.3  # Pode causar problemas

# ❌ Brute force sem autorização
nmap --script=brute 10.89.0.0/24
```

---


## 📚 Referência Rápida

```bash
# === BÁSICO ===
nmap --script=nome-script host
nmap --script=cat1,cat2 host
nmap --script="wildcard*" host
nmap -sC host                    # Scripts padrão

# === CATEGORIAS ÚTEIS ===
nmap --script=safe host          # Seguros
nmap --script=vuln host          # Vulnerabilidades
nmap --script=discovery host     # Descoberta
nmap --script=auth host          # Autenticação

# === POR SERVIÇO ===
nmap -p 80 --script=http-* host
nmap -p 22 --script=ssh-* host
nmap -p 445 --script=smb-* host
nmap -p 3306 --script=mysql-* host

# === INFO ===
nmap --script-help=nome          # Help
nmap --script-updatedb           # Atualizar
ls /usr/share/nmap/scripts/ | grep palavra
```

---

## 🔗 Próximos Passos

1. **Continue:** [06 - Exploitation Guide](06-exploitation-guide.md)
2. **Pratique:** Complete os 3 exercícios
3. **Explore:** Teste 10+ scripts diferentes
4. **Documente:** Anote scripts úteis para cada serviço

---

## 📖 Recursos

- [NSE Documentation](https://nmap.org/nsedoc/)
- [NSE Scripts List](https://nmap.org/nsedoc/scripts/)
- [Writing NSE Scripts](https://nmap.org/book/nse.html)