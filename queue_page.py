
from imports import *
import flet as ft
from db_retrieve import *
from order_confirmed_page import *

# def redis_connection9(ips):
# 	try:
# 		global r
# 		r = redis.Redis()
# 		r = redis.Redis(host=ips,port=6380)
# 	except Exception as e :
# 		print(f"The error is {e}")
# 		redis_connection9("100.96.37.82")
# 		# pass

# def mqtt_connection9(ips):
# 	try:
# 		global client
# 		mqttBroker = ips
# 		# mqttBroker = "mosquittorcx"
# 		client = mqtt.Client("rc")
# 		client.loop_start()
# 		client.connect(mqttBroker,1883)
# 	except Exception as e :
# 		print(f"The error is {e}")
# 		pass

# def connection9(ips):
# 	try:
# 		global con
# 		con = pg8000.native.Connection(host = ips, user="postgres", password="mysecretpassword",port="5433", database="test_recipe")
# 	except Exception as e :
# 		print(f"The error is {e}")
# 		connection9("100.96.37.82")
		# pass
	

def order_queue(page:ft.Page,recipe_id,sugar,ice):
	print("order queue page")
	page.client_storage.set("end","1")
	page.client_storage.set("current","queue")
	# recipe_id = recipe_id

	# page.appbar.disabled = True

	def add(rec_id, sugar, ice):
		s = 0
		id = get_laststep()
		order_id = int(id) + 1
		add_order(order_id,rec_id,sugar,ice)
		
		if page.client_storage.get("order_id_1") == None :
			page.client_storage.set("order_id_1",f"{order_id}")
			s = 1
		
		if page.client_storage.get("order_id_2") == None and s == 0:
			page.client_storage.set("order_id_2",f"{order_id}")

	cur = page.client_storage.get("order_id_1")
	cur1 = page.client_storage.get("order_id_2")
	print(f"the cur and cur 1 is {cur}, {cur1}")
	sleep(0.1)

	# if cur == None or cur1 == None: 
	add(recipe_id,sugar,ice)

## No of orders - status created
# 	orders = list_orders()

# ## First order id - status created
# 	first_order_id = get_first_orderid()

# ## Get order id if already cooking going on
# 	in_progress_1 = progress_orderid(1)
# 	in_progress_2 = progress_orderid(2)

# ## Get order id if already cooking going on
# 	tot_time = int(orders_time())/60

# 	my_order_id_1 = int(page.client_storage.get("order_id_1"))
# 	my_order_id_2 = int(page.client_storage.get("order_id_2"))


# 	if in_progress_1 != my_order_id_1 or in_progress_2 != my_order_id_2:

# 		page.clean()

# 		image_progress = ft.Image(src="https://i.pinimg.com/originals/3d/6a/a9/3d6aa9082f3c9e285df9970dc7b762ac.gif",
# 								width=400,
# 								height=400,
# 								fit=ft.ImageFit.CONTAIN
# 								)
# 		order_text = ft.Text(
# 								value=f"Your Order Id : {my_order_id_1}",
# 								size=35,
# 								color=ft.colors.BLACK,
# 								font_family="RobotoSlab",
# 								weight=ft.FontWeight.W_700,
# 							)
# 		text = ft.Text(
# 								value=f"Pls wait Your Order in Queue, Will be completed in {int(tot_time)} mins",
# 								size=35,
# 								color=ft.colors.BLUE,
# 								font_family="RobotoSlab",
# 								weight=ft.FontWeight.W_700,
# 							)
# 		completed = ft.Column(
# 				spacing=10,
# 				scroll=ft.ScrollMode.ALWAYS,
# 				controls=[
# 					image_progress,
# 					order_text,
# 					text,
# 					ft.ResponsiveRow(
# 						[

# 						],
# 					),
# 				],
# 				horizontal_alignment=ft.CrossAxisAlignment.CENTER,
# 					)
		
		
# 		page.add(
# 			ft.ResponsiveRow(
# 			[
# 				ft.Column(
				
# 				[
# 					completed,
# 				],
# 			alignment= ft.MainAxisAlignment.CENTER,
# 			spacing = 10,
# 			scroll=ft.ScrollMode.ALWAYS,
# 			on_scroll_interval=0,
# 				),
# 			],
# 			alignment= ft.MainAxisAlignment.CENTER,
# 			spacing = "spaceBetween"
# 			),
# 				)
	
# 		page.update()

# 		while (in_progress != my_order_id_1):
			
# 			tot_time = int(orders_time())/60
# 			text.value = f"Pls wait Your Order in Queue, Will be completed in {int(tot_time)} mins",
# 			text.update()
# 			sleep(5)
# 			in_progress = int(progress_orderid())
# 			print(f"my id = {my_order_id_1}")
		

# 	if in_progress != 0 and in_progress == my_order_id_1 :
# 		page.clean()
# 		order_confirmed(page, recipe_id)
