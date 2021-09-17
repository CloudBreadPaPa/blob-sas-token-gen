
import os
import logging
from datetime import datetime, timedelta
from azure.storage.blob import generate_blob_sas, BlobSasPermissions


AZURE_ACC_NAME = os.environ['AZURE_ACC_NAME']
AZURE_PRIMARY_KEY = os.environ['AZURE_PRIMARY_KEY']
AZURE_CONTAINER = os.environ['AZURE_CONTAINER']
file_name = "test.csv"

def generate_sas_token(file_name):
    sas = generate_blob_sas(account_name=AZURE_ACC_NAME,
                            account_key=AZURE_PRIMARY_KEY,
                            container_name=AZURE_CONTAINER,
                            blob_name=file_name,
                            permission=BlobSasPermissions(read=True),
                            expiry=datetime.utcnow() + timedelta(hours=2))

    logging.info('https://'+AZURE_ACC_NAME+'.blob.core.windows.net/'+AZURE_CONTAINER+'/'+file_name+'?'+sas)
    sas_url ='https://'+AZURE_ACC_NAME+'.blob.core.windows.net/'+AZURE_CONTAINER+'/'+file_name+'?'+sas
    return sas_url

print(generate_sas_token(file_name))