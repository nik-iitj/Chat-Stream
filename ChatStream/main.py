from cProfile import label
from matplotlib.pyplot import text
import requests
from vidstream import *
import tkinter as tk
import socket
import threading


local_ip_address = socket.gethostbyname("localhost")

server = StreamingServer(local_ip_address,9999)
reciever = StreamingServer(local_ip_address,8888)



def start_listening():
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=reciever.start_server)

    t1.start()
    t2.start()
    


def start_camera_stream():
    camera_client = CameraClient(text_target_ip.get(1.0,'end-1c'),7777)
    t3 = threading.Thread(target=camera_client.start_stream)
    t3.start()
    

def start_screen_sharing():
    screen_client = ScreenShareClient(text_target_ip.get(1.0,'end-1c'),7777)
    t4 = threading.Thread(target=screen_client.start_stream)
    t4.start()

def start_audio_stream():
    audio_sender = AudioSender(text_target_ip.get(1.0,'end-1c'),6666)
    t5 = threading.Thread(target=audio_sender.start_stream)
    t5.start()




window = tk.Tk()
window.title("Chat Stream")
window.geometry('400x300')

label_target_ip = tk.Label(window,text="Target IP:")
label_target_ip.pack()

text_target_ip = tk.Text(window,height=2)
text_target_ip.pack()

btn_listen = tk.Button(window,text="Start Listening", width=50, command=start_listening)
btn_listen.pack(anchor=tk.CENTER,expand=True)

btn_cam = tk.Button(window,text="Start Webcam", width=50, command=start_camera_stream)
btn_cam.pack(anchor=tk.CENTER,expand=True)

btn_screen = tk.Button(window,text="Start Screenshare", width=50, command=start_screen_sharing)
btn_screen.pack(anchor=tk.CENTER,expand=True)

btn_audio = tk.Button(window,text="Start Audio", width=50, command=start_audio_stream)
btn_audio.pack(anchor=tk.CENTER,expand=True)

window.mainloop()


