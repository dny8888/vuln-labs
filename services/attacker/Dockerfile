FROM kalilinux/kali-rolling:latest

LABEL maintainer="dny8888@gmail.com"
LABEL description="Kali Linux container optimizado para pentesting lab"
LABEL version="1.0"

# Configuração de ambiente
ENV DEBIAN_FRONTEND=noninteractive \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    TZ=America/Sao_Paulo
# ============================================================================
# CAMADA 1: Atualização do sistema e instalação de ferramentas essenciais
# ============================================================================
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    # === Core Tools ===
    curl \
    wget \
    vim \
    # === Network Tools ===
    nmap \
    netcat-traditional \
    net-tools \
    iputils-ping \
    dnsutils \
    iproute2 \
    traceroute \
    # === Additional Pentesting Tools ===
    mariadb-client-compat \
    redis-tools \
    sshpass \
    ftp \
    smbclient \
    # === Password Tools ===
    hydra \
    python3 \
    && \
    # Limpar cache do apt
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# ============================================================================
# CAMADA 2: Configurações e otimizações do Nmap
# ============================================================================
RUN if [ -f /usr/lib/nmap/nmap ]; then \
        chown root:root /usr/lib/nmap/nmap && \
        chmod 4755 /usr/lib/nmap/nmap || true; \
    fi && \
    # Atualizar scripts NSE
    nmap --script-updatedb

# ============================================================================
# CAMADA 3: Configurações de usuário e ambiente
# ============================================================================

# Criar diretórios de trabalho
RUN mkdir -p /root/nmap_results \
             /root/exploits \
             /root/loot \
             /root/wordlists \
             /root/scripts \
             /root/.config

# Configurar aliases úteis
RUN echo 'alias ll="ls -lath"' >> /root/.bashrc && \
    echo 'PS1="\[\e[31m\]\u\[\e[m\]@\[\e[32m\]attacker\[\e[m\]:\[\e[34m\]\w\[\e[m\]\\$ "' >> /root/.bashrc

# Configurar vim básico
RUN echo 'syntax on' >> /root/.vimrc && \
    echo 'set number' >> /root/.vimrc && \
    echo 'set tabstop=4' >> /root/.vimrc && \
    echo 'set expandtab' >> /root/.vimrc && \
    echo 'set autoindent' >> /root/.vimrc

# ============================================================================
# CAMADA 4: Configurações finais
# ============================================================================

# Definir diretório de trabalho padrão
WORKDIR /root

# Expor portas úteis (caso necessário para reverse shells, etc)
# Não expomos por padrão para manter isolamento
# EXPOSE 4444 4445

# Healthcheck (verificar se container está respondendo)
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD ping -c 1 10.89.0.1 > /dev/null || exit 1

# Comando padrão (mantém container vivo)
CMD ["tail", "-f", "/dev/null"]
# Fim do Dockerfile
