# Renato Claude Toolkit

Marketplace pessoal para o Claude Code. A Master Developer v2 coordena pedidos compostos, consulta um catálogo das capacidades instaladas e registra continuidade em Markdown nos projetos que adotarem essa opção.

## O que vem no repositório

- `plugins/master-developer/`: skill de orquestração, regras de roteamento e coletor de metadados em Python 3.10+.
- `.claude-plugin/marketplace.json`: catálogo do marketplace.
- `global/CLAUDE.md`: orientação global opcional e curta.
- `templates/project-memory/`: exemplo de memória por projeto.
- `scripts/`: instalação e exportação do inventário de plugins.

A Master não incorpora plugins de terceiros. Ela descobre metadados da instalação presente. Um candidato encontrado no catálogo ainda precisa estar exposto na sessão para ser invocado. O coletor não executa hooks, agentes ou MCPs.

## Teste local antes de instalar

Na raiz deste repositório:

```powershell
claude plugin validate .
claude plugin validate ./plugins/master-developer
claude --plugin-dir ./plugins/master-developer
python -m unittest discover -s tests -v
```

Na sessão, experimente `/master-developer:master-developer`. O uso de `--plugin-dir` vale somente para essa sessão; ele pode testar uma cópia local com o mesmo nome de um plugin já instalado. Consulte a [documentação oficial de plugins](https://code.claude.com/docs/en/plugins) para as regras de precedência.

## Instalação e atualização

Depois de publicar esta versão no repositório do marketplace:

```powershell
claude plugin marketplace update renato-claude-toolkit
claude plugin update master-developer@renato-claude-toolkit --scope user
```

Em uma instalação nova:

```powershell
claude plugin marketplace add renatomoraeeees/renato-claude-toolkit
claude plugin install master-developer@renato-claude-toolkit --scope user
```

Recarregue os plugins ou inicie outra sessão. O identificador para invocação explícita é `/master-developer:master-developer`. A versão do plugin é definida em `plugins/master-developer/.claude-plugin/plugin.json`; incremente esse campo a cada lançamento para que o Claude Code detecte a atualização. O cache em `~/.claude/plugins/cache` é gerenciado pelo Claude Code e não deve ser editado manualmente. Veja a [referência de versionamento](https://code.claude.com/docs/en/plugins-reference).

## Catálogo e memória

Para criar ou atualizar o catálogo de um projeto:

```powershell
python plugins/master-developer/scripts/catalog.py refresh --project .
python plugins/master-developer/scripts/catalog.py search --project . --query "saúde orçamento cronograma"
```

O catálogo local contém caminhos e metadados da instalação; não o publique. Um índice Markdown pequeno permite consultar somente as páginas relevantes. A Master distingue capacidade instalada, anunciada na sessão e efetivamente invocada.

Para continuidade, use [o modelo por projeto](templates/project-memory/CLAUDE.md). Ele grava estado em `memory/` após marcos relevantes e o relê na sessão seguinte. Configure permissão de escrita apenas para esse diretório quando rodar o Claude Code sem perguntas. Claude-Mem, ECC e memória nativa podem coexistir como fontes; atribua um único responsável pela camada Markdown curada e evite hooks duplicados.

## Limites do ensaio

A versão v2 foi testada com uma instalação que continha 15 plugins e centenas de skills. Um piloto restrito carregou apenas a Master e PM Skills: confirmou invocação do especialista, gravação do estado Markdown e retomada em sessão separada. Esse ensaio não confirma comportamento simultâneo de todos os plugins, saúde de MCPs e hooks, nem instalação global.

## Manutenção

Atualize o plugin, valide o marketplace, aumente a versão de `plugin.json` e revise o efeito sobre o catálogo. Não copie configurações globais automaticamente: o arquivo `global/CLAUDE.md` é opcional e deve ser incorporado às regras existentes sem sobrescrevê-las.
