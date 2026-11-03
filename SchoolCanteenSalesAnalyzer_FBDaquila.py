def calculate_average(total_sales, number_fooditems):
    average = total_sales / number_fooditems
    return average

number_fooditems = int(input("\nEnter the number of food items: "))

def count_targets_hit(number_fooditems):
    count_target = 0
    count_below_target = 0
    total_sales = 0
    for n in range(1, number_fooditems + 1):
        sales = int(input(f"Enter sales for item {n}: "))
        total_sales = total_sales + sales
        if sales > 500:
            count_target = count_target + 1
        else:
            count_below_target = count_below_target + 1
    return total_sales, count_target, count_below_target



total_sales, count_target, count_below_target = count_targets_hit(number_fooditems)
average = calculate_average(total_sales, number_fooditems)

print(f"CANTEEN SALES REPORT\nAverage sales: {average:.2f} | Meeting Target: {count_target} | Below Target: {count_below_target}")