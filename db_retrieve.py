from imports import *

def connection(ips):
    try:
        global con
        con = pg8000.native.Connection(host = ips, user="postgres", password="mysecretpassword",port="5433", database="test_recipe")
    
    except Exception as e :
        print(f"The error is {e}")
        connection("100.106.178.97")
        # pass

scid ={}
pcid ={}
v1lcid={}
v2lcid={}
v3lcid={}
v4lcid={}


def recnames():
   records = con.run("SELECT recipe_name FROM recipe_list  WHERE recipe_id > 222 ORDER BY recipe_id  ASC LIMIT 1000")
   return records

def dbextractRecipeList():
    try:
        records = con.run("SELECT recipe_id, recipe_name, description, image_url, veg_non_veg, price, available, image_greyscale FROM recipe_list  WHERE recipe_id > 245 ORDER BY recipe_id  ASC LIMIT 1000")
        return records
    
    except Exception as e :
        print(f"The error is {e}")
        pass

def ext_coll_recipes(coll):
    try:
        records = con.run("SELECT recipe_id, recipe_name, description, image_url, veg_non_veg, collection FROM recipe_list WHERE recipe_id > 222 ORDER BY recipe_id")
        return records
    except Exception as e :
        print(f"The error is {e}")
        pass


def getrecipenames(start):
    try:
        records = con.run(f"SELECT recipe_id, recipe_name, description, image_url, veg_non_veg FROM recipe_list  WHERE recipe_name  LIKE 'S%'")
        return records
    except Exception as e :
        print(f"The error is {e}")
        pass

def extractRecipeId(recipe_name):
    try:
        print('Extracting Recipe id from Db')
        records = con.run("SELECT * FROM recipe_list where recipe_name = '"+str(recipe_name)+"'  ORDER BY recipe_id ASC")
        print(records)
        for record in records:
            print("Printing ID = ", end='')
            print(record[0])
            return record[0]
        
    except Exception as e :
        print(f"The error is {e}")
        pass


def extractRecipeAvailable(recipe_name):
    try:
        print('Extracting Recipe id from Db')
        records = con.run("SELECT * FROM recipe_list where recipe_name = '"+str(recipe_name)+"'  ORDER BY recipe_id ASC")
        print(records)
        for record in records:
            print("Printing ID = ", end='')
            print(record[10])
            return record[10]
        
    except Exception as e :
        print(f"The error is {e}")
        pass


def getrecipeid():
    try:
        records = con.run("SELECT * FROM recipe_step ORDER BY step_no  DESC")
        # #records = cursor.fetchall()
        if len(records) != 0:
            print(records)
            return records[0][18]
        if len(records) == 0:
            return 0
    except Exception as e :
        print(f"The error is {e}")
        pass

def getrecipedescription(recipe_id):
    try:
        records = con.run("SELECT * FROM recipe_list  where recipe_id = '"+str(recipe_id)+"'")
        print(records[0][2])
        return records[0][2]
    except Exception as e :
        print(f"The error is {e}")
        pass

def getrecipeimage(recipe_id):
    try:
        records = con.run("SELECT * FROM recipe_list  where recipe_id = '"+str(recipe_id)+"'")
        print(records[0][5])
        return records[0][5]
    
    except Exception as e :
        print(f"The error is {e}")
        pass


def getrecipeprice(recipe_id):
    try:
        records = con.run("SELECT * FROM recipe_list  where recipe_id = '"+str(recipe_id)+"'")
        print(records[0][8])
        return records[0][8]
    
    except Exception as e :
        print(f"The error is {e}")
        pass

def getrecipetime(recipe_id):
    try:
        records = con.run("SELECT * FROM recipe_list  where recipe_id = '"+str(recipe_id)+"'")
        print(records[0][9])
        return records[0][9]
    
    except Exception as e :
        print(f"The error is {e}")
        pass

def getrecipename(recipe_id):
    rid = recipe_id
    try:
        print(f"recipe_id= {rid}")
        records = con.run(f"SELECT * FROM recipe_list  where recipe_id = {rid}")
        print(records[0][1])
        return records[0][1]
    
    except Exception as e :
        print(f"The error is recipename {e}")
        connection("100.106.178.97")
        getrecipename(rid)
        pass

def get_ingredients():
  try:
    print("Entered Extraxting recipe_step")
    records = con.run(f"SELECT ingredient_name, quantity FROM cups")
    print(type(records))
    return records
  
  except Exception as e :
        print(f"The error is {e}")
        pass

def getingcup(n):
    try:
        print("Entered Extraxting recipe_step")
        records = con.run(f"SELECT ingredient_name, quantity FROM cups where cup_id = '"+str(n)+"'")
        print(type(records))
        return records
    
    except Exception as e :
        print(f"The error is {e}")
        pass

def progress_percent(vid):
  
  try:
    pro = 0
    records = con.run("SELECT * FROM recipe_step ORDER BY step_no ASC")
    if (len(records) != 0):
        total_step = len(records)
        records1 = con.run(f"SELECT * FROM recipe_step where status = '3' and vessel_id = '{vid}' ORDER BY step_no ASC")
        #   #records = cursor.fetchall() 
        if (len(records1) != 0):
            completed_steps = len(records1)
            progress_percent1 = (completed_steps/total_step) * 100
            perc = int(progress_percent1)
            return perc

    if (len(records) == 0):
        perc = 0
        return perc
    
    if (len(records1) == 0):
        perc = 5
        return perc
    
  except Exception as e :
    print(f"The error is progress percent{e}")
    connection("100.106.178.97")
    progress_percent()
    pass


