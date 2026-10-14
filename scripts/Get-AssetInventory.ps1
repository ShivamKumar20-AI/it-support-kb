<#
.SYNOPSIS
    Collects basic asset details from a Windows PC and appends them to a CSV.
.EXAMPLE
    .\Get-AssetInventory.ps1 -OutputPath .\asset_record.csv
#>
param(
    [string]$OutputPath = ".\asset_record.csv"
)

$cs   = Get-CimInstance Win32_ComputerSystem
$bios = Get-CimInstance Win32_BIOS
$os   = Get-CimInstance Win32_OperatingSystem
$disk = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'"

$record = [PSCustomObject]@{
    collected_at  = (Get-Date).ToString("s")
    hostname      = $env:COMPUTERNAME
    username      = $env:USERNAME
    os            = $os.Caption
    os_version    = $os.Version
    architecture  = $os.OSArchitecture
    manufacturer  = $cs.Manufacturer
    model         = $cs.Model
    serial_number = $bios.SerialNumber
    ram_gb        = [math]::Round($cs.TotalPhysicalMemory / 1GB, 1)
    disk_total_gb = [math]::Round($disk.Size / 1GB, 1)
    disk_free_gb  = [math]::Round($disk.FreeSpace / 1GB, 1)
}

$record | Export-Csv -Path $OutputPath -Append -NoTypeInformation
Write-Host "Recorded $($record.hostname) to $OutputPath"
