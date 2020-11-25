grocery_list = ["Juice", "Patatoes","Tomatoes","Bananas"]
print(f"First Item: {grocery_list[0]}")

grocery_list[0] = "Orange"
print(f"New Item: {grocery_list[0]}")
print(grocery_list[1:3])

others_events = ["Wash Cars","Pick up kids","Cash checks"]
to_do_list = [others_events,grocery_list]
print(to_do_list)
print(to_do_list[0][2])

grocery_list.append("Carrot")
print(grocery_list)

grocery_list.insert(1,"Bean")
print(grocery_list)

grocery_list.remove("Orange")
print(grocery_list)

grocery_list.sort()
print(grocery_list)

to_do_list2 = others_events + grocery_list
print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))