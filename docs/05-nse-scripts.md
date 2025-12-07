# 05 - NSE Scripts

Resumo e exemplos de uso dos scripts NSE do Nmap para descoberta e detecção de vulnerabilidades.

## Objetivo

Explicar como usar scripts NSE para automação de enumeração e verificação de vulnerabilidades.

## Uso básico

- Executar um script: `nmap --script <script-name> -p <ports> <ip>`
- Executar categoria: `nmap --script vuln <ip>`

## Scripts comuns

- `http-enum`, `http-vuln*`, `smb-vuln*`, `ftp-vsftpd-backdoor`

## Exemplos

- `nmap -sV --script=http-enum -p80,443 <ip>`
- `nmap --script vuln -p- <ip>`

TODO: listar scripts recomendados e interpretar saídas.