def progress_step(vessel):
  try:
    records = con.run(f"SELECT status, type, customization FROM recipe_step where vessel_id = "+str(vessel)+" ORDER BY step_no ASC")
    if len(records)!= 0:
        return records
  except Exception as e :
    print(f"The error is {e}")
    pass

def getmanualstep():
    try:
        records = con.run("SELECT vessel_id, ingredient_name, quantity FROM recipe_step where (type = 'Manual') AND (status = '2') ORDER BY step_no ASC LIMIT 1")
        if len(records)!= 0:
            return records
    except Exception as e :
        print(f"The error is {e}")
        pass



def getmanualing():
    try:
        records = con.run("SELECT ingredient_name FROM recipe_step where (type = 'Manual') AND (status = '2') ORDER BY step_no ASC")
        if len(records)!= 0:
            return records
        
    except Exception as e :
        print(f"The error is {e}")
        pass

def getmanualquantity():
    try:
        records = con.run("SELECT quantity FROM recipe_step where (type = 'Manual') AND (status = '2') ORDER BY step_no ASC")
        if len(records)!= 0:
            return records
        
    except Exception as e :
        print(f"The error is {e}")
        pass

def check_recipe_step(vessel):
    try:
        records = con.run("SELECT * FROM recipe_step where (type = 'Cook' and vessel_id = "+str(vessel)+")")
        if len(records)!= 0:
            return 1
        if len(records)== 0:
            return 0
    
    except Exception as e :
        print(f"The error is {e}")
        pass



def check_ing_db():
    try:
        records = con.run("SELECT type FROM recipe_step where (status = '0') OR (status = '2') or (status = '1')")
        if len(records)!= 0:
            return 1
        if len(records)== 0:
            return 0
    
    except Exception as e :
        print(f"The error is {e}")
        pass




def get_rec_step():
    try:
        records = con.run("SELECT type FROM recipe_step where (status = '0') OR (status = '2') or (status = '1') or (status = '3') or (status = '-2')")
        if len(records)!= 0:
            return 1
        if len(records)== 0:
            return 0

    except Exception as e :
        print(f"The error is {e}")
        pass


def check_recipe_start(vessel):
    try:
        records = con.run("SELECT type FROM recipe_step where (status = '-2' and vessel_id = "+str(vessel)+")")
        if len(records)!= 0:
            return 1
        if len(records)== 0:
            return 0
    
    except Exception as e :
        print(f"The error is {e}")
        pass



def ckeckList(lst):

    try:
        ele = -2
        chk = True
        # Comparing each element with -2 value 
        for item in lst:
            if ele != item:
                chk = False
                break
                
        if (chk == True): print("Equal") ; return 0
        else: print("Not equal")   ;  return 1
    
    except Exception as e :
        print(f"The error is {e}")
        pass
    

def pauseorStart(vid):
    try:
        records = con.run(f"SELECT * FROM recipe_step where vessel_id = {vid}")
        iteration = len(records)
        checklist =[]
        for i in range(iteration) :
            checklist.append(records[i][12])
        x = ckeckList(checklist)
        print(f"value of x == {x}")
        if x == 0 :
            print(f"Recipe for Vessel == {vid} starting from the -----Start------")
            return 0 # recipie starting from from start
        if x == 1 :
            print(f"Recipe for Vessel == {vid} starting from the -------Middle--------- ")
            return 1 # recipe starting from middle
   
    except Exception as e :
        print(f"The error is {e}")
        pass




