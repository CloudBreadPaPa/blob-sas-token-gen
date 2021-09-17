# Azure Blob Storage SAS token generate code
In this repository, will generate Azure Blob Storage SAS token with Pyhton code

# Getting Started
TODO: Setup python 3.8+ environment and run code
- Create Azure Blob Storage in Azure
- review [Grant limited access to Azure Storage resources using shared access signatures (SAS)](https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview) doc and [Stack Overflow](https://stackoverflow.com/a/62673046)
- pip package insall code, `pip install azure-storage-blob`
- make & run `run-sas-token-gen.sh` with environment variable

## example `run-sas-token-gen.sh` file
```
export AZURE_ACC_NAME="<YOUR-AZURE-STORAGE-ACCOUNT-NAME>"
export AZURE_PRIMARY_KEY="<YOUR-AZURE-STORAGE-ACCOUNT-KEY>"
export AZURE_CONTAINER="<CONTAINER-NAME>"

python sas-token-gen.py
```

# Build and Test
- Compatible with Python 3.8+