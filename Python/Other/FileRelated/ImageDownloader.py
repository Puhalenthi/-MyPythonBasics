import requests

urls = []

done = False
while done == False:
    url = input('Please enter an image url to download:     ')
    urls.append(url)
    useryesorno = input('Would you like to enter another image? Type Y or y for yes and N or n for no:      ')
    if useryesorno == 'y' or useryesorno == 'Y':
        done = False
    elif useryesorno == 'n' or useryesorno == 'N':
        done = True
    else:
        try:
            raise BaseException()
        except BaseException as e:
            print('Invalid Item Entered. Error:        {}'.format(e))


def downloader():
    try:
        for i in urls:
            imagebytes = requests.get(i).content
            downloadname = i.split('/')[3]
            downloadname += '.jpg'
            with open(downloadname, 'wb') as f:
                f.write(imagebytes)
                print('{} was just downloaded a few moments ago...'.format(downloadname))
    except BaseException as e:
        return 'Invalid Link Entered. Error:        {}'.format(e)
    return 'Finished downloaded all pictures'


print(downloader())