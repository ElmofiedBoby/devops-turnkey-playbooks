import sys

idFile = open(sys.argv[1], 'r')
idLines = ""
for i in idFile:
    idLines += i
idFile.close()
# Replace variables in file
with open('ssh-groovy', 'r+') as f:
    content = f.read()
    f.seek(0)
    f.truncate()
    f.write(content.replace('BASEDANDPILLED', idLines))
