import json, urllib, zipfile, os

# Slack token
token = raw_input("Please enter your token: ")

print "Start downloading..."

# Slack get emoji list's api: token is required
url = "https://slack.com/api/emoji.list?token=" + token

urlResponse = urllib.urlopen(url)
data = json.loads(urlResponse.read())
if data['ok']:
    emojis = data['emoji']
    emojiZipFile = zipfile.ZipFile("emojis.zip", "w")
    for index in emojis:
        # Ignores alias
        if "alias" not in emojis[index]:
            extension = "." + emojis[index].split('.')[-1]
            fileName = index + extension
            try:
                # Downloads emoji image from url.
                urllib.urlretrieve(emojis[index], fileName)
                # Writes image file to a zip file.
                emojiZipFile.write(fileName)
                # Deletes image file after write into zip file.
                if os.path.exists(fileName):
                    os.remove(fileName)
            except:
                print "Some exception happened while downloading emoji: %s" % fileName 
    emojiZipFile.close()
    print "Emojis have been downloaded to %s" % os.path.dirname(os.path.abspath(__file__))
else: 
    print data['error']
