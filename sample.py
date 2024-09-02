import json

def lambda_handler(event, context):
    orderId = json.loads(event["body"])["message"]["orderId"]
    clientName = json.loads(event["body"])["message"]["clientName"]
    orderDate = json.loads(event["body"])["message"]["orderDate"]
    companyName = json.loads(event["body"])["message"]["companyName"]
    shares = json.loads(event["body"])["message"]["shares"]
    message="Details of client: \n  Order Id = {orderId},\n  Client Name = {clientName},\n  Order Date = {orderDate},\n  Company Name = {companyName}, \n  Shares = {shares}".format(orderId=orderId, clientName=clientName, orderDate=orderDate, companyName=companyName, shares=shares)
    return message
