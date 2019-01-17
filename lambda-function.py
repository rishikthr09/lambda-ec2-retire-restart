import json
import boto3

region="ap-northeast-1"
roles_to_restart=['kubernetes']

def lambda_handler(event, context):

    to_restart = []

    ec2 = boto3.client('ec2', region_name=region)

    for r in ec2.describe_instances(InstanceIds=event["resources"], Filters=[{'Name':'tag:roles', 'Values':roles_to_restart}])["Reservations"]:
        for instance in r["Instances"]:
            to_restart.append(instance["InstanceId"])

    print "Rebooting instances: %s" %(str(to_restart))
    ec2.reboot_instances(InstanceIds=to_restart)

    return {
        'statusCode': 200,
        'body': event
    }

