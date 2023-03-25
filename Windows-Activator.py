import os
import time
from colorama import Fore
import random

os.system("title WINTO10 - Windows Activation Multitool")
os.system("mode con:cols=80 lines=20")
os.system("cls")

print(f"""{Fore.WHITE}
            ══════════════════════════════════════════════

                    {Fore.LIGHTGREEN_EX}[{Fore.WHITE}1{Fore.LIGHTGREEN_EX}]{Fore.WHITE}. Activate Windows
                    {Fore.LIGHTGREEN_EX}[{Fore.WHITE}2{Fore.LIGHTGREEN_EX}]{Fore.WHITE}. Generate Windows 10 Key

                    {Fore.LIGHTGREEN_EX}[{Fore.WHITE}E{Fore.LIGHTGREEN_EX}]{Fore.WHITE}. Exit

            ══════════════════════════════════════════════
""")

main = input("      > ")

if main == "1":
    os.system("slmgr /ipk AKSIU-WY2CT-JWBJ2-T68TQ-YBH2V")
    os.system("slmgr /skms kms8.msguides.com")
    os.system("slmgr /ato")

    print(f"\n{Fore.LIGHTGREEN_EX} Windows is activated!")

    print(f"\n{Fore.LIGHTGREEN_EX} Restart your computer!!!!!!!!!!!!!"*5)
    time.sleep(50)


elif main == "2":
    keys = [
        'VK7JG-NPHTM-C97JM-9MPGT-3V66T',
        'DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4',
        'W269N-WFGWX-YVC9B-4J6C9-T83GX',
        'MH37W-N47XK-V7XM9-C7227-GCQG9',
        'TX9XD-98N7V-6WMQ6-BX7FG-H8Q99',
        'WNMTR-4C88C-JK8YV-HQ7T2-76DF9',
        'W269N-WFGWX-YVC9B-4J6C9-T83GX',
        'AKJUS-WY2CT-JWBJ2-T68TQ-YBH2V',
        'JAHSU-QMPVW-D7KKK-3GKT6-VCFB2',
        'AKSIU-WY2CT-JWBJ2-T68TQ-YBH2V',
        'SJUY7-NFMTC-H88MJ-PFHPY-QJ4BJ',
        'AJUYS-8C467-V2W6J-TX4WX-WT2RQ',
        'AJSU7-GRT3P-VKWWX-X7T3R-8B639',
        'ALSOI-MHBT6-FXBX8-QWJK7-DRR8H',
        '8UY76-TNFGY-69QQF-B8YKP-D69TJ',
        'AJSUY-NPHTM-C97JM-9MPGT-3V66T',
        'ALSOI-4C88C-JK8YV-HQ7T2-76DF9',
        'CB7KF-BWN84-R7R2Y-793K2-8XDDG',
        'WC2BQ-8NRM3-FDDYY-2BFGV-KHKQY',
        'JCKRF-N37P4-C2D82-9YXRT-4M63B',
        'W269N-WFGWX-YVC9B-4J6C9-T83GX',
        'MH37W-N47XK-V7XM9-C7227-GCQG9',
        'NPPR9-FWDCX-D2C8J-H872K-2YT43',
        'DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4',
        'NW6C2-QMPVW-D7KKK-3GKT6-VCFB2',
        '2WH4N-8QGBV-H22JP-CT43Q-MDWWJ'
    ]
    print(Fore.LIGHTGREEN_EX)
    print(f"Heres a Windows 10 activation key: {random.choice(keys)}")
    os.system("pause")

elif main == "E" or main == "e":
    exit()

else:
    print(Fore.LIGHTGREEN_EX)
    print("Wrong choice run the script again")
    os.system("pause")
