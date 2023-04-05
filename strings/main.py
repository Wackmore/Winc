# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

Scorer_0 = "Ruud Gullit"
Scorer_1 = "Marco van Basten"

Goal_0 = 32
Goal_1 = 54

First_name_len_0 = Scorer_0.find(" ")
First_name_len_1 = Scorer_1.find(" ")


First_Name_0 = Scorer_0[0:(First_name_len_0)]
First_Name_1 = Scorer_1[0:First_name_len_1]

last_name_len_0 = len(Scorer_0) - First_name_len_0
last_name_len_1 = len(Scorer_1) - First_name_len_1

last_name_0 = Scorer_0[-last_name_len_0:]
last_name_1 = Scorer_1[-last_name_len_1:]

first_leter_0 = Scorer_0[0]
first_leter_1 = Scorer_1[0]

name_short_0 = f"{first_leter_0}.{last_name_0}"
name_short_1 = f"{first_leter_1}.{last_name_1}"

report = F"{Scorer_0} scored in the {Goal_0}nd minute \n{Scorer_1} scored in the {Goal_1}th minute"




print(report)
#print(last_name_len)
#print(First_Name_0)
#print(First_Name_1)
#print(last_name_len_0)
#print(last_name_len_1)
#print(last_name_0)
#print(last_name_1)
print(name_short_0)
print(name_short_1)

# 2 do de chant! & de good chant
