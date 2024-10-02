param($ProductName = 'Code Modern Explorer Menu', $Variant = 'stable', $Platform = 'x64', $Version = '1.0.0')

Import-Module PSMSI

$ScriptRoot = if ( $PSScriptRoot ) { $PSScriptRoot} else { ($(try { $script:psEditor.GetEditorContext().CurrentFile.Path } catch {}), $script:MyInvocation.MyCommand.Path, $script:PSCommandPath, $(try { $script:psISE.CurrentFile.Fullpath.ToString() } catch {}) | % { if ($_ ) { $_.ToLower() } } | Split-Path -EA 0 | Get-Unique ) | Get-Unique }

$OutputDirectory = "$ScriptRoot\output"

if (Test-Path $OutputDirectory) {
    Get-ChildItem -Path $OutputDirectory | ForEach-Object { Remove-Item -Path $_ -Force -Recurse  }
}

$ProductId = 'a434e5cf-1a39-49a1-b956-362c95aa85df'
$UpgradeCode = '6b06a391-688d-4b09-961c-9a655292bc05'

if ($Variant -eq 'insiders') {
    $ProductName = 'Code Insiders Modern Explorer Menu'
    $ProductId = 'd634ca99-9829-44e2-a4bb-48f9e726fa3b'
    $UpgradeCode = '41d8bac9-bea2-457b-ac00-8c296b1d8e1b'
}

$CustomAction = @(
    New-InstallerCustomAction -FileId 'RunOnInstall' -RunOnInstall
    New-InstallerCustomAction -FileId 'RunOnUninstall' -RunOnUninstall
)

$InstallerFile = {
    New-InstallerFile -Source "$ScriptRoot\[Content_Types].xml"
    New-InstallerFile -Source "$ScriptRoot\AppxBlockMap.xml"
    New-InstallerFile -Source "$ScriptRoot\out\$($Variant)_explorer_pkg_$($Platform)\AppxManifest.xml"
    New-InstallerFile -Source "$ScriptRoot\out\$ProductName $Platform.appx"
    New-InstallerFile -Source "$ScriptRoot\out\$ProductName.dll"
    New-InstallerFile -Source "$ScriptRoot\msi\RunOnInstall.ps1" -Id 'RunOnInstall'
    New-InstallerFile -Source "$ScriptRoot\msi\RunOnUninstall.ps1" -Id 'RunOnUninstall'
}

New-Installer -ProductName $ProductName -ProductId $ProductId -UpgradeCode $UpgradeCode -Platform $Platform -Version $Version -Content {
    New-InstallerDirectory -PredefinedDirectory "LocalAppDataFolder" -Content {
        New-InstallerDirectory -DirectoryName "Programs" -Content {
            New-InstallerDirectory -DirectoryName $ProductName -Content $InstallerFile
        }
    }
} -CustomAction $CustomAction -OutputDirectory $OutputDirectory #-RequiresElevation
