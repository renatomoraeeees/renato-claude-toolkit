# Exporta a lista real de plugins instalados no computador.
# O arquivo gerado pode ser usado para reconstruir o setup em outro PC.
$ErrorActionPreference = "Stop"

$out = Join-Path (Get-Location) "plugin-snapshot.json"
claude plugin list --json | Out-File -FilePath $out -Encoding utf8

Write-Host "Snapshot criado em: $out" -ForegroundColor Green
Write-Host "Esse arquivo registra plugins, versões, marketplaces e status."
Write-Host "Não compartilhe credenciais, tokens ou arquivos de configuração privados."
