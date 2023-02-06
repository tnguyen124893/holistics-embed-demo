# Example code below uses pyJWT for encoding
# Please execute 'pip install PyJWT' to install it first

import time
import jwt
import json

embed_code = "9095310189db79f89c738dd2"
secret_key = "cdd4014a564fd7b992af773e518eb2c14015939d5c89cd10708ff0aad52118f9862080f9157e81da0de13096d7377b567d2b5b458ba2aeac4e685adb43d8d4a7"

# Will expire after 1 day, change it to the value that you want
expired_time = int(time.time()) + 24 * 60 * 60
settings = {
  "enable_export_data": False
}

permissions = {
  "row_based": []
}

filters = {
  "date": {
    "hidden": False,
    "default_condition": {
      "operator": "matches",
      "values": [
        None
      ],
      "modifier": None,
      "options": None
    }
  }
}


payload = {
  "settings": settings,
  "permissions": permissions,
  "filters": filters,
  "exp": expired_time
}

token = jwt.encode(payload, secret_key, 'HS256')
token = token.decode('utf-8') # This is to remove b-prefix of byte literals
