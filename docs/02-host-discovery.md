# 02 - Descoberta de Hosts (Host Discovery)

## 📋 Visão Geral

Host discovery é a primeira fase do reconhecimento: identificar quais IPs estão ativos na rede sem escanear todas as portas. Pense nisso como ver quais casas têm luzes acesas antes de bater na porta.

**Tempo:** 10-15 minutos | **Nível:** Iniciante

---

## 🎯 Por Que é Importante?

- **Eficiência:** Não perde tempo com IPs inativos
- **Stealth:** Menos ruído = menor chance de detecção
- **Mapeamento:** Visão geral da infraestrutura
- **Planejamento:** Identifica alvos prioritários

---

## 🛠️ Ferramentas do Lab

### Instaladas no Attacker

| Ferramenta | Uso Principal |
|------------|---------------|
| `nmap` | Discovery completo com múltiplas técnicas |
| `ping` | Teste manual ICMP |
| `nc` | Teste manual de portas TCP/UDP |

### Outras Ferramentas (Referência)

Se precisar instalar: `apt-get install masscan arp-scan fping netdiscover`

**💡 Para este lab, Nmap é suficiente para tudo!**

---

## 📚 Técnicas de Discovery (Nmap)

### 1. Scan Padrão (ARP + ICMP) - Recomendado

```bash
# Automático: Nmap escolhe a melhor técnica
nmap -sn 10.89.0.0/24
```

**No lab:** Usa ARP automaticamente (rede local) = mais rápido e confiável

---

### 2. ICMP Echo (Ping)

```bash
# ICMP Echo específico
nmap -sn -PE 10.89.0.0/24

# Apenas ICMP (sem ARP)
nmap -sn -PE --disable-arp-ping 10.89.0.0/24
```

**Quando usar:** Redes onde ICMP não é bloqueado

---

### 3. TCP SYN Ping - Bypass de Firewall

```bash
# Portas comuns do lab
nmap -sn -PS22,80,443,3306,9999 10.89.0.0/24

# Apenas web
nmap -sn -PS80,443 10.89.0.0/24
```

**Quando usar:** ICMP bloqueado ou para detectar serviços específicos

---

### 4. TCP ACK Ping

```bash
nmap -sn -PA80,443 10.89.0.0/24
```

**Quando usar:** Bypass de firewalls stateless

---

### 5. Combinação de Técnicas

```bash
# Maximizar detecção
nmap -sn -PE -PS80,443,22 -PA80,443 10.89.0.0/24
```

---

## 💻 Exemplos Práticos

### Descoberta Completa do Lab

```bash
cd /root/nmap_results

# Scan padrão (mais eficiente)
nmap -sn 10.89.0.0/24 -oA 01_host_discovery
```

**Saída esperada:**
```
Starting Nmap 7.95 ( https://nmap.org )
Nmap scan report for _gateway (10.89.0.1)
Host is up (0.000012s latency).
Nmap scan report for lab_nginx (10.89.0.3)
Host is up (0.000023s latency).
[... 10 hosts ...]
Nmap done: 256 IP addresses (12 hosts up) scanned in 2.15 seconds
```

---

### Scan por Hostnames (Mais Rápido)

```bash
# Apenas alvos conhecidos
nmap -sn lab_nginx lab_apache lab_ssh lab_ftp lab_mysql lab_redis lab_smb lab_smtp lab_dns lab_pyserver \
     -oA 02_targets_only
```

---

### Ajustando Velocidade

```bash
# Rápido (use no lab)
nmap -sn -T4 10.89.0.0/24

# Stealth (pentest real)
nmap -sn -T2 10.89.0.0/24
```

| Timing | Velocidade | Stealth | Tempo Lab |
|--------|------------|---------|-----------|
| T2 (Polite) | Médio | Alto | ~5 min |
| T3 (Normal) | Normal | Médio | ~2 min |
| T4 (Aggressive) | Rápido | Baixo | ~1 min |

---

### Teste Manual com Ping

```bash
# Um host
ping -c 4 lab_nginx

# Loop simples
for ip in {3..12}; do
    ping -c 1 -W 1 10.89.0.$ip &>/dev/null && echo "10.89.0.$ip UP"
done
```

---

### Teste Manual com Netcat

```bash
# Testar porta específica
nc -zv lab_nginx 80
nc -zv lab_pyserver 9999
```

