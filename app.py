from datetime import datetime
from dateutil.relativedelta import relativedelta
import SoftLayer, argparse, os, logging, logging.config, json
import pandas as pd
import numpy as np
from logdna import LogDNAHandler
import ibm_boto3
from ibm_botocore.client import Config, ClientError
from ibm_platform_services import IamIdentityV1, UsageReportsV4
from ibm_cloud_sdk_core import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apiKey = os.environ.get('LOGDNA_INGESTION_KEY')

log = logging.getLogger('logdna')
log.setLevel(logging.INFO)

options = {
  'env': 'CodeEngine',
  'level': 'Info',
  'index_meta': True,
  'url': 'https://logs.us-south.logging.cloud.ibm.com/logs/ingest'
}

ibmlogging = LogDNAHandler(apiKey, options)

log.addHandler(ibmlogging)

bind_data = os.environ.get('CE_SERVICES')
print(bind_data)

log.info(bind_data)


# cos = ibm_boto3.resource("s3",
#     ibm_api_key_id=os.environ.get('COS_APIKEY'),
#     ibm_service_instance_id=os.environ.get('COS_CRN'),
#     config=Config(signature_version="oauth"),
#     endpoint_url=os.environ.get('COS_ENDPOINT')
# )

# dict = json.loads(os.environ['CE_DATA'])
# bucket_name = dict['bucket']
# item_name = dict['key']
# parse_bucket = os.environ.get('COS_PARSED_BUCKET')

# print(bucket_name)
# print(item_name)
# print(parse_bucket)

# cos.meta.client.download_file(bucket_name, item_name, 'invoice.xlsx')

# usage = pd.read_excel('invoice.xlsx', 'PaaS_Usage', engine='openpyxl')
# charges = usage.get(["charges"])

# charges.to_csv('charges.csv', na_rep='(missing)')

# cos.Object(parse_bucket, 'parsed-invoice.csv').upload_file('charges.csv')

