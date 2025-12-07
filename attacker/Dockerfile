FROM kalilinux/kali-rolling:latest

# Instala nmap de forma não interativa
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
       nmap \
       iputils-ping \
       dnsutils \
       iproute2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Garantir que o binário do nmap possa ser executado mesmo quando capacidades
# de arquivo (file capabilities) não estiverem disponíveis no host/overlayfs.
# Definimos o bit setuid no binário principal como fallback seguro para lab.
RUN if [ -f /usr/lib/nmap/nmap ]; then \
            chown root:root /usr/lib/nmap/nmap && \
            chmod 4755 /usr/lib/nmap/nmap || true; \
        fi

# Usuário e entrada ficam a cargo do docker-compose
CMD ["tail", "-f", "/dev/null"]
