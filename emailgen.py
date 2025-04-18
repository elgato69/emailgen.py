import requests
import argparse
import yaml
from dataclasses import dataclass

cfg = None

@dataclass
class Config:
    base_domain: str
    mailcow_endpoint: str
    mailcow_api_key: str
    dest_mailbox: str

def generate_random_name():
    response = requests.get('https://random-word-api.vercel.app/api?words=2') # todo: something more reliable
    if (response.status_code == 200):
        return "".join(response.json())
    else:
        print (f"Error generating random name: {response.status_code}")
    
def generate_email_address(name):
    address = f"{name}@{cfg.base_domain}"
    endpoint = f"https://{cfg.mailcow_endpoint}/api/v1/add/alias"

    payload = {
        "address": address,
        "goto": cfg.dest_mailbox,
        "active": "1"
    }
    headers = {
        "X-API-Key": cfg.mailcow_api_key,
        "Content-Type": "application/json"
    }
    response = requests.post(
        endpoint,
        json=payload,
        headers=headers
    )

    if response.status_code == 200:
        print(f"Successfully created email: {address}")
    else:
        print (f"Error generating email {response.status_code}");

def initialize():
    global cfg
    parser = argparse.ArgumentParser(
        prog="emailgen.py",
        description="Generate new random email addresses on mail.lmoss.co.za"
    )

    parser.add_argument(
        '--new',
        action='store_true',
        help="Generate a new email address"
    )

    parser.add_argument(
        '--custom-name',
        type=str,
        default=None,
        metavar="NAME",
        help="Specify your own name instead of an auto-generated one"
    )

    args = parser.parse_args()

    with open("config.yml", "r") as f:
        config = yaml.safe_load(f)
        cfg = Config(
            base_domain=config["BASE_DOMAIN"],
            mailcow_endpoint=config["MAILCOW_ENDPOINT"],
            mailcow_api_key=config["MAILCOW_API_KEY"],
            dest_mailbox=config["DEST_MAILBOX"]
        )
        
    if args.custom_name is not None and not args.new:
        parser.error("--custom-name can only be used together with --new")
        return None

    return args
    
def main():
    args = initialize()
    if args is not None and args.new:
        try:
            name = args.custom_name if args.custom_name is not None else generate_random_name()
            generate_email_address(name)
        except requests.HTTPError as e:
            print (f'Error generating email address: {e}')


main()