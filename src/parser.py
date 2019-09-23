import csv
import json as json

#  Edit File path and year of the file accoding to the needs.
# Creates `YEAR`-cvehash.csv file in the current file path unless 
#  Specified.

# Source File. 
file  = '../data/nvd/nvdcve-1.1-2015.json'
year = 2015
# Destination path Type String only
path = ''



with open(file, encoding='utf-8') as f :
    data = json.load(f)
data = data['CVE_Items']
# Desitination file creation.
f = open(path+str(year)+'-cvehash.csv','w')

# coloums of the newly created cvehash file.
head = ['cveid','year','hash','desc','link','publishedDate']

with f :
    writer = csv.writer(f)
    l = [head]
    writer.writerow(head)
    for n in range(0,len(data)):
        url = []
        date = data[n]['publishedDate']
        describtion =  data[n]['cve']['description']['description_data'][0]['value']
        for ref in data[n]['cve']['references']['reference_data']:
            url = ref['url']
            t = url
            url = url.strip().split('://')
            if(url[1].split('/')[0] == 'github.com') and (url[1].split('/')[-2] == "commit"):
                link = ''.join([x for x in url[1]])
                link = "http://"+link
                url = url[1].split('/')
                if len(url[-1])>40:
                    hashid = (url[-1][:40])
                else:
                    hashid = (url[-1])
                s =[str(n),str(year),hashid,describtion,link,date]
                writer.writerow(s) 