
from imports import *
import flet as ft
from db_retrieve import *
from queue_page import *
import requests


def payment(page:ft.Page,recipe_id,sugar1,ice1,userid, number, name):

	page.clean()
	page.update()

	def dlg_close(e):
		page.close(dlg_modal1)
		page.update()
	
	def dlg_open(e):
		page.open(dlg_modal1)
		page.update()

	dlg_modal1 = ft.AlertDialog(
		modal=True,
		title=ft.Text(""),
		content=ft.Text(""),
		actions=[
			ft.ProgressRing(),
		],
		actions_alignment=ft.MainAxisAlignment.CENTER,
	)

	# page.add(dlg_modal)
	dlg_open(1)
	page.client_storage.set("current","payment")

	page.client_storage.set("end","1")

	model = "tab"
	sugar = sugar1
	ice = ice1

	# o_id = page.client_storage.get("order_id")
	o_id = 1
	if o_id == 1:

		# order_queue(page,recipe_id,sugar,ice)
		if (model == "mobile"):
			ti = time.time()
			def payment_link(price,recipe_name):
				try:
					url = "https://api.razorpay.com/v1/payment_links"
					data = {
						"upi_link": True,
						"amount": price,
						"currency": "INR",
						"description": f"{recipe_name}",
						"customer": {
							"name": "Gaurav Kumar",
							"email": "gaurav.kumar@example.com",
							"contact": "+919000090000"
						},
						"notify": {
							"sms": False,
							"email": False
						},
						"reminder_enable": False,
						"notes": {
							"policy_name": "Jeevan Bima"
						}
						}
					response = requests.post(url, auth=("rzp_live_YDqmG6kyPkYdAJ", "lcT8WFhLrx4VMoD999SacgWb"),json = data)
					if response.status_code == 200:
						return response.json()

				except Exception as e:
					print(e)
					dlg_close(1)
					page.clean()
					page.add(ft.Text("Something Went Wrong, Pls Try Again Later"))
					page.client_storage.set("error")


			recipe_price = getrecipeprice(recipe_id)
			recipe_name = getrecipename(recipe_id)
			price = (recipe_price*100)
			get_link = payment_link(price,recipe_name)
			link = get_link["short_url"]
			payment_id =  get_link["id"]
			print(link, payment_id)

			page.clean()
			
			timer = ft.Text(
				value = f"Page will automatically closes in 120 secs",
				bgcolor=ft.colors.YELLOW_300,
				weight=ft.FontWeight.W_100,
				)

			wv = ft.WebView(
				f"{link}",
				expand=True,
				on_page_started=lambda _: print("Page started"),
				on_page_ended=lambda _: print("Page ended"),
				on_web_resource_error=lambda e: print("Page error:", e.data),
			)
			
			completed_text = ft.Text(
											value=f"Scan QR code to pay ₹ {price/100}",
											size=35,
											color=ft.colors.BLUE,
											font_family="RobotoSlab",
											weight=ft.FontWeight.W_700,
										)
			
			img = ft.Image(src="https://i.gifer.com/origin/11/1184b4c0aa977f925dde58d2075772dd.gif",
				width=400,
				height=400,
				fit=ft.ImageFit.CONTAIN
				)
			
			img_failed = ft.Image(src="https://i.pinimg.com/originals/6e/f9/f2/6ef9f2fd6425c578274e72ce1f44a778.gif",
				width=400,
				height=400,
				fit=ft.ImageFit.CONTAIN
				)
			
			def display_timer():
				return ft.ResponsiveRow(
						[
						ft.Container(
					content=ft.Column(
						[
							# completed_text,
							timer,
							# wv,
						],
						horizontal_alignment=ft.MainAxisAlignment.CENTER,
						scroll=ft.ScrollMode.ALWAYS,
						on_scroll_interval=0,
					)
				),
						],
				)
			


			# page.appbar.disabled = True
			page.scroll = False
			dlg_close(1)
			page.clean()
			page.add(display_timer())
			# page.add(wv)
			sleep(5)

			i = 0


			def check_status(payment_id):
				# return (client1.payment_link.fetch(payment_id))
				url1 = f"https://api.razorpay.com/v1/payment_links/{payment_id}"
				response1 = requests.get(url1, auth=("rzp_live_YDqmG6kyPkYdAJ", "lcT8WFhLrx4VMoD999SacgWb"))
				print(response1.json())
				s2 = response1.json()
				return s2["status"]

			while(i < 120):
				sleep(2)
				print("in while")
				timer.value = f"Page will automatically closes in {120-i} secs"
				timer.update()
				status =  check_status(payment_id)
				print(status)
				if status == "paid":
					print("Exiting now")
					break
				i = i+2

			if i < 119:
				page.appbar.disabled = False
				print("Payment Confirmed")
				page.clean()
				page.add(ft.Column(
							spacing=10,
							scroll=ft.ScrollMode.ALWAYS,
							controls=[
								img, 
								ft.Text("Payment Confirmed"),
								ft.ResponsiveRow(
									[

									],
								),
							],
							horizontal_alignment=ft.CrossAxisAlignment.CENTER,
								))
				
				page.update()
				sleep(3)
				add_contact(userid, name, number)
				order_queue(page,recipe_id,sugar,ice)
				# order_confirmed(page,recipe_id)
			
			if i>=120:
				page.clean()
				page.appbar.disabled = False
				page.add(timer)
				timer.value = f"Payment Failed, Press Home Button to Go Back"
				page.add(img_failed)
				sleep(2)
				page.update()


		if model == "tab":
			ti = time.time()
			def payment_link(price,recipe_name):
				try:
					# test = l
					url = "https://api.razorpay.com/v1/payment_links"
					data = {
						"upi_link": True,
						"amount": price,
						"currency": "INR",
						"description": f"{recipe_name}",
						"customer": {
							"name": "Gaurav Kumar",
							"email": "gaurav.kumar@example.com",
							"contact": "+919000090000"
						},
						"notify": {
							"sms": False,
							"email": False
						},
						"reminder_enable": False,
						"notes": {
							"policy_name": "Jeevan Bima"
						}
						}
					response = requests.post(url, auth=("rzp_live_YDqmG6kyPkYdAJ", "lcT8WFhLrx4VMoD999SacgWb"),json = data)
					if response.status_code == 200:
						return response.json()
				except Exception as e:
					print(e)
					dlg_close(1)
					sleep(0.3)
					page.clean()
					page.add(ft.Text("Something Went Wrong, Pls Try Again Later"))
					page.client_storage.set("current","error")
					pass
			
			def get_image(s):
				qrcode = segno.make(s)
				out = io.BytesIO()
				qrcode.save(out, scale=5, kind='png', dark='black')
				s1 = base64.b64encode(out.getvalue())
				b64_string = s1.decode ('utf-8')
				return(b64_string)
			try:
				recipe_price = getrecipeprice(recipe_id)
				recipe_name = getrecipename(recipe_id)
				price = (recipe_price*100)
				get_link = payment_link(price,recipe_name)
			
			except Exception as e:
				print(e)
				dlg_close(1)
				sleep(0.3)
				page.clean()
				page.add(ft.Text("Something Went Wrong, Pls Try Again Later"))
				page.client_storage.set("error")
				pass

			if get_link != None:
				link = get_link["short_url"]
				payment_id =  get_link["id"]
				print(link, payment_id)

				
				# GENERATE TO IMAGE FROM QRCODE
				url = get_image(link)
				# wv = ft.Image(src_base64=url)
				wv= ft.Image(
						src_base64=url,
						width=300,
						height=300,
						fit=ft.ImageFit.FILL,
						col={"sm":2, "md": 1, "xl": 1},
											)
				# page.clean()
				
				timer = ft.Text(
					value = f"Page will automatically closes in 120 secs",
					bgcolor=ft.colors.YELLOW_300,
					weight=ft.FontWeight.W_100,
					)

				completed_text = ft.Text(
												value=f"Scan QR code to pay ₹ {price/100}",
												size=35,
												color=ft.colors.BLUE,
												font_family="RobotoSlab",
												weight=ft.FontWeight.W_700,
											)
				
				img = ft.Image(src="https://i.gifer.com/origin/11/1184b4c0aa977f925dde58d2075772dd.gif",
					width=400,
					height=400,
					fit=ft.ImageFit.CONTAIN
					)
				
				img_failed = ft.Image(src="https://i.pinimg.com/originals/6e/f9/f2/6ef9f2fd6425c578274e72ce1f44a778.gif",
					width=400,
					height=400,
					fit=ft.ImageFit.CONTAIN
					)
				
				
				cont = ft.Container(
						margin=1,
						padding=10,
						alignment=ft.alignment.center,
						theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.ORANGE_100)),
						bgcolor=ft.colors.AMBER_100,
						border=ft.border.all(2, ft.colors.GREEN_50),
						border_radius=10,
						content=ft.Column(
							[
								completed_text,
								wv,
								timer,
							],
						horizontal_alignment=ft.MainAxisAlignment.CENTER,
						)
					)


				page.scroll = False
				
				dlg_close(1)
				page.update()
				page.add(cont)

				i = 0


				def check_status(payment_id):
					url1 = f"https://api.razorpay.com/v1/payment_links/{payment_id}"
					response1 = requests.get(url1, auth=("rzp_live_YDqmG6kyPkYdAJ", "lcT8WFhLrx4VMoD999SacgWb"))
					print(response1.json())
					s2 = response1.json()
					print(s2["status"])
					# sleep(10)
					return s2["status"]
				

				while(i < 120):
					sleep(2)
					print("in while")
					timer.value = f"Page will automatically closes in {120-i} secs"
					timer.update()
					status =  check_status(payment_id)
					print(status)
					if status == "paid":
						print("Exiting now")
						break
					s = page.client_storage.get("current")
					if s != 'payment':
						i = 201
						break
					
					i = i+2
					# break

				if i < 119:
					page.appbar.disabled = False
					print(i)
					print("Payment Confirmed")
					page.clean()
					page.add(ft.Column(
								spacing=10,
								scroll=ft.ScrollMode.ALWAYS,
								controls=[
									img, 
									ft.Text("Payment Confirmed"),
									ft.ResponsiveRow(
										[

										],
									),
								],
								horizontal_alignment=ft.CrossAxisAlignment.CENTER,
									))
					
					page.update()
					sleep(2)
					order_queue(page,recipe_id,sugar,ice)
					# order_confirmed(page,recipe_id)
				
				if i>=120 and i<200:
					page.clean()
					page.appbar.disabled = False
					page.add(timer)
					timer.value = f"Payment Failed, Press Home Button to Go Back"
					page.add(img_failed)
					sleep(2)
					page.update()
		
		# if o_id != None:
		# 	page.clean()
		# 	page.add(ft.Text(value = "Already Your Order in Queue",size = 25))
		# 	sleep(3)
		# 	order_queue(page,recipe_id,sugar,ice)