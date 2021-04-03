import logging
import azure.functions as func


def main(myblob: func.InputStream, userJson: func.Out[func.Document]):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")

    json_data = myblob.read()
    logging.info(f"{json_data}")

    try:
        # Store output data using Cosmos DB output binding
        # use the value of the name parameter found in the output binding, in this case userJson
        userJson.set(func.Document.from_json(json_data))
    except Exception as e:
        logging.info(f"Error: {e}")
        print('Error:')
        print(e)    
