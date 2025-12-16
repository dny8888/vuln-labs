# 03 - Port Scanning

## 📋 Visão Geral

Após identificar hosts ativos, o próximo passo é descobrir quais **portas estão abertas**. Cada porta aberta representa um serviço potencialmente explorável. É como saber quais janelas e portas de uma casa estão destrancadas.

**Tempo:** 15-20 minutos | **Nível:** Iniciante

---

## 🎯 Objetivos

- Identificar portas abertas em hosts
- Distinguir diferentes tipos de port scan
- Escolher a técnica apropriada para cada cenário
- Interpretar resultados e estados de portas
- Otimizar velocidade vs precisão

---

## 🚪 Estados de Portas

O Nmap classifica portas em 6 estados:

| Estado | Significado | Ação |
|--------|-------------|------|
| **open** | Serviço aceitando conexões | ✅ Investigar |
| **closed** | Porta acessível mas sem serviço | ℹ️ Anotar |
| **filtered** | Firewall bloqueando | ⚠️ Tentar bypass |
| **unfiltered** | Acessível mas estado incerto | 🔍 Scan adicional |
| **open\|filtered** | Não consegue determinar | 🔍 Scan adicional |
| **closed\|filtered** | Não consegue determinar | 🔍 Scan adicional |

**No lab:** Você verá principalmente **open** e **closed**

---

## 🛠️ Tipos de Port Scan

### 1. TCP SYN Scan (-sS) - Padrão e Recomendado

```bash
# Scan padrão do Nmap
nmap -sS 10.89.0.3

# Portas específicas
nmap -sS -p 80,443,22 10.89.0.3
```

**Como funciona:** Envia SYN, recebe SYN/ACK (aberta) ou RST (fechada), envia RST

**Vantagens:**
- ✅ Rápido e eficiente
- ✅ Stealth (não completa handshake)
- ✅ Funciona contra maioria dos hosts

**Requer:** Privilégios root/sudo

---

### 2. TCP Connect Scan (-sT)

```bash
# Usado automaticamente sem root
nmap -sT 10.89.0.3

# Ou forçar
sudo nmap -sT 10.89.0.3
```

**Como funciona:** Completa handshake TCP (3-way handshake)

**Quando usar:** Sem privilégios de root

**Desvantagens:** Mais lento, deixa logs nos servidores

---

### 3. UDP Scan (-sU)

```bash
# Scan UDP (lento!)
sudo nmap -sU -p 53,161,123 10.89.0.11

# UDP + TCP combinado
sudo nmap -sS -sU -p U:53,T:80,443 10.89.0.11
```

**Como funciona:** Envia pacote UDP vazio, ICMP Port Unreachable = fechada

**Importante no lab:** DNS (53), SNMP (161)

**Desvantagens:** Muito lento, muitos falsos positivos

---

### 4. Scan Agressivo (-A)

```bash
# Detecta SO, versão, scripts e traceroute
nmap -A 10.89.0.12
```

**Inclui:** `-sV -sC -O --traceroute`

**Quando usar:** Enumeração completa de um alvo específico

**Cuidado:** Muito ruidoso, usa muitos recursos

---

## 📦 Selecionando Portas

### Portas Comuns (Top 1000)

```bash
# Padrão: top 1000 portas
nmap -sS 10.89.0.3
```

---

### Portas Específicas

```bash
# Lista de portas
nmap -sS -p 21,22,80,443,3306 10.89.0.7

# Range
nmap -sS -p 1-1000 10.89.0.3

# Portas do lab
nmap -sS -p 21,22,25,53,80,445,1025,3306,6379,8025,9999 10.89.0.0/24
```

---

### Scan Completo de Portas

```bash
# Todas as 65535 portas (demorado!)
nmap -sS -p- 10.89.0.12

# Top 100 portas (rápido)
nmap -sS --top-ports 100 10.89.0.0/24

# Top 20 portas (muito rápido)
nmap -sS --top-ports 20 10.89.0.0/24
```

---

## ⚡ Controlando Velocidade

### Templates de Timing

```bash
# T2 - Polite (pentests)
nmap -sS -T2 10.89.0.3

# T3 - Normal (padrão)
nmap -sS 10.89.0.3

# T4 - Aggressive (lab - use este!)
nmap -sS -T4 10.89.0.3
```

