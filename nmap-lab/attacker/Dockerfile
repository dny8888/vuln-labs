FROM kalilinux/kali-rolling:latest

# Instala nmap de forma não interativa
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
       nmap \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Usuário e entrada ficam a cargo do docker-compose (mantemos padrão)
CMD ["/bin/sh", "-c", "tail -f /dev/null"]
