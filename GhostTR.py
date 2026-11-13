#!/usr/bin/python
# << CODE BY HUNX04
# << MAU RECODE ??? IZIN DULU LAH,  MINIMAL TAG AKUN GITHUB MIMIN YANG MENGARAH KE AKUN INI, LEBIH GAMPANG SI PAKE FORK
# << KALAU DI ATAS TIDAK DI IKUTI MAKA AKAN MENDAPATKAN DOSA KARENA MIMIN GAK IKHLAS
# “Wahai orang-orang yang beriman! Janganlah kamu saling memakan harta sesamamu dengan jalan yang batil,” (QS. An Nisaa': 29). Rasulullah SAW juga melarang umatnya untuk mengambil hak orang lain tanpa izin.

# IMPORT MODULE

import argparse
import functools
import json
import requests
import socket
import time
import os
import phonenumbers
from concurrent.futures import ThreadPoolExecutor, as_completed
from phonenumbers import carrier, geocoder, timezone
from sys import stderr

REQUEST_TIMEOUT = 10
DEFAULT_PHONE_REGION = "TW"
WMN_DATA_URL = "https://raw.githubusercontent.com/WebBreacher/WhatsMyName/main/wmn-data.json"

Bl = '\033[30m'  # VARIABLE BUAT WARNA CUYY
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'


# utilities

