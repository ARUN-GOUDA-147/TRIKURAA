from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "12787577"))
API_HASH = getenv("API_HASH", "d30cef43991a144be80615919bfcfc6c")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","TRIKURAA")
BOT_USERNAME = getenv("BOT_USERNAME", "TRIKURAA_BOT")
OWNER_USERNAME = getenv("OWNER_USERNAME", "@my_heart_beats_147")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "agora_robots")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/aa3e01fa6489ec19cbf9d.jpg")
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/aa3e01fa6489ec19cbf9d.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5176660730").split()))
