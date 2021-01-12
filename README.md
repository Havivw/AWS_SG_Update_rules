# IPSetter
​
IPSetter is a simple tool that allow you to change a specific rule in Security Group on AWS via description.

## Prerequisites

Create Api key on AWS with atleast that policy.
```shell script
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "ec2:RevokeSecurityGroupIngress",
                "ec2:AuthorizeSecurityGroupEgress",
                "ec2:AuthorizeSecurityGroupIngress",
                "ec2:UpdateSecurityGroupRuleDescriptionsEgress",
                "ec2:RevokeSecurityGroupEgress",
                "ec2:UpdateSecurityGroupRuleDescriptionsIngress",
                "ec2:DescribeSecurityGroup"
            ],
            "Resource": "arn:aws:ec2:eu-central-1:xxxxxx"
        }
    ]
```
​
## IPSetter Installation
Download the IPSetter folder and install with pip.
​
```shell
$ sudo pip3 install .
```

## Supported ​
 * Windows
 * Linux
## config file
 change ipsetter/consts.py
 
    ```
    SG_ID = 'sg-xxx'
    AWS_ACCESS_KEY_ID = 'xxx'
    AWS_SECRET_ACCESS_KEY = 'xxxxx'
    AWS_USER_IN_DESCRIPTION = 'description'
    REGION_NAME = 'eu-central-1'

    ```
## Run
With default value
 
  Linux
   ```shell script
    $ ipsetter
    INFO - Run Change IP Address on PT-GroupPolicy (Default) Security Group on AWS.
    INFO - changed {'CidrIp': 'x.x.x.x/32', 'Description': 'Haviv'} to {'CidrIp': 'y.y.y.y/32', 'Description': 'Haviv'} Success!.
```
 
  Windows
   ```shell script
    c:\> ipsetter
    INFO - Run Change IP Address on PT-GroupPolicy (Default) Security Group on AWS.
    ERROR - Your IP x.x.x.x/32 is already exists on the Security Group!
```

## Contributions..
​
..are always welcome.
