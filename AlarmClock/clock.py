#alarm clock

import time
import datetime
import pygame


def countdown(alarmtime):
    print("ALARM HAS BEEN SET! \n STARTING COUNTDOWN :")
    while True:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        if(alarmtime==current_time):
            sound_path="alarm.wav"
            print("WAKE UP😊😊")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
            break
        else:
            time.sleep(1)
            print(current_time)



if __name__=="__main__":
    alarmtime=input("Enter the time to set an alarm for (HH:MM:SS) : ")
    countdown(alarmtime)