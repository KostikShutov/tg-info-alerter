# tg-info-alerter

Install requirements:

```bash
pip install -r requirements.txt
```

Run:

```bash
python alerter.py
```

Crontab:

```bash
*/10 * * * * /usr/bin/python3 /path/to/alerter.py > /tmp/alerter.log
```
