# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line


leek_price = 2
leek_order = "leek 4"

broccoli_price = 2.34
broccoli_order = 1.6


number_place = leek_order.find(" ")
number_true_place = number_place + 1
leeks = int(leek_order[(number_true_place)])

broccoli_order_price = (broccoli_order * broccoli_price)
broccoli_order_price = round(broccoli_order_price,2)


sum_total = leeks * leek_price


print (F" Leek is {leek_price} euro per kilo.")
print (sum_total)
print (F"{broccoli_order}kg broccoli costs {broccoli_order_price}e")


#print(type (leeks))