def parseRecipeUI(rid):

    global recipe_id
    recipe_id = rid
    con.run(f'TRUNCATE TABLE public.recipe_view')
    records = con.run(f"SELECT * FROM recipe_list where recipe_id = {rid}")
    print(records[0][3])
    data = records[0][3]
    liquids = []
    solids = []
    powders = []
    cookingtime = 0
   
    vstart = 0
    
  
    block = 0
    j = 1
    for i in range(len(data)):
        try:
            # print(f'key is{data[i]}')
            for k, v in data[i].items():
                if k == "AT_Get_Liquid":
                    print(
                        f'get liquid ingredient {v["title"]} of {v["quantity"]} gms')
                    liquids.append(v["title"])
                    # f =int(v["quantity"])
                    ing_id = int(v["id"])
                    weight = float(float(v["quantity"])/1000)
                    records = con.run(f"SELECT * FROM ingredient_table where ingredient_type = 'Liquid' AND ingredient_id = {ing_id}")
                    #records = cursor.fetchall()
                    ing_name = str(records[0][1])
                    # records = con.run(f'INSERT INTO public.recipe_step (oid, step_no, type, block, vessel_id, ingredient_name, container_id, quantity, induction, "time", lid, spin_every, status, percent,manual, ingredient_id, actual_weight) VALUES ({oid}, {j+vstart}, \'Liquid\', {block}, {ves},\'{str(ing_name)}\', 0, {weight}, 0, 0, 0, 0, -2, 0, 0, {ing_id}, 0);')

                    con.run(f'INSERT INTO public.recipe_view ( step_no, type, ingredient_name, quantity) VALUES ({j+vstart}, \'Liquid\', \'{str(ing_name)}\', \'{str(weight)+str(" Kilograms")}\');')
                    # records = con.run(f'INSERT INTO public.procurement_plan_meta (  type, ingredient_name, quantity) VALUES ( \'Liquid\', \'{str(ing_name)}\', \'{str(weight)}\');')
                    j = j+1

                if k == "AT_Get_Powder":
                    print(
                        f'get powder ingredient {v["title"]} of {v["quantity"]} gms')
                    powders.append(v["title"])
                    total_weight = float(float(v["quantity"])/1000)
                    print(f"Total weight is {total_weight}")
                    ing_id = int(v["id"])
                    records = con.run(f"SELECT * FROM ingredient_table where ingredient_type = 'Powder' AND ingredient_id = {ing_id}")
                    #records = cursor.fetchall()
                    print(records)
                    ing_name = records[0][1]
                    print(f"Ingredient name is {ing_name}")
                    if (len(records) != 0):
                      fill_percent = records[0][5]
                      fill_quantity = records[0][7]
                      print(f"the quantity of {fill_quantity} of {ing_name} will get filled to {fill_percent}")
                      a = float(total_weight/fill_quantity)
                      b = float(a * fill_percent)
                      c = float(b / 75)
                      if (c < 1):
                        d = 1
                        print(f"total trips needed for the {ing_name} is {d}")
                      if (c >= 1):
                        d = round(c)
                        print(f"total trips needed for the {ing_name} is {d}")

                      percent  = b/d
                      print(f"The Expected percent value in one cup is {percent}")
        
                      div_quantity = float(total_weight)
                      con.run(f'INSERT INTO public.recipe_view ( step_no, type, ingredient_name, quantity) VALUES ({j+vstart}, \'Powder\', \'{str(ing_name)}\', \'{str(div_quantity)+str(" Kilograms")}\');')
                      j = j+1
                      e = 0
                

                if k == "AT_Get_Solid":
                    print(
                        f'get solid ingredient {v["title"]} of {v["quantity"]} gms')
                    solids.append(v["title"])
                    total_weight = float(float(v["quantity"])/1000)
                    print(f"Total weight is {total_weight}")
                    ing_id = int(v["id"])
                    records = con.run(f"SELECT * FROM ingredient_table where ingredient_type = 'Solid' AND ingredient_id = {ing_id}")
                    #records = cursor.fetchall()
                    print(records)
                    ing_name = records[0][1]
                    print(f"Ingredient name is {ing_name}")
                    if (len(records) != 0):
                      fill_percent = records[0][5]
                      fill_quantity = records[0][7]
                      print(f"the quantity of {fill_quantity} of {ing_name} will get filled to {fill_percent}")
                      a = float(total_weight/fill_quantity)
                      b = float(a * fill_percent)
                      c = float(b / 75)
                      if (c < 1):
                        d = 1
                        print(f"total trips needed for the {ing_name} is {d}")
                      if (c >= 1):
                        d = round(c)
                        print(f"total trips needed for the {ing_name} is {d}")

                      percent  = b/d
                      print(f"The Expected percent value in one cup is {percent}")
                      div_quantity = float(total_weight)
                      con.run(f'INSERT INTO public.recipe_view ( step_no, type, ingredient_name, quantity) VALUES ({j+vstart}, \'Solid\', \'{str(ing_name)}\', \'{str(div_quantity)+str(" Kilograms")}\');')
                      j = j+1
                      #Adding in database
                      e = 0
                      # while(e < d): 
                      #   # records = con.run(f'INSERT INTO public.recipe_step (oid, step_no, type, block, vessel_id, ingredient_name, container_id, quantity, induction, "time", lid, spin_every, status, percent, manual, ingredient_id, actual_weight) VALUES ({oid}, {j+vstart}, \'Solid\', {block}, {ves}, \'{str(ing_name)}\', 0, {div_quantity}, 0, 0, 0, 0, -2, {percent}, 0, {ing_id}, 0);')
                      #   records = con.run(f'INSERT INTO public.recipe_view ( step_no, type, ingredient_name, quantity) VALUES ({j+vstart}, \'Solid\', \'{str(ing_name)}\', \'{str(div_quantity)+str(" Kilograms")}\');')
                      #   # records = con.run(f'INSERT INTO public.procurement_plan_meta (  type, ingredient_name, quantity) VALUES ( \'Solid\', \'{str(ing_name)}\', \'{str(div_quantity)}\');')
                      #   print(j)
                      #   j = j+1
                      #   print("Adding solid row")
                      #   e = e + 1

                if k == "AT_Start_Cooking":
                    stir_every = 0
                    print(
                        f'Cooking at {v["temperature"]} temperature for {v["time"]} seconds', sep='')
                    secs = int(v["time"])
                    if "lid" in v:
                        print(
                            f' with Lid {"closed" if v["lid"] else "open"}', sep='')
                        if (v["lid"] == False):
                          lid = 1
                        if (v["lid"] == True):
                          lid = 0
                        print(f"the Stirrer value is {lid}")
                        # sleep(1)
                    if "spin" in v:
                        print(
                            f' also Stirrer {"TO SPIN" if v["spin"] else "NO SPIN"}', sep='')
                        if (v["spin"] == False):
                          spin = 0
                        if (v["spin"] == True):
                          spin = 1
                        print(f"the spin value is {lid}")  
                    
                    if "speed" in v:
                        print(
                            f' with speed as {"NONE" if v["speed"]== None else v["speed"]}', sep='')
                    if "stir_every" in v:
                        print(f' for every {v["stir_every"]} secs')

                        stir_every = int(v["stir_every"])
                        if (stir_every < secs):
                            lid = 0

                    if (int(v["temperature"]) == 60 or int(v["temperature"]) == 1):
                        temp = 1
                    if (int(v["temperature"]) == 100 or int(v["temperature"]) == 2):
                        temp = 2
                    if (int(v["temperature"]) == 130 or int(v["temperature"]) == 3):
                        temp = 3
                    if (int(v["temperature"]) == 160 or int(v["temperature"]) == 4):
                        temp = 4
                    if (int(v["temperature"]) == 180 or int(v["temperature"]) == 5):
                        temp = 5
                    if (int(v["temperature"]) == 200 or int(v["temperature"]) == 6):
                        temp = 6
                    if (int(v["temperature"]) == 220 or int(v["temperature"]) == 7):
                        temp = 7
                    if (int(v["temperature"]) == 240 or int(v["temperature"]) == 8):
                        temp = 8

                    if (secs >= 0):
                        # records = con.run(f'INSERT INTO public.recipe_step (oid, step_no, type, block, vessel_id, ingredient_name, container_id, quantity, induction, "time", lid, spin_every, status, percent, manual, ingredient_id, actual_weight) VALUES ({oid}, {j+vstart}, \'Cook\', {block}, {ves}, \'Cook\', 0, 0, {temp}, {secs},{lid}, {stir_every}, -2, 0, 0, 0, 0);')
                      
                        
                        con.run(f'INSERT INTO public.recipe_view ( step_no, type, ingredient_name, quantity) VALUES ({j+vstart}, \'Cook\', \'{"Ind Level : "+str(temp)+" Lid : "+str(lid)+""+" SE(sec): "+str(stir_every)+""}\', \'{str(secs)+str(" Seconds")}\');')
                        
                        # print(f' also Stirrer {"TO SPIN" if v["spin"] else "NO SPIN"} with speed as {v["speed"]} for every {v["stir_every"]} secs')
                        cookingtime = cookingtime + int(v['time'])
                        j = j+1
                        block = block + 1

        except KeyError:
            print("KEY ERROR")
            print("[red]KEY ERROR[/] while [bold magenta]Parsing[/]!")
            print(data[i])
            pass
    print(
        f'Total cooking time is {cookingtime} seconds or {cookingtime/60} minutes')
    print(f'Liquids Used are')
    print(liquids)
    print(f'Solids Used are')
    print(solids)
    print(f'Powders Used are')
    print(powders)
    print("AUTO-ASSIGNING CONTAINERS to Ingredients")
 
