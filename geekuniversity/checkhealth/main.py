import requests
from requests import Response

import subprocess

result = subprocess.run(["pgrep", "java"], stdout=subprocess.PIPE)
STATUSPID = result.stdout.decode("utf-8").strip()

SERVER_IP = "192.168.5.14"

def verificarServico():
    if STATUSPID is None:
        pass
        print("Reiniciar Wildfly")
        #reiniciarWildfly()
    else:
        for i in range(1, 4):
            response = requests.get("http://" + SERVER_IP + "/login.jsf", timeout=15)

    STATUSCODE = Response.status_code
    print(STATUSCODE)

    if STATUSCODE is None:
        STATUSCODE = "NULL"
        MESSAGE = "STATUS CODE da página recebido é " + STATUSCODE
        # gravarLog()
        # notificacao()
    else:
        if STATUSCODE != 200:
            MESSAGE = "STATUS CODE da página recebido é " + STATUSCODE
            # gravarLog()
            # notificacao()
        else:
            exit()
    
    print(MESSAGE)

verificarServico()