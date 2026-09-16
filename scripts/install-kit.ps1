# Renato Claude Toolkit - instalação e atualização
param([switch]$Update)
$ErrorActionPreference = 'Stop'
$pluginId = 'master-developer@renato-claude-toolkit'

if ($Update) {
    & claude plugin marketplace update renato-claude-toolkit
    if ($LASTEXITCODE -ne 0) { throw 'Falha ao atualizar o marketplace.' }
    & claude plugin update $pluginId --scope user
    if ($LASTEXITCODE -ne 0) { throw 'Falha ao atualizar a Master Developer.' }
} else {
    $marketplacePath = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
    & claude plugin marketplace add $marketplacePath --scope user
    if ($LASTEXITCODE -ne 0) { throw 'Falha ao adicionar o marketplace.' }
    & claude plugin install $pluginId --scope user
    if ($LASTEXITCODE -ne 0) { throw 'Falha ao instalar a Master Developer.' }
}

Write-Output 'Concluído. Recarregue os plugins ou abra uma nova sessão.'
Write-Output 'As regras globais são opcionais. Integre global/CLAUDE.md manualmente, sem sobrescrever seu arquivo existente.'
