# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

spain_language_spoken = "Spanish"
spain_religion = "Catholic"
spain_capital = "Madrid"
spain_gdp = 37900
spain_pop_growth = 0.12
spain_pop = 47222613



switserland_language_spoken = "German"
switserland_religion = "Catholic"
switserland_capital = "Bern"
switserland_gdp = 71000
switserland_growth = 0.64
switserland_pop = 8563760



print(spain_language_spoken == switserland_language_spoken)
print(spain_religion == switserland_religion)
print(len(spain_capital) != len(switserland_capital))
print(spain_gdp < switserland_gdp)
print(spain_pop_growth > 1 and switserland_growth >1)
print(spain_pop > 10000000 or switserland_pop > 10000000)
print((spain_pop_growth > 1 and switserland_growth <1) or(spain_pop_growth < 1 and switserland_growth >1) )

