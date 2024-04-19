from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from flask import Flask,request,jsonify
from flask_cors import CORS, cross_origin
import requests
app=Flask(__name__)
cors=CORS(app)
app.config['CORS_HEADERS']='Content-Type'
# Connect to your Azure Storage Account
connection_string = "DefaultEndpointsProtocol=https;AccountName=insuranceclaimninja;AccountKey=Fl9dFlXnQBCk1NMlvzy8VWUYh/BRTN59JgyCyuKPQsV9wz/HI9O6JKDcp+zuLHwqx0aWzgDOq8rN+AStpPHliA==;EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Upload data to Blob Storage
def upload_to_blob(data, container_name, blob_name):
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(data)
global count
count=0
# Example route to handle incoming data and upload to Blob Storage
@app.route('/upload', methods=['POST'])
def upload_data():
    print("hi")
    if 'audio' not in request.files:
        return jsonify({'error':'No file part'}),400
    
    file=request.files['audio'] 
    
     # Assuming data is sent in the request body
    #count=count+1
    file_name=file.filename
    upload_to_blob(file, "input", file_name)
    return "Data uploaded successfully"
if __name__=='__main__':
    app.run()