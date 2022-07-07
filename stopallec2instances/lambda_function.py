import boto3


ec2 = boto3.resource('ec2', region_name="ap-northeast-1")


def lambda_handler(event, context):
    filters = [{'Name': 'tag:Type', 'Values': ['Temp']}]
    for i in ec2.instances.filter(Filters=filters):
        if i.state["Name"] == "running":
            i.stop()


if __name__ == '__main__':
    lambda_handler(None, None)