def recipe_view():

    try:
        records = con.run("Select * FROM recipe_view ORDER BY step_no ASC")
        return records
    
    except Exception as e :
        print(f"The error is {e}")
        pass

def vessel1_step():
    try:
        records = con.run("Select step_no, type, ingredient_name, container_id, quantity, time, spin_every FROM recipe_step WHERE vessel_id = 1 ORDER BY step_no ASC")
        return records
    except Exception as e :
        print(f"The error is {e}")
        pass

def vessel2_step():
    try:
        records = con.run("Select step_no, type, ingredient_name, container_id, quantity, time, spin_every FROM recipe_step WHERE vessel_id = 2 ORDER BY step_no ASC")
        return records
    
    except Exception as e :
        print(f"The error is {e}")
        pass

def vessel3_step():
    try:
        records = con.run("Select step_no, type, ingredient_name, container_id, quantity, time, spin_every FROM recipe_step WHERE vessel_id = 3 ORDER BY step_no ASC")
        return records
    
    except Exception as e :
        print(f"The error is {e}")
        pass

def vessel4_step():
    try:
        records = con.run("Select step_no, type, ingredient_name, container_id, quantity, time, spin_every FROM recipe_step WHERE vessel_id = 4 ORDER BY step_no ASC")
        return records
    
    except Exception as e :
        print(f"The error is {e}")
        pass


def edit_ing_step(step_no,value):
    try:
        i = int(value)
        i = i/1000
        con.run(f"UPDATE recipe_step SET quantity = {i} where step_no = {step_no}")
        con.run(f"UPDATE recipe_step SET customization = 'true' where step_no = {step_no}")
    
    except Exception as e :
        print(f"The error is {e}")
        pass

def edit_cook_step(step_no,value):
    try:
        i = int(value)
        con.run(f"UPDATE recipe_step SET time = {i} where step_no = {step_no}")
        con.run(f"UPDATE recipe_step SET customization = 'true' where step_no = {step_no}")
    
    except Exception as e :
        print(f"The error is {e}")
        pass



def set_manual_db(step_no):
    try:
        con.run(f"UPDATE recipe_step SET type = 'Manual' where step_no = {step_no}")
    
    except Exception as e :
        print(f"The error is {e}")
        pass


def get_ing_id(step_no):
    try:
        records = con.run(f"Select ingredient_id FROM recipe_step WHERE step_no = {step_no}")
        return records
    
    except Exception as e :
        print(f"The error is {e}")
        pass

def set_automatic_db(step_no,ing):
    try:
        con.run(f"UPDATE recipe_step SET type = '{ing}' where step_no = {step_no}")
    
    except Exception as e :
        print(f"The error is {e}")
        pass


def get_ing_list(ing_type):
    try:
        records = con.run(f"SELECT ingredient_name FROM ingredient_table WHERE ingredient_type = '{ing_type}'")
        return records
    
    except Exception as e :
        print(f"The error is {e}")
        pass


def solid_container_mapping_getdb(cid):
  try:
    print("Going to get Solid Container Mapping from db ")
    records = con.run("SELECT * FROM solid_container_mapping")
    print(cid)
    records = con.run("SELECT * FROM solid_container_mapping WHERE solid_container_number = '"+str(cid)+"' ")
    #records = cursor.fetchall()
    print(records[0][1])
    solid_container_mapping_getdb_value = records[0][1]
    # solid_container_mapping_getdb_list.append(solid_container_mapping_getdb_value)
    return solid_container_mapping_getdb_value
  except Exception as e :
        print(f"The error is {e}")
        pass
  

