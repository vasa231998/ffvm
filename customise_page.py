
import flet as ft
from db_retrieve import *
from imports import *
from payment_page import *
from order_confirmed_page import *
from id_generator import *



def Display(page : ft.Page,recipe_id):

	page.clean()
	page.update()
	
	def dlg_close(e):
		page.close(dlg_modal1)
		# page.clean()
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

	dlg_open(1)
	sleep(0.5)

	try:
		page.client_storage.contains_key("end")
		page.client_storage.set("current","customise")
		page.client_storage.set("end","1")
	except Exception as e:
		showStatusMsg(f"The error is {e}")
		pass

	# global recipe_id
	global recipe_image
	global recipe_name
	global ice
	global sugar
	ice = 0
	sugar = 0
	page.clean()

	print(f"recipe_id is {recipe_id}")
	recipe_name = getrecipename(recipe_id)

	print(f"recipe_name is {recipe_name}")
	recipe_description = getrecipedescription(recipe_id)
	
	recipe_image = getrecipeimage(recipe_id)
	
	recipe_price = getrecipeprice(recipe_id)


	rec_name = ft.Text(
			spans=[
				ft.TextSpan(
					f"{recipe_name}",
					ft.TextStyle(
						size=40,
						weight=ft.FontWeight.BOLD,
						foreground=ft.Paint(
							gradient=ft.PaintLinearGradient(
								(0, 20), (150, 20), [ft.colors.AMBER, ft.colors.AMBER]
							)
						),
					),
				),
			],
		)
	
	rec_image = ft.Image(
						src=f"{recipe_image}",
						width=180,
						height=180,
						fit=ft.ImageFit.CONTAIN,
						repeat=ft.ImageRepeat.NO_REPEAT,
						border_radius=10,
						expand=True,
						)


	def title():
		return ft.ResponsiveRow(
					
					[
					ft.Container(
				bgcolor=ft.colors.BLUE_100,
				border_radius= 10,
				width=200,
				# height=250,
				content =
						ft.ResponsiveRow(
							[   
								rec_name,
								rec_image,
							],
						alignment = "center",
						spacing = 20,

						),
					padding = 10,
					margin = ft.margin.all(10),

					),
					],
	)

	def display_product_page_header():
		return ft.ResponsiveRow(
				[
				ft.Container(
			content=ft.Row(
				[
					ft.Text("Customise Page"),
				],
				alignment="center",
			)
		),
				],
		)
	def close_dlg3(e):
			# dlg_modal3.open = False
			page.close(dlg_modal3)
			page.update()

	dlg_modal3 = ft.AlertDialog(
			modal=True,
			title=ft.Text(""),
			data = "2",
			actions=[
				ft.TextButton("OK", on_click=close_dlg3),
			],
			actions_alignment=ft.MainAxisAlignment.END,
			on_dismiss=lambda e: print("Modal dialog dismissed!"),
		)
	
	def open_dlg_modal3(e):
		print(e)
		# page.dialog = dlg_modal3
		# dlg_modal3.open = True
		page.open(dlg_modal3)
		page.update()
		
	def containers_mapping():
		dlg_modal3.actions.clear()
		dlg_modal3.content = ft.ProgressBar()
		open_dlg_modal3(1)
		global pcid
		for i in range (30) :
			if i == 0 :
				continue
			updatepowder = {str(i) : f'{powder_container_mapping_getdb(i)}'}
			pcid.update(updatepowder)
		updatePowderContainer()

	def cancel_click(e):
		page.close(bottom_sheet)

	
	# page.add(dlg_modal)
	name_text = ft.TextField(disabled=False,width= 200, label = "Your Name *",bgcolor="WHITE",border_radius=10,label_style=ft.TextStyle(color=ft.colors.BLACK,bgcolor = ft.colors.WHITE,))
	number_text = ft.TextField(disabled=False,width= 200, label = "Mobile Number *",input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""),keyboard_type = ft.KeyboardType.NUMBER,bgcolor="WHITE",border_radius=10,label_style=ft.TextStyle(color=ft.colors.BLACK,bgcolor = ft.colors.WHITE,))


	def pay_dlg(e):
		if number_text.value != '':
			if(len(number_text.value) == 10):
				if name_text.value != '':
					dlg_modal3.actions.clear()
					close_dlg3(1)
					userid = generate_username(name_text.value)
					print(userid)
					payment(page,recipe_id,sugar,ice, userid, number_text.value, name_text.value)

				if name_text.value == '':
					name_text.border_color = "RED"
					name_text.border_width = 1
					page.update()

			if len(number_text.value) != 10:
				number_text.border_color = "RED"
				number_text.border_width = 1
				page.update()

		if number_text.value == '':
			number_text.border_color = "RED"
			number_text.border_width = 1
			page.update()

	def get_contact():
		dlg_modal3.title = ft.Text("Contact Details")
		dlg_modal3.content = ft.Text("We will use this information to provide a better experience and keep you updated. Thank you!")
		dlg_modal3.actions.clear()
		dlg_modal3.actions.append(ft.Column(
			[
				name_text,
				number_text,
				ft.Row(
					[
				ft.ElevatedButton(text= "Cancel",on_click=close_dlg3),
				ft.ElevatedButton(text = "Confirm Payment", on_click= pay_dlg),
					],
				)
			],
			alignment=ft.alignment.center,
		))
		open_dlg_modal3(1)
		page.update()

	
	def handle_click(e):
		dlg_modal3.actions.clear()
		get_contact()
		
	
	action_sheet = ft.CupertinoActionSheet(
		title=ft.Row([ft.Text("Choose Payment Type")], alignment=ft.MainAxisAlignment.CENTER),
		# message=ft.Row([ft.Text("Description")], alignment=ft.MainAxisAlignment.CENTER),
		cancel=ft.CupertinoActionSheetAction(
			content=ft.Text("Cancel"),
			on_click=cancel_click,
		),
		actions=[
			ft.CupertinoActionSheetAction(
				content=ft.Text("Scan UPI QR"),
				is_default_action=True,
				on_click=handle_click,
			),
			# ft.CupertinoActionSheetAction(
			# 	content=ft.Text("Credit/Debit Card"),
			# 	is_default_action=True,
			# 	on_click=handle_click,
			# ),
		],
	)
	bottom_sheet = ft.CupertinoBottomSheet(action_sheet)


