import sys

# Replace variables in file
with open('template69.xml', 'r+') as f:
    content = f.read()
    f.seek(0)
    f.truncate()
    f.write(content.replace('BASED', sys.argv[1]))

with open('template69.xml', 'r+') as w:
    contentw = w.read()
    w.seek(0)
    w.truncate()
    w.write(contentw.replace('DABABY', sys.argv[2]))
