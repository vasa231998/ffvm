
import flet as ft
from db_retrieve import *
from imports import *
# from datetime import datetime

def redis_connection6(ips):
	try:
		global r
		r = redis.Redis()
		r = redis.Redis(host=ips,port=6380)
	except Exception as e :
		print(f"The error is redis error {e}")
		redis_connection6("100.96.37.82")
		# pass



def display_footer():
			return ft.Row(
				[
					ft.Text("ChillBot", size=10),
				]
			)


## Main Function
def order_confirmed(page : ft.Page,recipe_id):
	page.appbar.disabled = True
	page.clean()
	page.client_storage.set("current","final")
	# global end
	global recipe_time
	# end = 0
	page.client_storage.set("end","0")
	
	ingredient_name = "none"
	quantity = "none"
	start_time =  time.time()

	# global now
   ## this function will call with the interval of every 2secs with async function below
	def refresh():
		try:
			global recipe_time
			showStatusMsg("in refresh")

			oid1 = page.client_storage.get("order_id")
			if oid1 != None:
				oid = int(oid1)
				recipe_id = getrecipeidfromqueue(oid) ## Getting the recipe id from recipe step tables

			pwt = time.time() - start_time
			remaining_time = int(recipe_time - pwt)

			if recipe_id == 0: ## if the recipe is not ordered
				i =  0
				pr.value = i * 0.01  ## Progress value is 0
				stack.value = f"Recipe Not Selected" # Progress Text Displaying
				new_task.value = "Recipe Not Selected" # Recipe name Text
				# filter.disabled = True
				# cancel_cooking_btn.disabled = True # Cancel cooking button disabled
				img.src = "https://www.thrindle.com/static/media/emptyCart.4e943399.png" # no orders png
				page.update()

			## if the recipe is orders
			if recipe_id != 0:
				recipe_name = getrecipename(recipe_id) 
				new_task.value = f"{recipe_name}" # Recipe name Text
				# i =  int(progress_percent())
				i = int((pwt / recipe_time) * 100)
				pr.value = i * 0.01
				showStatusMsg(f"percentage is {i}")
				page.update()
			
			
			# recipe_name = getrecipename(recipe_id)

			if remaining_time > 62:
				stack.value = f"{recipe_name} --- Getting ready"
			
			if remaining_time < 61:
				stack.value = f"{recipe_name} --- Hold on for a minute"
			
			if remaining_time < 30:
				stack.value = f"{recipe_name} --- Hold Tight"

			page.update()
			vessel_1_rec_complete = (r.get('vessel1_comp')).decode("utf-8") ## checking all the steps completed ?

			if vessel_1_rec_complete == "yes": ## If all steps completed
				showStatusMsg("vessel_1_rec_complete")
				oid = int(page.client_storage.get("order_id"))
				cur = completed_orderid(oid)
				if cur == 1:
					page.client_storage.set("end","1")
					r.set("vessel1_comp","no")
					page.clean()
					page.appbar.disabled = False
					image_completed = ft.Image(src="https://static.vecteezy.com/system/resources/thumbnails/010/985/457/small_2x/gold-volumetric-3d-text-balloons-thank-you-cut-out-png.png",
										width=400,
										height=400,
										fit=ft.ImageFit.CONTAIN
										)
					completed_text = ft.Text(
											value=f"{recipe_name} Completed...Enjoy the Drink",
											size=35,
											color=ft.colors.BLUE,
											font_family="RobotoSlab",
											weight=ft.FontWeight.W_700,
										)
					
					mix_text = ft.Text(
											value=f"Give it a good mix before sipping",
											size=25,
											color=ft.colors.BLUE,
											font_family="RobotoSlab",
											weight=ft.FontWeight.W_600,
										)
					completed = ft.Column(
							spacing=10,
							scroll=ft.ScrollMode.ALWAYS,
							controls=[
								image_completed,
								completed_text,
								mix_text,
								ft.ResponsiveRow(
									[

									],
								),
							],
							horizontal_alignment=ft.CrossAxisAlignment.CENTER,
								)
					page.add(
						ft.ResponsiveRow(
						[
						ft.Column(
							
							[
								completed,
								# display_footer(),
							],
						alignment= ft.MainAxisAlignment.CENTER,
						spacing = 10,
						scroll=ft.ScrollMode.ALWAYS,
						on_scroll_interval=0,
						),
						],
						alignment= ft.MainAxisAlignment.CENTER,
						spacing = "spaceBetween"
						),
							)
					page.client_storage.remove("order_id")
					page.client_storage.set("end","1")
					page.update()

		except Exception as e:
			print(e)

	recipe_time = getrecipetime(recipe_id)
	recipe_name = getrecipename(recipe_id)

	## Recipe name Text Component
	new_task = ft.Text(
		f"Order Confirmed - Preparing the {recipe_name}",
		size=40,
		color=ft.colors.BLACK,
		font_family="RobotoSlab",
		weight=ft.FontWeight.W_500,
	)
	
	tasks = ft.Column()

	## Recipe Cooking progress Bar
	pr = ft.ProgressBar(height=10,value=0.05,color="green")

	## Recipe cooking percentage text 
	stack = ft.Text(
		value=f"{recipe_name} will be Out in {recipe_time} secs",
		size=24,
		color=ft.colors.GREEN,
		font_family="RobotoSlab",
		weight=ft.FontWeight.W_700,
	)

	## Gif Loader
	img = ft.Image(src="https://media.baamboozle.com/uploads/images/120763/1649326640_44612_gif-url.gif",
		width=200,
		height=200,
		fit=ft.ImageFit.CONTAIN
		)

	## Page Heading
	fl = ft.Row(
		ft.Text(value="Cooking Progress", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
		alignment=ft.MainAxisAlignment.CENTER,
	),
	
	## Async function starts the task of calling refresh function
	async def functhatcallsabovefuncevery10s(func):
		# global end
		end = page.client_storage.get("end")
		print("in refresh async")
		showStatusMsg("in refresh async")
		while end == "0":
			func()
			showStatusMsg("functhatcallsabovefuncevery5s")
			await asyncio.sleep(5)
			end = page.client_storage.get("end")
	
	## Aligning all the components in columnwise for first tab
	cont = ft.Column(
					spacing=10,
					scroll=ft.ScrollMode.ALWAYS,
					controls=[
						new_task, 
						img,
						pr,
						stack,
						tasks,
						ft.ResponsiveRow(
							[

							],
						),
					],
					horizontal_alignment=ft.CrossAxisAlignment.CENTER,
						)

	## Adding components to the page
	page.add(
		ft.ResponsiveRow(
				[
				 ft.Column(
					
					[
						cont,
						# display_footer(),
					],
				alignment= ft.MainAxisAlignment.CENTER,
				spacing = 10,
				scroll=ft.ScrollMode.ALWAYS,
				on_scroll_interval=0,
				 ),
				],
				alignment= ft.MainAxisAlignment.CENTER,
				spacing = "spaceBetween"
				),
	)
	
	page.update()

	# now = datetime.now()


	## After updating the page, Refresh task will start 
	task =asyncio.run(functhatcallsabovefuncevery10s(func= refresh))
