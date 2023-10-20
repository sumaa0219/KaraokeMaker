from gpiozero import Button
import pygame
import serial
import makeJson
import json

mkJson = makeJson.makejson()

# ボタンのピン番号
play_button_pin = 17
stop_button_pin = 18
pause_button_pin = 27

# GPIOピンの設定
play_button = Button(play_button_pin)
stop_button = Button(stop_button_pin)
pause_button = Button(pause_button_pin)

last_serial_data = None
playList = mkJson.getFileList()

# pygameの初期化
pygame.init()

# シリアル通信の初期化
ser = serial.Serial('/dev/ttyUSB0', 9600)  # ポートとボーレートを適切な値に変更

# pygame.mixerの初期化
pygame.mixer.init()


while True:
    
    # シリアル通信からデータを受信
    data = ser.readline().decode().strip()

    if data != last_serial_data:
        playList = mkJson.getFileList()
        pygame.mixer.music.load(playList[str(data)]["musicName"] + ".mp3")
        pygame.mixer.music.play()
        last_serial_data = data

    # 再生ボタンが押されたら
    if play_button.is_pressed:
        pygame.mixer.music.load(playList[str(data)]["musicName"] + ".mp3")
        pygame.mixer.music.play()

    # 停止ボタンが押されたら
    elif stop_button.is_pressed:
        pygame.mixer.music.stop()

    # 一時停止ボタンが押されたら
    elif pause_button.is_pressed:
        pygame.mixer.music.pause()

    # 一時停止解除ボタンが押されたら
    elif not pause_button.is_pressed and pygame.mixer.music.get_busy():
        pygame.mixer.music.unpause()
