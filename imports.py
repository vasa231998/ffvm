import flet as ft      ## version 0.23.2
import paho.mqtt.client as mqtt # ver 1.6.1
from time import time
from time import sleep
import sys, os
import time
import redis ## ver 4.3.3
import pg8000.native ## ver 1.30.4
import asyncio
from io import BytesIO
import io
import base64
import segno
from client import *

# def redis_connection6(ips):
# 	try:
# 		global r
# 		r = redis.Redis()
# 		r = redis.Redis(host=ips,port=6380)
# 	except Exception as e :
# 		print(f"The error is redis error {e}")
# 		redis_connection6("100.96.37.82")
		
# redis_connection6("100.96.37.82")