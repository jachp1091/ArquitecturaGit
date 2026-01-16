import json
import boto3

# Conexión con los servicios de AWS
textract = boto3.client('textract')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    # Seleccionamos la tabla que definiste en el template.yaml
    table = dynamodb.Table('TablaResultados')

    # Procesamos cada mensaje que llega de la cola SQS
    for record in event['Records']:
        print("Procesando nueva factura desde SQS...")
        
        # Aquí la Lambda extraería el texto con Textract
        # Por ahora, guardamos un resultado de éxito en DynamoDB
        table.put_item(
           Item={
                'id': record['messageId'],
                'estado': 'Factura Procesada',
                'detalle': 'Texto extraído correctamente'
            }
        )
        print(f"ID {record['messageId']} guardado en DynamoDB.")
        
    return {
        'statusCode': 200,
        'body': json.dumps('Proceso completado')
    }