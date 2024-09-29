import psutil
import requests
from dotenv import dotenv_values


def merge_envs(base: dict, override: dict) -> dict:
    result: dict = base.copy()
    result.update(override)

    return result


def get_message() -> str:
    message: str = ''
    temperatures: dict = psutil.sensors_temperatures()

    for name, entries in temperatures.items():
        message += name + '\n'

        for entry in entries:
            message += ("    %-20s %s °C (high = %s °C, critical = %s °C)\n" % (
                entry.label or name,
                entry.current,
                entry.high,
                entry.critical))

        message += '\n'

    return message


env: dict = merge_envs(
    base=dotenv_values('.env'),
    override=dotenv_values('.env.local'),
)

token: str = env['TOKEN']
chat_id: str = env['CHAT_ID']
message: str = get_message()
url: str = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"

print(requests.get(url).json())