def solid_current_weight_extract(cid):
  try:
    print("Going to extract solid current weight")
    records = con.run(f"SELECT * FROM solid_tare_refresh_weights WHERE container_number = '"+str(cid)+"'")
    #records = cursor.fetchall()
    print(records)
    print(records[0][3])

    return [float(records[0][3]),float(records[0][2])] # load cell current weight from db
  
  except Exception as e :
        print(f"The error is {e}")
        pass
  

def updateSolidContainer():
    print("Entered Updating Solid Container")
    x = len(scid)  # Scid is no of solid containers
    print(x)
    while (x >0):
        try:
            if (x==0):
                return
                
            for i in scid :
                print(f'value of i is {i}') 
                print(scid[i])
                x -= 1
                print(f"value of x is {x}")
                con.run("SELECT * FROM recipe_step")

                con.run("UPDATE public.recipe_step SET container_id = "+str(i)+" WHERE ingredient_name = '"+str(scid[i])+"' and type = 'Solid' ")     
                
                print(f"Container ID Update for {i} for ingredient {scid[i]} is success")
                
                # ingredient_name
                ingredient_name = scid[i]
                print(f"Ingredient name = {ingredient_name}")
                # ingredient id 
                records = con.run("SELECT ingredient_id FROM ingredient_table WHERE ingredient_name = '"+str(ingredient_name)+"'")
                #records = cursor.fetchall()
                ingredient_id = records[0][0]
                print(f"Ingredient id = {ingredient_id}")

                con.run("SELECT * FROM solid_container_mapping")
                con.run("UPDATE public.solid_container_mapping SET ingredient_name = '"+str(ingredient_name)+"'  WHERE solid_container_number = '"+str(i)+"' ")     
                con.run("UPDATE public.solid_container_mapping SET ingredient_id = '"+str(ingredient_id)+"'  WHERE solid_container_number = '"+str(i)+"' ")     
                con.run("UPDATE public.solid_container_mapping SET last_updated = now()  WHERE solid_container_number = '"+str(i)+"' ")     
                
        except Exception as error1 :
            print("Solid Ingredient Not in the Current Recipe")
            print(error1)
    print("updating Solid Containers is success")



def powder_container_mapping_getdb(cid):
  
  try:
    print("Going to get powder Container Mapping from db ")
    con.run("SELECT * FROM powder_container_mapping")
    print(cid)
    records = con.run("SELECT * FROM powder_container_mapping WHERE powder_container_number = '"+str(cid)+"' ")
    #records = cursor.fetchall()
    print(records[0][1])
    powder_container_mapping_getdb_value = records[0][1]
    return powder_container_mapping_getdb_value
  
  except Exception as e :
        print(f"The error is {e}")
        pass

def extractrecipe_yeild():
    try:
        yeild_list = []
        print("Entered Extraxting total yeild from recipe_view")
        records = con.run(f"SELECT quantity FROM recipe_view WHERE type = 'Solid' or type = 'Powder' or type = 'Liquid'")
        #records = cursor.fetchall()
        print(type(records))
        print(len(records))
        print(records)
        x = "1 1"
        y = x.split()
        print(y)
        print(y[0])
        for record in records :
            print(record[0])
            record = record[0]
            y = record.split()
            yeild_list.append(float(y[0]))

        print(yeild_list)
        total_weight = sum(yeild_list)
        print(total_weight)
        return total_weight
    
    except Exception as e :
        print(f"The error is {e}")
        pass




def updatePowderContainer():
    
    print("Entered Powder Container Updating")
    x = len(pcid)
    print(x)
    while (x >0):
        try:
            if (x==0):
                return
                
            for i in pcid : # Here i is container id and pcid[i] is ingrdient name (refer gui.py line - 3352)
                print(pcid[i])
                x -= 1
                print(f"value of x is {x}")
                con.run("SELECT * FROM recipe_step")
                con.run("UPDATE public.recipe_step SET container_id = "+str(i)+" WHERE ingredient_name = '"+str(pcid[i])+"' and type = 'Powder' ")     
                print(f"Container ID Update for {i} for ingredient {pcid[i]} is success  type = Powder ")


                # ingredient_name
                ingredient_name = pcid[i]
                print(f"Ingredient name = {ingredient_name}")
                # ingredient id 
                # ingredient_id = dbpowder_ingdict[ingredient_name]  # here dbpowder_ingdict contains ing_name:ing_id
                records = con.run("SELECT ingredient_id FROM ingredient_table WHERE ingredient_name = '"+str(ingredient_name)+"'")
                #records = cursor.fetchall()
                ingredient_id = records[0][0]

                print(f"Ingredient id = {ingredient_id}")

                con.run("SELECT * FROM powder_container_mapping")
                con.run("UPDATE public.powder_container_mapping SET ingredient_name = '"+str(ingredient_name)+"'  WHERE powder_container_number = '"+str(i)+"' ")     
                con.run("UPDATE public.powder_container_mapping SET ingredient_id = '"+str(ingredient_id)+"'  WHERE powder_container_number = '"+str(i)+"' ")     
                con.run("UPDATE public.powder_container_mapping SET last_updated = now()  WHERE powder_container_number = '"+str(i)+"' ")     
                

        except Exception as error1 :
            print("Powder Ingredient Not in the Current Recipe")
            print(error1)
    print("updating Powder Containers is success")


