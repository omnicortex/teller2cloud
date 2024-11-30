import http.client
from beautifultable import BeautifulTable
import ssl
import json
from base64 import b64encode
from colored import fg, bg, attr
import pandas as pd
import click
import warnings
import os
from dotenv import load_dotenv
from teller import *

warnings.filterwarnings("ignore", category=DeprecationWarning) 

load_dotenv()

MY_ENV_VAR = os.getenv('MY_ENV_VAR')
# use certificate and private key, replace with your own ones
certificate_file = os.getenv('PATH_TO_CERTIFICATE')
pk_file = os.getenv('PATH_TO_PRIVATE_KEY')
context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.load_cert_chain(certfile=certificate_file, keyfile=pk_file)
conn = http.client.HTTPSConnection("api.teller.io", port=443, context=context)


def main():
    df_token = pd.read_csv('tokens.csv')
    df = df_token.reset_index()  # make sure indexes pair with number of rows

    for index, row in df.iterrows():
        print(row['token'], row['institution'])
        try:
            token = row['token']
            token += ":"
            encodedToken = b64encode(token.encode()).decode()
            accountData = listAccounts(encodedToken)
            if len(accountData) == 0: continue
            else: 
                for accountSel in range(len(accountData)):
                    txns = listTxns(encodedToken,accountData[int(accountSel)]["id"])
                    exportTxnCSV(txns,accountData[int(accountSel)])
                    print('%sCSV saved to current directory%s' % (fg(2),attr(0)))
        except KeyboardInterrupt:
            break

main()
