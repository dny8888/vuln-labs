# 01 - Setup

Breve guia de preparação do ambiente para o laboratório.

## Objetivo

Descrever os passos necessários para configurar o ambiente local e os serviços do laboratório.

## Pré-requisitos

- Sistema operacional compatível (Linux recomendado)
- Docker e Docker Compose instalados
- Acesso ao repositório e permissões necessárias

## Passos de instalação

1. Clonar o repositório: `git clone <repo-url>`
2. Revisar `docker-compose.yaml` e ajustar variáveis conforme necessário
3. Subir os serviços: `docker compose up -d`
4. Verificar logs: `docker compose logs -f`

## Verificação

- Confirmar containers em execução: `docker ps`
- Testar conectividade com os serviços expostos

## Notas

TODO: detalhar passos específicos de cada serviço e exemplos de configuração.

