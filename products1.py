import flet as ft
from db_retrieve import *
from imports import *
from customise_page import *
recipe_id = 0


def Recipes(page : ft.Page):

	check_db_recipe_step =  0

	try :
		page.client_storage.set("end","1")
		page.client_storage.set("current","recipes")
	
	except Exception as e:
		showStatusMsg(f"The error is client storage recipespage {e}")
		pass
	def dlg_close(e):
		page.close(dlg_modal)
		page.update()
		page.clean()
		Recipes(page)
	
	def dlg_open(e):
		page.open(dlg_modal)
		page.update()

	dlg_modal = ft.AlertDialog(
		modal=True,
		title=ft.Text("Recipe Not Available"),
		content=ft.Text(""),
		actions=[
			ft.TextButton("OK", on_click=lambda e:dlg_close(1))
		],
		actions_alignment=ft.MainAxisAlignment.CENTER,
	)

	if check_db_recipe_step == 0:
		vid = 1
		recipe_list = dbextractRecipeList()

		def showrecipe(e: ft.TapEvent):
			try:
				data=e.control.data
				print(f"Data is {data}")
				
				recipe_id = extractRecipeId(data)
				
				
				avail = extractRecipeAvailable(data)
				

				if avail != "available":
					print("not_available")
					page.add(dlg_modal)
					dlg_open(1)
					page.client_storage.set("current","medium")
					Recipes(page)

				if avail == "available":
					print('Recipe_id = ',recipe_id)
					Display(page, recipe_id)


			except Exception as e :
				showStatusMsg(f"The error is {e}")
				pass

		
		def filter_recipe(e):
			print(e)
			if e != "all":
				images.controls.clear()
				counter = 1
				for i in recipe_list:
					#ima = base64.b64encode(i[3])
					if i[4] == e:
						if i[6] == "available":
							images.controls.append(
								ft.Container(
									margin=5,
									padding=5,
									alignment=ft.alignment.center,
									theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.ORANGE_100)),
									width=200,
									height=250,
									bgcolor=ft.colors.SURFACE_VARIANT,
									border_radius=10,
									ink=True,
									border=ft.border.all(2, ft.colors.ORANGE_100),
									data = i[1],
									on_click=lambda e:showrecipe(e),
									content = ft.Column(
										controls = [ft.Text(
							spans=[
								ft.TextSpan(
									f"{i[1]}",
									ft.TextStyle(
										size=25,
										weight=ft.FontWeight.BOLD,
										foreground=ft.Paint(
											gradient=ft.PaintLinearGradient(
												(0, 20), (150, 20), [ft.colors.GREEN, ft.colors.BLUE]
											)
										),
									),
								),
							],
						),
													ft.Text(value = f"₹ {i[5]} ",
															weight=ft.FontWeight.W_800,
															size=15),
													ft.Image(src= f"{i[3]}"),
													]
									),
								)
							)
						counter = counter+1
						
						if counter%10 == 0:
							page.update()
					
					
						if i[6] != "available":
							images.controls.append(
								ft.Container(
									margin=5,
									padding=5,
									alignment=ft.alignment.center,
									theme=ft.Theme(color_scheme_seed=ft.colors.GREY),
									theme_mode=ft.ThemeMode.DARK,
									width=200,
									height=250,
									bgcolor=ft.colors.SURFACE_VARIANT,
									border_radius=10,
									disabled = True,
									opacity= 0.5,
									ink=True,
									border=ft.border.all(2, ft.colors.ORANGE_100),
									data = i[1],
									on_click=lambda e:showrecipe(e),
									content = ft.Column(
										controls = [ft.Text(
							spans=[
								ft.TextSpan(
									f"{i[1]} - (out of stock)",
									ft.TextStyle(
										size=25,
										weight=ft.FontWeight.BOLD,
										foreground=ft.Paint(
											gradient=ft.PaintLinearGradient(
												(0, 20), (150, 20), [ft.colors.WHITE, ft.colors.WHITE]
											)
										),
									),
								),
							],
						),
													ft.Text(value = f"₹ {i[5]} ",
															weight=ft.FontWeight.W_800,
															size=15),
													ft.Image(src= f"{i[7]}"),
													]
									),
								)
							)
						counter = counter+1
						
						if counter%10 == 0:
							page.update()
					


				if e == "latte":
					all_button.disabled = False
					others_button.disabled = False
					juice_button.disabled = False
					milkshake_button.disabled = False
					bubbletea_button.disabled = False
					latte_button.disabled = True
				
				if e == "milkshake":
					all_button.disabled = False
					others_button.disabled = False
					juice_button.disabled = False
					milkshake_button.disabled = True
					bubbletea_button.disabled = False
					latte_button.disabled = False
				
				if e == "bubbletea":
					all_button.disabled = False
					others_button.disabled = False
					juice_button.disabled = False
					milkshake_button.disabled = False
					bubbletea_button.disabled = True
					latte_button.disabled = False
				
				if e == "juice":
					all_button.disabled = False
					others_button.disabled = False
					juice_button.disabled = True
					milkshake_button.disabled = False
					bubbletea_button.disabled = False
					latte_button.disabled = False
				
				if e == "other":
					all_button.disabled = False
					others_button.disabled = True
					juice_button.disabled = False
					milkshake_button.disabled = False
					bubbletea_button.disabled = False
					latte_button.disabled = False
				
				page.update()
			
			if e == "all":
				images.controls.clear()
				counter = 1
				for i in recipe_list:
					#ima = base64.b64encode(i[3])
					if i[6] == "available":
						images.controls.append(
							ft.Container(
								margin=5,
								padding=5,
								alignment=ft.alignment.center,
								theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.ORANGE_100)),
								width=200,
								height=250,
								bgcolor=ft.colors.SURFACE_VARIANT,
								border_radius=10,
								ink=True,
								border=ft.border.all(2, ft.colors.ORANGE_100),
								data = i[1],
								on_click=lambda e:showrecipe(e),
								content = ft.Column(
									controls = [ft.Text(
						spans=[
							ft.TextSpan(
								f"{i[1]}",
								ft.TextStyle(
									size=25,
									weight=ft.FontWeight.BOLD,
									foreground=ft.Paint(
										gradient=ft.PaintLinearGradient(
											(0, 20), (150, 20), [ft.colors.GREEN, ft.colors.BLUE]
										)
									),
								),
							),
						],
					),
												ft.Text(value = f"₹ {i[5]} ",
														weight=ft.FontWeight.W_800,
														size=15),
												ft.Image(src= f"{i[3]}"),
												]
								),
							)
						)
						counter = counter+1
						if counter%10 == 0:
							page.update()

					if i[6] != "available":
						images.controls.append(
							ft.Container(
								margin=5,
								padding=5,
								alignment=ft.alignment.center,
								theme=ft.Theme(color_scheme_seed=ft.colors.GREY),
								theme_mode=ft.ThemeMode.DARK,
								width=200,
								height=250,
								bgcolor=ft.colors.SURFACE_VARIANT,
								border_radius=10,
								ink=True,
								border=ft.border.all(2, ft.colors.ORANGE_100),
								data = i[1],
								disabled= True,
								opacity=0.5,
								on_click=lambda e:showrecipe(e),
								content = ft.Column(
									controls = [ft.Text(
						spans=[
							ft.TextSpan(
								f"{i[1]} - (out of stock)",
								ft.TextStyle(
									size=25,
									weight=ft.FontWeight.BOLD,
									foreground=ft.Paint(
										gradient=ft.PaintLinearGradient(
											(0, 20), (150, 20), [ft.colors.WHITE, ft.colors.WHITE]
										)
									),
								),
							),
						],
					),
												ft.Text(value = f"₹ {i[5]} ",
														weight=ft.FontWeight.W_800,
														size=15),
												ft.Image(src= f"{i[7]}",
					 									fit=ft.ImageFit.CONTAIN,),
												]
								),
							)
						)
						counter = counter+1
						if counter%10 == 0:
							page.update()

				all_button.disabled = True

				juice_button.disabled = False
				milkshake_button.disabled = False
				bubbletea_button.disabled = False
				latte_button.disabled = False
				others_button.disabled = False


				page.update()

		all_button = ft.FilledButton(
                "ALL",
				on_click=lambda e:filter_recipe("all")
            )
		
		juice_button = ft.FilledButton(
                "Fresh Juice",
				on_click=lambda e:filter_recipe("juice")
            )
		
		milkshake_button = ft.FilledButton(
                "Milkshakes",
				on_click=lambda e:filter_recipe("milkshake")
            )
		
		latte_button = ft.FilledButton(
                "Latte",
				on_click=lambda e:filter_recipe("latte")
            )
	
		bubbletea_button = ft.FilledButton(
                "Boba",
				on_click=lambda e:filter_recipe("bubbletea")
            )
		
		others_button = ft.FilledButton(
                "Others",
				on_click=lambda e:filter_recipe("other")
            )
		
		

		def display_product_page_header():
			return ft.ResponsiveRow(
					[
					ft.Container(
				content=ft.Row(
					[
						all_button,
						juice_button,
						milkshake_button,
						latte_button,
						bubbletea_button,
						others_button,
					],
					alignment="spaceBetween",
				)
			),
					],
			)


		def inputsearch(e):
			try:
				search_name = anchor.value.lower()
				print(search_name)
				check = search_name
				images.controls.clear()
				counter = 1
				for i in recipe_list:
					p = i[1]
					if check.lower() in p.lower():
						#ima = base64.b64encode(i[3])
						if i[6] == "available":
							images.controls.append(
							ft.Container(
								margin=5,
								padding=5,
								alignment=ft.alignment.center,
								theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.ORANGE_100)),
								width=200,
								height=250,
								bgcolor=ft.colors.SURFACE_VARIANT,
								border_radius=10,
								ink=True,
								border=ft.border.all(2, ft.colors.ORANGE_100),
								data = i[1],
								on_click=lambda e:showrecipe(e),
								content = ft.Column(
									controls = [ft.Text(
						spans=[
							ft.TextSpan(
								f"{i[1]}",
								ft.TextStyle(
									size=25,
									weight=ft.FontWeight.BOLD,
									foreground=ft.Paint(
										gradient=ft.PaintLinearGradient(
											(0, 20), (150, 20), [ft.colors.GREEN, ft.colors.BLUE]
										)
									),
								),
							),
						],
					),
					ft.Text(f"Price: ₹ {i[5]} "),
					ft.Image(src= f"{i[3]}"),
					]
					),
					)
					)
					
						
						if i[6] != "available":
							images.controls.append(
							ft.Container(
								margin=5,
								padding=5,
								alignment=ft.alignment.center,
								theme=ft.Theme(color_scheme_seed=ft.colors.GREY),
            					theme_mode=ft.ThemeMode.DARK,
								width=200,
								height=250,
								bgcolor=ft.colors.SURFACE_VARIANT,
								border_radius=10,
								ink=True,
								disabled=True,
								opacity=0.5,
								border=ft.border.all(2, ft.colors.ORANGE_100),
								data = i[1],
								on_click=lambda e:showrecipe(e),
								content = ft.Column(
									controls = [ft.Text(
						spans=[
							ft.TextSpan(
								f"{i[1]} - (out of stock)",
								ft.TextStyle(
									size=25,
									weight=ft.FontWeight.BOLD,
									foreground=ft.Paint(
										gradient=ft.PaintLinearGradient(
											(0, 20), (150, 20), [ft.colors.WHITE, ft.colors.WHITE]
										)
									),
								),
							),
						],
					),
					ft.Text(f"Price: ₹ {i[5]} "),
					ft.Image(src= f"{i[7]}"),
					]
					),
					)
					)
					page.update()

			except Exception as e :
				showStatusMsg(f"The error is {e}")
				pass


		
		anchor = ft.TextField(label="Search Recipes Here",
				on_change=inputsearch
		
				)
 

		images = ft.GridView(
		expand=1,
		runs_count=2,
		max_extent=300,
		child_aspect_ratio=0.75,
		spacing=5,
		run_spacing=5,
	)

		counter = 1

		def press_clicked(e :ft.TapEvent):
			print(f"in animate {e.control}")
			# e.width = 100 if e.width == 200 else 200
			# e.height = 100 if e.height == 200 else 200
			# e.bgcolor = "blue" if e.bgcolor == "red" else "red"
			# e.update()


		for i in recipe_list:
			if i[6] == "available":
				images.controls.append(
					ft.Container(
						margin=5,
						padding=5,
						alignment=ft.alignment.center,
						theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.ORANGE_100)),
						width=200,
						height=250,
						bgcolor=ft.colors.SURFACE_VARIANT,
						border_radius=10,
						ink=True,
						border=ft.border.all(2, ft.colors.ORANGE_100),
						data = i[1],
						on_click=lambda e:showrecipe(e),
						content = ft.Column(
							controls = [ft.Text(
				spans=[
					ft.TextSpan(
						f"{i[1]}",
						ft.TextStyle(
							size=25,
							weight=ft.FontWeight.BOLD,
							foreground=ft.Paint(
								gradient=ft.PaintLinearGradient(
									(0, 20), (150, 20), [ft.colors.GREEN, ft.colors.BLUE]
								)
							),
						),
					),
				],
			),
										ft.Text(value = f"₹ {i[5]} ",
												weight=ft.FontWeight.W_800,
												size=15),
										ft.Image(src= f"{i[3]}"),
										]
						),
					)
				)

			if i[6] != "available":
				images.controls.append(
					ft.Container(
						margin=5,
						padding=5,
						alignment=ft.alignment.center,
						theme=ft.Theme(color_scheme_seed=ft.colors.GREY),
            			theme_mode=ft.ThemeMode.DARK,
						width=200,
						height=250,
						bgcolor=ft.colors.SURFACE_VARIANT,
						border_radius=10,
						ink=True,
						border=ft.border.all(2, ft.colors.ORANGE_100),
						data = i[1],
						disabled=True,
						opacity = 0.5,
						on_click= ft.AnimationCurve.BOUNCE_IN_OUT,
						content = ft.Column(
							controls = [ft.Text(
				spans=[
					ft.TextSpan(
						f"{i[1]} - (out of stock)",
						ft.TextStyle(
							size=25,
							weight=ft.FontWeight.BOLD,
							foreground=ft.Paint(
								gradient=ft.PaintLinearGradient(
									(0, 20), (150, 20), [ft.colors.WHITE, ft.colors.WHITE]
								)
							),
						),
					),
				],
			),
										ft.Text(value = f"₹ {i[5]} ",
												weight=ft.FontWeight.W_800,
												size=15),
										ft.Image(src= f"{i[7]}"),
										]
						),
					)
				)
			page.update()
				

		img = ft.ResponsiveRow(
					[
					ft.Container(
				content=ft.Row(
					[
						images,
					],
					alignment="spaceBetween",
				)
			),
					],
			)


		page.scroll = True
		page.add(
			 ft.ResponsiveRow(
				  [
					   ft.Column(
							[
							anchor,
							display_product_page_header(),
							img,
							],
						horizontal_alignment=ft.MainAxisAlignment.CENTER,
						scroll=ft.ScrollMode.ALWAYS,
						on_scroll_interval=0,
					   ),
				  ],
				alignment=ft.MainAxisAlignment.CENTER,
			 ),
		)

		page.update()
		page.bottom_appbar.content.controls.clear()
	# current = page.client_storage.get("current")

	# def orders_check():

	# 	current = page.client_storage.get("current")
	# 	page.bottom_appbar.content.controls.clear()
	# 	order_in_progress = progress_orderid()
	# 	if order_in_progress == 0:
	# 		prog = " - "
	# 	if order_in_progress != 0:
	# 		prog = order_in_progress
	# 	order_completed = last_completed_orderid()
	# 	if order_completed == 0:
	# 		comp = " - "
	# 	if order_completed != 0:
	# 		comp = order_completed

	# 	orders_queue = get_created_orders()
	# 	if orders_queue  == 0:
	# 		que = " - "
	# 	if orders_queue  != 0:
	# 		que = orders_queue 

	# 	order_completed_container = ft.Row(
	# 				[
	# 					ft.Container(
	# 						margin=5,
	# 						padding=5,
	# 						theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.ORANGE_100)),
	# 						width=200,
	# 						bgcolor=ft.colors.GREEN_200,
	# 						border_radius=10,
	# 						ink=True,
	# 						border=ft.border.all(2, ft.colors.ORANGE_100),
	# 						content = ft.ResponsiveRow(
	# 							[
	# 							ft.Text(f"Completed",size=15, weight=ft.FontWeight.W_700),
	# 							ft.Text(f"Order ID : {comp}",size=25, weight=ft.FontWeight.W_700,text_align =ft.TextAlign.CENTER),
	# 							],
	# 						),
	# 					),
	# 				],
	# 		)
		
	# 	order_preparing_container = ft.Row(
	# 				[
	# 					ft.Container(
	# 						margin=5,
	# 						padding=5,
	# 						theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.ORANGE_100)),
	# 						width=200,
	# 						bgcolor=ft.colors.YELLOW_100,
	# 						border_radius=10,
	# 						ink=True,
	# 						border=ft.border.all(2, ft.colors.ORANGE_100),
	# 						content = ft.ResponsiveRow(
	# 							[
	# 							ft.Text(f"Preparing",size=15, weight=ft.FontWeight.W_700),
	# 							ft.Text(f"Order ID : {prog}",size=25, weight=ft.FontWeight.W_700,text_align =ft.TextAlign.CENTER),
	# 							],
	# 						),
	# 					),
	# 				],
	# 		)
		
	# 	order_queue_container = ft.Row(
	# 				[
	# 					ft.Container(
	# 						margin=5,
	# 						padding=5,
	# 						alignment=ft.alignment.center,
	# 						theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.ORANGE_100)),
	# 						width=200,
	# 						bgcolor=ft.colors.ORANGE_200,
	# 						border_radius=10,
	# 						ink=True,
	# 						# expand = True,
	# 						border=ft.border.all(2, ft.colors.ORANGE_100),
	# 						content = ft.ResponsiveRow(
	# 							[
	# 							ft.Text(f"In Queue -Order IDs:",size=15, weight=ft.FontWeight.W_700),
	# 							ft.Text(f"{que}",size=20, weight=ft.FontWeight.W_700,text_align =ft.TextAlign.CENTER),
	# 							],
	# 						),
	# 					),
	# 				],
	# 		)


	# 	order_status = ft.ResponsiveRow(
	# 				[
	# 				ft.Container(
	# 			content=ft.Row(
	# 				[
	# 			order_completed_container,
	# 			order_preparing_container,
	# 			order_queue_container,
	# 				],
	# 				alignment="spaceBetween",
	# 			)
	# 		),
	# 				],
	# 		)
	# 	page.bottom_appbar.content.controls.append(order_status)
	# 	page.update()
	# 	showStatusMsg("checking orders")

	# async def functhatcallsabovefuncevery5s(func):
	# 	# global end
	# 	current = page.client_storage.get("current")
	# 	while current == "recipes":
	# 		func()
	# 		showStatusMsg("functhatcallsabovefuncevery10s")
	# 		await asyncio.sleep(5)

	# task =asyncio.run(functhatcallsabovefuncevery5s(func= orders_check))
		 