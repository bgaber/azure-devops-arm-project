import logging
import json
import os

import azure.functions as func
import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey

HOST = os.environ['COSMOS_DB_HOST']
MASTER_KEY = os.environ['COSMOS_MASTER_KEY']
DATABASE_ID = os.environ['COSMOS_DATABASE_ID']
CONTAINER_ID = os.environ['COSMOS_CONTAINER_ID']
PREFIX = os.environ['COSMOS_PREFIX']

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info(f"Python HTTP trigger function processed a request \n"
                 f"Value of CosmosDB Container Prefix: /{PREFIX}")
    
    client = cosmos_client.CosmosClient(
        HOST, {'masterKey': MASTER_KEY}, user_agent="CosmosDBDotnetQuickstart", user_agent_overwrite=True)
    try:
        # setup database
        try:
            db = client.create_database_if_not_exists(id=DATABASE_ID)

        except exceptions.CosmosResourceExistsError:
            pass

        # setup container
        try:
            container = db.create_container(id=CONTAINER_ID, partition_key=PartitionKey(
                path=f'/{PREFIX}'), offer_throughput=400)
            print('Container with id \'{0}\' created'.format(CONTAINER_ID))

        except exceptions.CosmosResourceExistsError:
            container = db.get_container_client(CONTAINER_ID)
            print('Container with id \'{0}\' was found'.format(CONTAINER_ID))

        item_list = list(container.read_all_items(max_item_count=100))
        reduced_list = item_list
        #reduced_list = []
        #for doc in item_list:
        #    reduced_list.append({"id": format(doc.get('id')), "account_number": format(
        #        doc.get(f'{PREFIX}')), "_ts": format(doc.get('_ts'))})

        # send both lists to Logs
        print(json.dumps(item_list, indent=3))
        print(json.dumps(reduced_list, indent=3))
    except exceptions.CosmosHttpResponseError as e:
        print('\nCaught an error. {0}'.format(e.message))

    return json.dumps(reduced_list)
