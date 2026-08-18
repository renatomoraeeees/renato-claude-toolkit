# Instala os Plugins que estavam habilitados no ambiente de origem.
# As fontes/IDs abaixo foram extraídos do plugin-snapshot.json fornecido pelo usuário.
$ErrorActionPreference = "Stop"

$plugins = @(
  "deep-research@claude-community",
  "document-skills@anthropic-agent-skills",
  "frontend-design@claude-plugins-official",
  "pm-skills@claude-code-skills",
  "reflexion@context-engineering-kit",
  "security-guidance@claude-plugins-official",
  "superpowers@claude-plugins-official"
)

foreach ($plugin in $plugins) {
    Write-Host "Instalando $plugin..." -ForegroundColor Yellow
    claude plugin install $plugin --scope user
}

Write-Host ""
Write-Host "Concluído. Use /plugins e /skills no Claude Code para conferir." -ForegroundColor Green