## Radi Buttons List

	def sugar_changed(e):
		global sugar
		customise = e.control.value
		sugar = customise
		# customisesugar_value(customise)
	
	def ice_changed(e):
		global ice
		customise = e.control.value
		ice = customise
		# customiseice_value(customise)
		 
	
	sugar_radio = ft.RadioGroup(
		content=ft.Column(
			[
				ft.Radio(value="High", label="Extra Sugar", adaptive=True, active_color=ft.colors.BLUE),
				ft.Radio(value="Less", label="Less Sugar", adaptive=True, active_color=ft.colors.BLUE),
				ft.Radio(value="Normal", label="Normal Sugar", adaptive=True, active_color=ft.colors.BLUE, autofocus=True),
			]
		),
		on_change=sugar_changed,
	)
	
	ice_radio = ft.RadioGroup(
		content=ft.Column(
			[
				ft.Radio(value="High", label="Extra Ice", adaptive=True, active_color=ft.colors.BLUE),
				ft.Radio(value="Less", label="Less Ice", adaptive=True, active_color=ft.colors.BLUE),
				ft.Radio(value="Normal", label="Normal Ice", adaptive=True, active_color=ft.colors.BLUE, autofocus=True),
			]
		),
		on_change=ice_changed,
	)


	sugar_container = ft.Container(
				bgcolor=ft.colors.AMBER_100,
				border_radius= 10,
				margin=5,
				padding=5,
			content=ft.Column(
				[
					sugar_radio,
				],
				alignment="center",
			),
			col={"sm": 6, "md": 6, "xl": 6},
		)
	
	ice_container = ft.Container(
				bgcolor=ft.colors.AMBER_100,
				border_radius= 10,
				margin=5,
				padding=5,
			content=ft.Column(
				[
					ice_radio,
				],
				alignment="center",
			),
			col={"sm": 6, "md": 6, "xl": 6},
		)
	

	def customise_container():
		return ft.ResponsiveRow(
				[
				ft.Container(
				bgcolor=ft.colors.BLUE_100,
				border_radius= 10,
				margin=5,
				padding=5,
			content=ft.ResponsiveRow(
				[
					sugar_container,
					ice_container,
				],
				alignment="left",
			),
		),
				],
		)
	page.scroll = True

	# price_text = ft.Text(f"Total Amount : ₹ {recipe_price}", size=16, weight=ft.FontWeight.W_900, selectable=True)

	bottom_appbar = ft.BottomAppBar(
		bgcolor=ft.colors.ORANGE,
		shape=ft.NotchShape.CIRCULAR,
		content=ft.ResponsiveRow(
			controls=[
				# price_text,
				# ft.Container(expand=True),
				ft.FloatingActionButton(
				text = f"""Total Amount : ₹ {recipe_price}
						Make Payment""",width=200, on_click=lambda e: handle_click(e),
						# col={"sm": 10, "md": 4, "xl": 2},
						),

			]
		),
		col={"sm": 6, "md": 6, "xl": 6},
	)
	dlg_close(1)
	page.update()

	page.add(
			 ft.ResponsiveRow(
				  [
					   ft.Column(
							[
							display_product_page_header(),
							title(),
							# customise_container(),
							bottom_appbar,
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