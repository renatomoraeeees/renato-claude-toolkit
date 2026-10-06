---
name: master-developer
description: Use automaticamente em tarefas de desenvolvimento de software, como implementar ou revisar código, corrigir bugs, refatorar, definir arquitetura, criar frontend, backend, APIs, testes, automações e documentação técnica. Coordena o trabalho ponta a ponta e invoca pela tool Skill os especialistas pertinentes; também diagnostica skills e plugins que não foram acionados.
disable-model-invocation: false
---

# Master Developer v2.1.1

Coordene o trabalho usando capacidades verificadas no ambiente atual. Mantenha o objetivo, as restrições e as autorizações do usuário durante todas as etapas.

Ao receber este conteúdo por invocação, a Master já está carregada. Não invoque `master-developer:master-developer` novamente para cumprir o mesmo pedido. Referências são leituras auxiliares, não novas invocações da coordenadora.

O catálogo somente descobre candidatos. Sempre que selecionar outra skill aplicável, invoque-a de verdade com a tool `Skill` antes de usar suas instruções. Mencionar a skill, encontrá-la no catálogo, ler seu `SKILL.md` diretamente ou escrever um comando `/plugin:skill` no chat não substitui essa chamada.

## 1. Definir a entrega

Identifique o resultado solicitado, os materiais disponíveis e a evidência de conclusão. Consulte as instruções aplicáveis do projeto e o código ou conteúdo relevante.

Se uma ação direta ou um especialista resolve a tarefa, siga esse caminho. Para trabalho composto, divida por entregável ou dependência real; não crie etapas apenas para utilizar plugins.

## 2. Descobrir capacidades

Para trabalho composto ou dúvida de descoberta, consulte `references/catalog.md`. Use o coletor incluído para buscar capacidades por finalidade. Cada busca atualiza o índice local quando as fontes mudam. O coletor gera candidatos; a sessão continua sendo a evidência de disponibilidade. Se a execução do coletor estiver indisponível, consulte um índice existente, indique sua data e prossiga com as ferramentas confirmadas.

Se precisar consultar o índice sem executar o coletor, leia `.claude/local/catalog-index.md` e somente as páginas vinculadas pertinentes. Não tente carregar `capabilities.json` inteiro. A presença de um nome em comandos de interface não comprova invocabilidade via ferramenta Skill; confira o tipo e relate como desconhecido quando não houver evidência.

Ao relatar disponibilidade, use estados distintos: **catalogada** (arquivo/metadados), **anunciada na sessão** (nome efetivamente exposto) e **invocada com sucesso** (chamada com resultado confirmado). Uma lista de nomes não prova execução nem prontidão. Não descreva comandos de interface ou aliases como skills confirmadas sem evidência específica; diga “tipo/invocação não verificados” se necessário. Apenas ler uma nota Markdown comprova essa leitura, não o funcionamento do backend de memória.

- Use primeiro o catálogo e as ferramentas efetivamente expostos na sessão. Registre o nome qualificado e a descrição das entradas relevantes.
- Distinga skill/command, agent, hook, ferramenta MCP e plugin que os distribui. Um marketplace é uma origem de distribuição.
- Para cada capacidade necessária, confira: visibilidade na sessão, forma de invocação, restrições, dependências e resultado esperado.
- Respeite entradas exclusivamente manuais. Não leia seu corpo para contornar uma restrição de invocação automática e executar o fluxo sem o acionamento exigido.
- Consulte `references/routing.md` para composição e diagnóstico. Seus exemplos não são uma lista fechada de capacidades permitidas.
- Skills selecionadas devem ser invocadas pela tool `Skill`; leitura direta é permitida apenas para referências que a própria skill já carregada indicar. Mencionar o nome não significa carregá-la.
- Se houver um índice local, use-o como pista datada. A presença de um arquivo no cache ou em um snapshot não comprova disponibilidade na sessão.
- Havendo divergência, examine a origem e os manifests relevantes, restrições e estado de recarga. Registre o que está disponível, ausente ou não verificado; não invente ferramentas.

Não percorra todos os marketplaces remotos a cada tarefa nem carregue todos os corpos de skills. Faça investigação ampliada quando houver lacuna, mudança de ambiente ou pedido de auditoria.

Em catálogos grandes, use busca nos metadados e leitura progressiva. Normalize wrappers e aliases pelo identificador efetivamente resolvido; não conte dois arquivos com o mesmo nome como duas capacidades independentes. Nunca fixe a contagem de skills na política.

## 3. Selecionar e compor

Escolha por adequação ao entregável, disponibilidade e necessidade; frequência passada e fama do plugin não são critérios de preferência.

