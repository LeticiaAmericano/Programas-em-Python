$ErrorActionPreference = "Stop"

#Comando que retorna os nomes das impressoras
function Name
{
    Get-Printer | select Name | Format-Wide -Column 1
}

#Comando que retorna os nomes dos drivers das impressoras
function DriverName
{
    Get-Printer | select DriverName | Format-Wide -Column 1
}

#Comando que retorna as portas das impressoras
function PortName
{
    Get-Printer | select PortName | Format-Wide -Column 1
}

#Comando que retorna o processador de impressão
function PrintProcessor
{
    Get-Printer | select PrintProcessor | Format-Wide -Column 1
}