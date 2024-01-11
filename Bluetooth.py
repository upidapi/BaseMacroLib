import subprocess

# inp
HEADPHONES_NAME = "WH-1000XM4"

# https://stackoverflow.com/questions/54338990/how-can-i-run-windows-powershell-commands-from-python
PS_DIR = r"%SystemRoot%\system32\WindowsPowerShell\v1.0\powershell.exe"

# https://stackoverflow.com/questions/62502414/how-to-connect-to-a-paired-audio-bluetooth-device-using-windows-uwp-api/71539568#71539568

x = f"""
# "Disable-PnpDevice" and "Enable-PnpDevice" commands require admin rights
#Requires -RunAsAdministrator

$headphonesName = "{HEADPHONES_NAME}"

$bluetoothDevices = Get-PnpDevice -class Bluetooth

# here we get the following devices:             
# * OK          Microsoft Bluetooth LE Enumerator     
# * OK          TP-Link Bluetooth 5.0 USB Adapter     
# * Unknown     Microsoft Bluetooth LE Enumerator     
# * Unknown     WH-1000XM4                            
# * OK          Service Discovery Service             
# * OK          Personal Area Network NAP Service     
# * OK          WH-1000XM4                            
# * Unknown     WH-1000XM4 Avrcp Transport            
# * Unknown     Intel(R) Wireless Bluetooth(R)        
# * OK          WH-1000XM4 Avrcp Transport            
# * OK          Microsoft Bluetooth Enumerator        
# * OK          Vides – iPhone Avrcp Transport        
# * OK          WH-1000XM4 Avrcp Transport            
# * Unknown     Microsoft Bluetooth Enumerator        
# * OK          Bluetooth Device (RFCOMM Protocol TDI)
# * Unknown     Bluetooth Device (RFCOMM Protocol TDI)
# * OK          Vides – iPhone Avrcp Transport        
# * OK          Phonebook Access Pse Service          
# * OK          Vides – iPhone                        
# * Unknown     WH-1000XM4 Avrcp Transport            

# first we find the devices "associated" to our headphones
# by checking if the name starts with $headphonesName
# here we get the following devices:             
# * Unknown     WH-1000XM4                            
# * OK          WH-1000XM4                            
# * Unknown     WH-1000XM4 Avrcp Transport            
# * OK          WH-1000XM4 Avrcp Transport            
# * OK          WH-1000XM4 Avrcp Transport            
# * Unknown     WH-1000XM4 Avrcp Transport            

# for some reason they're duplicated
# where the duplicates have a status of unknown
# if we try to do the following steps with them, it just crashes

$headphonePnpDevices = $bluetoothDevices | Where-Object {{ $_.Name.StartsWith("$headphonesName") }} | Where-Object {{ $_.Status -eq ‘OK’ }}

if(!$headphonePnpDevices) {{
    Write-Host "Couldn't find any devices related to the '$headphonesName'"
    Write-Host "Whole list of available devices is:"
    $bluetoothDevices
    return
}}

# ForEach($d in $headphonePnpDevices) {{$d}}

# Disable all these devices
ForEach($d in $headphonePnpDevices) {{
    Disable-PnpDevice -InstanceId $d.InstanceId -Confirm:$false
}}

# Enable all these devices
ForEach($d in $headphonePnpDevices) {{
    Enable-PnpDevice -InstanceId $d.InstanceId -Confirm:$false
}}

Write-Host "connected to $headphonesName" 


# The headphones should be connected now
# It may take around 10 seconds until the Windows starts showing audio devices related to these headphones
"""

print(x
      .replace("{{", "{")
      .replace("}}", "}")
)
print(subprocess.call(["powershell", "/C", x]))


