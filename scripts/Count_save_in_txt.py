#This counts values from the mongoBD and saves as a .txt file





# Defining the dictionaries and lists
counter = 0
dictionary = {}
genre_name = []
count_value = []
for a in genre.find():
# The for loop was returning a KeyError. To avoid this: I ignore the error by using the 
# Try and except conditions.
  try:
# Getting the name of the genre
    genre_name_temp = a['name']
  except KeyError:
    continue
# Counting the events for each genre in the topic => genres tree
  genre_count_temp = db.event.find({u'topic.genres.name':  genre_name_temp}).count()
# Print just if the count is bigger than 0
  if genre_count_temp != 0:
    counter += genre_count_temp
    dictionary[' genre_name_temp'] = genre_count_temp
    genre_name.append( genre_name_temp)
    count_value.append(genre_count_temp)
    print  genre_name_temp, genre_count_temp

# Staking the two lists using numpy
DAT =  np.column_stack((genre_name, count_value))
# Saving the DAT file in a .txt document using space as a delimiter and also importing 
#the values as strings(fmt='%s').