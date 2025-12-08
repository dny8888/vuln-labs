## 📝 Descrição

<!-- Descreva suas mudanças de forma clara e concisa -->

Closes #(issue)

## 🎯 Tipo de Mudança

<!-- Marque com [x] todas as opções que se aplicam -->

- [ ] 🐛 Bug fix (non-breaking change que corrige uma issue)
- [ ] ✨ Nova feature (non-breaking change que adiciona funcionalidade)
- [ ] 💥 Breaking change (fix ou feature que causaria quebra de funcionalidade existente)
- [ ] 📝 Documentação
- [ ] 🎨 Style (formatação, renomeação)
- [ ] ♻️ Refatoração (nem fix nem feature)
- [ ] ⚡ Performance
- [ ] ✅ Testes
- [ ] 🔧 Configuração (build, CI/CD, etc.)

## 💭 Motivação e Contexto

<!-- Por que essa mudança é necessária? Qual problema resolve? -->

## 🧪 Como Foi Testado?

<!-- Descreva os testes que você realizou -->

- [ ] Testei localmente com `docker compose up`
- [ ] Testei em ambiente limpo (fresh clone)
- [ ] Testei em [sistema operacional]
- [ ] Verifiquei que não quebra funcionalidades existentes

**Comandos de teste executados:**
```bash
# Cole os comandos de teste aqui

```

**Resultados dos testes:**
```
[Cole os resultados aqui]
```

## 📸 Screenshots (se aplicável)

<!-- Adicione screenshots das mudanças visuais -->

### Antes
<!-- Screenshot do comportamento anterior -->

### Depois
<!-- Screenshot do novo comportamento -->

## 📋 Checklist

<!-- Marque com [x] todos os itens concluídos -->

### Geral
- [ ] Meu código segue o style guide deste projeto
- [ ] Realizei self-review do meu código
- [ ] Comentei código complexo ou não óbvio
- [ ] Minhas mudanças não geram novos warnings
- [ ] Adicionei testes que provam que minha correção/feature funciona
- [ ] Testes unitários novos e existentes passam localmente

### Documentação
- [ ] Atualizei a documentação relevante (README, docs/, etc.)
- [ ] Atualizei CHANGELOG.md (se aplicável)
- [ ] Adicionei comentários no código onde necessário
- [ ] Verifiquei que os links da documentação funcionam

### Docker/Compose
- [ ] Testei build de todas as imagens afetadas
- [ ] Verifiquei que containers iniciam corretamente
- [ ] Testei conectividade entre containers (se aplicável)
- [ ] Verifiquei que não há exposição acidental de portas

### Segurança (se aplicável)
- [ ] Não commitei secrets, senhas ou chaves
- [ ] Verifiquei que mudanças não introduzem vulnerabilidades não intencionais
- [ ] Atualizei .gitignore (se necessário)
- [ ] Revisei imagens Docker por vulnerabilidades conhecidas

### Git
- [ ] Commits seguem padrão [Conventional Commits](https://www.conventionalcommits.org/)
- [ ] Branch está atualizada com `main`
- [ ] Resolvi todos os conflitos de merge
- [ ] Adicionei meu nome ao CONTRIBUTORS.md (se primeira contribuição)

## 🔗 Issues Relacionadas

<!-- Liste issues relacionadas -->
- Fixes #(issue number)
- Related to #(issue number)
- Part of #(issue number)

## 📚 Referências

<!-- Links para documentação, artigos, ou recursos usados -->

## ⚠️ Breaking Changes

<!-- Se há breaking changes, descreva-as aqui -->
<!-- Como usuários devem migrar suas configurações? -->

## 📊 Impacto

<!-- Descreva o impacto das mudanças -->

**Componentes afetados:**
- [ ] Attacker container
- [ ] Vuln service
- [ ] Docker Compose config
- [ ] Documentation
- [ ] Scripts
- [ ] Outro: ___________

**Backwards compatibility:**
- [ ] ✅ Totalmente compatível
- [ ] ⚠️ Requer migração (documentei no PR)
- [ ] ❌ Breaking change (documentei no PR)

## 🤔 Dúvidas/Discussão

<!-- Há algo que você gostaria de discutir? -->
<!-- Alternativas que considerou? -->
<!-- Decisões de design que gostaria de feedback? -->

## 📝 Notas para Reviewers

<!-- Informações úteis para quem vai revisar -->
<!-- Áreas específicas onde gostaria de feedback -->

---

## ✅ Checklist para Maintainers

<!-- NÃO preencher - apenas para maintainers -->

- [ ] Code review completo
- [ ] Testado localmente
- [ ] Documentação revisada
- [ ] Labels apropriadas adicionadas
- [ ] Milestone definido (se aplicável)
- [ ] CHANGELOG.md atualizado
- [ ] Pronto para merge
