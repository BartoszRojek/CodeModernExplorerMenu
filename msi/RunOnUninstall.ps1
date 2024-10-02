# If not running as Administrator, re-launch the script with elevated privileges
if (-not ([Security.Principal.WindowsPrincipal]::new([Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator))) {
    Start-Process powershell.exe -ArgumentList "-NoLogo -NoProfile -NonInteractive -ExecutionPolicy Bypass -File `"$($script:MyInvocation.MyCommand.Path)`"" -Verb RunAs -Wait -WindowStyle Minimized
    exit
}

$ScriptRoot = if ( $PSScriptRoot ) { $PSScriptRoot } else { ($(try { $script:psEditor.GetEditorContext().CurrentFile.Path } catch {}), $script:MyInvocation.MyCommand.Path, $script:PSCommandPath, $(try { $script:psISE.CurrentFile.Fullpath.ToString() } catch {}) | % { if ($_ ) { $_.ToLower() } } | Split-Path -EA 0 | Get-Unique ) | Get-Unique }

$ProductName = 'Code Modern Explorer Menu'
$PackageName = $ProductName -replace '\s+', '.'
$RegKeyPath = 'HKCU\SOFTWARE\Classes\' + $ProductName -replace '\s+'

if ($ScriptRoot -match 'Insiders') {
    $ProductName = 'Code Insiders Modern Explorer Menu'
    $PackageName = $ProductName -replace '\s+', '.'
    $RegKeyPath = 'HKCU\SOFTWARE\Classes\' + $ProductName -replace '\s+'
}

# Process both cases at once
REG DELETE "$RegKeyPath" /reg:64 /f
REG DELETE "$RegKeyPath" /reg:32 /f

Get-AppxPackage -Name $PackageName | Remove-AppxPackage 

if ($ScriptRoot -eq "$Env:LOCALAPPDATA\Programs\$ProductName") {
    Remove-Item -Path "$Env:LOCALAPPDATA\Programs\$ProductName" -Recurse -Force
}
