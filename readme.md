# 📧 emailgen.py

**emailgen.py** is a small Python script for generating throwaway email addresses by creating aliases on a [Mailcow](https://mailcow.email/) server.

Note: this script creates **ALIASES** not full mailboxes, because I use this to generate steam accounts and have all the 2fa confirmations in a single mailbox.

---

## Usage

### Create a new alias with a random name

```bash
python emailgen.py --new
```

### Specify a custom name instead of a randomly generated one
```bash
python emailgen.py --new --custom-name myalias
```
---

## Requirements

- Python 3.7+
- A running [Mailcow](https://mailcow.email/) instance
- An API key with permission to create aliases

Install dependencies:

```bash
pip install requests pyyaml
```

Set required values in config.yml

```yaml
#base domain to create addresses for. change to your own domain
BASE_DOMAIN: example.com

#the public-facing address of your mailcow instance
MAILCOW_ENDPOINT: mailcow.example.com

#api key for your mailcow user
MAILCOW_API_KEY: 000000-000000-000000-000000-000000

#the destination mailbox for the alias, since this script works by creating aliases and not full mailboxes
DEST_MAILBOX: tempmail@example.com
```

---

## Todo

- Automatic clearing of aliases older than a given time period
- Check if alias exists before attempting to add
- Ability to delete and edit aliases
- Ability to add a full mailbox