# 01 - Setup do Laboratório

## 📋 Visão Geral

Este guia cobre a instalação completa do vuln-labs, desde os pré-requisitos até a verificação do ambiente funcionando.

**Tempo estimado:** 15-20 minutos

---

## ✅ Pré-requisitos

### Hardware Mínimo

| Recurso | Mínimo | Recomendado |
|---------|--------|-------------|
| CPU | 2 cores | 4+ cores |
| RAM | 4GB | 8GB+ |
| Disco | 10GB livre | 20GB+ livre |
| Rede | Conexão internet (setup inicial) | - |

### Software Necessário

1. **Docker Engine** (versão 20.10+)
2. **Docker Compose** (versão 2.0+)
3. **Git** (para clonar o repositório)

---

## 🐳 Instalação do Docker

### Linux (Ubuntu/Debian)

```bash
# Remover versões antigas (se existir)
sudo apt-get remove docker docker-engine docker.io containerd runc

# Instalar dependências
sudo apt-get update
sudo apt-get install -y ca-certificates curl gnupg lsb-release

# Adicionar chave GPG oficial do Docker
sudo mkdir -m 0755 -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Adicionar repositório
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Instalar Docker
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Adicionar usuário ao grupo docker (evita usar sudo)
sudo usermod -aG docker $USER

# Aplicar mudanças (logout e login novamente ou use)
newgrp docker
```

### macOS

```bash
# Instalar Docker Desktop via Homebrew
brew install --cask docker

# Ou baixar Docker Desktop manualmente:
# https://www.docker.com/products/docker-desktop
```

### Windows

1. Baixe [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop)
2. Instale e reinicie o sistema
3. Habilite WSL 2 backend (recomendado)

---

## 📥 Instalação do Lab

### 1. Clonar o Repositório

```bash
# Clonar via HTTPS
git clone https://github.com/dny8888/vuln-labs.git
cd vuln-labs

# Ou via SSH (se configurado)
git clone git@github.com:dny8888/vuln-labs.git
cd vuln-labs
```

### 2. Verificar Estrutura

```bash
# Listar arquivos
ls -la

# Estrutura esperada:
# docker-compose.yaml
# attacker/
# vuln_service/
# dnsmasq/
# docs/
# README.md
```

### 3. Construir e Iniciar

```bash
# Construir imagens e subir containers
docker compose up -d --build

# Flags explicadas:
# -d: modo detached (background)
# --build: força rebuild das imagens
```

**Saída esperada:**

```
[+] Building 45.2s (12/12) FINISHED
[+] Running 11/11
 ✔ Network vuln-labs_labnet        Created
 ✔ Container lab_attacker           Started
 ✔ Container lab_nginx              Started
 ✔ Container lab_apache             Started
 ✔ Container lab_ssh                Started
 ✔ Container lab_ftp                Started
 ✔ Container lab_mysql              Started
 ✔ Container lab_redis              Started
 ✔ Container lab_smb                Started
 ✔ Container lab_smtp               Started
 ✔ Container lab_dns                Started
 ✔ Container lab_pyserver               Started
```

---

## ✔️ Verificação do Ambiente

### 1. Verificar Containers Ativos

```bash
# Listar todos os containers
docker compose ps

# Ou com mais detalhes
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
```

**Saída esperada:**

```
NAMES         STATUS                  PORTS
lab_attacker  Up 8 minutes
lab_nginx     Up 8 minutes            80/tcp
lab_apache    Up 8 minutes            80/tcp
lab_ssh       Up 8 minutes            2222/tcp
lab_ftp       Up 8 minutes            21/tcp, 21000-21010/tcp
lab_mysql     Up 8 minutes            3306/tcp, 33060/tcp
lab_redis     Up 8 minutes            6379/tcp
lab_smb       Up 8 minutes (healthy)  139/tcp, 445/tcp, 137-138/udp
lab_smtp      Up 8 minutes            1025/tcp, 8025/tcp
lab_dns       Up 8 minutes            53/tcp, 53/udp
lab_pyserver      Up 8 minutes            9999/tcp
```

### 2. Verificar Logs (Troubleshooting)

