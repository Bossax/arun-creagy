param(
    [Parameter(Mandatory = $true)]
    [string]$NotebookId,

    [Parameter(Mandatory = $true)]
    [string]$PromptFile,

    [string[]]$SourceIds = @(),

    [string]$OutputDir = "notebooklm_runs",

    [switch]$Inventory
)

$ErrorActionPreference = 'Stop'

function Write-RunHeader {
    param(
        [string]$Title,
        [string]$Path
    )

    Write-Host "[$Title] $Path"
}

if (-not (Test-Path -LiteralPath $PromptFile)) {
    throw "Prompt file not found: $PromptFile"
}

if (-not (Test-Path -LiteralPath $OutputDir)) {
    New-Item -ItemType Directory -Path $OutputDir | Out-Null
}

$prompt = Get-Content -LiteralPath $PromptFile -Raw
$timestamp = Get-Date -Format 'yyyy-MM-dd_HHmm'

Write-Host "Checking NotebookLM auth..."
& nlm login --check | Out-Host

if ($Inventory) {
    $inventoryPath = Join-Path $OutputDir "${timestamp}_raw_source_inventory.json"
    Write-Host "Listing sources for notebook $NotebookId"
    & nlm list sources $NotebookId --json | Tee-Object -FilePath $inventoryPath | Out-Host
    Write-RunHeader -Title 'Inventory saved to' -Path $inventoryPath
    return
}

$queryArgs = @('query', 'notebook', $NotebookId, $prompt)
if ($SourceIds.Count -gt 0) {
    $queryArgs += @('-s', ($SourceIds -join ','))
}
$queryArgs += @('--json', '--timeout', '120')

$runName = [IO.Path]::GetFileNameWithoutExtension($PromptFile)
$safeRunName = ($runName -replace '[^A-Za-z0-9._-]', '_')
$outputPath = Join-Path $OutputDir "${timestamp}_raw_${safeRunName}.json"

Write-Host "Running NotebookLM query for notebook $NotebookId"
& nlm @queryArgs | Tee-Object -FilePath $outputPath | Out-Host

Write-RunHeader -Title 'Query saved to' -Path $outputPath
