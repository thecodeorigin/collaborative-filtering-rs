import math
import numpy
# Horizontal: Item
item = ['Phim hành động', 'Phim Hàn Quốc', 'Phim khoa học', 'Phim tình cảm', 'Phim Nhật Bản']
# Vertical: User
user = ['Tú', 'Thắng', 'Trâm', 'Ý', 'Trinh']

rating_matrix = [
  [0,4,1,4,1],
  [1,2,5,2,5],
  [4,5,1,3,4],
  [0,1,5,1,4],
  [4,3,1,3,1],
]
# Item similarity matrix
similarity = numpy.zeros((len(user),len(user)))
# Calculate the similarity
for i in range(len(item)):
  for j in range(len(item)):
    if i == j:
      similarity[i][j] = 1
    else:
      sum1 = 0
      sum2 = 0
      sum3 = 0
      # Calculate average without 0 elements
      avg_user_i = sum(rating_matrix[i])/(len(rating_matrix[i])-sum(map(lambda x : x == 0, rating_matrix[i])))
      avg_user_j = sum(rating_matrix[j])/(len(rating_matrix[j])-sum(map(lambda x : x == 0, rating_matrix[j])))
      # Calculate similarity using formula
      for k in range(len(rating_matrix[0])):
        if rating_matrix[i][k] != 0 and rating_matrix[j][k] != 0:
          sum1 += (rating_matrix[i][k]-avg_user_i)*(rating_matrix[j][k]-avg_user_j)
          sum2 += pow((rating_matrix[i][k]-avg_user_i), 2)
          sum3 += pow((rating_matrix[j][k]-avg_user_j), 2)
      similarity[i][j] = sum1/(math.sqrt(sum2)*math.sqrt(sum3))
# Making prediction on every empty review
for item_index in range(len(rating_matrix)):
  for user_index in range(len(rating_matrix[0])):
    if rating_matrix[item_index][user_index] == 0:
      print("Guessing rating of item " + item[item_index] + " for user " + user[user_index])
      k_neighbor = []
      for neighbor_index in range(len(similarity[item_index])):
        # Similarity rate
        if similarity[item_index][neighbor_index] > 0.5 and item_index != neighbor_index:
          print("Neighbor: " + item[neighbor_index])
          k_neighbor.append(neighbor_index)
      # Make prediction
      avg_user_i = sum(rating_matrix[item_index])/(len(rating_matrix[item_index])-sum(map(lambda x : x == 0, rating_matrix[item_index])))
      sum1 = 0
      sum2 = 0
      for k_i in range(len(k_neighbor)):
        avg_user_l = sum(rating_matrix[k_neighbor[k_i]])/(len(rating_matrix[k_neighbor[k_i]])-sum(map(lambda x : x == 0, rating_matrix[k_neighbor[k_i]])))
        sum1 += similarity[item_index][k_neighbor[k_i]]*(rating_matrix[k_neighbor[k_i]][user_index]-avg_user_l)
        sum2 += similarity[item_index][k_neighbor[k_i]]
      if(sum2 == 0): 
        print("Cannot make prediction because this item has no neighbor")
      else:
        print("Prediction rating: " + str(avg_user_i + (sum1/sum2)))
      print("-----------------------------------------------------------------")

