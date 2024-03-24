import uuid
input_string ='siloe-project.com/feed.xml'
# input_string ='podnews.net/rss'
podcast_namespace = uuid.UUID('ead4c236-bf58-58c6-a2c6-a6b28d128cb6')
result = uuid.uuid5(podcast_namespace,input_string)
print(result)

# print(uuid.NAMESPACE_URL)
