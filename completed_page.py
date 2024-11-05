from imports import *
from db_retrieve import *

def redis_connection7(ips):
	try:
		global r
		r = redis.Redis()
		r = redis.Redis(host=ips,port=6380)
	except Exception as e :
		print(f"The error is redis error {e}")
		redis_connection7("100.106.178.97")

def completedPage(page : ft.Page,vid):

    page.client_storage.set("current","completed_page")

    if vid == 1:
        vessel1_id = extract_recipe_id(1)
        vessel1_recipe = getrecipename(vessel1_id)
        vessel1_oid = extract_order_id(1)
        r.set("vessel1_comp","no")
    
    if vid == 2:
        vessel1_id = extract_recipe_id(2)
        vessel1_recipe = getrecipename(vessel1_id)
        vessel1_oid = extract_order_id(2)
        r.set("vessel2_comp","no")
    
    page.clean()
    page.appbar.disabled = False
    image_completed = ft.Image(src="https://static.vecteezy.com/system/resources/thumbnails/010/985/457/small_2x/gold-volumetric-3d-text-balloons-thank-you-cut-out-png.png",
                        width=400,
                        height=400,
                        fit=ft.ImageFit.CONTAIN
                        )
    order_text = ft.Text(
                            value=f"Order Numer : {vessel1_oid} - Completed",
                            size=35,
                            color=ft.colors.BLUE,
                            font_family="RobotoSlab",
                            weight=ft.FontWeight.W_700,
                        )
    completed_text = ft.Text(
                            value=f"{vessel1_recipe} Completed...Enjoy your Food",
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
                order_text,
                completed_text,
                # mix_text,
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