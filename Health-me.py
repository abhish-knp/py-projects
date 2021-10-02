## Health Managenment system:
## 3 clients - Harry, Rohan and Hamad

# total 6 files
def getdate():
    import datetime
    return datetime.datetime.now()

# To lock or retrieve.
# One more fuction to retrive excercise.
print(getdate())



usr_name = input("Enter the user name: ")
add_ret = input("retrieve/add :")
meal_exer = input("meal/excercise")

def addharry(meal_exer):
    if meal_exer == "meal":
        a = input("Enter your meal: ")
        with open ("harry_meal.txt",'a+') as f:
            f.write(str(getdate()) + ': Meal: ' + a +'\n')
        with open ("harry_meal.txt") as f:
            print(f.readlines()) 
            
    elif meal_exer == "excercise":
        a = input("Enter your Wrokout: ")
        with open ("harry_workout.txt",'a+') as f:
            f.write(str(getdate()) + ': Excercise: ' + a +'\n')
        with open ("harry_workout.txt") as f:
            print(f.readlines())
    else:
        print("Wrong Input")
        
# add rohan
def addrohan(meal_exer):
    if meal_exer == "meal":
        a = input("Enter your meal: ")
        with open ("rohan_meal.txt",'a+') as f:
            f.write(str(getdate()) + ': Meal: ' + a +'\n')
        with open ("rohan_meal.txt") as f:
            print(f.readlines()) 
            
    elif meal_exer == "excercise":
        a = input("Enter your Wrokout: ")
        with open ("rohan_workout.txt",'a+') as f:
            f.write(str(getdate()) + ': Excercise: ' + a +'\n')
        with open ("rohan_workout.txt") as f:
            print(f.readlines())
    else:
        print("Wrong Input")

        
# add hamad
def addhamad(meal_exer):
    if meal_exer == "meal":
        a = input("Enter your meal: ")
        with open ("hamad_meal.txt",'a+') as f:
            f.write(str(getdate()) + ': Meal: ' + a +'\n')
        with open ("hamad_meal.txt") as f:
            print(f.readlines()) 
            
    elif meal_exer == "excercise":
        a = input("Enter your Wrokout: ")
        with open ("hamad_workout.txt",'a+') as f:
            f.write(str(getdate()) + ': Excercise: ' + a +'\n')
        with open ("hamad_workout.txt") as f:
            print(f.readlines())
    else:
        print("Wrong Input")
        


#Logic builder:

# for harry
if usr_name == "harry" and add_ret == "add":
#     meal_exer == input("meal/excercise")
    addharry(meal_exer)
elif usr_name == 'harry' and add_ret == 'retrieve':
#     meal_exer = input("meal/excercise")
    if meal_exer == "meal":
        with open ("harry_meal.txt") as f:
            print(f.readlines())
    elif meal_exer == 'excercise':
        with open ("harry_excercise.txt") as f:
            print(f.readlines())

# for rohan
elif usr_name == "rohan" and add_ret == "add":
#     meal_exer == input("meal/excercise")
    addrohan(meal_exer)
elif usr_name == 'rohan' and add_ret == 'retrieve':
#     meal_exer = input("meal/excercise")
    if meal_exer == "meal":
        with open ("rohan_meal.txt") as f:
            print(f.readlines())
    elif meal_exer == 'excercise':
        with open ("rohan_excercise.txt") as f:
            print(f.readlines())

# for hamad
elif usr_name == "hamad" and add_ret == "add":
#     meal_exer == input("meal/excercise")
    addhamad(meal_exer)
elif usr_name == 'hamad' and add_ret == 'retrieve':
#     meal_exer = input("meal/excercise")
    if meal_exer == "meal":
        with open ("hamad_meal.txt") as f:
            print(f.readlines())
    elif meal_exer == 'excercise':
        with open ("hamad_excercise.txt") as f:
            print(f.readlines())            
            