# decorator for attaching run_banner to a function
def is_option(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        run_banner()
        func(*args, **kwargs)


    return wrapper


# FUNCTIONS FOR MENU
@is_option
def IP_Track(ip=None):
    if ip is None:
        ip = input(f"{Wh}\n Enter IP target : {Gr}")  # INPUT IP ADDRESS
    ip = ip.strip()
    if ip and ":" not in ip and not ip.replace(".", "").isdigit():
        try:
            resolved = socket.gethostbyname(ip)
        except (socket.gaierror, UnicodeError):
            print(f"\n {Re}Error : could not resolve hostname '{ip}'")
            return
        print(f"{Wh}\n Resolved {ip} to {Gr}{resolved}")
        ip = resolved
    try:
        ip_data = requests.get(f"https://ipwho.is/{ip}", timeout=REQUEST_TIMEOUT).json()  # API IPWHOIS.IS
    except requests.RequestException as e:
        print(f"\n {Re}Error : could not reach ipwho.is ({type(e).__name__})")
        return
    if not ip_data.get("success"):
        print(f"\n {Re}Error : {ip_data.get('message', 'lookup failed')}")
        return
    connection = ip_data.get("connection", {})
    tz = ip_data.get("timezone", {})
    print()
    print(f' {Wh}============= {Gr}SHOW INFORMATION IP ADDRESS {Wh}=============')
    print(f"{Wh}\n IP target       :{Gr}", ip_data.get("ip", ip))
    print(f"{Wh} Type IP         :{Gr}", ip_data.get("type"))
    print(f"{Wh} Country         :{Gr}", ip_data.get("country"))
    print(f"{Wh} Country Code    :{Gr}", ip_data.get("country_code"))
    print(f"{Wh} City            :{Gr}", ip_data.get("city"))
    print(f"{Wh} Continent       :{Gr}", ip_data.get("continent"))
    print(f"{Wh} Continent Code  :{Gr}", ip_data.get("continent_code"))
    print(f"{Wh} Region          :{Gr}", ip_data.get("region"))
    print(f"{Wh} Region Code     :{Gr}", ip_data.get("region_code"))
    print(f"{Wh} Latitude        :{Gr}", ip_data.get("latitude"))
    print(f"{Wh} Longitude       :{Gr}", ip_data.get("longitude"))
    print(f"{Wh} Maps            :{Gr}", f"https://www.google.com/maps?q={ip_data.get('latitude')},{ip_data.get('longitude')}")
    print(f"{Wh} EU              :{Gr}", ip_data.get("is_eu"))
    print(f"{Wh} Postal          :{Gr}", ip_data.get("postal"))
    print(f"{Wh} Calling Code    :{Gr}", ip_data.get("calling_code"))
    print(f"{Wh} Capital         :{Gr}", ip_data.get("capital"))
    print(f"{Wh} Borders         :{Gr}", ip_data.get("borders"))
    print(f"{Wh} Country Flag    :{Gr}", ip_data.get("flag", {}).get("emoji"))
    print(f"{Wh} ASN             :{Gr}", connection.get("asn"))
    print(f"{Wh} ORG             :{Gr}", connection.get("org"))
    print(f"{Wh} ISP             :{Gr}", connection.get("isp"))
    print(f"{Wh} Domain          :{Gr}", connection.get("domain"))
    print(f"{Wh} ID              :{Gr}", tz.get("id"))
    print(f"{Wh} ABBR            :{Gr}", tz.get("abbr"))
    print(f"{Wh} DST             :{Gr}", tz.get("is_dst"))
    print(f"{Wh} Offset          :{Gr}", tz.get("offset"))
    print(f"{Wh} UTC             :{Gr}", tz.get("utc"))
    print(f"{Wh} Current Time    :{Gr}", tz.get("current_time"))


@is_option
def phoneGW(number=None):
    if number is None:
        number = input(
            f"\n {Wh}Enter phone number target {Gr}Ex [+886912345678] {Wh}: {Gr}")  # INPUT NUMBER PHONE
    default_region = DEFAULT_PHONE_REGION

    try:
        parsed_number = phonenumbers.parse(number, default_region)  # VARIABLE PHONENUMBERS
    except phonenumbers.NumberParseException:
        print(f"\n {Re}Error : invalid phone number '{number}'")
        return
    region_code = phonenumbers.region_code_for_number(parsed_number)
    jenis_provider = carrier.name_for_number(parsed_number, "en")
    location = geocoder.description_for_number(parsed_number, "en")
    is_valid_number = phonenumbers.is_valid_number(parsed_number)
    is_possible_number = phonenumbers.is_possible_number(parsed_number)
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region,
                                                                                with_formatting=True)
    number_type = phonenumbers.number_type(parsed_number)
    timezone1 = timezone.time_zones_for_number(parsed_number)
    timezoneF = ', '.join(timezone1)

    print(f"\n {Wh}========== {Gr}SHOW INFORMATION PHONE NUMBERS {Wh}==========")
    print(f"\n {Wh}Location             :{Gr} {location}")
    print(f" {Wh}Region Code          :{Gr} {region_code}")
    print(f" {Wh}Timezone             :{Gr} {timezoneF}")
    print(f" {Wh}Operator             :{Gr} {jenis_provider}")
    print(f" {Wh}Valid number         :{Gr} {is_valid_number}")
    print(f" {Wh}Possible number      :{Gr} {is_possible_number}")
    print(f" {Wh}International format :{Gr} {formatted_number}")
    print(f" {Wh}Mobile format        :{Gr} {formatted_number_for_mobile}")
    print(f" {Wh}Original number      :{Gr} {parsed_number.national_number}")
    print(
        f" {Wh}E.164 format         :{Gr} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
    print(f" {Wh}Country code         :{Gr} {parsed_number.country_code}")
    print(f" {Wh}Local number         :{Gr} {parsed_number.national_number}")
    if number_type == phonenumbers.PhoneNumberType.MOBILE:
        print(f" {Wh}Type                 :{Gr} This is a mobile number")
    elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
        print(f" {Wh}Type                 :{Gr} This is a fixed-line number")
    else:
        print(f" {Wh}Type                 :{Gr} This is another type of number")


@is_option
def TrackLu(username=None):
    if username is None:
        username = input(f"\n {Wh}Enter Username : {Gr}")
    username = username.strip()
    if not username:
        print(f"\n {Wh}[ {Re}! {Wh}] {Re}Username cannot be empty")
        return

    try:
        sites = requests.get(WMN_DATA_URL, timeout=REQUEST_TIMEOUT).json()["sites"]
    except (requests.RequestException, ValueError, KeyError):
        print(f"\n {Wh}[ {Re}! {Wh}] {Re}Could not load the site list, check your connection")
        return
    # ponytail: the 23 POST sites are skipped; add POST support when needed.
    sites = [site for site in sites if site.get("valid", True) and "post_body" not in site]

    browser_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0"}
    found = {}
    errors = 0
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {}
        for site in sites:
            name = username
            for char in site.get("strip_bad_char", ""):
                name = name.replace(char, "")
            url = site["uri_check"].replace("{account}", name)
            headers = {**browser_headers, **site.get("headers", {})}
            futures[executor.submit(requests.get, url, headers=headers, timeout=REQUEST_TIMEOUT)] = (site, name)

        for checked, future in enumerate(as_completed(futures), 1):
            stderr.write(f"\r checked {checked}/{len(sites)}")
            stderr.flush()
            site, name = futures[future]
            try:
                response = future.result()
                if site_has_account(site, response.status_code, response.text):
                    found[site["name"]] = site.get("uri_pretty", site["uri_check"]).replace("{account}", name)
            except Exception:
                errors += 1
    stderr.write("\n")

    print(f"\n {Wh}========== {Gr}SHOW INFORMATION USERNAME {Wh}==========")
    print()
    for site_name in sorted(found):
        print(f" {Wh}[ {Gr}+ {Wh}] {site_name} : {Gr}{found[site_name]}")
    print(f"\n {Wh}found {Gr}{len(found)} {Wh}| checked {Gr}{len(sites)} {Wh}| errors {Gr}{errors}")


def site_has_account(site, status_code, text):
    return status_code == site["e_code"] and site["e_string"] in text


@is_option
def showIP():
    try:
        respone = requests.get('https://api.ipify.org/', timeout=REQUEST_TIMEOUT)
        respone.raise_for_status()
    except requests.RequestException as e:
        print(f"\n {Re}Error : could not reach api.ipify.org ({type(e).__name__})")
        return
    Show_IP = respone.text

    print(f"\n {Wh}========== {Gr}SHOW INFORMATION YOUR IP {Wh}==========")
    print(f"\n {Wh}[{Gr} + {Wh}] Your IP Adrress : {Gr}{Show_IP}")
    print(f"\n {Wh}==============================================")


# OPTIONS
options = [
    {
        'num': 1,
        'text': 'IP Tracker',
        'func': IP_Track
    },
    {
        'num': 2,
        'text': 'Show Your IP',
        'func': showIP

    },
    {
        'num': 3,
        'text': 'Phone Number Tracker',
        'func': phoneGW
    },
    {
        'num': 4,
        'text': 'Username Tracker',
        'func': TrackLu
    },
    {
        'num': 0,
        'text': 'Exit',
        'func': exit
    }
]


def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux
    else:
        _ = os.system('clear')


def call_option(opt):
    if not is_in_options(opt):
        raise ValueError('Option not found')
    for option in options:
        if option['num'] == opt:
            if 'func' in option:
                option['func']()
            else:
                print('No function detected')


def execute_option(opt):
    call_option(opt)
    input(f'\n{Wh}[ {Gr}+ {Wh}] {Gr}Press enter to continue')


def option_text():
    text = ''
    for opt in options:
        text += f'{Wh}[ {opt["num"]} ] {Gr}{opt["text"]}\n'
    return text


def is_in_options(num):
    for opt in options:
        if opt['num'] == num:
            return True
    return False


def option():
    # BANNER TOOLS
    clear()
    stderr.writelines(rf"""
       ________               __      ______                __  
      / ____/ /_  ____  _____/ /_    /_  __/________ ______/ /__
     / / __/ __ \/ __ \/ ___/ __/_____/ / / ___/ __ `/ ___/ //_/
    / /_/ / / / / /_/ (__  ) /_/_____/ / / /  / /_/ / /__/ ,<   
    \____/_/ /_/\____/____/\__/     /_/ /_/   \__,_/\___/_/|_| 

              {Wh}[ + ]  C O D E   B Y  H U N X  [ + ]
    """)

    stderr.writelines(f"\n\n\n{option_text()}")


def run_banner():
    clear()
    stderr.writelines(f"""{Wh}
         .-.
       .'   `.          {Wh}--------------------------------
       :g g   :         {Wh}| {Gr}GHOST - TRACKER - IP ADDRESS {Wh}|
       : o    `.        {Wh}|       {Gr}@CODE BY HUNXBYTS      {Wh}|
      :         ``.     {Wh}--------------------------------
     :             `.
    :  :         .   `.
    :   :          ` . `.
     `.. :            `. ``;
        `:;             `:'
           :              `.
            `.              `.     .
              `'`'`'`---..,___`;.-'
        """)


def main():
    notice = ''
    while True:
        option()
        stderr.write(notice)
        notice = ''
        try:
            opt = int(input(f"{Wh}\n [ + ] {Gr}Select Option : {Wh}"))
        except ValueError:
            notice = f'\n{Wh}[ {Re}! {Wh}] {Re}Please input number'
            continue
        if not is_in_options(opt):
            notice = f'\n{Wh}[ {Re}! {Wh}] {Re}Option not found'
            continue
        execute_option(opt)


def cli():
    parser = argparse.ArgumentParser(
        description='GhostTrack: OSINT lookups for IP addresses, phone numbers and usernames. '
                    'Run without a command for the interactive menu.')
    commands = parser.add_subparsers(dest='command', title='commands')
    ip_cmd = commands.add_parser('ip', help='track an IPv4/IPv6 address or domain, e.g. ip 8.8.8.8 '
                                            '(no target looks up your own IP)')
    ip_cmd.add_argument('target', nargs='?', help='IPv4, IPv6 or domain, e.g. 8.8.8.8 or example.com')
    commands.add_parser('myip', help='show your public IP, e.g. myip')
    phone_cmd = commands.add_parser('phone', help='track a phone number, e.g. phone +886912345678')
    phone_cmd.add_argument('number', help='e.g. +886912345678; numbers without + are parsed as '
                                          f'{DEFAULT_PHONE_REGION}')
    user_cmd = commands.add_parser('user', help='search a username on 600+ sites, e.g. user johndoe')
    user_cmd.add_argument('username', help='e.g. johndoe')
    args = parser.parse_args()

    if args.command == 'ip':
        IP_Track.__wrapped__(args.target or "")
    elif args.command == 'myip':
        showIP.__wrapped__()
    elif args.command == 'phone':
        phoneGW.__wrapped__(args.number)
    elif args.command == 'user':
        TrackLu.__wrapped__(args.username)
    else:
        main()


if __name__ == '__main__':
    try:
        cli()
    except (KeyboardInterrupt, EOFError):
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit')
