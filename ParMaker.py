file = open('0-rezult.txt', 'w')
Target =""
payload='b1n>9o'
with open('target.txt') as f:
        lines = f.readlines()
        i=0
        lineOfParams=Target
        jName=0
        for line in lines:
        	param = line.rstrip('\n')
        	lineOfParams= lineOfParams+"&"+param+"="+payload
        	i=i+1
        	jName= jName+1
        	if(i == 100):
        		customFileName = str(jName)+"-rezult.txt"
        		#tmpFile = open(customFileName, 'w')
        		file.write(lineOfParams+"\n")
        		lineOfParams=Target
        		i=0
        file.write(lineOfParams+"\n")


