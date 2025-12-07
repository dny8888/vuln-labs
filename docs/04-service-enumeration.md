# 04 - Service Enumeration

Procedimentos para identificar serviços, versões e possíveis vetores de ataque.

## Objetivo

Coletar informações detalhadas sobre serviços (HTTP, SMB, FTP, SSH, etc.).

## Ferramentas

- `nmap` (scripts de enumeração)
- `nikto`, `whatweb`, `gobuster` para web
- `smbclient`, `enum4linux` para SMB

## Exemplos rápidos

- Enumeração HTTP: `gobuster dir -u http://<ip> -w wordlist.txt`
- Enumeração SMB: `enum4linux -a <ip>`
- Teste de banner: `nmap -sV --script=banner <ip>`

## Coletando evidências

Salvar respostas HTTP, banners e listagens em arquivos para o relatório.

TODO: incluir exemplos de parsing e scripts úteis.