def liquid_container_mapping_getdb(cid):
    try:
        print("Going to get liquid Container Mapping from db ")
        con.run("SELECT * FROM liquid_container_mapping")
        print(cid)
        records = con.run("SELECT * FROM liquid_container_mapping WHERE liquid_container_number = '"+str(cid)+"' ")
        print(records[0][1])
        liquid_container_mapping_getdb_value = records[0][1]
        return liquid_container_mapping_getdb_value

    except Exception as e :
        print(f"The error is {e}")
        pass


def updateV1LiquidContainer():
    # global liquid_inglist
    # checkv1LiquidIngredientExist() 
    # v1lcid["1"]
    x = len(v1lcid)
    print(x)
    while (x >0):
        try:
            if (x==0):
                return
                
            for i in v1lcid :
                print(v1lcid[i])
                x -= 1
                print(f"value of x is {x}")
                con.run("SELECT * FROM recipe_step")
                con.run("UPDATE public.recipe_step SET container_id = "+str(i)+" WHERE ingredient_name = '"+str(v1lcid[i])+"' and type = 'Liquid' and vessel_id = 1")     
                print(f"Container ID Update for {i} for ingredient {v1lcid[i]} is success  type = Liquid for v1")




                # ingredient_name
                ingredient_name = v1lcid[i]
                print(f"Ingredient name = {ingredient_name}")
                # ingredient id 
                records = con.run("SELECT ingredient_id FROM ingredient_table WHERE ingredient_name = '"+str(ingredient_name)+"'")
                #records = cursor.fetchall()
                ingredient_id = records[0][0]
                print(f"Ingredient id = {ingredient_id}")

                con.run("SELECT * FROM liquid_container_mapping")
                con.run("UPDATE public.liquid_container_mapping SET ingredient_name = '"+str(ingredient_name)+"'  WHERE liquid_container_number = '"+str(i)+"' ")     
                con.run("UPDATE public.liquid_container_mapping SET ingredient_id = '"+str(ingredient_id)+"'  WHERE liquid_container_number = '"+str(i)+"' ")     
                con.run("UPDATE public.liquid_container_mapping SET last_updated = now()  WHERE liquid_container_number = '"+str(i)+"' ")     
                


        except Exception as error1 :
            print("Liquid Ingredient Not in the Current Recipe for vessel 1")
            print(error1)
    print("updating Liquid Containers is success for vessel 1")


# Liquid containers of vessel 2 updating in the recipe_step Table
def updateV2LiquidContainer():
    x = len(v2lcid)
    print(x)
    while (x >0):
        try:
            if (x==0):
                return
                
            for i in v2lcid :
                print(v2lcid[i])
                x -= 1
                print(f"value of x is {x}")
                con.run("SELECT * FROM recipe_step")
                con.run("UPDATE public.recipe_step SET container_id = "+str(i)+" WHERE ingredient_name = '"+str(v2lcid[i])+"' and type = 'Liquid' and vessel_id = 2 ")     
                print(f"Container ID Update for {i} for ingredient {v2lcid[i]} is success  type = Liquid for v2")


                # ingredient_name
                ingredient_name = v2lcid[i]
                print(f"Ingredient name = {ingredient_name}")
                # ingredient id 
                records = con.run("SELECT ingredient_id FROM ingredient_table WHERE ingredient_name = '"+str(ingredient_name)+"'")
                #records = cursor.fetchall()
                ingredient_id = records[0][0]
                print(f"Ingredient id = {ingredient_id}")

                con.run("SELECT * FROM liquid_container_mapping")
                con.run("UPDATE public.liquid_container_mapping SET ingredient_name = '"+str(ingredient_name)+"'  WHERE liquid_container_number = '"+str(i)+"' ")     
                con.run("UPDATE public.liquid_container_mapping SET ingredient_id = '"+str(ingredient_id)+"'  WHERE liquid_container_number = '"+str(i)+"' ")     
                con.run("UPDATE public.liquid_container_mapping SET last_updated = now()  WHERE liquid_container_number = '"+str(i)+"' ")     
                

                # if str(v2lcid[i]) in liquid_inglist1 :
                #     print(f"Ingredient <<<<<< {str(v2lcid[i])} >>>>>> Exist in the recipe type = Liquid for v2")
                # else :
                #     print(f"Ingredient <<<<<< {str(v2lcid[i])} >>>>> Not Exist in the recipe type = Liquid for v2")

        except Exception as error1 :
            print("Liquid Ingredient Not in the Current Recipe")
            print(error1)
    print("updating Liquid Containers is success for vessel 2")



# Liquid containers of vessel 3 updating in the recipe_step Table
def updateV3LiquidContainer():
    
    x = len(v3lcid)
    print(x)
    while (x >0):
        try:
            if (x==0):
                return
                
            for i in v3lcid :
                print(v3lcid[i])
                x -= 1
                print(f"value of x is {x}")
                con.run("SELECT * FROM recipe_step")
                con.run("UPDATE public.recipe_step SET container_id = "+str(i)+" WHERE ingredient_name = '"+str(v3lcid[i])+"' and type = 'Liquid' and vessel_id = 3 ")     
                print(f"Container ID Update for {i} for ingredient {v3lcid[i]} is success  type = Liquid for v3")


                # ingredient_name
                ingredient_name = v3lcid[i]
                print(f"Ingredient name = {ingredient_name}")
                # ingredient id 
                records = con.run("SELECT ingredient_id FROM ingredient_table WHERE ingredient_name = '"+str(ingredient_name)+"'")
                #records = cursor.fetchall()
                ingredient_id = records[0][0]
                print(f"Ingredient id = {ingredient_id}")

                con.run("SELECT * FROM liquid_container_mapping")
                con.run("UPDATE public.liquid_container_mapping SET ingredient_name = '"+str(ingredient_name)+"'  WHERE liquid_container_number = '"+str(i)+"' ")     
                con.run("UPDATE public.liquid_container_mapping SET ingredient_id = '"+str(ingredient_id)+"'  WHERE liquid_container_number = '"+str(i)+"' ")     
                con.run("UPDATE public.liquid_container_mapping SET last_updated = now()  WHERE liquid_container_number = '"+str(i)+"' ")     
                

        except Exception as error1 :
            print("Liquid Ingredient Not in the Current Recipe")
            print(error1)

    print("updating Liquid Containers is success for vessel 3")



