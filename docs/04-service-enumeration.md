# 04 - Service Enumeration

## 📋 Visão Geral

Após descobrir hosts e portas, identifique **que serviços** estão rodando. Saber que porta 80 está aberta é útil, mas saber que é **Nginx 1.25.3** com vulnerabilidade conhecida é ouro!

**Tempo:** 20 minutos | **Nível:** Intermediário

---

## 🎯 Objetivos

- Detectar versões de serviços
- Coletar banners e informações sensíveis
- Usar scripts NSE básicos
- Documentar findings de forma estruturada

---

## 🛠️ Ferramentas do Lab

| Ferramenta | Uso |
|------------|-----|
| `nmap -sV` | Detection de versões |
| `nmap -sC` | Scripts NSE padrão |
| `nc` | Captura manual de banners |
| `curl` | Enumerar web servers |

---

## 📡 Service Detection com Nmap

### Version Detection (-sV)

```bash
# Detection padrão
nmap -sV 10.89.0.3

# Agressivo (mais probes)
nmap -sV --version-intensity 9 10.89.0.3

# Rápido (menos probes)
nmap -sV --version-intensity 2 10.89.0.3
```

**Version Intensity:** 0 (rápido) a 9 (completo). Padrão: 7

---

### Scripts Padrão (-sC)

```bash
# Scripts NSE básicos
nmap -sC -p 80 10.89.0.3

# Combinação recomendada
nmap -sV -sC 10.89.0.3
```

Scripts incluem: `http-title`, `ssh-hostkey`, `ssl-cert`, etc.

---

### OS Detection (-O)

```bash
# Detectar sistema operacional
sudo nmap -O 10.89.0.3

# Scan completo
sudo nmap -sV -sC -O -T4 10.89.0.12
```

**Nota:** Pode não funcionar bem em containers Docker

---

## 💻 Exemplos Práticos

### Exemplo 1: Enumerar Vuln Service

```bash
cd /root/nmap_results

# Enumeração completa
sudo nmap -sV -sC -O -T4 -p9999 lab_vuln -oA 01_vuln_enum
```

**Saída esperada:**
```
PORT     STATE SERVICE VERSION
9999/tcp open  abyss?
| fingerprint-strings: 
|   VulnService v0.0.2 (Build 2025-12-07)
|   Running on: Alpine Linux 3.18
|   Python: 3.11.6
|   Commands: help, login, ping, base64, exec, flag, exit
```

**Informações coletadas:** Versão, SO, linguagem, comandos

---

### Exemplo 2: Enumerar Web Servers

```bash
# Detectar versões
nmap -sV -p 80,8025 10.89.0.0/24 -oA 02_web_enum
```
```bash
# Visto na seção anterior
nmap -sn 10.89.0.0/24 -oG - | grep "Up" | awk '{print $2}' > hosts.txt
```
```bash
# Imprime em formato agradavel
for ip in $(cat hosts.txt); do
    service=$(sed -n "/($ip)/,/MAC Address/p" 02_web_enum.nmap \
              | grep "open *http" \
              | sed 's/.*open *http *//')
    [ -n "$service" ] && echo "$ip: $service"
done
```

**Saída esperada:**
```
10.89.0.3:  nginx 1.25.3
10.89.0.4:  Apache httpd 2.4.58
10.89.0.10: Go net/http server
```

---

### Exemplo 3: SSH Enumeration

```bash
# Scripts SSH
nmap -p 2222 --script=ssh-hostkey,ssh-auth-methods lab_ssh -oA 03_ssh_enum
```

**Informações úteis:**
- Tipos de chaves (ECDSA, ED25519)
- Métodos de auth (password, publickey)
- **password aceito** = vulnerável a brute force

---

### Exemplo 4: MySQL Info

```bash
# Script MySQL
nmap -p 3306 --script=mysql-info lab_mysql -oA 04_mysql_enum
```

**Saída:**
```
| mysql-info: 
|   Protocol: 10
|   Version: 5.7.44
|   Capabilities flags: 65535
```

---

## 🌐 Enumeração Manual

### Banner Grabbing com Netcat

```bash
# HTTP
echo -e "GET / HTTP/1.0\r\n\r\n" | nc lab_nginx 80

# Custom service
nc lab_pyserver 9999
# Digite: help
```

---

### Web Headers com Curl

```bash
# Capturar headers
curl -I http://lab_nginx

# Verbose (ver handshake)
curl -v http://lab_apache
```

**Saída útil:**
```
Server: nginx/1.25.3
Date: Mon, 09 Dec 2024 23:00:00 GMT
```

---

### Teste de Serviços

```bash
# MySQL
mariadb -h lab_mysql -u root -prootpass --ssl=0 -e "SELECT version();"

# Redis
redis-cli -h lab_redis INFO server

# FTP
ftp lab_ftp
# user: ftpuser / pass: ftppass
```

---

## 🎓 Exercícios

### Exercício 1: Identificar Versões

**Pergunta:** Quantos e quais serviços encontrou?


---

## ⚠️ Boas Práticas

### ✅ Faça

```bash
# Sempre combine -sV com -sC
nmap -sV -sC 10.89.0.3

# Salve resultados
nmap -sV -sC -oA enum_$(date +%Y%m%d) 10.89.0.3

# Valide manualmente
nc lab_vuln 9999
```

### ❌ Não Faça

```bash
# ❌ Só -sV sem especificar portas
nmap -sV 10.89.0.3

# ✅ Especifique portas ou use -p-
nmap -sV -p- 10.89.0.3
```

---

## 📚 Referência Rápida

```bash
# === BÁSICO ===
nmap -sV 10.89.0.3                # Versões
nmap -sV -sC 10.89.0.3            # + Scripts
nmap -sV -sC -O 10.89.0.3         # + OS detection

# === SCRIPTS POR SERVIÇO ===
nmap -p 22 --script=ssh-* lab_ssh
nmap -p 80 --script=http-* lab_nginx
nmap -p 445 --script=smb-* lab_smb
nmap -p 3306 --script=mysql-* lab_mysql

# === MANUAL ===
nc lab_vuln 9999                  # Banner
curl -I http://lab_nginx          # HTTP headers
echo "GET /" | nc lab_nginx 80    # HTTP raw

# === PORTAS DO LAB ===
nmap -sV -sC -p 22,80,445,1025,3306,6379,9999 10.89.0.0/24
```

---

## 🔗 Próximos Passos

1. **Continue:** [05 - NSE Scripts](05-nse-scripts.md)
2. **Pratique:** Complete os 3 exercícios
3. **Documente:** Tabela de serviços e versões
4. **Pesquise:** CVEs para versões encontradas

---

## 📖 Recursos

- [Nmap Service Detection](https://nmap.org/book/vscan.html)
- [NSE Scripts](https://nmap.org/nsedoc/)
- [CVE Search](https://cve.mitre.org/)
- [Exploit-DB](https://www.exploit-db.com/)