| Template | Uso | Velocidade |
|----------|-----|------------|
| T0 (Paranoid) | IDS evasion | Muito lento |
| T1 (Sneaky) | IDS evasion | Lento |
| T2 (Polite) | Pentests reais | Médio |
| T3 (Normal) | Padrão | Normal |
| T4 (Aggressive) | **Lab** | Rápido ✅ |
| T5 (Insane) | Nunca usar | Muito rápido ⚠️ |

---

### Flags Avançadas

```bash
# Paralelismo
nmap -sS --min-parallelism 100 10.89.0.3

# Taxa de pacotes
nmap -sS --max-rate 1000 10.89.0.3

# Timeout por host
nmap -sS --host-timeout 5m 10.89.0.0/24
```

---

## 💻 Exemplos Práticos no Lab

### Exemplo 1: Scan Rápido de Portas Comuns

```bash
cd /root/nmap_results

# Scan rápido em toda a rede
nmap -sS -T4 --open -p 21,22,25,53,80,139,443,445,1025,3306,6379,8025,9999 \
     10.89.0.0/24 -oA 01_quick_ports
```

**Saída esperada:**
```
Nmap scan report for lab_nginx (10.89.0.3)
PORT   STATE SERVICE
80/tcp open  http

Nmap scan report for lab_ssh (10.89.0.5)
PORT   STATE SERVICE
22/tcp open  ssh

Nmap scan report for lab_pyserver (10.89.0.12)
PORT     STATE SERVICE
9999/tcp open  abyss

Nmap done: 256 IP addresses (10 hosts up) scanned in 3.21 seconds
```

---

### Exemplo 2: Scan Completo em Alvo Específico

```bash
# Todas as portas no alvo vulnerável
nmap -sS -p- -T4 lab_pyserver -oA 02_full_scan_vuln
```

**Tempo esperado:** ~2 minutos

**Saída:**
```
PORT     STATE SERVICE
9999/tcp open  abyss
```

---

### Exemplo 3: Scan de Serviços Específicos

```bash
# Apenas web servers
nmap -sS -p 80,443,8080,8443 10.89.0.0/24 -oA 03_web_services

# Apenas bancos de dados
nmap -sS -p 3306,5432,1433,6379 10.89.0.0/24 -oA 04_databases

# Apenas compartilhamento de arquivos
nmap -sS -p 21,445,139,2049 10.89.0.0/24 -oA 05_file_sharing
```

---

### Exemplo 4: Scan UDP para DNS

```bash
# DNS server (porta 53 UDP)
sudo nmap -sU -p 53 lab_dns -oA 06_udp_dns
```

**Importante:** UDP scans são MUITO lentos. Use apenas portas específicas!

---

### Exemplo 5: Top Ports para Reconhecimento Rápido

```bash
# Top 100 portas em todos os hosts
nmap -sS --top-ports 100 --open 10.89.0.0/24 -oA 07_top100

# Ver quais portas são consideradas "top"
nmap --top-ports 100 localhost -v -oG - | grep "Ports scanned"
```

---

### Exemplo 6: Scan com Detecção de SO e Versão

```bash
# Scan completo no vuln service
nmap -sS -sV -O -T4 -p9999 lab_pyserver -oA 08_vuln_detailed
```

**Saída esperada:**
```
PORT     STATE SERVICE VERSION
9999/tcp open  abyss?
| fingerprint-strings: 
|   NULL: 
|     ========================================
|     VulnService v0.0.2 (Build 2025-12-07)
|     Running on: Alpine Linux 3.18
|     Python: 3.11.6
```

---

## 📊 Interpretando Resultados

### Analisando Output

```bash
# Após scan: nmap -sS -p- lab_pyserver -oA scan

# Listar portas abertas
grep "open" scan.nmap

# Contar portas abertas
grep -c "open" scan.nmap

# Extrair só números de portas
grep "open" scan.nmap | awk '{print $1}' | cut -d'/' -f1

# Criar lista de portas para próximo scan
grep "open" scan.nmap | awk '{print $1}' | cut -d'/' -f1 | tr '\n' ',' | sed 's/,$//'
```

---

### Formato Grepable

```bash
# Arquivo .gnmap é mais fácil para parsing
grep "Ports:" scan.gnmap

# Extrair host e portas abertas
grep "Ports:" scan.gnmap | awk '{print $2, $5}'
```

---

## 🎓 Exercícios Práticos

### Exercício 1: Identificar Todos os Serviços Web

```bash
# Scan portas web em toda rede
nmap -sS -p 80,443,8080,8443,8025 --open 10.89.0.0/24 -oA ex1_web

# Quantos servidores web encontrou?
```
---

### Exercício 2: Full Port Scan em Múltiplos Alvos

