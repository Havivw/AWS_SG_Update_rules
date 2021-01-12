import argparse
from requests import get

import boto3

from ipsetter.consts import *



def change_SG_json(name, SG_id, region_name, ip, aws_access_key_id, aws_secret_access_key):
    client = boto3.client('ec2', region_name=region_name, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    client_SG = client.describe_security_groups(GroupIds=[SG_id])
    resource = boto3.resource('ec2', region_name=region_name, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    resource_SG = resource.SecurityGroup(SG_id)
    sg_name = client_SG['SecurityGroups'][0]['GroupName']
    print("INFO - Run Change IP Address on {sg_name} Security Group on AWS.".format(sg_name=sg_name))
    for i in client_SG['SecurityGroups'][0]['IpPermissions'][0]['IpRanges']:
        if name in i['Description']:
            old_rule_copy = i.copy()
            changed_rule = i.copy()
            changed_rule['CidrIp'] = ip
    try:
        _ = resource_SG.authorize_ingress(IpPermissions=[{'IpProtocol': '-1', 'IpRanges': [changed_rule]}])
        _ = resource_SG.revoke_ingress(IpPermissions=[{'IpProtocol': '-1', 'IpRanges': [old_rule_copy]}])
        print("INFO - changed {old_rule_copy} to {changed_rule} Success!.".format(old_rule_copy=old_rule_copy, changed_rule=changed_rule))
    except Exception as error:
        if 'already exists' in str(error):
            print('ERROR - Your IP {ip} is already exists on the Security Group!'.format(ip=ip))
        else:
            print('ERROR failed - {error}'.format(error=error))


def get_current_ip():
    return get('https://checkip.amazonaws.com/').text.replace('\n', '/32')


def parse_argumets():
    parser = argparse.ArgumentParser(description='Amazon Security Group Updater')
    parser.add_argument('--name', '-n', help="The user's name (The description in the security group)", type=str,
                        required=False, default=AWS_USER_IN_DESCRIPTION)
    parser.add_argument('--ip', '-i', help="The specific IP adress to set for your security group. default: current external ip", type=str,
                        required=False, default='')
    return parser.parse_args()


def main():
    args = parse_argumets()
    ip = args.ip if args.ip else get_current_ip()
    if '/' not in ip:
        ip = "{ip}/32".format(ip=ip)
    change_SG_json(name=args.name, SG_id=SG_ID, ip=ip, region_name=REGION_NAME, aws_access_key_id=AWS_ACCESS_KEY_ID,
                   aws_secret_access_key=AWS_SECRET_ACCESS_KEY)


if __name__ == '__main__':
    main()
