import requests

from bcolors import bcolors

server_url = "http://192.168.1.122:8000"


def upload_image(image_path):
    with open(image_path, 'rb') as f:
        r = requests.post(server_url, files={'image': f})
        if r.status_code == 201:
            print(bcolors.OKGREEN + "Upload success" + bcolors.ENDC)
        else:
            print(bcolors.FAIL + "Upload failed" + bcolors.ENDC)
        f.close()