```bash
# Scan completo em 3 alvos
nmap -sS -p- -T4 lab_ssh lab_mysql lab_pyserver -oA ex2_full

# Qual tem mais portas abertas?
for host in lab_ssh lab_mysql lab_pyserver; do
    echo -n "$host: "
    sed -n "/^Nmap scan report for $host/,/^Nmap scan report for /p" ex2_full.nmap | grep -c "open"
done
```

---

### Exercício 3: Comparação de Velocidade

```bash
# T2 vs T4
time nmap -sS -T2 -p 1-1000 lab_pyserver -oN ex3_t2.txt
time nmap -sS -T4 -p 1-1000 lab_pyserver -oN ex3_t4.txt

# Comparar diferença de tempo
```

**Pergunta:** Qual a diferença em segundos?

---

### Exercício 4: Pipeline Completo

```bash
# 1. Host discovery
nmap -sn 10.89.0.0/24 -oG - | grep "Up" | awk '{print $2}' > hosts.txt

# 2. Port scan nos hosts ativos
nmap -sS -p- -T4 -iL hosts.txt -oA ex4_complete

# 3. Extrair resumo
```

---

## ⚠️ Boas Práticas

### ✅ Faça

1. **Sempre salve resultados**
   ```bash
   nmap -sS -p- lab_pyserver -oA scan_$(date +%Y%m%d_%H%M%S)
   ```

2. **Use --open para focar no importante**
   ```bash
   nmap -sS --open -p- 10.89.0.0/24
   ```

3. **Combine com host discovery**
   ```bash
   nmap -sS -Pn --open -p 80,443,22 10.89.0.0/24
   ```

4. **Documente portas incomuns**
   - Porta 9999 no lab é suspeita
   - Sempre investigue portas não-padrão

5. **Use timing apropriado**
   - Lab: `-T4`
   - Pentest: `-T2` ou `-T3`

---

### ❌ Não Faça

1. **Scan UDP sem portas específicas**
   ```bash
   # ❌ Vai demorar HORAS
   nmap -sU -p- 10.89.0.0/24
   
   # ✅ Apenas portas conhecidas
   nmap -sU -p 53,161,123,137 10.89.0.0/24
   ```

2. **Usar -T5 (insane)**
   - Causa timeouts
   - Falsos negativos
   - Pode derrubar serviços

3. **Scan completo em grandes redes sem filtrar**
   ```bash
   # ❌ 65535 portas x 256 hosts = dias
   nmap -p- 10.89.0.0/24
   
   # ✅ Top ports primeiro
   nmap --top-ports 1000 10.89.0.0/24
   ```

4. **Ignorar estados filtered**
   - Indica firewall
   - Tente técnicas de bypass

---

## 📚 Referência Rápida

```bash
# === SCANS BÁSICOS ===
nmap -sS 10.89.0.3                    # SYN scan padrão
nmap -sT 10.89.0.3                    # Connect scan (sem root)
nmap -sU -p 53 10.89.0.11             # UDP scan

# === SELEÇÃO DE PORTAS ===
nmap -p 80,443 10.89.0.3              # Portas específicas
nmap -p 1-1000 10.89.0.3              # Range
nmap -p- 10.89.0.3                    # Todas (65535)
nmap --top-ports 100 10.89.0.3        # Top 100

# === VELOCIDADE ===
nmap -T4 10.89.0.3                    # Rápido (lab)
nmap -T2 10.89.0.3                    # Stealth (pentest)

# === FILTROS ===
nmap --open 10.89.0.3                 # Apenas abertas
nmap -Pn 10.89.0.3                    # Sem ping (assume up)

# === PORTAS DO LAB ===
nmap -p 21,2222,25,53,80,445,1025,3306,6379,8025,9999 10.89.0.0/24

# === ANÁLISE ===
grep "open" scan.nmap                 # Ver abertas
grep -c "open" scan.nmap              # Contar
grep "open" scan.nmap | awk '{print $1}'  # Só portas
```

---

## 🔗 Próximos Passos

Com as portas mapeadas:

1. **Continue:** [04 - Service Enumeration](04-service-enumeration.md)
2. **Pratique:** Complete os 4 exercícios
3. **Documente:** Liste portas abertas por host
4. **Explore:** Conecte manualmente com `nc` nas portas encontradas

---

## 📖 Recursos Adicionais

- [Nmap Port Scanning Basics](https://nmap.org/book/man-port-scanning-basics.html)
- [Nmap Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html)
- [Common Port Numbers](https://www.speedguide.net/ports.php)
