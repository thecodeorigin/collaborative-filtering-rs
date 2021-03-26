import math
import numpy
# Horizontal: User
user = ['Tú', 'Thắng', 'Trâm', 'Ý', 'Trinh']
# Vertical: Item
item = ['Phim hành động', 'Phim Hàn Quốc', 'Phim khoa học', 'Phim tình cảm', 'Phim Nhật Bản']
rating_matrix = [
  [0,1,4,0,4],
  [4,2,5,1,3],
  [1,5,1,5,1],
  [4,2,3,1,3],
  [1,5,4,4,1],
]
# User similarity matrix
similarity = numpy.zeros((len(user),len(user)))

# Calculate the user similarity
for i in range(len(user)):
  for j in range(len(user)):
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
for user_index in range(len(rating_matrix)):
  for item_index in range(len(rating_matrix[0])):
    if rating_matrix[user_index][item_index] == 0:
      print("Guessing rating of user " + user[user_index] + " for item " + item[item_index])
      k_neighbor = []
      for neighbor_index in range(len(similarity[user_index])):
        # Similarity rate
        if similarity[user_index][neighbor_index] > 0.5 and user_index != neighbor_index:
          print("Neighbor: " + user[neighbor_index] + " (sim=" + str(similarity[user_index][neighbor_index]) + ")")
          k_neighbor.append(neighbor_index)
      # Make prediction
      avg_user_i = sum(rating_matrix[user_index])/(len(rating_matrix[user_index])-sum(map(lambda x : x == 0, rating_matrix[user_index])))
      sum1 = 0
      sum2 = 0
      for k_i in range(len(k_neighbor)):
        avg_user_l = sum(rating_matrix[k_neighbor[k_i]])/(len(rating_matrix[k_neighbor[k_i]])-sum(map(lambda x : x == 0, rating_matrix[k_neighbor[k_i]])))
        sum1 += similarity[user_index][k_neighbor[k_i]]*(rating_matrix[k_neighbor[k_i]][item_index]-avg_user_l)
        sum2 += similarity[user_index][k_neighbor[k_i]]
      if(sum2 == 0): 
        print("Cannot make prediction because this user has no neighbor")
      else:
        print("Prediction rating: " + str(avg_user_i + (sum1/sum2)))
      print("-----------------------------------------------------------------")

