import random

cusine = ['American', 'Japanese', 'Chinese']


home_foods = ['Chicken and rice', 'Steak', 'Porksteak', 'Spahgetti', 'Fetachini alfredo', 'Crab', 'Tuna and noodles']

food = [['Burger', 'Wings', 'Chicken', 'Steak'], ['Ramen', 'Bento box', 'Yakisoba', 'Rice', 'Soba'], ['Orange chicken', 'Cashew chicken', 'Noodles', 'Sweet and sour chicken'] ]

print("Welcome to my food picker program")

home_cooked = input('Do you want a home cooked meal or to go out: ')
print(home_cooked)

cusine_choice = input('What cusine do you want: ')



if home_cooked == 'home cooked':
    print(random.sample(home_foods, 1))
else:
    print(cusine_choice)
    if cusine_choice == 'american':
        for x in food[0:1]:
            print(x)           
    else:
        if cusine_choice == 'japanese':
            for x in food[1:2]:
                print(x)
        else:
            if cusine_choice == 'chinese':
                for x in food[2:3]:
                    print(x)
