# JT.IA - backup, permissoes e interface

## Caminhos e copia de seguranca

- Projeto original: `C:\Users\JONATHA SILVA\Downloads\aplicativo para Android iOS`
- Backup: `C:\Users\JONATHA SILVA\Desktop\BACKUP_JT_IA_ANTES_DA_CORRECAO`
- Pasta autorizada com aprovacao do utilizador: `C:\Users\JONATHA SILVA\Desktop\JT_IA_PROJETOS`
- Nao existe repositorio Git neste projeto; nao foi possivel atribuir a regressao a um commit.

O snapshot do projeto foi criado antes das alteracoes desta correcao. Foram
copiados 118 ficheiros sem modificacao, totalizando 5.327.081 bytes, e todos
foram comparados ao original por SHA-256. A configuracao foi copiada
separadamente, retirando campos de credenciais: o snapshot do projeto tem
119 ficheiros e 5.327.892 bytes. O BOM dessa copia JSON foi retirado para
permitir leitura pelo carregador UTF-8 existente.

O backup foi complementado com 26 ficheiros externos, 1.983.495.189 bytes,
tambem comparados por SHA-256, sem excluir modelos locais:

| Origem | Destino relativo ao backup |
|---|---|
| `%LOCALAPPDATA%\MarkLV` | `dados_externos\MarkLV` |
| `%LOCALAPPDATA%\JT.IA` | `dados_externos\JT_IA` |
| `%USERPROFILE%\.ollama\models` | `dados_externos\Ollama` |

Foram excluidos ambientes virtuais duplicados, caches de Python/pytest e
chaves privadas de certificados. Codigo, documentacao, recursos, memoria,
bases de dados existentes e modelos locais foram preservados. As credenciais
e chaves privadas originais continuam no computador e nao foram apagadas.
A copia nao secreta nao permite recuperar credenciais perdidas: uma
restauracao noutro computador exige reinseri-las ou regenerar certificados.

O manifesto `HASHES_SHA256.csv` e o guia `LEIA_ME_BACKUP.txt` ficaram dentro
do backup. A verificacao final contra o manifesto aprovou 146 ficheiros
(145 ficheiros de projeto/dados mais o guia), sem divergencias.

Foi feita uma simulacao de recuperacao de oito ficheiros essenciais numa
pasta temporaria isolada: copia, hashes, sintaxe Python e leitura JSON
passaram. Nao foi feita uma reinstalacao completa nem um arranque usando
credenciais do backup.

## Causas comprovadas e correcoes

1. A politica independente de controlo Windows estava vazia: pasta,
   aplicacoes, ferramentas e comandos nao estavam autorizados, embora as
   capacidades gerais de internet/captura/edicao estivessem habilitadas.
   Com aprovacao do utilizador, foi configurada apenas a pasta acima.
2. `open_application("browser")` tentava abrir a URL incompleta `https://`.
   Agora reutiliza o lancador existente do navegador padrao.
3. O terminal dependia exclusivamente de `wt.exe`, ausente neste computador.
   Foi adicionada uma alternativa explicita com `cmd.exe`, na pasta
   autorizada e numa consola maximizada. Se Windows Terminal estiver
   instalado, continua a ser preferido, tambem maximizado.
4. O arranque forcava `CREATE_NO_WINDOW` ate nas consolas interativas.
   Agora preserva `CREATE_NEW_CONSOLE` e a configuracao de janela solicitada;
   os processos de fundo continuam ocultos.
5. O teste real do programador recebeu uma proposta JSON incompleta do
   Ollama. Foi exigido um esquema estruturado com os campos necessarios e
   limite de oito ficheiros. A validacao de conteudo/caminhos e a aprovacao
   antes de aplicar continuam obrigatorias.
6. Os paineis de trabalho eram filhos fixos do HUD, incluindo configuracoes
   com apenas 390 px. Agora sao janelas nativas redimensionaveis, com
   minimizar/maximizar, conteudo existente e rolagem quando necessario.
7. `qwen2.5:3b` informa apenas capacidades `completion, tools`, sem `vision`.
   Isso impede interpretacao de imagens por IA, mas nao captura ou OCR.
   Nao e um bloqueio do Windows. Nao foi instalado nem substituido um modelo.

Aplicacoes autorizadas: navegador, Explorador e terminal. Comando autonomo
autorizado: descoberta de testes Python unittest. Foram habilitadas somente
as ferramentas de projeto correspondentes e consulta/cancelamento das
tarefas. Controlo generico do ambiente de trabalho e ferramentas nao
aprovadas nao foram liberados.

O programador reaproveita a pasta autorizada ao abrir. O modo permanece
`assisted`; confirmacoes criticas e backup antes de edicoes permanecem
obrigatorios. Compartilhamento externo de capturas permanece desativado.
A Visao Local fica em modo manual, sem ativar captura continua.

Nao foram alterados UAC, antivirus, permissoes administrativas ou politicas
do Windows. Um terminal interativo usa as permissoes normais da conta:
a pasta inicial nao e uma sandbox do sistema operativo.

## Janelas e legibilidade

Dimensoes em pixels logicos do Qt, limitadas automaticamente pela area
disponivel do monitor e respetiva escala:

| Painel | Dimensao inicial pretendida |
|---|---|
| Configuracoes | 1000 x 800 |
| Diagnostico e programador de diagnostico | 1000 x 760 |
| Programador autonomo e Visao Local | 1100 x 820 |
| Tarefas, controlo Windows, memoria e plugins | 960 x 720 |
| Dispositivos de audio | 820 x 640 |
| Terminal | Maximizado |