---

## 📊 Analisando Resultados

### Formatos de Saída

Ao usar `-oA nome`, Nmap cria:

- `.nmap` - Legível (para humanos)
- `.gnmap` - Grepável (para scripts)
- `.xml` - Estruturado (para ferramentas)

### Extraindo Informações

```bash
# Contar hosts ativos
grep -c "Host is up" discovery.nmap

# Listar IPs
grep "Nmap scan report" discovery.nmap | awk '{print $NF}' | tr -d '()'

# Criar lista de alvos
grep "Nmap scan report" discovery.nmap | awk '{print $NF}' | tr -d '()' > targets.txt

# Ver MACs
grep "MAC Address" discovery.nmap
```

---

## 🎓 Exercícios Práticos

### Exercício 1: Descoberta Básica

```bash
# 1. Execute
nmap -sn 10.89.0.0/24 -oA ex1

# 2. Conte hosts
grep -c "Host is up" ex1.nmap

# 3. Liste IPs
grep "Nmap scan report" ex1.nmap | awk '{print $NF}' | tr -d '()'
```

**Pergunta:** Quantos hosts encontrou?

---

### Exercício 2: Comparar Técnicas

```bash
# Padrão vs TCP SYN
time nmap -sn 10.89.0.0/24 -oN test1.txt
time nmap -sn -PS80,443 --disable-arp-ping 10.89.0.0/24 -oN test2.txt

# Comparar
echo -n "Padrão: "; grep -c "Host is up" test1.txt
echo -n "TCP SYN: "; grep -c "Host is up" test2.txt
```

**Pergunta:** Qual foi mais rápido e por quê?

---

### Exercício 3: Pipeline de Discovery

```bash
# 1. Discovery
nmap -sn 10.89.0.0/24 -oA discovery

# 2. Extrair IPs (excluir gateway e attacker)
grep "Nmap scan report" discovery.nmap | \
    awk '{print $NF}' | tr -d '()' | \
    grep -v "10.89.0.[12]" > targets.txt

# 3. Ver resultado
cat targets.txt
```

---

## ⚠️ Boas Práticas

### ✅ Faça

- Sempre salve resultados: `nmap -sn 10.89.0.0/24 -oA discovery_$(date +%Y%m%d)`
- Use scan padrão em LANs: `nmap -sn 10.89.0.0/24`
- Ajuste timing: `-T4` no lab, `-T2` em pentest real
- Documente seus achados

### ❌ Não Faça

- Usar `-T5` em produção (muito agressivo)
- Confiar apenas em ICMP (pode ser bloqueado)
- Escanear sem salvar resultados
- Escanear sem autorização

---

## 🐛 Troubleshooting

### Nenhum host encontrado?

```bash
# Verificar sua rede
ip addr show eth0

# Testar conectividade
ping -c 1 10.89.0.1

# Forçar ARP
sudo nmap -sn -PR 10.89.0.0/24
```

---

### Scan muito lento?

```bash
# Aumentar velocidade
nmap -sn -T4 10.89.0.0/24

# Reduzir retransmissões
nmap -sn --max-retries 1 10.89.0.0/24
```

---

### Permission denied?

```bash
# Usar sudo
sudo nmap -sn 10.89.0.0/24
```

---

## 📚 Referência Rápida

```bash
# Discovery básico
nmap -sn 10.89.0.0/24

# Por hostnames
nmap -sn lab_nginx lab_mysql lab_pyserver

# Com timing
nmap -sn -T4 10.89.0.0/24

# Múltiplas técnicas
nmap -sn -PE -PS80,443 10.89.0.0/24

# Ping manual
ping -c 4 10.89.0.3

# Netcat test
nc -zv lab_pyserver 9999

# Extrair IPs
grep "Nmap scan report" scan.nmap | awk '{print $NF}' | tr -d '()'
```

---

## 🔗 Próximos Passos

Agora que identificou os hosts ativos:

1. **Continue:** [03 - Port Scanning](03-port-scanning.md)
2. **Pratique:** Executar os 3 exercícios acima
3. **Documente:** Criar sumário dos hosts encontrados

---

**📖 Recursos Adicionais:**
- [Nmap Host Discovery](https://nmap.org/book/man-host-discovery.html)
- [Nmap Timing](https://nmap.org/book/man-performance.html)
