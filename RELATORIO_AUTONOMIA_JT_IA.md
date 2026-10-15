# JT.IA - autonomia delimitada e navegador real

## Atualizacao posterior: modelo visual instalado

Em 11/10/2026, o utilizador autorizou instalar `moondream:latest` exclusivamente
para Visao Local. Ollama confirmou `completion, vision`. A configuracao
`local_vision_model` foi salva separadamente; `llm_model=qwen2.5:3b` foi
preservado para chat/programacao. Isso resolve a ausencia de modelo visual
descrita no relatorio original abaixo, sem alterar retroativamente seus testes.

O primeiro teste revelou JSON invalido; a integracao Moondream agora solicita
uma descricao curta e a identifica como legenda gerada, sem inventar listas
de observacoes ou recomendacoes. Uma imagem sintetica com forma vermelha e
circulo azul foi interpretada em 4,22 segundos: cores e circulo foram
identificados; a interpretacao de "bandeira" era inferencia nao comprovada.
Isso evidencia tanto funcionamento real quanto limitacoes do modelo pequeno.
Nenhuma imagem da area de trabalho foi usada nesse teste.

Passaram 56 testes direcionados de analise, interface visual, captura, OCR e
autonomia. Pylance nao apontou diagnosticos no modulo visual. Codigo anterior
foi copiado e verificado em
`C:\Users\JONATHA SILVA\Desktop\BACKUP_JT_IA_ANTES_MODELO_VISUAL`.
Nenhum modelo de chat foi removido nem chave de API alterada.

Data: 11/10/2026. Projeto existente preservado; nenhum executavel gerado.

## Projeto e backups

- Original: `C:\Users\JONATHA SILVA\Downloads\aplicativo para Android iOS`.
- Backup anterior: `C:\Users\JONATHA SILVA\Desktop\BACKUP_JT_IA_ANTES_DA_CORRECAO`.
- Snapshot anterior de autonomia: `C:\Users\JONATHA SILVA\Desktop\BACKUP_JT_IA_ANTES_DA_AUTONOMIA`.
- Novo backup autorizado: `C:\Users\JONATHA SILVA\Desktop\BACKUP_JT_IA_ESTADO_ATUAL_VERIFICADO`.

A nova verificacao do backup antigo conferiu 146 entradas e encontrou tres
divergencias: configuracao, certificado publico e `core/local_models.py`.
Nao foi determinada a origem das mudancas. As copias anteriores foram
preservadas e o utilizador autorizou criar um novo snapshot do estado atual.
Nao se apresenta essa copia nova como backup anterior as primeiras correcoes.

O novo snapshot inicial verificou 154 arquivos por SHA-256, totalizando
1.986.488.433 bytes, incluindo modelos locais e dados externos. A configuracao
foi sanitizada; credenciais originais nao foram apagadas. Caches, ambientes,
artefatos compilados, chaves privadas e perfis autenticados nao foram copiados.
As pequenas correcoes posteriores e este relatorio sao incluidos separadamente
em `correcoes_finais`, com hashes e instrucoes de sobreposicao. A raiz inicial
do snapshot nao e sobrescrita. JSON, perfil salvo e sintaxe dos arquivos
essenciais foram verificados; nao houve reinstalacao autenticada completa.

## Causas e correcoes

1. O perfil assistido confirmava passos rotineiros e o chat local nao expunha
   ferramentas. O perfil `maximum` agora usa os mesmos controles de permissao,
   auditoria, cancelamento e evidencias do despacho online.
2. O navegador podia buscar elementos ambiguos e reportar resultados sem
   observar o estado final. A integracao Playwright existente agora verifica
   campos, selecoes, checkbox e resultados visiveis, preservando falhas parciais.
3. Formularios funcionavam internamente, mas `fields` faltava na declaracao
   enviada ao modelo. O contrato foi publicado e testado no despacho real.
4. A API Gemini Live rejeitou `additionalProperties` durante uma inicializacao
   real. O contrato foi corrigido para lista de pares `selector`/`text`;
   chamadas internas com dicionario continuam compativeis. A ultima
   inicializacao conectou, abriu o microfone e iniciou a saida de audio.
