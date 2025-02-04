import flet as ft
from flet import *
from imports import *
from db_retrieve import *
from products1 import *
from customise_page import *
from payment_page import *
from order_confirmed_page import *
from queue_page import *
from completed_page import *

def redis_connection6(ips):
	try:
		global r
		r = redis.Redis()
		r = redis.Redis(host=ips,port=6380)
	except Exception as e :
		print(f"The error is redis error {e}")
		redis_connection6("100.96.37.82")


def main(page:Page):
	page.client_storage.remove("order_id_1")
	geter = 0
	# showStatusMsg("At Main")


	def dlg_close(e):
		page.close(dlg_modal)
		page.update()
	
	def dlg_open(e):
		page.open(dlg_modal)
		page.update()

	dlg_modal = ft.AlertDialog(
		modal=True,
		title=ft.Text(""),
		content=ft.Text(""),
		actions=[
			ft.ProgressRing(),
		],
		actions_alignment=ft.MainAxisAlignment.CENTER,
	)
	page.add(dlg_modal)
	dlg_open(1)

	page.client_storage.set("end","1")

	page.theme = ft.Theme(
		color_scheme_seed=ft.colors.ORANGE,
	)
	page.update()
	value = "100.106.178.97"


	def on_submit(e):
		i = text_val.value
		page.client_storage.set("ip",f"{i}")
		
	text_val = ft.TextField(disabled=False,width= 150, label = "Enter ID")
	submit_button =   ft.ElevatedButton(
						"SUBMIT",
						icon="NOT_STARTED",
						disabled=False,
						icon_color="green400",
						on_click = lambda e:on_submit(1),
						col={"sm": 10, "md": 4, "xl": 2}
						)
	if value == None:
		page.add(
			text_val,
			submit_button,
		) 
		page.update()
	# page.theme = ft.Theme(
	#     color_scheme_seed=ft.colors.YELLOW,
	# )
	if value != None:
		# ips = page.client_storage.get("ip")
		ips = "100.106.178.97"

		print(f"ips value is {ips}")
		connection(ips)
		redis_connection6(ips)
		redis_connection7("100.106.178.97")


		def home_clicked(e):
			dlg_open(1)
			sleep(0.5)
			dlg_close(1)
			page.clean()
			Recipes(page)
		
		def clicked_back(e):
			dlg_open(1)
			sleep(0.5)
			dlg_close(1)
			
			print("clicked_back")
			cp = page.client_storage.get("current")


			if cp == "customise":
				page.clean()
				Recipes(page)

			if cp == "payment":
				page.clean()
				Recipes(page)
			
			if cp == "final":
				page.clean()
				Recipes(page)

		page.appbar = ft.AppBar(
			leading=ft.FilledTonalButton(
					text = ft.Text("BACK"),
					icon=ft.icons.ARROW_BACK,
					icon_color="blue400",
					# icon_size=50,
					tooltip="Back",
					on_click= clicked_back,
				),
		title=ft.Text(
			"FFVM", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK87
		),
		bgcolor=ft.colors.ORANGE_100,
		center_title=True,
		actions=[
			ft.Image(src = "https://drive.google.com/file/d/1BOs5AdaKncweym2AqXh-W5kkCfP36WJP/view?usp=sharing"),
			ft.IconButton(
					icon=ft.icons.HOME_ROUNDED,
					icon_color="blue",
					icon_size=40,
					tooltip="Goto Home",
					on_click=home_clicked,
				),
		],
		color=ft.colors.WHITE,
		)

		order_in_progress = progress_orderid(1)
		if order_in_progress == 0:
			prog = " - "
		if order_in_progress != 0:
			prog = order_in_progress
		
		order_in_progress = progress_orderid(2)
		if order_in_progress == 0:
			prog2 = " - "
		if order_in_progress != 0:
			prog2 = order_in_progress

		order_completed = last_completed_orderid()
		if order_completed == 0:
			comp = " - "
		if order_completed != 0:
			comp = order_completed

		orders_queue = get_created_orders()
		if orders_queue  == 0:
			que = " - "
		if orders_queue  != 0:
			que = orders_queue 

		order_completed_container = ft.Row(
					[
						ft.Container(
							margin=5,
							padding=5,
							theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.ORANGE_100)),
							width=200,
							bgcolor=ft.colors.GREEN_200,
							border_radius=10,
							ink=True,
							border=ft.border.all(2, ft.colors.ORANGE_100),
							content = ft.ResponsiveRow(
								[
								ft.Text(f"Completed",size=15, weight=ft.FontWeight.W_700),
								ft.Text(f"Order ID : {comp}",size=25, weight=ft.FontWeight.W_700,text_align =TextAlign.CENTER),
								],
							),
						),
					],
			)
		
		order_preparing_container_1 = ft.Row(
					[
						ft.Container(
							margin=5,
							padding=5,
							theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.ORANGE_100)),
							width=200,
							bgcolor=ft.colors.YELLOW_100,
							border_radius=10,
							ink=True,
							border=ft.border.all(2, ft.colors.ORANGE_100),
							content = ft.ResponsiveRow(
								[
								ft.Text(f"V1 Preparing",size=15, weight=ft.FontWeight.W_700),
								ft.Text(f"Order ID : {prog}",size=25, weight=ft.FontWeight.W_700,text_align =TextAlign.CENTER),
								],
							),
						),
					],
			)
		
		order_preparing_container_2 = ft.Row(
					[
						ft.Container(
							margin=5,
							padding=5,
							theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.ORANGE_100)),
							width=200,
							bgcolor=ft.colors.YELLOW_100,
							border_radius=10,
							ink=True,
							border=ft.border.all(2, ft.colors.ORANGE_100),
							content = ft.ResponsiveRow(
								[
								ft.Text(f"V2 Preparing",size=15, weight=ft.FontWeight.W_700),
								ft.Text(f"Order ID : {prog2}",size=25, weight=ft.FontWeight.W_700,text_align =TextAlign.CENTER),
								],
							),
						),
					],
			)
		
		order_queue_container = ft.Row(
					[
						ft.Container(
							margin=5,
							padding=5,
							alignment=ft.alignment.center,
							theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.ORANGE_100)),
							width=200,
							bgcolor=ft.colors.ORANGE_200,
							border_radius=10,
							ink=True,
							# expand = True,
							border=ft.border.all(2, ft.colors.ORANGE_100),
							content = ft.ResponsiveRow(
								[
								ft.Text(f"In Queue -Order IDs:",size=15, weight=ft.FontWeight.W_700),
								ft.Text(f"{que}",size=20, weight=ft.FontWeight.W_700,text_align =TextAlign.CENTER),
								],
							),
						),
					],
			)


		order_status = ft.ResponsiveRow(
					[
					ft.Container(
				content=ft.Row(
					[
				order_completed_container,
				order_preparing_container_1,
				order_preparing_container_2,
				order_queue_container,
					],
					alignment="spaceBetween",
				)
			),
					],
			)

		page.bottom_appbar = ft.BottomAppBar(
		bgcolor=ft.colors.DEEP_ORANGE_100,

		shape=ft.NotchShape.CIRCULAR,
		content=ft.ResponsiveRow(
			controls=[
				order_status,
				]
		),
		height= 150,
	)
		id = page.client_storage.get("order_id")

		if id == None:
			dlg_close(1)
			Recipes(page)

		if id != None:
			cur = check_while_entry(int(id))
			
			if cur != "completed":
				rec_id = getrecipeidfromqueue(id)
				sugar = "Normal"
				ice = "Normal"
				order_queue(page,rec_id,sugar,ice)

			if cur == "completed":
				page.client_storage.remove("order_id")
				dlg_close(1)
				Recipes(page)
				
	def handle_close(e):
		page.close(dlg_completed)


	dlg_completed = ft.AlertDialog(
		modal=True,
		title=ft.Text("Order Completed"),
		content=ft.Text(""),
		actions=[
			# ft.TextButton("Yes", on_click=handle_close),
			ft.TextButton("OK", on_click=handle_close),
		],
		actions_alignment=ft.MainAxisAlignment.END
	)

	def orders_check():
		global geter
		geter = 1
		current = page.client_storage.get("current")
		page.bottom_appbar.content.controls.clear()
		oiid = page.client_storage.get("order_id")

		if current == "final" and oiid == None:
			print("Now Going to Recipes Page")
			sleep(5)
			page.clean()
			page.update()
			Recipes(page)
		
		if current == "error" and oiid == None:
			sleep(5)
			page.clean()
			page.update()
			Recipes(page)
		
		if current == "queue":
			sleep(0.5)
			page.clean()
			page.update()
			Recipes(page)

		if current == "completed_page":
			print("Now Going to Recipes Page")
			sleep(5)
			page.clean()
			page.update()
			Recipes(page)

		if r.get("vessel1_comp").decode("utf-8") == "yes":
			# dlg_completed.title  = ft.Text("Order Completed")
			# vessel1_id = extract_recipe_id(1)
			# if vessel1_id != 0:
			# 	vessel1_recipe = getrecipename(vessel1_id)
			# 	vessel1_oid = extract_order_id(1)
			# 	dlg_completed.content=ft.Text(f"""{vessel1_recipe} Completed
			# 					Pls Take the Order
			# 					Order Id - {vessel1_oid}""")
			# 	page.add(dlg_completed)
			# 	page.open(dlg_completed)
			# 	print("opening dlg_modal")
			# 	# sleep(5)
			# 	page.update()
			# r.set('vessel1_comp','no')
			completedPage(page,1)
			sleep(5)


		if r.get("vessel2_comp").decode("utf-8") == "yes":
			# dlg_completed.title  = ft.Text("Order Completed")
			# vessel2_id = extract_recipe_id(2)
			# if vessel2_id != 0:
			# 	vessel2_recipe = getrecipename(vessel2_id)
			# 	vessel2_oid = extract_order_id(2)
			# 	dlg_completed.content=ft.Text(f"""{vessel2_recipe} Completed
			# 					Pls Take the Order
			# 					Order Id - {vessel2_oid}""")
			# 	page.add(dlg_completed)
			# 	page.open(dlg_completed)
			# 	page.update()
			# r.set('vessel2_comp','no')
			completedPage(page,2)
			sleep(5)


		pb1 = ft.ProgressBar(width=400,color = "green", bgcolor="#eeeeee")
		pb1.value = 50*0.01
		
		pb2 = ft.ProgressBar(width=400,color = "green", bgcolor="#eeeeee")
		pb2.value = 50*0.01
		
		
		order_in_progress = progress_orderid(1)
		if order_in_progress == 0:
			prog = " - "
			pb1.value = 0
			rec1_text = ft.Text("")
		print(order_in_progress)
		sleep(5)
		if order_in_progress != 0:
			prog = order_in_progress
			p = progress_percent(1)
			pb1.value = int(p)*0.01
			vessel1_id = extract_recipe_id(1)
			vessel1_recipe = getrecipename(vessel1_id)
			rec1_text = ft.Text(f"{vessel1_recipe}")

		order_in_progress = progress_orderid(2)
		if order_in_progress == 0:
			prog2 = " - "
			pb2.value = 0
			rec2_text = ft.Text("")
		if order_in_progress != 0:
			prog2 = order_in_progress
			p = progress_percent(2)
			pb2.value = int(p)*0.01
			vessel2_id = extract_recipe_id(2)
			vessel2_recipe = getrecipename(vessel2_id)
			rec2_text = ft.Text(f"{vessel2_recipe}")

		order_completed = last_completed_orderid()
		if order_completed == 0:
			comp = " - "
		if order_completed != 0:
			comp = order_completed

		orders_queue = get_created_orders()
		if orders_queue  == 0:
			que = " - "
		if orders_queue  != 0:
			que = orders_queue 

		order_completed_container = ft.Row(
					[
						ft.Container(
							margin=5,
							padding=5,
							theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.ORANGE_100)),
							width=200,
							bgcolor=ft.colors.GREEN_200,
							border_radius=10,
							ink=True,
							border=ft.border.all(2, ft.colors.ORANGE_100),
							content = ft.ResponsiveRow(
								[
								ft.Text(f"Completed",size=15, weight=ft.FontWeight.W_700),
								ft.Text(f"Order ID : {comp}",size=25, weight=ft.FontWeight.W_700,text_align =ft.TextAlign.CENTER),
								],
							),
						),
					],
			)
		
		order_preparing_container_1 = ft.Row(
					[
						ft.Container(
							margin=5,
							padding=5,
							theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.ORANGE_100)),
							width=200,
							bgcolor=ft.colors.YELLOW_100,
							border_radius=10,
							ink=True,
							border=ft.border.all(2, ft.colors.ORANGE_100),
							content = ft.ResponsiveRow(
								[
								ft.Text(f"V1 Preparing",size=15, weight=ft.FontWeight.W_700),
								rec1_text,
								pb1,
								ft.Text(f"Order ID : {prog}",size=25, weight=ft.FontWeight.W_700,text_align =ft.TextAlign.CENTER),
								],
							),
						),
					],
			)
		order_preparing_container_2 = ft.Row(
					[
						ft.Container(
							margin=5,
							padding=5,
							theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.ORANGE_100)),
							width=200,
							bgcolor=ft.colors.YELLOW_100,
							border_radius=10,
							ink=True,
							border=ft.border.all(2, ft.colors.ORANGE_100),
							content = ft.ResponsiveRow(
								[
								ft.Text(f"V2 Preparing",size=15, weight=ft.FontWeight.W_700),
								rec2_text,
								pb2,
								ft.Text(f"Order ID : {prog2}",size=25, weight=ft.FontWeight.W_700,text_align =ft.TextAlign.CENTER),
								],
							),
						),
					],
			)
		
		order_queue_container = ft.Row(
					[
						ft.Container(
							margin=5,
							padding=5,
							alignment=ft.alignment.center,
							theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.ORANGE_100)),
							width=200,
							bgcolor=ft.colors.ORANGE_200,
							border_radius=10,
							ink=True,
							# expand = True,
							border=ft.border.all(2, ft.colors.ORANGE_100),
							content = ft.ResponsiveRow(
								[
								ft.Text(f"In Queue -Order IDs:",size=15, weight=ft.FontWeight.W_700),
								ft.Text(f"{que}",size=20, weight=ft.FontWeight.W_700,text_align =ft.TextAlign.CENTER),
								],
							),
						),
					],
			)


		order_status = ft.ResponsiveRow(
					[
					ft.Container(
				content=ft.Row(
					[
				order_completed_container,
				order_preparing_container_1,
				order_preparing_container_2,
				order_queue_container,
					],
					alignment="spaceBetween",
				)
			),
					],
			)
		page.bottom_appbar.content.controls.append(order_status)
		page.update()
		showStatusMsg("checking orders")
		

	
	async def functhatcallsabovefuncevery5s(func):
		current = page.client_storage.get("current")
		while geter <= 1:
			func()
			showStatusMsg(f"{geter}")
			showStatusMsg("functhatcallsabovefuncevery10s")
			await asyncio.sleep(5)

	showStatusMsg(f"{geter}")
	task = asyncio.run(functhatcallsabovefuncevery5s(func= orders_check))


ft.app(main)
# ft.app(main, view=ft.AppView.WEB_BROWSER)