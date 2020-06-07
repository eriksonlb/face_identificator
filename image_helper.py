import requests

def get_image_from_url(url):
    resp = requests.get(url)
    imgbytes = resp.content
    return imgbytes

def get_image_from_file(filename):
    with open(filename, 'rb') as imgfile:
        return imgfile.read()