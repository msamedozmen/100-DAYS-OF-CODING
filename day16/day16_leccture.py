# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(188)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()
#Solution 1
# table.field_names=["Pokemon Name","Type"]
# table.add_row(["Pikachu","Electric"])
# table.add_row(["Squirtle","Water"])
# table.add_row(["Charmander","Fire"])

#Solution 2 
table.add_column("Pokemon Names",["Pikachu,","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align='l'
print(table)