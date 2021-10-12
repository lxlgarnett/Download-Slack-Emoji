import json, urllib, zipfile, os

def main():
    # Slack token
    token = input('Please enter your token: ')
    print('Start downloading...')

    emoji_download_url = 'https://slack.com/api/emoji.list?token=%s' % token
    url_response = urllib.urlopen(emoji_download_url)
    data = json.loads(url_response.read())
    if data['ok']:
        emojis = data['emoji']
        emoji_zip_file = zipfile.ZipFile("emojis.zip", "w")
        for index in emojis:
            # Ignores alias
            if "alias" not in emojis[index]:
                extension = "." + emojis[index].split('.')[-1]
                file_name = index + extension
                try:
                    # Downloads emoji image from url.
                    urllib.urlretrieve(emojis[index], file_name)
                    # Writes image file to a zip file.
                    emoji_zip_file.write(file_name)
                    # Deletes image file after write into zip file.
                    if os.path.exists(file_name):
                        os.remove(file_name)
                except:
                    print('Some exception happened while downloading emoji: %s' % file_name)
        emoji_zip_file.close()
        print('Emojis have been downloaded to %s' % os.path.dirname(os.path.abspath(__file__)))
    else: 
        print(data['error'])

if __name__ == '__main__':
    main()