# Liquid containers of vessel 4 updating in the recipe_step Table
def updateV4LiquidContainer():
    
    x = len(v4lcid)
    print(x)
    while (x >0):
        try:
            if (x==0):
                return
                
            for i in v4lcid :
                print(v4lcid[i])
                x -= 1
                print(f"value of x is {x}")
                con.run("SELECT * FROM recipe_step")
                con.run("UPDATE public.recipe_step SET container_id = "+str(i)+" WHERE ingredient_name = '"+str(v4lcid[i])+"' and type = 'Liquid' and vessel_id = 4 ")     
                print(f"Container ID Update for {i} for ingredient {v4lcid[i]} is success  type = Liquid for v4")


                # ingredient_name
                ingredient_name = v4lcid[i]
                print(f"Ingredient name = {ingredient_name}")
                # ingredient id 
                records = con.run("SELECT ingredient_id FROM ingredient_table WHERE ingredient_name = '"+str(ingredient_name)+"'")
                # ##records = cursor.fetchall()
                ingredient_id = records[0][0]
                print(f"Ingredient id = {ingredient_id}")

                con.run("SELECT * FROM liquid_container_mapping")
                con.run("UPDATE public.liquid_container_mapping SET ingredient_name = '"+str(ingredient_name)+"'  WHERE liquid_container_number = '"+str(i)+"' ")     
                con.run("UPDATE public.liquid_container_mapping SET ingredient_id = '"+str(ingredient_id)+"'  WHERE liquid_container_number = '"+str(i)+"' ")     
                con.run("UPDATE public.liquid_container_mapping SET last_updated = now()  WHERE liquid_container_number = '"+str(i)+"' ")     
                
        except Exception as error1 :
            print("Liquid Ingredient Not in the Current Recipe")
            print(error1)
    print("updating Liquid Containers is success for vessel 4")




def extract_recipe_id(vessel):

    try:

        records = con.run("SELECT * FROM recipe_step WHERE vessel_id = "+str(vessel)+"")
        if len(records) != 0:
            print(records)
            return records[0][18]
        if len(records) == 0:
            return 0
        
    except Exception as e :
        print(f"The error is {e}")
        pass

def extract_order_id(vessel):

    try:

        records = con.run("SELECT * FROM recipe_step WHERE vessel_id = "+str(vessel)+"")
        if len(records) != 0:
            print(records)
            return records[0][0]
        if len(records) == 0:
            return 0
        
    except Exception as e :
        print(f"The error is {e}")
        pass
    

def dbExtractgms(vid):
    try:
        records = con.run("SELECT ingredient_name, quantity, actual_weight FROM recipe_step WHERE (vessel_id = "+str(vid)+" and (type = 'Solid' or type = 'Powder' or type = 'Liquid')) ORDER BY step_no ASC")

        if len(records) != 0:
            print(records)
            return records
        if len(records) == 0:
            return 0
        
    except Exception as e :
        print(f"The error is {e}")
        pass

def extract_past():
    try:
        records = con.run("SELECT uuid, recipe_name, vessel_no, ordered_at, status FROM orders_index ORDER BY serial_no DESC LIMIT 50")
        return records

    except Exception as e :
        print(f"The error is {e}")
        pass

def customisesugar_value(customise):

    try:
        records = con.run("SELECT quantity FROM recipe_step WHERE ingredient_id = 1050")
        if len(records) != 0:
            if customise == "High":
                quantity = (float(records[0][0])*1000) + 15
                corrected_quantity = float(quantity/1000)
                con.run(f"UPDATE public.recipe_step SET quantity = {corrected_quantity}  WHERE ingredient_id = 1050 ")
            
            if customise == "Less":
                quantity = (float(records[0][0])*1000) - 15
                corrected_quantity = float(quantity/1000)
                con.run(f"UPDATE public.recipe_step SET quantity = {corrected_quantity}  WHERE ingredient_id = 1050 ")
    
    except Exception as e :
        print(f"The error is {e}")
        pass

def customiseice_value(customise):

    try:
        records = con.run("SELECT quantity FROM recipe_step WHERE ingredient_id = 1045")
        if len(records) != 0:
            if customise == "High":
                quantity = (float(records[0][0])*1000) + 15
                corrected_quantity = float(quantity/1000)
                con.run(f"UPDATE public.recipe_step SET quantity = {corrected_quantity}  WHERE ingredient_id = 1045")
            
            if customise == "Less":
                quantity = (float(records[0][0])*1000) - 15
                corrected_quantity = float(quantity/1000)
                con.run(f"UPDATE public.recipe_step SET quantity = {corrected_quantity}  WHERE ingredient_id = 1045")
    
    except Exception as e :
        print(f"The error is {e}")
        pass


