# https://superuser.com/questions/1426949/scripting-connecting-disconnecting-a-paired-bluetooth-device

headphones_name = "WH-1000XM4"
headphones_addr = "WH-1000XM4"

# connect
# btcom -b AC:80:0A:2E:81:6A -c -s110E

# disconnect
# btcom -b AC:80:0A:2E:81:6A -r -s110E

# find
# PS C:\Windows\system32> btdiscovery -s
# (44:4A:DB:34:C5:6E) Vides û iPhone
#         1801    0       GATT
#         7C74    0       AAP Client
#         1134    2       MAP MAS-iOS
#         1116    0       PAN Network Access Profile
#         1101    1       Wireless iAP v2
#         1101    1       Wireless iAP
#         110E    0       AVRCP Device
#         110E    0       AVRCP Device
#         110D    0       Audio Source
#         1130    13      Phonebook
#         111E    8       Handsfree Gateway
#         1000    0
# (AC:80:0A:2E:81:6A) WH-1000XM4
#         111E    1       Hands-Free unit
#         1108    2       Headset
#         110D    0
#         110E    0
#         110E    0
#         1101    10      IAPSERVER
#         1101    9       Serial HPC
#         1101    11      Serial MC
#         1101    21      Airoha_APP
#         1101    19      GSOUND_BT_CONTROL
#         1101    20      GSOUND_BT_AUDIO
#         7E8A    22      Amazon Alexa
# PS C:\Windows\system32>
