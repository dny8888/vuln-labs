# 02 - Descoberta de Hosts

Guia para identificar hosts ativos na rede-alvo e mapear endereços IP.

## Objetivo

Detectar quais máquinas estão ativas e obter um inventário inicial.

## Ferramentas comuns

- `nmap`
- `arp-scan`
- `masscan`
- `fping`

## Comandos de exemplo

- Varredura ARP em rede local: `sudo arp-scan --localnet`
- Ping sweep com fping: `fping -a -g 192.168.1.0/24`
- Descoberta com nmap (host discovery): `nmap -sn 192.168.1.0/24`

## Observações

Anotar IPs, MACs e possíveis serviços expostos para análise posterior.

TODO: incluir exemplos de saída e interpretação.

