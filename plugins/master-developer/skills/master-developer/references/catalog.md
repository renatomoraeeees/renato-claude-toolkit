# Catálogo executável

O script requer Python 3.10+ e usa somente a biblioteca padrão. Resolve registros de instalação, manifests e entradas pessoais/do projeto indicado. Não executa hooks, inicia servidores ou instala dependências.

## Uso pela Master

Na raiz do projeto, com os valores do ambiente resolvidos:

```text
python "${CLAUDE_PLUGIN_ROOT}/scripts/catalog.py" search --project "." --query "saúde orçamento projeto" --exclude "master-developer:master-developer"
```

Use termos de finalidade, objeto e formato. Para pedidos compostos, faça buscas separadas por etapa. `--automatic` restringe a busca a candidatos cuja metadata permite invocação automática; isso não comprova disponibilidade no runtime. A busca padrão também mostra entradas manuais e agents, para diagnóstico.

Ao procurar especialistas, exclua a própria entrada que já coordena a etapa com `--exclude`. Isso evita que a Master selecione a si mesma como próximo especialista. Numa auditoria de todas as capacidades, omita essa opção.

Antes de invocar, confirme o nome no catálogo real da sessão. Nunca use leitura direta de um corpo para contornar uma restrição manual. Os campos `session_visible` e `dependencies_ready` ficam desconhecidos até existir evidência externa.

O índice é gravado em `.claude/local/capabilities.json`. A cada busca, as fontes são conferidas; conteúdo idêntico não regrava o índice. Não é um serviço em segundo plano. A política da Master aciona a atualização durante o trabalho.

No Windows, use a ferramenta de shell realmente disponível, que pode ser PowerShell. Se não houver shell ou a busca retornar erro de processo, use `Read` em `.claude/local/catalog-index.md` e siga os links das páginas pequenas por origem. Essa alternativa é gerada pelo próprio coletor e não depende de `rg`. Não tente ler o JSON de centenas de componentes inteiro; ele pode ultrapassar o limite da ferramenta.

## Limitações explícitas

- A busca é lexical com expansão de termos PT/EN. Sua pontuação não é confiança estatística nem decisão final. Reformule e busque transversalmente quando necessário; não conclua ausência apenas porque um item ficou fora dos oito primeiros.
- Os grupos de sinônimos são editáveis no script e não vinculam intenções a plugins específicos.
- O índice tem caminhos locais e descrições de componentes privados que possam existir. Mantenha `.claude/local/` fora do Git.
- O coletor não resolve políticas gerenciadas, trust, arquivos de projetos ancestrais, ferramentas nativas, flags CLI nem o catálogo carregado numa sessão. Indique a raiz real do projeto em `--project`.
- Metadados YAML complexos são sinalizados. Não presuma que um campo desconhecido concede invocação automática.
- Wrappers de mesmo nome ficam agrupados, com todos os caminhos. A resolução final pertence ao Claude Code.
- MCPs aparecem como provedores com nomes de servidores; ferramentas e prontidão exigem verificação na sessão. Hooks são identificados por evento, nunca tratados como skills.

Para atualizar sem pesquisar:

```text
python "${CLAUDE_PLUGIN_ROOT}/scripts/catalog.py" refresh --project "."
```

`--config` permite auditar um diretório de configuração explícito. `--plugin` adiciona um plugin que será carregado via `--plugin-dir` naquela sessão; não instala o pacote.