```bash
# Ver logs de todos os containers
docker compose logs

# Logs de um container específico
docker compose logs lab_pyserver

# Seguir logs em tempo real
docker compose logs -f lab_attacker
```

### 3. Entrar no Container Atacante

```bash
# Acessar shell do Kali Linux
docker exec -it lab_attacker /bin/bash

# Você deve ver o prompt:
# root@<container-id>:~#
```

### 4. Verificar Conectividade Interna

**Dentro do container atacante:**

```bash
# Verificar IP do atacante
ip addr show eth0 | grep inet
# Esperado: inet 10.89.0.2/24

# Testar conectividade com outros hosts
ping -c 2 10.89.0.3  # lab_nginx
ping -c 2 lab_pyserver   # usando DNS interno

# Verificar resolução DNS
nslookup lab_mysql
getent hosts lab_ssh

# Testar porta específica
nc -zv lab_pyserver 9999
# Esperado: lab_pyserver [10.89.0.12] 9999 (?) open
```

### 5. Teste Rápido de Scan

```bash
# Dentro do atacante
nmap -sn 10.89.0.0/24

# Deve mostrar todos os 11 hosts (incluindo gateway)
```

---

## 🔧 Configurações Opcionais

### Ajustar Recursos dos Containers

Edite `docker-compose.yaml` para limitar recursos:

```yaml
services:
  attacker:
    # ... configuração existente ...
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 2G
        reservations:
          memory: 512M
```

### Expor Portas para o Host (Cuidado!)

**⚠️ Não recomendado para ambiente real!**

Para acessar serviços do host (ex: MySQL Workbench):

```yaml
mysql:
  # ... configuração existente ...
  ports:
    - "3306:3306"  # Expõe MySQL no host
```

---

## 🛑 Parar e Remover o Lab

### Parar Containers (Manter Dados)

```bash
docker compose stop
```

### Parar e Remover (Limpar Tudo)

```bash
# Remove containers, rede e volumes
docker compose down --volumes

# Para também remover imagens construídas
docker compose down --volumes --rmi all
```

### Limpar Sistema Completamente

```bash
# Remover containers parados
docker container prune -f

# Remover imagens não usadas
docker image prune -a -f

# Remover volumes não usados
docker volume prune -f

# Remover redes não usadas
docker network prune -f
```

---

## 🐛 Troubleshooting Comum

### Problema: "Cannot connect to the Docker daemon"

**Solução:**

```bash
# Verificar se Docker está rodando
sudo systemctl status docker

# Iniciar Docker
sudo systemctl start docker

# Habilitar no boot
sudo systemctl enable docker
```

### Problema: "port is already allocated"

**Causa:** Outra aplicação usando a mesma porta

**Solução:**

```bash
# Descobrir processo usando a porta
sudo lsof -i :9999
sudo netstat -tlnp | grep 9999

# Matar processo ou mudar porta no docker-compose.yaml
```

### Problema: Containers reiniciando continuamente

```bash
# Ver logs para identificar erro
docker compose logs <container-name>

# Exemplo comum: falta de memória
# Solução: aumentar RAM disponível ou limitar containers
```

### Problema: DNS não resolve nomes internos

**Dentro do atacante:**

```bash
# Verificar arquivo resolv.conf
cat /etc/resolv.conf

# Deve conter o IP do container DNS (10.89.0.11)

# Testar DNS manualmente
nslookup lab_pyserver 10.89.0.11
```

**Se não funcionar:**

```bash
# No host, reiniciar container DNS
docker compose restart lab_dns

# Verificar logs do DNS
docker compose logs lab_dns
```

---

## 📚 Próximos Passos

Agora que o lab está funcionando:

1. ✅ Leia [02 - Descoberta de Hosts](02-host-discovery.md)
2. ✅ Explore [03 - Port Scanning](03-port-scanning.md)
3. ✅ Tente os [Desafios CTF](../CHALLENGES.md) *(em breve)*

---

## 🆘 Suporte

Problemas não resolvidos?

- 🐛 Abra uma [issue no GitHub](https://github.com/dny8888/vuln-labs/issues)
- 💬 Use as [Discussions](https://github.com/dny8888/vuln-labs/discussions)
- 📧 Consulte a [documentação do Docker](https://docs.docker.com/)

---

**Última atualização:** 2024-12-07