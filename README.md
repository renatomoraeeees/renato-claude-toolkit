# Renato Claude Toolkit

Marketplace pessoal para o Claude Code. A Master Developer v2.1.1 entra automaticamente em tarefas de desenvolvimento, coordena o trabalho e invoca de fato as skills especializadas pela tool `Skill`. O catálogo continua sendo usado para descoberta; ele não é tratado como execução.

## O que mudou na v2.1.1

- Auto-trigger ampliado para implementação, bugs, revisão, refatoração, arquitetura, frontend, backend, APIs, testes, automação e documentação técnica.
- `disable-model-invocation: false` explícito na Master Developer.
- Protocolo obrigatório de chamada pela tool `Skill` para cada especialista selecionado e aplicável.
- Separação clara entre capacidade catalogada, anunciada na sessão e invocada com sucesso.
- Fallback explícito quando a tool ou a skill não está disponível, sem simular execução por leitura de `SKILL.md`.

## O que vem no repositório

- `plugins/master-developer/`: skill de orquestração, regras de roteamento e coletor de metadados em Python 3.10+.
- `.claude-plugin/marketplace.json`: catálogo do marketplace.
- `global/CLAUDE.md`: orientação global opcional e curta.
- `templates/project-memory/`: exemplo de memória por projeto.
- `scripts/`: instalação e exportação do inventário de plugins.

A Master não incorpora plugins de terceiros. Ela descobre metadados da instalação presente e usa a tool `Skill` para carregar as skills escolhidas. Um candidato encontrado no catálogo ainda precisa estar exposto na sessão e ter sua chamada confirmada. O coletor não executa skills, hooks, agents ou MCPs.

## Como o roteamento funciona

1. A Master identifica as etapas reais do pedido.
2. Quando necessário, consulta o catálogo para descobrir candidatas.
3. Confirma o identificador qualificado anunciado na sessão.
4. Invoca cada skill selecionada pela tool `Skill`.
5. Aplica as instruções carregadas, executa o trabalho e valida o resultado.

Encontrar `plugin:skill` no catálogo, mencionar seu nome, ler seu arquivo ou imprimir `/plugin:skill` não conta como invocação. Skills manuais, agents, hooks e MCPs mantêm seus mecanismos próprios.

## Teste local antes de instalar

Na raiz deste repositório:

```powershell
claude plugin validate .
claude plugin validate ./plugins/master-developer
claude --plugin-dir ./plugins/master-developer
python -m unittest discover -s tests -v
```

Na sessão, experimente `/master-developer:master-developer` para o acionamento manual e faça também um pedido normal de desenvolvimento para observar o auto-trigger. No trace da sessão, confirme uma chamada da tool `Skill` para a Master e, quando houver especialista aplicável, outra chamada com o identificador qualificado desse especialista. A simples aparição do nome no catálogo não comprova a execução.

O uso de `--plugin-dir` vale somente para essa sessão; ele pode testar uma cópia local com o mesmo nome de um plugin já instalado. Consulte a [documentação oficial de plugins](https://code.claude.com/docs/en/plugins) para as regras de precedência.

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

Recarregue os plugins ou inicie outra sessão. O identificador qualificado da tool `Skill` é `master-developer:master-developer`; a forma manual é `/master-developer:master-developer`. A versão do plugin é definida em `plugins/master-developer/.claude-plugin/plugin.json`; incremente esse campo a cada lançamento para que o Claude Code detecte a atualização. O cache em `~/.claude/plugins/cache` é gerenciado pelo Claude Code e não deve ser editado manualmente. Veja a [referência de versionamento](https://code.claude.com/docs/en/plugins-reference).

## Catálogo e memória

Para criar ou atualizar o catálogo de um projeto:

```powershell
python plugins/master-developer/scripts/catalog.py refresh --project .
python plugins/master-developer/scripts/catalog.py search --project . --query "saúde orçamento cronograma"
```

O catálogo local contém caminhos e metadados da instalação; não o publique. Um índice Markdown pequeno permite consultar somente as páginas relevantes. A Master distingue capacidade catalogada, anunciada na sessão e efetivamente invocada pela tool `Skill`.

Para continuidade, use [o modelo por projeto](templates/project-memory/CLAUDE.md). Ele grava estado em `memory/` após marcos relevantes e o relê na sessão seguinte. Configure permissão de escrita apenas para esse diretório quando rodar o Claude Code sem perguntas. Claude-Mem, ECC e memória nativa podem coexistir como fontes; atribua um único responsável pela camada Markdown curada e evite hooks duplicados.

## Limites do ensaio

A linha v2 foi testada com uma instalação que continha 15 plugins e centenas de skills. Um piloto restrito carregou apenas a Master e PM Skills: confirmou invocação do especialista, gravação do estado Markdown e retomada em sessão separada. Para a v2.1.1, valide separadamente o auto-trigger e as chamadas da tool `Skill` no trace de uma nova sessão; testes estáticos do repositório não comprovam o roteamento do modelo em runtime. Esses ensaios não confirmam comportamento simultâneo de todos os plugins, saúde de MCPs e hooks, nem instalação global.

## Manutenção

Atualize o plugin, valide o marketplace e mantenha sincronizadas as versões de `plugins/master-developer/.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` e do coletor. Revise também o efeito sobre o catálogo. Não copie configurações globais automaticamente: o arquivo `global/CLAUDE.md` é opcional e deve ser incorporado às regras existentes sem sobrescrevê-las.
