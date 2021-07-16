#Concatenate the ssh keys to the authorized_keys file
#Given a list of textfiles containing strings (SSH keys), add it into the authorized_keys file

import sys
import logging
import boto3
from botocore.exceptions import ClientError

#sys.argv[0] == bucket.py
#sys.argv[1] == bucket name
#sys.argv[2] == Boolean value to determine if key is written to AuthKeys. or uploaded to bucket (True = written to file, False = uploaded to bucket)
#sys.argv[3] == Name of file to upload (Only if uploading to bucket)
#Command line call: python3 buckets.py argv[1] argv[2] (argv[3])
keyList = []

#register s3 with boto, then store all buckets in the response variable
s3 = boto3.client('s3')
response = s3.list_buckets()

#method that looks up the team's bucket name, sifts through their s3 files, and finds their public keys
def lookUp(NameOfBucket):
    
    #loop through all s3 buckets
    for bucket in response['Buckets']:
       
        #get the bucket name and store it in a variable to use for the 'list_objects' method
        bucketName = bucket["Name"]
         
        #if the current bucketname is equal to the user's team bucket name
        if bucketName == NameOfBucket:
            
            #use boto3 resource to smoothly iterate over objects
            s3 = boto3.resource('s3')
            
            #store the bucket
            bucket = s3.Bucket(bucketName)
            
            #loop through all the objects in the team's bucket
            for obj in bucket.objects.all():
                key = obj.key
                
                #if the object is a public key, append the contents to keyList
                if '.pub' in key:
                    body = obj.get()['Body'].read()
                    
                    #make body into a string rather than an object
                    strBody = str(body)
                    
                    #strip the leading b, in addition to the new line
                    strBody = strBody.strip()
                    strBody = strBody.lstrip("b'")
                    strBody = strBody.rstrip("'")
                    strBody = strBody.rstrip("n")
                    strBody = strBody.rstrip("\\")
                    
                    keyList.append(strBody)
            
            #since we don't care about the other buckets after we find the team's, break the loop    
            break                 



#writes the public keys to the authorized keys file
def writeToFile():
    try:
        authorizedFile = open("/var/lib/docker/volumes/captain--githome/_data/.ssh/authorized_keys", "w")
        
        authorizedFile.write('\n')
        for key in keyList:
            authorizedFile.write(key + '\n')
    
    except FileNotFoundError:
        print("Wrong file or file path")
        
    authorizedFile.close()
    
def main():

    #get bucketname from user
    bucketName = sys.argv[1]
    if sys.argv[2] == "True":
        isGet = True
    else:
        isGet = False
    
    #get the keys and store key contents in keyList   
    if isGet:
        lookUp(bucketName)
        #print(keyList)
        
        #append keys to end of authorized keys file
        writeToFile()
    else:
        s3.upload_file(sys.argv[3], sys.argv[1], sys.argv[3][18:len(sys.argv[3])])

main()