def cancel_recipe():

    try:
        con.run("TRUNCATE public.recipe_step")
        
    except Exception as e :
        print(f"The error is {e}")
        pass

def start_recipe():
    try:
        con.run("UPDATE public.recipe_step SET status = 0 WHERE status = '-2'")
        
    except Exception as e :
        print(f"The error is {e}")
        pass

def get_laststep():
    try:
        records = con.run("SELECT id FROM order_queue ORDER BY id DESC LIMIT 1")
        if len(records) != 0:
            return records[0][0]
        if len(records) == 0:
            return 0
        
    except Exception as e :
        print(f"The error is {e}")
        pass


def add_order(order_id,rec_id,sugar,ice):
    name = getrecipename(rec_id)
    time_t = getrecipetime(rec_id)
    try:
        con.run(f'INSERT INTO public.order_queue ( id,recipe_name,ordered_time,sugar_customise,ice_customise,time,status,recipe_id) VALUES ({order_id}, \'{str(name)}\', now(),\'{str(sugar)}\', \'{str(ice)}\',\'{str(time_t)}\' ,\'{str("created")}\',{rec_id});')
        
    except Exception as e :
        print(f"The error is {e}")
        pass


def list_orders():
    try:
        records = con.run("SELECT id FROM order_queue WHERE status = 'created' ORDER BY id ASC")
        if len(records) != 0:
            return len(records)
        if len(records) == 0:
            return 0

    except Exception as e :
        print(f"The error is {e}")
        pass

def orders_time():
    try:
        records = con.run("SELECT time FROM order_queue WHERE status = 'created' ORDER BY id ASC")
        print(records)
        # sleep(1)
        if len(records) != 0:
            i = 0
            time = 0
            s= len(records)
            for i in range(s):
                time = time + int(records[i][0])
                print(time)
            return time
        
        if len(records) == 0:
            return 0

    except Exception as e :
        print(f"The error is {e}")
        pass


def get_first_orderid():
    try:
        records = con.run("SELECT * FROM order_queue WHERE status = 'created' ORDER BY id ASC LIMIT 1")
        if len(records) != 0:
           return records[0][0]
        
        if len(records) == 0:
            return 0

    except Exception as e :
        print(f"The error is {e}")
        pass

def progress_orderid(vid):
    try:
        records = con.run(f"SELECT * FROM order_queue WHERE status = 'progress' and vessel_id = {int(vid)} ORDER BY id ASC LIMIT 1")

        if len(records) != 0:
           print(records[0][0])
           return records[0][0]

        if len(records) == 0:
            return 0

    except Exception as e :
        showStatusMsg(f"The error is {e} , progress_orderid")
        # connection("100.106.178.97")
        # progress_orderid()
        return 0
        pass

def check_while_entry(oid):
    oi = oid
    try:
        records = con.run(f"SELECT * FROM order_queue WHERE id = {oi}")
        if len(records) != 0:
           return records[0][6]
        
        if len(records) == 0:
            return 0

    except Exception as e :
        print(f"The error is completed_order_id {e}")
        connection("100.106.178.97")
        check_while_entry(oi)
        # pass


def completed_orderid(oid):
    oi = oid
    try:
        records = con.run(f"SELECT * FROM order_queue WHERE id = {oi} and status = 'progress' ORDER BY id DESC LIMIT 1")
        if len(records) != 0:
           return len(records)
        
        if len(records) == 0:
            return 0

    except Exception as e :
        print(f"The error is completed_order_id {e}")
        connection("100.106.178.97")
        completed_orderid(oi)
        # pass

def last_completed_orderid():
    try:
        records = con.run(f"SELECT * FROM order_queue WHERE status = 'completed' ORDER BY id DESC LIMIT 1")
        if len(records) != 0:
           return records[0][0]
        
        if len(records) == 0:
            return 0

    except Exception as e :
        showStatusMsg(f"The error is {e} , last_completed_orderid")
        connection("100.106.178.97")
        last_completed_orderid()
        return(0)
        pass


def get_created_orders():
    try:
        records = con.run("SELECT id FROM order_queue WHERE status = 'created' ORDER BY id ASC LIMIT 5")
        if len(records) != 0:
            s = []
            for i in range (len(records)):
                s.append(records[i][0])
            print(f"s is {s}")          
            return(s) 
        
        if len(records) == 0:
            return 0

    except Exception as e :
        showStatusMsg(f"The error is {e} , get_created_orders")
        connection("100.106.178.97")
        get_created_orders()
        return 0
        pass


def getrecipeidfromqueue(id):
    id1 = id
    try:
        records = con.run(f"SELECT * FROM order_queue WHERE  id = {int(id1)} ORDER BY id ASC LIMIT 1")
        if len(records) != 0:
            return records[0][7]
        
        if len(records) == 0:
            return 0

    except Exception as e :
        print(f"The error is idfrom queue{e}")
        connection("100.106.178.97")
        getrecipeidfromqueue(id1)
        pass


def add_contact(userid, name, number):
    num = int(number)
    try:
        records = con.run(f"SELECT * FROM customers WHERE  number = {num} ORDER BY id ASC LIMIT 1")
        
        records1 = con.run(f"SELECT * FROM customers ORDER BY id DESC LIMIT 1")
        stepno = int(records1[0][0])+1
        con.run(f'INSERT INTO public.customers ( id, name,number, orders, userid, order_time) VALUES ({stepno}, \'{name}\', {num}, {1}, \'{userid}\', \'now()\');')
    
    except Exception as e :
        print(f"The error is idfrom queue{e}")
        pass