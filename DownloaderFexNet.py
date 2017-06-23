''' 
Uploading a photo from fex.net
'''

import urllib.request
import progressbar
links = []
try:
    source = open(input('Enter name file (without .urls): ')+'.urls', 'r')
    for line in source.readlines():
        links.append(line.strip())
except:
    print('Reading is not completed. ERROR 1')
else:
    print('Reading is completed')
    source.close()
    try:
        numb = 0
        bar = progressbar.ProgressBar()
        folder = input('Enter name folder: ')
        extension = input('File extensions (without .): ')
        print('Downloading...')
        for link in bar(links):
            resource = urllib.request.urlopen(link)
            out = open(folder+'/'+str(numb)+'.'+extension, 'wb')
            out.write(resource.read())
            out.close()
            numb += 1
    except:
        print('Writing is not completed. ERROR 2')
    else:
        print('Done!')
