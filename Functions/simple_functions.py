# Define three functions
# favorite_things
def favorite_things(name, fav_movie, fav_artist):
    print(f'My name is {name}\nMy favorite movie is {fav_movie}\nMy favorite artist is {fav_artist}')

favorite_things('Craig Bowman', 'Friday Night Lights', 'Chance The Rapper')

# why_im_here
def why_im_here():
    return f'I am here because I have an affinity for math and I am naturally curious. I wasn\'t made for Data Analytics, it was made for me!'

# creating the function a dfiferent way
def why_im_here2(reason):
    return reason

print(why_im_here())
print(why_im_here2('DA was made for me'))

# favorite_place
def favorite_place(place, why):
    return f'One of my favorite places to visit is {place}, because {why}'

print(favorite_place('California', 'the weather is always good'))
print(favorite_place('Downtown Chicago', 'I love the atmosphere'))