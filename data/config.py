BOT_TOKEN = '7198896114:AAGVuEFYdkMj-AtTxjw_ke53ri3SV0C9h3Q'

PREFIX = "!/."

ANTISPAM = int(120)

OWNER = 6191863486

APP_ID = ""

API_HASH = ''

SESSION = ""

OWNERID = int(6191863486)

OWNER_NAME = "<a href='tg://user?id=6191863486'>⏤͟͞B3</a>"

CHANNEL = "https://t.me/Brav_Updates"

GROUP = "https://t.me/Brav_Updates"

OWNER_LINK = "https://t.me/Was_B3"

from database import check_user, check_admin

def check_owner(id):
  if id == OWNER: return True
def ok(id):
  if check_owner(id):
    user = "OWNER"
    return user
  if check_admin(id) == True:
    user = "ADMIN"
    return user

  elif check_user(id) == True:
    user = "PAID"
    return user

  elif check_user(id) == False or check_admin(id) == False:
    user = "FREE"
    return user

  else:
    user = "FREE"
    return user
