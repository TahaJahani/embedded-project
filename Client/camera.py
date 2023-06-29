import requests

CAM_HOST = "http://192.168.1.6:8080/shot.jpg"


def take_image(save_path="image.jpg"):
    response = requests.get(CAM_HOST)
    with open(save_path, "wb") as f:
        f.write(response.content)