5. Qwen 2.5 3B produziu chamadas incorretas ou vazias com o contrato generico
   extenso. Adaptadores locais `browser_*` fornecem contratos menores e
   encaminham a operacao para o mesmo `browser_control`. O teste real com
   Ollama preencheu o campo e verificou o DOM do Edge.
6. Uma submissao incerta podia ser repetida. Agora a tentativa fica registrada
   antes do clique; repetir a mesma submissao apenas verifica, sem clicar.
7. Confirmacoes nao tinham dono cancelavel. Agora a tarefa dona pode impedir
   uma operacao depois de cancelada/substituida. O fluxo local continua apos
   confirmacao aceita, usando o resultado, sem refazer a submissao.
8. A ferramenta nova de programacao usa a pasta autorizada ou um subprojeto
   relativo, proposta local, recuperacao, verificacao de digest/sintaxe,
   unittest e tentativas limitadas. Zero testes descobertos nao sao sucesso.
9. Uma falha de teste dependia da RAM livre real. O teste de progresso de
   download usa recursos simulados adequados; o teste separado de pouca RAM
   continua recusando download. A protecao de memoria em producao foi mantida.
10. Diagnosticos antigos do editor estavam desatualizados. Pylance foi
    consultado novamente e o Pylint ja fornecido pela extensao foi executado,
    sem instalar dependencias.

## Permissoes efetivamente salvas

- Perfil: `maximum`.
- Pasta: `C:\Users\JONATHA SILVA\Desktop\JT_IA_PROJETOS`.
- Comando autorizado: `python-unittest`; nenhum shell arbitrario foi liberado.
- Permissao `workspace_programmer` acrescentada, preservando as demais.
- Origens de sites para edicao: nenhuma. Salvamentos automaticos: nenhum.
  Esses acessos devem ser escolhidos explicitamente nas configuracoes.
- O perfil maximo nao ativa capacidades desativadas nem expande a pasta.
- A permissao preexistente `external_screen_sharing` estava ativa e foi
  preservada, nao ativada por estas alteracoes. A ferramenta local nova nao
  envia imagens a servicos externos.
- UAC, antivirus, firewall, autenticacao e controles criticos nao foram
  desativados. Testes de projetos executam codigo com os direitos da conta
  Windows atual; a pasta autorizada nao e um sandbox do sistema operativo.

## Resultados executados

| Verificacao | Resultado real |
|---|---|
| Regressao completa final | 323 testes executados, 320 aprovados, 3 ignorados; nenhum erro/falha |
| Navegador Edge com site HTTP local | Campos, conteudo editavel, opcoes, checkbox, obrigatoriedade, ambiguidade, timeout, preservacao, confirmacao, cancelamento e nao duplicacao testados |
| Formulario salvo e retomada | POST real, resultado visivel verificado, continuacao apos uma confirmacao sem repetir a submissao |
| Ollama real -> despacho compartilhado -> Edge | Campo `#name` recebeu o texto de teste; etapa `completed_verified`; resposta final gerada |
| Programador com Ollama real | Corrigiu apenas `answer.py` num subprojeto temporario autorizado; unittest executou e aprovou um teste |
| Recuperacao | Testes verificaram `.jtia.bak` original e ponto de recuperacao antes da edicao |
| Navegacao visivel real | Edge com perfil dedicado abriu `https://example.com/`; titulo observado `Example Domain`; sessao de teste fechada |
| Pesquisa real | Retornou fontes HTTP(S) para documentacao Python unittest |
| Captura/OCR local | Captura real 1920x1080 e retorno com OCR; conteudo da tela omitido dos registros de verificacao |
| Interpretacao visual por IA | Indisponivel: modelo instalado declara `completion, tools`, sem `vision` |
| Voz | Despacho de transcricao local aceito testado; no modo Offline + Maximum segue direto para o mesmo comando de texto |
| Reinicio | Aplicacao fechada por WM_CLOSE e reaberta; janela real visivel 994x738; perfil `maximum` lido num processo novo |
| Online e dashboard | Ultima inicializacao Gemini Live conectou; microfone e reproducao iniciados; dashboard HTTPS respondeu 200 |
| Analise estatica | Pylance sem erros nos modulos consultados; Pylint passou para E, W0640 e W0201 nos nove modulos selecionados |