Minimo normal: 720 x 480, reduzido quando o monitor nao comporta esse
tamanho. A escala real observada foi 125%: monitor fisico 1920 x 1080,
area util Qt 1536 x 816; os paineis de teste abriram com 1000 x 752.
Reabrir um painel ocupado preserva o tamanho escolhido pelo utilizador.

Fontes dos controlos de trabalho: minimo de 10 pt. Etiquetas ganham quebra
de linha e melhor contraste, mantendo o tema existente. Botoes mantem
largura suficiente para os nomes, com rolagem horizontal quando necessaria.
O relatorio de diagnostico tem altura minima de 240 px. Botoes de seguranca
longos foram separados em mais linhas. Ferramentas ganharam nomes
compreensiveis em portugues; identificadores internos nao foram alterados.
Os paineis compactos de confirmacao/configuracao inicial nao foram
convertidos indiscriminadamente em janelas grandes.

## Resultados reais de validacao

| Verificacao | Resultado observado |
|---|---|
| Testes automatizados relevantes | 165 executados; 163 passaram, 2 ignorados |
| Diagnosticos do editor nos ficheiros alterados | Nenhum erro reportado |
| Arranque | Interface abriu, 29 acoes carregadas, sessao conectada, fluxos de audio iniciados |
| Dashboard | HTTPS local respondeu HTTP 200; certificado local de desenvolvimento |
| Navegador/site | Lancador real chamado para `https://www.python.org/`; requisicao HTTP independente retornou 200 |
| Pesquisa real | DuckDuckGo retornou fontes para `Python unittest documentation` |
| Pasta permitida | Ficheiro temporario criado, lido e removido; conteudo comparado |
| Caminho fora da pasta | `..` recusado com PermissionError |
| Comando permitido | Runner real executou um teste unittest temporario: exit 0, `Ran 1 test`, `OK` |
| Programador local | Ollama 0.40.2 / qwen2.5:3b gerou proposta estruturada valida de um ficheiro; nao foi aplicada |
| Captura local real | Ecran principal capturado em 1920 x 1080; imagem nao guardada nem enviada |
| OCR Windows real | Imagem sintetica reconhecida como `JT IA TESTE LOCAL 12345`, sem truncamento |
| Janelas Qt nativas | Configuracoes, diagnostico e programador abriram visiveis; maximizar/restaurar/redimensionar para 820 x 600 passaram |
| Monitor pequeno e deslocado | Regressao validou limites num monitor 640 x 480, com origem deslocada |
| Memoria/configuracao | Diagnostico leu memoria persistente e configuracao; politica persistida confirmada num processo separado |
| Recuperacao do backup | Oito ficheiros essenciais restaurados temporariamente, hashes/sintaxe/JSON aprovados |
| Chat/audio | Regressao de transporte, eventos, dashboard e voz passou; nao foi repetida uma conversa completa por voz neste ciclo |

Os ficheiros de teste temporarios foram removidos. A memoria pode adquirir
resumos de sessao pelo funcionamento normal da aplicacao; nao foi
substituida pela copia antiga. O diagnostico foi executado sem uma nova
execucao completa de todos os testes do projeto; apenas as suites
diretamente relacionadas foram executadas.

## Ficheiros alterados nesta correcao

- [main.py](main.py): preservar consolas interativas explicitas.
- [ui.py](ui.py): janelas de trabalho, fontes, rolagem, nomes e projeto autorizado.
- [core/windows_control.py](core/windows_control.py): navegador, terminal e nomes das ferramentas.
- [core/autonomous_programmer.py](core/autonomous_programmer.py): esquema estruturado de proposta.
- [translations/ui.json](translations/ui.json): nomes das ferramentas em portugues.
- [config/api_keys.json](config/api_keys.json): politica Windows limitada e modo visual manual; credenciais originais preservadas.
- [tests/test_windows_control.py](tests/test_windows_control.py): regressao de navegador, terminal e flags de arranque.
- [tests/test_programmer_ui.py](tests/test_programmer_ui.py): dimensoes, redimensionamento, monitor pequeno e pasta autorizada.
- [tests/test_autonomous_programmer.py](tests/test_autonomous_programmer.py): contrato do esquema enviado ao Ollama.
- Este relatorio: registo de backup, alteracoes, evidencias e limitacoes.

## Pendencias e limites

- Interpretacao visual por IA: exige um modelo local com capacidade `vision`.
  Captura e OCR foram testados e nao dependem desse modelo. Nenhum download
  foi iniciado sem aprovacao.
- Diagnostico encontrou dependencias opcionais `google-api-python-client`
  e `paho-mqtt` indisponiveis; nao foram instaladas sem necessidade comprovada.
- Dois testes de links simbolicos foram ignorados porque esta conta Windows
  nao tem permissao para cria-los; nao foram marcados como aprovados.
- O lancamento do navegador e o HTTP 200 nao comprovam, por si so, a
  renderizacao completa da pagina no navegador do utilizador.
- Janelas foram verificadas por propriedades/acoes Qt nativas e testes,
  nao por uma revisao visual manual de cada controlo em todas as resolucoes.
- Nenhum executavel foi gerado, nenhuma funcionalidade foi removida e
  nenhuma permissao ilimitada foi concedida.

## Recuperacao, se necessaria

Fechar o JT.IA antes de restaurar. Copiar seletivamente os ficheiros
essenciais do snapshot para o projeto; guardar primeiro quaisquer dados
mais recentes. Nao substituir credenciais atuais pela configuracao
sanitizada sem planear a sua reinsercao.

Recriar o ambiente Python 3.12 usando os manifestos de dependencias do
projeto. Restaurar dados externos para as origens indicadas na tabela;
modelos Ollama pertencem a `.ollama\models`, nao a pasta de codigo.
Nao sobrescrever memorias ou logs mais recentes sem decisao explicita.
