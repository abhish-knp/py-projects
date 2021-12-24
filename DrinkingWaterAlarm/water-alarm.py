from pygame import mixer
from datetime import datetime
from time import time


def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
    
    

def log_now(msg):
    with open("MyLogss.txt", "a") as f:
        f.write(f"{msg} {datetime.now()} \n ")
    
    
if __name__ == '__main__':
    
#     musiconloop("water.mp3","stop")
    init_water = time()
    init_eyes = time()
    init_excercise = time()
    watertimer = 5
    extimer = 10
    eyetime = 15
    
    while True:
        if time() - init_water > watertimer:
            print("Water Drinking time. Enter drank to stop alarm")
            musiconloop('water.mp3','drank')
            init_water = time()
            log_now("Drank Water at: ")
                
        if time() - init_excercise > extimer:
            print("Physical Workout time. Enter done to stop alarm")
            musiconloop('pyhsical.mp3','done')
            init_excercise = time()
            log_now("Workout Done at: ")
            
        if time() - init_eyes > eyetime:
            print("Eye Workout time. Enter done to stop alarm")
            musiconloop('eyes.mp3','done')
            init_eyes = time()
            log_now("Eye Workout Done at: ")