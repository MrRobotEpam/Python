def get_total(costs, items, tax):
    total = 0           #inicializar a 0 el costo toal

    for item in items:
        if item in costs:
            total += costs[item]  #sumar el costo de los items al total

    total_with_tax = total * (1 + tax)  #Agregar el Iva al total 

    return round(total_with_tax, 2)  #Regresamos el total con IVA y redondeamos a 2 decimales

groceries = {'apples': 15, 'bananas': 30, 'watermelon': 60}

result = get_total(groceries, ['apples', 'bananas'], 0.16)
###
# 15 + 30 = 45
# 45 * 0.16 of 45 = 52.2
# output = 52.2
###
print(result)