import requests
from requests.exceptions import ConnectionError
requests.packages.urllib3.disable_warnings()

def rest_connect(device, container, headers):

#auth_var,

      url = f"https://{device}{container}"

      try:
            response = requests.get(
                                    url,
                                   # auth=auth_var,
                                    headers=headers,
                                    verify=False,
                                    timeout=3)

            if response.status_code == 200:
                  return response.json(), True

      except ConnectionError:
            return "unsuccessful connection", False

      return f"unsuccessful:{response.status_code}", False
