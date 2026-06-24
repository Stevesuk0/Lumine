$VERSION = "1.4"
$LUMINE_PY = "src\lumine.py"
$DIST_DIR = "dist\lumine"
$LANGS = @("en_US", "hi_IN", "ja_JP", "ko_KR", "ru_RU", "zh_CN", "zh_TW")

$originalContent = Get-Content $LUMINE_PY -Raw

function Set-Language($lang) {
    $content = $originalContent
    foreach ($l in $LANGS) {
        if ($l -eq $lang) {
            $content = $content -replace "(?m)^# (use_language = $l)", '$1'
        } else {
            $content = $content -replace "(?m)^(use_language = $l)", '# $1'
        }
    }
    Set-Content $LUMINE_PY $content -NoNewline
}

foreach ($lang in $LANGS) {
    Write-Host ""
    Write-Host "========================================"
    Write-Host "  Packing: Lumine-v$VERSION-$lang"
    Write-Host "========================================"

    Write-Host "[1/4] Setting language to $lang..."
    Set-Language $lang

    Write-Host "[2/4] Building with PyInstaller..."
    pyinstaller --icon=App.ico src/lumine.py --uac-admin -w
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Build failed for $lang!" -ForegroundColor Red
        Set-Content $LUMINE_PY $originalContent -NoNewline
        exit 1
    }

    Write-Host "[3/4] Copying icons..."
    Copy-Item -Path "icons" -Destination "$DIST_DIR\icons" -Recurse -Force

    Write-Host "[4/4] Zipping..."
    $zipName = "Lumine-v$VERSION-$lang.zip"
    if (Test-Path $zipName) { Remove-Item $zipName -Force }
    Compress-Archive -Path "$DIST_DIR\*" -DestinationPath $zipName
    Write-Host "  -> $zipName created." -ForegroundColor Green
}

Write-Host ""
Write-Host "Restoring lumine.py..."
Set-Content $LUMINE_PY $originalContent -NoNewline

Write-Host ""
Write-Host "All done!" -ForegroundColor Green
