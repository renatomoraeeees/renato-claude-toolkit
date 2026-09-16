# Descoberta e composição

Leia para selecionar especialistas ou investigar capacidades ausentes. Os nomes abaixo foram observados em fontes públicas e na instalação local auditada em 15/09/2026; confirme o catálogo da sessão antes de invocá-los. Uma instalação diferente pode expor outros nomes.

## Modelo de disponibilidade

Trate separadamente: origem cadastrada, pacote instalado, habilitação no escopo, componente descoberto, componente invocável, dependências prontas e execução bem-sucedida. Uma etapa não comprova a seguinte.

O catálogo local, quando implementado, deve registrar:

- ID qualificado, tipo, plugin/origem, versão e caminho de entrada;
- descrição de finalidade e condições de invocação;
- escopo, evidência de visibilidade e data de verificação;
- dependências, ferramentas necessárias e estado desconhecido quando não verificado;
- hash/revisão para detectar alterações, separado da contagem de uso.

Não armazene transcrições, tokens ou credenciais nesse catálogo. Gere-o a partir dos componentes exportados pelos manifests e diretórios suportados; não considere todo arquivo de um monorepositório como componente instalado.

Para centenas de entradas, busque primeiro por finalidade, objeto e formato de entrega, com termos naturais em português e inglês. A busca deve alcançar todo o catálogo quando um grupo inicial não oferecer candidatos adequados. Não restrinja a seleção aos grupos ou exemplos desta referência.

Mantenha aliases e wrappers associados à entrada canônica, flags de invocação e indicação de depreciação. A contagem de arquivos, a de nomes únicos e a lista efetiva da sessão são medidas diferentes. Ausência de uso histórico não prova irrelevância de uma capacidade nova ou rara.

## Exemplos de rotas

| Intenção | Entradas candidatas, condicionadas à disponibilidade |
|---|---|
| Nova interface ou mudança visual | `frontend-design:frontend-design`; processo de design conforme a política do projeto |
| Bug reproduzível | `superpowers:systematic-debugging`, seguido das verificações necessárias |
| Plano de implementação solicitado | `superpowers:writing-plans` |
| Arquivo Word, planilha, slides ou PDF | `document-skills:docx`, `document-skills:xlsx`, `document-skills:pptx`, `document-skills:pdf` |
| Portfólio, cronograma e riscos | `pm-skills:senior-pm` |
| Sprint, fluxo e retrospectiva | `pm-skills:scrum-master` |
| Operação técnica Jira | `pm-skills:jira-expert` |
| Documentação Confluence | `pm-skills:confluence-expert` |
| Administração de acesso Atlassian | `pm-skills:atlassian-admin` |
| Template reutilizável Atlassian | `pm-skills:atlassian-templates` |
| Análise de reunião | `pm-skills:meeting-analyzer` |
| Comunicação interna | `pm-skills:team-communications` |
| Coordenação de entrega PM | `pm-skills:pm-skills`, respeitando suas dependências e limites |
| Pesquisa aprofundada solicitada | `deep-research:research`, com o modo e os pré-requisitos adequados |
| Reflexão/revisão adicional solicitada | `reflexion:reflect` ou `reflexion:critique` |
| Padrões de frontend e acessibilidade | `ecc:frontend-patterns`, `ecc:frontend-a11y`; separar de direção visual |
| Inspecionar navegador, rede e desempenho | `chrome-devtools-mcp:chrome-devtools`, com MCP pronto |
| Diagnosticar LCP | `chrome-devtools-mcp:debug-optimize-lcp` |
| Escrever testes Playwright | `ecc:e2e-testing`; ferramentas Playwright conforme conexão real |
| Simplificar código preservando comportamento | Agent `code-simplifier:code-simplifier`, quando delegação estiver autorizada |
| Analisar vídeo | `watch:watch`, após conferir ferramentas de mídia |
| Recuperar trabalho de sessões anteriores | `claude-mem:mem-search`, com busca restrita ao projeto pertinente |
| Memória Markdown entre ferramentas | `ecc:unified-memory`, após verificar seu runtime e escopo de escrita |
| Orientação sobre componentes ECC | `ecc:ecc-guide`; resolver caminhos pela instalação real |

`claude-security:claude-security` foi encontrada como exclusivamente manual. `ecc:auto-update` e `ecc:setup-pm` também têm invocação automática desabilitada. Respeite as flags atuais; não as contorne por leitura direta do corpo.

Playwright fornece MCP na instalação auditada, Code Simplifier fornece agent e Security Guidance fornece hooks. Não invente skills com os nomes desses pacotes.

Security Guidance é um provedor de hooks na fonte examinada. Não invente `security-guidance:security-guidance`. Ausência de mensagem visível não comprova ausência de execução.

Não confunda os commands PM documentados como `/cs:pm` com identificadores comprovados da instalação. Confira as entradas expostas; o plugin contém arquivos `cs-pm.md`, `cs-grill-pm.md` e `cs-pm-loop.md`.

## Tarefas compostas

- Relatório executivo em Word: análise de projeto → redação para o público, se necessária → docx.
- Investigação de bug com interface: debugging → correção pertinente → validação funcional/visual.
- Reunião com plano e apresentação: análise de reunião → decisões/ações → pptx.

Não chame automaticamente outro orquestrador quando o especialista já está identificado. Se o usuário escolheu um orquestrador com regras próprias, preserve-as ou esclareça o conflito necessário antes da etapa afetada.

Os fluxos `ecc:orch-*`, Superpowers e `claude-mem:make-plan`/`claude-mem:do` podem disputar o mesmo trabalho. Escolha um responsável pelo processo; não empilhe todos. Um fluxo de plugin que menciona push ou publicação não concede autorização externa adicional.

## Diagnóstico de ausência

1. Existe entrada na sessão? Se sim, verificar adequação da descrição e restrições de invocação.
2. Só existe no snapshot/cache? Conferir instalação, escopo, habilitação, manifests e recarga.
3. Está visível, mas falha? Conferir dependências e resolução de caminhos.
4. Carrega, mas não compõe? Conferir regras de encadeamento e sobreposição entre orquestradores.
5. Funciona em inglês e falha em português? Distinguir seleção pelo modelo de classificadores literais internos. Preservar o pedido original ao normalizar intenção.
6. Funciona manualmente e não automaticamente? Comparar descrição, visibilidade, orçamento de contexto e evidência de chamadas.

Use comandos de diagnóstico suportados pela versão instalada. Nunca simule saída de `/skills`, `/hooks`, `/mcp` ou de logs que não foram consultados.
