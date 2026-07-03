#  list creation, append, remove, sort, indexing

movie_lst = ["Uncharted", "Interstellar", "Oppenheimer", "Inception", "Fast & Furious"]

movie_lst.append("Transformers")
print("Actual list :",movie_lst)
movie_lst.remove("Interstellar")
print("Removed Second element :",movie_lst)
# movie_lst.pop(1)

print("Sorted list :",sorted(movie_lst))