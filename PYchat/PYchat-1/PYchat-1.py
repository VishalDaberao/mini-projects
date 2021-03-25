from tkinter import *
from tkinter import ttk
from multiprocessing.dummy import Pool
import time
import requests
import sys
import paho.mqtt.client as mqtt #import the client1


root = Tk()
root.configure(background="#f2f2f2")
root.title("PYchat by VishalKD")
root.geometry('602x539')
root.resizable(False,False)
#sub_topic = "/topic/for/subscribing/msg/by/vishalKD"
pub_topic = "/topic/for/subscribing/msg/by/vishalKD"
sub_topic = "/topic/for/publishing/msg/by/vishalKD"
broker_url = "broker.mqttdashboard.com"
broker_port = 1883

def mqtt_publish(arg_broker_url, arg_broker_port, arg_mqtt_topic, arg_mqtt_message, arg_mqtt_qos):
    try:        
        mqtt_client = mqtt.Client("mqtt_pub")
        mqtt_client.connect(arg_broker_url, arg_broker_port)
        mqtt_client.loop_start()

        print("Publishing message to topic", arg_mqtt_topic)
        mqtt_client.publish(arg_mqtt_topic, arg_mqtt_message, arg_mqtt_qos)
        time.sleep(0.1) # wait

        mqtt_client.loop_stop() #stop the loop
        return 0
    except:
        return -1



def mqtt_subscribe_thread_start(arg_callback_func, arg_broker_url, arg_broker_port, arg_mqtt_topic, arg_mqtt_qos):
    try:
        mqtt_client = mqtt.Client()
        mqtt_client.on_message = arg_callback_func
        mqtt_client.connect(arg_broker_url, arg_broker_port)
        mqtt_client.subscribe(arg_mqtt_topic, arg_mqtt_qos)
        time.sleep(1) # wait
        # mqtt_client.loop_forever() # starts a blocking infinite loop
        mqtt_client.loop_start()    # starts a new thread
        return 0
    except:
        return -1




def iot_func_callback_sub(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)



def send_message():
	try:
		mqtt_publish(broker_url, broker_port, pub_topic, msg_send.get(), 0)
		s_msg = "YOU : "+msg_send.get()
		cht.config(state='normal')
		cht.insert(END, s_msg+'\n')
		msg_send.delete(0, 'end')
		cht.config(state='disabled')
	except:
		pass

def mqtt_sub_cb(client, userdata, message):
	payload = str(message.payload.decode("utf-8"))
	msg = "SOMEONE : "+payload
	cht.config(state='normal')
	cht.insert(END, msg+'\n')
	cht.config(state='disabled')


iot_to_ros=mqtt_subscribe_thread_start(mqtt_sub_cb,broker_url,broker_port,sub_topic,0)   


#text input field
clabel = Label(root, text="CHAT", font=("Verdana",12))
clabel.pack(pady=10)
cht = Text(root, width=70, height=20)
cht.pack()
cht.config(state='disable')
send = Button(root, text="SEND", command=send_message)
send.place(x=250, y=450)
msg_send = Entry(root, width=30, font=("Verdana",12))
msg_send.place(x=130, y=410) 



root.mainloop()
