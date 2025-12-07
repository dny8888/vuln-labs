# 🎯 DOCKER-LAB - Pentest Training Environment

[![Docker](https://img.shields.io/badge/Docker-Required-blue)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)]()

> Ambiente Docker completo para treinamento em Nmap e técnicas de Red Team

## 🌟 Features

- 🐳 **10+ serviços vulneráveis** isolados em containers
- 🎓 **Desafios CTF progressivos** (iniciante → avançado)
- 🤖 **Scripts de automação** para scans e análises
- 📊 **Análise de resultados** com Python
- 📚 **Documentação completa** com exemplos práticos
- 🔒 **Totalmente offline** e seguro para aprendizado

[Demo Video](todo) | [Challenges](comming_soon) | [Documentation](comming_soon)

------------

## NMAP-LAB — README.md

> Laboratório Docker para treinar **nmap** (tudo executado **a partir do shell do pod atacante**).
> Objetivo: simular uma campanha de reconhecimento e enumeração de uma rede interna composta por containers (cada “pod” = container).
> **IMPORTANTE:** use **apenas** em ambiente controlado / de teste. Não realize scans em redes/hosts sem autorização explícita.

---

## Aviso inicial — entre no pod atacante

Antes de qualquer coisa **entre no shell do pod/contêiner atacante** (assume-se que o `docker-compose up -d --build` já foi executado no host e o lab está no ar):

No host (apenas para entrar no atacante):

```bash
docker exec -it lab_attacker /bin/bash
```

A partir desse shell **todos** os comandos abaixo devem ser executados. Não execute os comandos `nmap` no host — execute-os dentro do pod atacante.

---

# Sumário

1. Preparação (dentro do atacante)
2. Descoberta de rede / coleta de informações iniciais
3. Descoberta de hosts (host discovery)
4. Descoberta de portas (port scan)
5. Enumeração de serviços/versões (service/version)
6. Execução de scripts NSE e enumerações específicas
7. Varredura UDP e scans avançados
8. Salvar/Exportar resultados e análise
9. Checklists de testes práticos
10. Boas práticas e segurança
11. Limpeza do lab (nota sobre host)

---

## 1 — Preparação (dentro do atacante)

Crie um diretório para salvar resultados dentro do container atacante:

```sh
mkdir -p /root/nmap_results
cd /root/nmap_results
```

Verifique se o `nmap` está disponível:

```sh
nmap --version
```
---

## 2 — Coleta de informações iniciais (somente dentro do atacante)

Descubra o IP do seu próprio container e a interface de rede (útil para entender a sub-rede do lab):

```sh
ip -4 addr show eth0
# ex: 172.18.0.2/24
```

Descubra a rota (ajuda a ver a máscara/rede):

```sh
ip -4 route
# ex: default via 172.18.0.1 dev eth0  proto static
```

Teste resolução de nomes internos (os nomes dos serviços do docker-compose normalmente resolvem via DNS interna):

```sh
ping -c1 lab_nginx
ping -c1 lab_vuln
getent hosts lab_nginx || true
```

Se `ip` mostra `172.18.0.2/24`, o range provável é `172.18.0.0/24`. Substitua por sua sub-rede real quando for rodar scans.

---

## 3 — Descoberta de hosts (Host discovery) — tudo dentro do atacante

Objetivo: identificar hosts ativos.

Varredura simples (ping sweep) na sub-rede (substitua SUBNET pela sua rede, ex: `172.18.0.0/24`):

```sh
SUBNET="172.18.0.0/24"
nmap -sn $SUBNET -oA host_discovery
# Saídas: host_discovery.nmap, host_discovery.gnmap, host_discovery.xml
```

Varredura por nomes (útil porque nomes do compose resolvem):

```sh
nmap -sn lab_nginx lab_apache lab_ssh lab_ftp lab_mysql lab_redis lab_smb lab_smtp lab_dns lab_vuln -oA host_by_name
```

O que anotar: lista de IPs e nomes que aparecem como `Host is up`.

---

## 4 — Descoberta de portas (Port scan) — dentro do atacante

Objetivo: identificar portas abertas em cada host.

### 4.1 Scan rápido em portas comuns para toda a sub-rede

```sh
nmap -sS -Pn -T4 --open -p 21,22,25,53,80,139,443,445,3306,6379,9999 $SUBNET -oA quick_ports
```

* `-sS`: TCP SYN scan
* `-Pn` : não faz host discovery (útil em rede isolada do lab)
* `--open`: mostra apenas portas abertas

### 4.2 Scan completo de todas as portas em um alvo específico (ex.: lab_vuln)

Use o nome do container (DNS interna) ou o IP:

```sh
TARGET="lab_vuln"
nmap -sS -p- -T4 $TARGET -oA full_ports_$TARGET
```

`-p-` varre portas 0-65535.

---

## 5 — Enumeração de serviços e versões (Service/version) — dentro do atacante

Objetivo: obter banners, versões e detectar SO (quando possível).

Exemplo em um alvo específico:

```sh
TARGET="lab_vuln"
nmap -sS -sV -sC -O -T4 $TARGET -oA svc_enum_$TARGET
```

* `-sV`: detecta versão do serviço
* `-sC`: roda scripts NSE padrão (`--script=default`)
* `-O`: tenta detectar o sistema operacional (containers podem confundir OSD)

Interprete o campo `SERVICE` / `VERSION` para procurar software e versões (pesquise CVEs offline em seguida).

---

## 6 — Execução de scripts NSE e enumerações específicas — dentro do atacante

Rodar scripts NSE focados em serviços descobertos (USE SOMENTE NO LAB).

### SSH (banner, hostkey, métodos de auth)

```sh
nmap -p22 --script=ssh-hostkey,ssh-auth-methods $TARGET -oA ssh_enum_$TARGET
```

### SMB (shares, info)

```sh
SMB_TARGET="lab_smb"
nmap -p445 --script=smb-enum-shares,smb-os-discovery $SMB_TARGET -oA smb_enum
```

### MySQL (informações básicas)

```sh
MYSQL_TARGET="lab_mysql"
nmap -p3306 --script=mysql-info $MYSQL_TARGET -oA mysql_info
```

### Scan de vulnerabilidades genérico (informativo)

```sh
nmap -sV --script=vuln $TARGET -oA vuln_scan_$TARGET
```

`--script=vuln` executa scripts que detectam vulnerabilidades conhecidas — revisões manuais são necessárias (falsos positivos existem).

---

## 7 — Varredura UDP e scans avançados — dentro do atacante

UDP é lento — ajuste `-T`/timeouts.

Exemplo para DNS (porta 53) e SNMP (161):

```sh
nmap -sU -p53,161 -T3 $SUBNET -oA udp_scan
```

Combinar TCP+UDP (cuidado com tempo):

```sh
nmap -sS -sU -p U:53,161,T:22,80,443 $TARGET -oA tcp_udp_combo_$TARGET
```

---

## 8 — Salvar/Exportar resultados e análise — dentro do atacante

Nós já usamos `-oA` para salvar em três formatos. Exemplos de comandos para análise rápida dentro do atacante:

```sh
# listar portas abertas rapidamente
grep -i "open" *.nmap

# procurar menções a "vuln" nos resultados de scripts
grep -i "vuln" *.nmap || true

```

Você pode copiar os arquivos do container para o host com `docker cp` (executar no host):

```bash
# no host, exemplo:
docker cp lab_attacker:/root/nmap_results ./nmap_results_from_container
```

---

## 9 — Checklists de testes práticos (sugestão de exercícios)

Execute e documente cada item — tudo a partir do shell do atacante:

1. `nmap -sn $SUBNET` — enumerar hosts vivos.
2. `nmap -sS --open -p 21,22,25,53,80,139,443,445,3306,6379,9999 $SUBNET` — mapear portas comuns.
3. Para `lab_vuln`: `nmap -sV -p9999 lab_vuln` — capturar banner, analisar.
4. `nmap -sS -sV -sC -O lab_vuln` — enumeração aprofundada.
5. `nmap --script=vuln -sV lab_vuln` — procurar indicadores de vulnerabilidade.
6. `nmap -p445 --script=smb-enum-shares lab_smb` — verificar shares SMB.
7. `nmap -sU -p53 $SUBNET` — verificar respostas UDP de DNS.
8. Salve tudo em `/root/nmap_results` e gere um breve relatório (anote IP, portas, serviços, versões e prioridades).

---

## 10 — Boas práticas e segurança (lembretes)

* Execute **somente** nesse lab isolado.
* Use `-T` apropriado (`-T3`/`-T4` em lab; evite `-T5` salvo se souber consequências).
* Guarde os resultados (`-oA`) para análise posterior.
* NSE `--script=vuln` é informativo — valide manualmente.
* Não exponha serviços vulneráveis para a internet.

---

## 11 — Limpeza / destruir o lab (nota importante)

A parada/removal dos containers e da rede **deve ser feita no host**, não a partir do pod atacante. No host:

```bash
docker-compose down --volumes --remove-orphans
```

Se você estiver ainda dentro do atacante e quiser sair:

```sh
exit
```

---

## Exemplo de sessão rápida (toda executada no shell do atacante)

```sh
# dentro do attacker
mkdir -p /root/nmap_results && cd /root/nmap_results
SUBNET=$(ip -4 addr show eth0 | awk '/inet /{print $2}' | sed 's#/[^/]*#/24#')
echo "subnet: $SUBNET"
nmap -sn $SUBNET -oA 01_host_discovery
nmap -sS -Pn -T4 --open -p 21,22,25,53,80,139,443,445,3306,6379,9999 $SUBNET -oA 02_quick_ports
TARGET="lab_vuln"
nmap -sS -sV -sC -O -T4 $TARGET -oA 03_service_enum_$TARGET
nmap --script=vuln -sV $TARGET -oA 04_vuln_scan_$TARGET
```

> Observação: o pequeno comando para determinar `SUBNET` faz uma suposição `/24` — verifique a máscara real com `ip -4 addr show eth0` e ajuste conforme necessário.

---

## Aviso Legal & Ético

Este README descreve técnicas de reconhecimento/enumeração usadas em testes de segurança. **Só realize essas ações em sistemas para os quais você tem autorização expressa.** Uso indevido de ferramentas de varredura em redes alheias pode ser ilegal.

