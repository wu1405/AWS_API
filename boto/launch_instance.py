#!/usr/bin/env python
import boto.ec2
import boto.ec2.networkinterface
import os,sys

s3key = os.environ.get('launchKEY')
s3secret = os.environ.get('launchS3SECRET')

conn = boto.ec2.connect_to_region('eu-west-1',aws_access_key_id=s3key,aws_secret_access_key=s3secret)
interface = boto.ec2.networkinterface.NetworkInterfaceSpecification(subnet_id='subnet-xxxxxxxx',
         groups=['sg-xxxxxxxx'],
         associate_public_ip_address=True)
interfaces = boto.ec2.networkinterface.NetworkInterfaceCollection(interface)


launchserver = conn.run_instances('ami-xxxxxxxx',
        key_name='my-key',
        instance_type='t2.small',
        network_interfaces=interfaces
        )
instance=launchserver.instances[0]

tags={'Name':'testserver','PROJECT':'Webapp','SITE':'Asia'}
instance.add_tags(tags)
