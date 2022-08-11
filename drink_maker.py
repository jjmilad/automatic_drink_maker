"""
----------AUTOMATIC COFFEE MAKING ALGORETHEM------------

  \ \ \
  / / /
  | | |
|~~~~~~~|
|       |\
|       | |
|_______|/  .1 FULL HOT CAPICINO

  \ \ \
  / / /
  | | |
|       |
|~~~~~~~|\
|       | |
|_______|/  .1 MEDIUM HOT CAPICINO

----------------------------------

  \ \ \
  / / /
  | | |
|~~~~~~~|
|       |\
|       | |
|_______|/  .1 FULL COLD COFFEE


|       |
|~~~~~~~|\
|       | |
|_______|/  .1 MEDIUM COLD COFFEE

--------------------------------


|*******|
|       |\
|       | |
|_______|/  .1 FULL CARBONATED WATER



|       |
|*******|\
|       | |
|_______|/  .1 MEDIUM CARBONATED WATER


"""

#required variables
carbonated_water = "*******"
coffee = "~~~~~~~"
hot_cup = """
      \ \ \ \t
      / / / \t
      | | | \t
"""
cold_cup = ""
full = 'full'
medium = 'medium'
drink_sizes = {full : full, medium : medium}
drink_types = {'coffee':coffee, 'carbonated_water':carbonated_water}
drink_tempratures = {'hot':hot_cup, 'cold':cold_cup}
note = '\nNote: you can either type the word or the number of it'
conformation_list = []
loop_count = 1
drink_type_new = None
drink_temprature_new = None
drink_size_new = None

#coffee making algorethem
def coffee_making_recipe(temprature_type, drink_type, drink_size):
    none = "       "
    cup = """
      {} \t
    |{}| \t
    |{}|\ \t
    |       | | \t
    |_______|/ \t
    """
    if drink_size == full:
        x = drink_type
        xx = none
    elif drink_size == medium:
        x = none
        xx = drink_type
    return cup.format(temprature_type,x,xx)

#input handler
def input_handler(options, input_type):
    loop_count = 1
    varify = None
    for k, v in options.items():
        print("{}. {}".format(loop_count, k))
        loop_count = loop_count + 1
    print(note)
    input_name = input('please choose your drink {} : '.format(input_type,))
    for index, val in enumerate(options, start=1):
        if input_name != None and input_name.lower() == val or input_name == str(index):
            varify = val
            break
    if varify is not None:
        if input_type == 'type':
            global drink_type_new
            drink_type_new = drink_types[varify]
            conformation_list.append(varify)
        elif input_type == 'temprature':
            global drink_temprature_new
            drink_temprature_new = drink_tempratures[varify]
            conformation_list.append(varify)
        elif input_type == 'size':
            global drink_size_new
            drink_size_new = drink_sizes[varify]
            conformation_list.append(varify)
    else:
        print('error, please choose the correct option\n')
        conformation_list.clear()



#the reponse check cycle
while True:
    #first output to the users
    print('welcome to our coffee shop where you can get customizable coffee')
    input('to continue please press any key ...\n')

    #drink type input + varification
    input_handler(drink_types, 'type')
    if drink_type_new is None:
        continue

    #drink temprature input + varification
    input_handler(drink_tempratures, 'temprature')
    if drink_temprature_new is None:
        drink_type_new = None
        continue

    #drink size input + varification
    input_handler(drink_sizes, 'size')
    if drink_size_new is None:
        drink_type_new = None
        drink_temprature_new = None
        continue


    #order conformation
    print('your order summary: \n')
    print('your drink is ',conformation_list[0],'and the tempratures is ',conformation_list[1],'and the size is ',conformation_list[2])
    continue_status = input('press c to cancel or any other key to continue ...')
    if continue_status.lower() == 'c':
        continue

    #your drink
    print(coffee_making_recipe(drink_temprature_new, drink_type_new, drink_size_new))

    #ending
    print('\n\n\n')
    print('thank you for ordering !\n happy drinking :)')
    next_order = input('do you want to order more 1 for yes , 0 or no : ')
    if next_order == str(1):
        continue
    break
