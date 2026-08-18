# Renato Claude Toolkit

Kit para compartilhar o ambiente de desenvolvimento do Claude Code.

## O que já vem neste pacote

- `master-developer`: Skill própria de orquestração.
- Regra global opcional em `global/CLAUDE.md`.
- Marketplace local pronto para teste.
- Scripts PowerShell para instalação e captura do inventário de Plugins.

## Estrutura

```text
renato-claude-toolkit/
├── .claude-plugin/
│   └── marketplace.json
├── plugins/
│   └── master-developer/
│       ├── .claude-plugin/plugin.json
│       └── skills/master-developer/SKILL.md
├── global/
│   └── CLAUDE.md
└── scripts/
    ├── install-kit.ps1
    ├── install-known-plugins.ps1
    └── export-installed-plugins.ps1
```

## Testar localmente

No PowerShell:

```powershell
claude plugin marketplace add .
enato-claude-toolkit
claude plugin install master-developer@renato-claude-toolkit
```

Depois:

```text
/skills
```

A Skill deve aparecer como:

```text
master-developer
```

## Compartilhar com seu amigo

Depois de colocar este diretório em um repositório GitHub, seu amigo poderá usar:

```text
/plugin marketplace add SEU_USUARIO/renato-claude-toolkit
/plugin install master-developer@renato-claude-toolkit
```

O marketplace é o mecanismo oficial do Claude Code para distribuir Plugins. O repositório do marketplace precisa conter `.claude-plugin/marketplace.json`.

## Plugins de terceiros

O inventário enviado pelo usuário confirmou **7 Plugins habilitados** no ambiente de origem: `deep-research`, `document-skills`, `frontend-design`, `pm-skills`, `reflexion`, `security-guidance` e `superpowers`. Os IDs completos e versões estavam no snapshot. fileciteturn0file0L3-L8

O instalador desta versão usa os IDs exatos do snapshot:

```text
deep-research@claude-community
document-skills@anthropic-agent-skills
frontend-design@claude-plugins-official
pm-skills@claude-code-skills
reflexion@context-engineering-kit
security-guidance@claude-plugins-official
superpowers@claude-plugins-official
```

As versões registradas no snapshot incluem Deep Research 1.3.1, PM Skills 2.11.1, Reflexion 3.0.0, Security Guidance 2.0.7 e Superpowers 6.3.0; Frontend Design aparece como `unknown` no inventário. fileciteturn0file0L3-L8 fileciteturn0file0L30-L36 fileciteturn0file0L45-L50 fileciteturn0file0L54-L60 fileciteturn0file0L63-L69

**Importante:** o kit não copia o conteúdo interno desses Plugins de terceiros. Ele registra/reinstala os Plugins pelas suas origens. Isso permite que cada Plugin continue sendo mantido pelo respectivo autor/marketplace.

O `pm-skills` do snapshot também declara um servidor MCP Atlassian; instalar o Plugin não significa necessariamente que seu amigo estará autenticado na conta Atlassian. O snapshot apenas registra que esse MCP existe no Plugin instalado. fileciteturn0file0L30-L40

## Capturar exatamente os Plugins do seu computador

Execute:

```powershell
.\scripts\export-installed-plugins.ps1
```

ou:

```powershell
claude plugin list --json > plugin-snapshot.json
```

O Claude Code fornece oficialmente `claude plugin list --json` para listar Plugins instalados, versão, marketplace de origem e status.

## Regra global

Plugins não carregam um `CLAUDE.md` na raiz do Plugin como contexto global. Se você quiser o comportamento global de "sempre informar Skills", copie o conteúdo de:

```text
global/CLAUDE.md
```

para:

```text
$HOME\.claude\CLAUDE.md
```

A `master-developer` continua sendo a Skill especializada.

## Publicação no GitHub

Depois de criar um repositório vazio no GitHub:

```powershell
cd .
enato-claude-toolkit
git init
git add .
git commit -m "feat: initial Claude Code toolkit"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/renato-claude-toolkit.git
git push -u origin main
```

Substitua `SEU_USUARIO` pelo seu usuário do GitHub.

## Atualizações

Quando você alterar a Master:

1. edite `plugins/master-developer/skills/master-developer/SKILL.md`;
2. incremente a versão em `plugin.json` e `marketplace.json`;
3. faça commit/push;
4. seu amigo pode atualizar o marketplace e o Plugin.

## Segurança

Só instale Plugins e marketplaces de fontes confiáveis. Plugins podem executar código com as permissões do usuário.
