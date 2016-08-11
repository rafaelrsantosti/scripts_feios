import boto3

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_REGION_NAME = ''

# Lista os perfis que deseja utilizar
# http://boto3.readthedocs.io/en/latest/guide/configuration.html


# Busca todas as instancias e mostra o id, o nome e o IP publico
ec2 = boto3.resource('ec2', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
instancias = ec2.instances.all()

for instancia in instancias:
    if instancia.tags is None:
        continue
    for tags in instancia.tags:
        if tags['Key'] == 'Name':
            print "{0} - {1} ({2}) - [{3}] - <{4}>".format(instancia.id, tags['Value'], instancia.instance_type, instancia.public_ip_address, instancia.state['Name'])
