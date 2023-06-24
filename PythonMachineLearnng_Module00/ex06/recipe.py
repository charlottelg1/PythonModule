import sys

cookbook = {'sandwich':{'ingredients':["ham", "bread", "cheese", "tomatoes"], 
                         'meal':'lunch', 
                         'prep_time':10},
			'cake':{'ingredients':['flour', 'sugar', 'eggs'],
					'meal':'dessert',
                    'prep_time':60},
            'salad':{'ingredients':['avocado', 'arugula', 'tomatoes', 'spinach'],
                     'meal':'lunch',
                     'prep_time':15}
}

def list():
	print("The recipes in the cookbook are:")
	for recipe in cookbook.items():
		print('* ', recipe[0])

def details():
	name = input("Please enter a recipe name to get its details:\n")
	if name in cookbook:
		for recipe in cookbook.items():
			if (recipe[0] == name):
				ingredients = str(recipe[1]['ingredients'])[1:-1].replace('\'', '')
				print(f"""The {name}\'s ingredients are {ingredients}. It is a {recipe[1]['meal']} and it takes {recipe[1]['prep_time']} minutes of preparation """)
	else:
		print(f'{name.capitalize()} is not a recipe in this cookbook')

def	delete_recipe():
	name = input("What recipe do you want to delete from the Python Cookbook ?\n")
	if name in cookbook:
		del cookbook[name]
		print(f'{name} has been deleted from the Python Cookbook')
	else:
		print(f'There is no {name} in the Python Cookbook') 

def new_recipe():
	name = input("Enter a name :\n")
	ingredients = [item for item in input("Enter ingredients:\n").split()]
	meal_type = input("Enter a meal type:\n")
	prep_time = input("Enter a preparation time:\n")
	cookbook[name] = {}
	cookbook[name]['ingredients'] = ingredients
	cookbook[name]['meal'] = meal_type
	cookbook[name]['prep_time'] = prep_time
	print(f'{name} has been added to the cookbook!\n')


if __name__ == "__main__":
	print("""Welcome to the Python Cookbook !
List of available option:
	1: Add a recipe
	2: Delete a recipe
	3: Print a recipe
	4: Print the cookbook
	5: Quit
		""")
	option = input("Please select and option: \n")
	while (1):
		if option == '1':
			new_recipe()
			option = input("Please select and option:\n")
		elif option == '2':
			delete_recipe()
			option = input("Please select and option:\n")
		elif option == '3':
			details()
			option = input("Please select and option:\n")
		elif option == '4':
			list()
			option = input("Please select and option:\n")
		elif option == '5':
			print("Cookbook closed. Goodbye!")
			exit()
		else:
			option = input("""Sorry, this option does not exist
List of available option:
	1: Add a recipe
	2: Delete a recipe
	3: Print a recipe
	4: Print the cookbook
	5: Quit

Please select and option: """)