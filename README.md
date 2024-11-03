# tg-info-alerter

Install requirements:

```bash
pip install -r requirements.txt
```

Configure `.env` or create `.env.local` and run:

```bash
python alerter.py
```

Crontab:

```bash
* * * * * /usr/bin/python3 /path/to/alerter.py > /path/to/alerter.log
```
