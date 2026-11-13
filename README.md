# GhostTrack
Useful tool to track location or mobile number, so this tool can be called osint or also information gathering

This is a fork of [HunxByts/GhostTrack](https://github.com/HunxByts/GhostTrack) that adds a command-line mode, a larger username search and a few usability fixes.

<img src="https://github.com/HunxByts/GhostTrack/blob/main/asset/bn.png"/>

### Installation (macOS / Linux)
Requires git and Python 3.
```
git clone https://github.com/calvinlee326/GhostTrack.git
cd GhostTrack
python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```

### Usage
Interactive menu:
```
python3 GhostTR.py
```

Command line:
```
python3 GhostTR.py ip 8.8.8.8              # IPv4, IPv6 or domain
python3 GhostTR.py ip                      # no target: look up your own IP
python3 GhostTR.py myip                    # show your public IP
python3 GhostTR.py phone +886912345678     # phone number
python3 GhostTR.py user johndoe            # username
python3 GhostTR.py --help
```

- Phone numbers without a leading `+` are treated as Taiwanese. Change `DEFAULT_PHONE_REGION` in `GhostTR.py` to use another default region.
- Username search checks the [WhatsMyName](https://github.com/WebBreacher/WhatsMyName) dataset (600+ sites) and shows only the accounts that were found.

Display on the menu ```IP Tracker```

<img src="https://github.com/HunxByts/GhostTrack/blob/main/asset/ip.png " />

on the IP Track menu, you can combo with the seeker tool to get the target IP
<details>
<summary>:zap: Install Seeker :</summary>
- <strong><a href="https://github.com/thewhiteh4t/seeker">Get Seeker</a></strong>
</details>

Display on the menu ```Phone Tracker```

<img src="https://github.com/HunxByts/GhostTrack/blob/main/asset/phone.png" />

on this menu you can search for information from the target phone number

Display on the menu ```Username Tracker```

<img src="https://github.com/HunxByts/GhostTrack/blob/main/asset/User.png"/>
on this menu you can search for the target username across the WhatsMyName site list

<details>
<summary>:zap: Author :</summary>
- <strong><a href="https://github.com/HunxByts">HunxByts</a></strong>
</details>
