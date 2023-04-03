# Do not modify these lines
__winc_id__ = '499e67d5cb54448e93cee7465be2c866'
__human_name__ = 'calculate'

# Add your code after this line

broccoli = 2
leek = 2
potato = 3
brussel_sprout = 7

num_potatoes = 7
num_broccolis = 5
num_leeks = 2
num_brussel_sprouts = 10

discount_percentage = 30

discount_multiply = ((100-(discount_percentage)) / 100)

sum_one_each = (broccoli+leek+potato+brussel_sprout)
sum_total = ((broccoli * num_broccolis) + (leek * num_leeks) + (potato * num_potatoes) + (brussel_sprout * num_brussel_sprouts))
avg_price = (sum_one_each / 4)

discounted_sum_total = (sum_total * discount_multiply)



print (sum_one_each)
print (sum_total)
print (avg_price)
print (discounted_sum_total)