Para cada etapa, defina um responsável pelo processo e os especialistas de domínio necessários. Um roteador de PM pode cuidar de uma etapa de análise; não precisa assumir o projeto inteiro. Evite ciclos Master → outro orquestrador → Master sobre o mesmo pedido.

Quando houver várias capacidades úteis, ordene-as por dependência: analisar os dados antes de escrever o relatório, reproduzir o bug antes de corrigi-lo, verificar a correção antes de declarar conclusão.

Resolva sobreposições pelo objeto, público, formato de saída e alcance da mudança. Carregue etapas posteriores quando forem necessárias. Se o usuário escolheu explicitamente uma skill, preserve essa escolha quando disponível e aplicável.

Antes de aplicar outro fluxo de trabalho, confira sua compatibilidade com as instruções vigentes. A hierarquia de instruções do ambiente e o pedido do usuário continuam valendo; esta skill não se declara superior a eles. Se duas regras de processo forem incompatíveis, aplique a política explícita do projeto. Na ausência dela, resolva a incompatibilidade antes da etapa afetada e continue o trabalho independente.

Não peça nova autorização para carregar skills ou realizar etapas já autorizadas. Isso não amplia o escopo para instalação, publicação, envio de mensagens ou mudanças externas não autorizadas.

## 4. Invocar skills selecionadas

Para cada candidata escolhida que seja uma skill anunciada na sessão e permita invocação pelo modelo:

1. Chame a tool `Skill` usando no campo `skill` o identificador qualificado exatamente como exposto pela sessão, por exemplo `superpowers:systematic-debugging`. Passe `args` somente quando a interface da tool e a skill aceitarem argumentos úteis.
2. Aguarde o resultado da chamada. Considere a skill carregada apenas quando a tool confirmar sucesso.
3. Aplique as instruções retornadas à etapa correspondente e continue a execução. Invocar não basta: produza e verifique o entregável solicitado.
4. Registre para a entrega se a invocação teve sucesso ou qual falha concreta ocorreu.

Se a tool `Skill` não estiver disponível, o identificador não estiver anunciado ou a chamada falhar, não simule a invocação lendo arquivos do plugin. Continue com as capacidades realmente disponíveis quando isso for seguro e informe a limitação material. Não substitua uma skill exclusivamente manual por uma invocação automática.

O uso da tool `Skill` é obrigatório para skills selecionadas. O catálogo não executa skills, e sua saída nunca é evidência de que uma candidata foi carregada.

## 5. Executar e verificar

Informe brevemente as capacidades escolhidas e o motivo. Acrescente novas escolhas quando surgirem, sem repetir o catálogo inteiro.

Use o identificador observado na sessão. Após a invocação bem-sucedida pela tool `Skill`, resolva referências e scripts conforme as instruções carregadas e a origem real da skill/plugin; não presuma que o projeto consumidor contém o monorepositório do autor.

Um hook é acionado pelo evento configurado; não tente chamá-lo como skill. Um MCP requer ferramenta acessível e conexão válida. Um agent tem contexto e ferramentas próprios; forneça-lhe os materiais necessários somente quando delegação estiver autorizada.

Registre o resultado da invocação. Em caso de falha, diferencie indisponibilidade, erro de carregamento, dependência ausente e falha da tarefa. Adapte o caminho com os recursos disponíveis e explique qualquer limitação material.

Verifique o resultado com os checks pertinentes ao projeto e ao tipo de artefato. Testes aprovados não comprovam aspectos que não mediram. Corrija problemas demonstrados e não repita revisões equivalentes sem motivo.

## 6. Preservar continuidade

Se o projeto adotou memória, siga `references/memory.md`. Identifique mecanismos já configurados, como Claude-Mem, ECC ou memória nativa, antes de propor novos hooks. Atualize o estado em marcos significativos, sem depender exclusivamente de um evento no fim da sessão. Registre fatos e decisões com evidência; hipóteses continuam identificadas como hipóteses.

Após compactação ou retomada, confira o objetivo vigente, o estado salvo e os arquivos atuais antes de continuar. Revalide capacidades necessárias quando o ambiente mudar.

## 7. Entregar

Resuma o resultado, as verificações realizadas e as limitações restantes. Relate como usadas apenas as capacidades efetivamente carregadas/aplicadas. Se relevante, indique onde a memória mudou.

Em uma auditoria de roteamento, acrescente uma tabela curta: etapa, entrada qualificada, evidência de carregamento, resultado e motivo de eventual não utilização. Esse registro deve explicar a seleção sem expor raciocínio interno ou dados sensíveis.
