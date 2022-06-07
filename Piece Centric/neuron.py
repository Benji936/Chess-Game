import numpy as np

def sig(x):
    1/(1*np.exp(x))

input_vector = [[1.72, 1.23],[1.72,1.23]]
weights_1 = [1.26, 0]
weights_2 = [2.17, 0.32]

#first_indexes_mult = input_vector[0] * weights_1[0]
#second_indexes_mult = input_vector[1] * weights_1[1]
dot_product_2 = np.dot(input_vector, weights_1)
#dot_product_1 = first_indexes_mult + second_indexes_mult
print(f"The dot product is: {dot_product_2}")
#The dot product is: 2.1672


#idée 1

"""Un perceptron pour chaque aspect qui détermine si le coup est bon:
 - position stratégique
 - libérer d'autre pièce
 - mettre en échec
 - manger une pièce
 - doubler les pions
 - clouer un pièce
 - attaquer une pièce
 - promotion
  """