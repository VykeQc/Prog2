# comment intaller un module qu'on n'a pas déjà installé dans python
# https://www.freecodecamp.org/news/how-to-interact-with-web-services-using-python/
# Dans le terminal              pip install requests

# Fake Store REST API
import requests
import json

BASE_URL = 'https://fakestoreapi.com'

# faire une demande de tous les produits (GET)
#response = requests.get(f"{BASE_URL}/products")

#print(response)
#print(response.json())

#######################################################################
# pour avoir seulement quelques produits
# l'API nous offre /products?limit=x

query_params = { "limit":3}

# faire une demande de 3 produits (GET/products?limit=3)





######################################################################
# pour avoir un produit précis
# l'API nous offre /products/productID

# faire une demande pour le produit dont l'id est 18 (GET/products?18)




#######################################################################
# Pour ajouter un produit 
# POST request

# Dans la documentation de Fake Store API, un produit a les attributs
#       title, price, description, image et category

nouveau_produit = {
    "title": 'produit de test',
    "price":15.5,
    "description": 'lorem ipsu, set',
    "image": 'https://i.pravatar.cc',
    "category": 'electronique'
}

# Ajouter le nouveau produit
response = requests.post(f"{BASE_URL}/products",json=nouveau_produit)
print(response.json())

#######################################################################
# Pour modifier un produit existant
# PUT request

# Dans la documentation de Fake Store API, un produit a les attributs
#       title, price, description, image et category
# Il nous faut l'id du produit qu'on veut mettre à jour

maj_produit = {
    "title": 'produit MAJ',
    "category": 'automobile'
}

# Pour mettre à jour un produit existant
response = requests.put(f"{BASE_URL}/products/21",json=maj_produit)
print(response.json())

###ATTENTION, avec PUT, cela enlève les attributs que le produit pouvait avoir et ne garde que les nouveaux attributs

#######################################################################

# Pour modifier CERTAINS ATTRIBUTS d'un produit existant
# PATCH request

# Dans la documentation de Fake Store API, un produit a les attributs
#       title, price, description, image et category
# Il nous faut l'id du produit qu'on veut mettre à jour

maj_produit = {
    "category": 'appliance'
}

# Pour mettre à jour CERTAINS attributs d'un produit existant
response = requests.patch(f"{BASE_URL}/products/21",json=maj_produit)
print(response.json())

#######################################################################

# Pour SUPPRIMER un produit existant
# DELETE request

# Il nous faut l'id du produit qu'on veut SUPPRIMER


# Pour supprimer l'id 21
response = requests.delete(f"{BASE_URL}/products/21")
print(response.json())
