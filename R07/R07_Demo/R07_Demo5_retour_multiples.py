def obtenir_echelle_salarial(echelon:int):
    if echelon > 10 or echelon < 0 :
        return
    
    match echelon :
        case 1 : return 25000
        case 2 : return 33000
        case 3 : return 39000
        case 4 : return 45000
        case 5 : return 52000
        
    return ( 50000 + (echelon-5) * 7500)

print(f"""Bob à un salaire de:
      {obtenir_echelle_salarial(32)}$ par année""")


