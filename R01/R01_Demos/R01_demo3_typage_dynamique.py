# Typage dynamique
# Assigner des valeurs aux variables afin qu'elles soient du type désiré, la changer si nécessaire.

exemple_une_variable = 32
print(f"""\nLa variable est : {type(exemple_une_variable)}""")

exemple_une_variable = None      # changer la variable en type float
print(f"""La variable est : {type(exemple_une_variable)}""")

exemple_une_variable = None    # changer la variable en type  boolean
print(f"""La variable est : {type(exemple_une_variable)}""")

exemple_une_variable = None     # changer la variable en type  string
print(f"""La variable est : {type(exemple_une_variable)}\n""")



# Typage dynamique. Le type change par lui-même selon s'il faut un int ou un float
variable_chiffre = 2
print(type(variable_chiffre))

variable_chiffre = 2 * 2
print(type(variable_chiffre))

variable_chiffre = 2 / 2
print(type(variable_chiffre))

variable_chiffre = variable_chiffre * 2
print(type(variable_chiffre))