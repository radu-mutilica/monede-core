import re




def sanitize(id):
    id = id.replace('-', ' ')
    return re.sub('[^A-Za-z0\\s]+', '', id)
