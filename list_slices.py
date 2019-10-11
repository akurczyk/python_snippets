list_ = [i for i in range(0, 20)]

print(list_[5:])        # returns elements skipping first 5
print(list_[:5])        # return only 5 first elements
print(list_[:-5])       # skip 5 last elements
print(list_[5:-5])      # skip first and last 5 elements
print(list_[5:-5:2])    # every 2nd
print(list_[-5:5:-1])   # reversed, the indexes also has to be reversed!
print(list_[::-2])      # reversed, only every 2nd element
