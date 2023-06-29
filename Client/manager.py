import buzzer
import bluetooth
import camera
import wifi
import fan

THRESHOLD_1 = 1
THRESHOLD_2 = 2


class Manager:
    @staticmethod
    def distance_updated(distance):
        if distance < THRESHOLD_1:
            return
        elif distance < THRESHOLD_2:
            buzzer.play_song()
            bluetooth.send_message("Danger Mode Activated!")
        else:
            camera.take_image("image.jpg")
            wifi.upload_image("image.jpg")
            fan.turn_off_fan()