O teste da transcricao utiliza texto/recognizer controlado; nao foi realizada
uma nova conversa completa capturada de uma pessoa ao microfone nesta etapa.
Conexao e abertura dos dispositivos nao provam reconhecimento de uma frase.
O teste real do modelo local foi de um campo; nao se garante que um modelo 3B
resolva corretamente qualquer formulario ou pedido complexo.

## Arquivos relevantes modificados

- `main.py`: ferramentas locais, adaptadores, voz local aceita, continuacao,
  cancelamento, tratamento de erro e omissao de dados em registros.
- `ui.py`, `translations/ui.json`: perfis, origens e seletores de salvamento.
- `core/security_manager.py`: autorizacao central de rotina/origem/salvamento
  e rejeicao de configuracoes de navegador malformadas.
- `core/windows_control.py`, `actions/windows_control.py`: politica do
  programador e confirmacoes por perfil, sem ampliar o sistema inteiro.
- `core/autonomous_programmer.py`: perfil compartilhado e evidencia de testes.
- `core/action_loader.py`, `core/task_orchestrator.py`, `core/confirm.py`:
  contexto cancelavel, resultados, confirmacao e continuacao delimitada.
- `core/llm_client.py`: orcamento maior de geracao quando ha ferramentas.
- `actions/browser_control.py`: perfil dedicado e operacoes DOM verificadas.
- `actions/workspace_programmer.py`, `actions/local_screen_analysis.py`:
  novas entradas para ferramentas existentes, nao outro aplicativo.
- `tests/test_browser_automation.py`, `tests/test_autonomy_actions.py`:
  testes novos com navegador real, programacao, voz e seguranca.
- `tests/test_security_manager.py`, `tests/test_windows_control.py`,
  `tests/test_programmer_ui.py`, `tests/test_task_orchestrator.py`,
  `tests/test_autonomous_programmer.py`, `tests/test_local_models.py`:
  regressao e fixtures coerentes com configuracoes persistentes.
- `readme.md` e este relatorio: documentacao das capacidades e limites reais.

## Janelas e uso

As melhorias anteriores de tamanho e legibilidade foram preservadas e seus
testes de interface continuam passando. Dimensoes logicas planejadas:
configuracoes 1000x800, diagnostico/programador 1000x760, workspace/visao
1100x820, ferramentas 960x720 e audio 820x640; minimo normal 720x480, limitado
pela area disponivel. Os detalhes e testes nativos anteriores constam em
`RELATORIO_CORRECAO_JT_IA.md`; esta etapa nao substituiu a interface.

Para formularios externos, abra Configuracoes > Seguranca e acrescente a
origem exata permitida. Para salvar sem confirmacao no perfil maximo,
registre `origem | seletor CSS exato` do botao reversivel. Nao registre
botoes de compra, publicacao ou mensagem externa como salvamento reversivel.
O login no perfil dedicado, MFA e CAPTCHA sao realizados manualmente.

## Limites pendentes

- Falta modelo local com visao; nenhuma imagem foi interpretada por IA e
  nenhum modelo adicional foi baixado.
- Sites reais de contas pessoais nao foram autorizados nem submetidos.
- Nao ha replay automatico de tarefas apos reiniciar a aplicacao.
  Confirmacoes podem retomar o fluxo local na mesma sessao; login manual
  permite continuar na pagina preservada com uma nova instrucao.
- Cancelamento e observado entre chunks/fases e durante esperas do navegador;
  chamadas de modelo bloqueadas dependem do timeout da requisicao.
- Apenas unittest esta autorizado como comando de desenvolvimento.
  Ambiente virtual, instalacao de dependencias e outros comandos nao foram
  liberados por inferencia.
- Nao foi reinstalado/restaurado integralmente o aplicativo a partir da copia
  sanitizada com autenticacao; segredos devem ser preservados separadamente.
