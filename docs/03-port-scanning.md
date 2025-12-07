# 03 - Port Scanning

Guia sobre técnicas de varredura de portas e identificação de serviços.

## Objetivo

Mapear portas e serviços abertos nos hosts identificados.

## Tipos de scan

- TCP SYN scan (`-sS`)
- TCP connect scan (`-sT`)
- UDP scan (`-sU`)
- Scan rápido (`-F`), scan agressivo (`-A`)

## Comandos nmap úteis

- Scan TCP completo: `nmap -sS -p- -T4 <ip>`
- Scan com detecção de versão e scripts: `nmap -sV -sC -p80,443 <ip>`
- Scan UDP (mais lento): `nmap -sU -p 53,123 <ip>`

## Boas práticas

- Ajustar `-T` conforme estabilidade da rede
- Registrar tempos e resultados

TODO: adicionar exemplos de parsing e análise de resultados.

