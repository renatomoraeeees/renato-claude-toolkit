# Renato Claude Toolkit - instalação
$ErrorActionPreference = "Stop"

Write-Host "== Renato Claude Toolkit ==" -ForegroundColor Cyan
Write-Host "1) Adicionando marketplace local..."
claude plugin marketplace add "$PSScriptRoot\.." --scope user

Write-Host "2) Instalando Master Developer..."
claude plugin install master-developer@renato-claude-toolkit --scope user

Write-Host ""
Write-Host "Master Developer instalada." -ForegroundColor Green
Write-Host "Para aplicar a regra global opcional, copie:"
Write-Host "  $PSScriptRoot\..\global\CLAUDE.md"
Write-Host "para:"
Write-Host "  $HOME\.claude\CLAUDE.md"
Write-Host ""
Write-Host "Depois reinicie o Claude Code ou use /reload-plugins."
