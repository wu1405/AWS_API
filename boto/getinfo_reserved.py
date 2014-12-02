#!/usr/bin/env python
from boto.ec2.connection import EC2Connection
from boto.ec2 import get_region
import os,sys
import logging
import boto.ec2


def RI(area):
        s3key = os.environ.get('S3KEY')
        s3secret = os.environ.get('S3SECRET')
        myRegion = get_region(area)
        #print "myRegion is %s" % myRegion
        conn = EC2Connection(aws_access_key_id=s3key,aws_secret_access_key=s3secret,region=myRegion)

        result=conn.get_all_reserved_instances()
        f=open('RI_out.log','a')
        for i in result:
                #print i.__dict__
                f.write("\t".join([str(i.instance_type),str(i.instance_count),i.availability_zone,i.start,str(i.duration),i.state])+'\n')
        f.close()



if __name__ == '__main__':
        logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %Y-%m-%d %H:%M:%S',
                filename='debug_ri.log',
                filemode='w')
        try:
                os.remove('RI_out.log')
        except OSError:
                pass
        areas=('ap-southeast-1','us-west-1','sa-east-1','eu-west-1','ap-northeast-1')
        for i in areas:
                RI(i)
