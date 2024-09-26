# %% [markdown]
# # Data Types in Python: Lists, Tuples, Sets
# These data types are all used to store multiple items in one variable. However, each data type have different formats and uses. 
# 

# %% [markdown]
# ## Javascript: Arrays
# Arrays in Javascript are the equivalent to Lists, Tuples, and Sets in Python
# <br>

# %%
#%%javascript
#const sesame_street = ["Elmo", "Cookie Monster", "Oscar the Grouch", "Grover"] 
#let sesame_street = sesame_street[0]

# %% [markdown]
# # Lists
# Lists use <strong>square brackets []</strong> and are ordered and can be modfied (are changeable). Lists are best used for storing multiple values of the same or different data types. Items can be duplicated in lists. Lists can be modified (lists are mutable).

# %%
sesame = ["Elmo", "Cookie Monster", "Oscar the Grouch", "Grover"]
print(sesame)

# %%
#Lists are indexed. "0" = the first item, "1" = the second item, and so on
print(sesame[2])

# %%
#looping this list
for x in sesame:
  print(x)

# %%
sesame = ["Elmo", "Cookie Monster", "Oscar the Grouch", "Grover"]
print(sesame)

sesame[3] = "Big Bird"
print(sesame)

# %% [markdown]
# # Tuples
# Tuples use <strong>round brackets ()</strong> and are ordered and are be defined/unmutable (cannot be changed). Tuples are useful for representing fixed sequences of data. Tuples are indexed so the first item is "0", the second item is "1", and so on. Items in tuples can be duplicated.

# %%
teletubbies = ("Dipsy", "Tinky-Winky", "Po", "Laa-Laa")
print(teletubbies)


# %%
#What happens you try to change the tuple?
teletubbies[2] = "Dipsy"

#The tuple does not allow for the change to occur

# %% [markdown]
# # Sets
# Sets use <strong>curly brackets {}</strong> and are unordered and unmutable (cannot be changed). Sets are best used for tasks such as removing duplicates from a list or performing set operations. Duplicates aren't allowed in sets but adding and removing items are allowed. Indexing on sets can't be done because sets are unordered.

# %%
backyardigans = {"Uniqua", "Pablo", "Tyrone", "Tasha"}
print(backyardigans)

# %%
#To add an item in a set:
backyardigans.add("Austin")
print(backyardigans)

#To remove an item in a set do: setname.remove
#Example: backyardigans.remove("Pablo")

# %% [markdown]
# # Popcorn Hack
# Create a list of data that could work with your GitHub Pages Blog Topic. For example, if your blog was about movies from different genres, make a list of movies for every genre. 


