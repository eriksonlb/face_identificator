import boto3
from pprint import pprint
from image_helper import get_image_from_file, get_image_from_url

def compare_faces(image_source):
    client = boto3.client('rekognition')
    
    response=client.search_faces_by_image(Image={'S3Object':{'Bucket':"bucketmarcaponto",'Name':image_source}}, MaxFaces=3)                                
    for faceMatch in response['FaceMatches']:
        similarity = faceMatch['Similarity']
        print(f'Matches with {round(similarity, 2)}% confidence')

url_img_src = 'images/eu.jpg'
url_img_target = 'images/role1.jpeg'

img_src = get_image_from_file(url_img_src)
img_target = get_image_from_file(url_img_target)

compare_faces(img_src)
