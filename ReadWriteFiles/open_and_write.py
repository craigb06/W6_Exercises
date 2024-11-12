# Create a new variable to work with a file

about_me = open('about_me.txt', 'a')
about_me.close()

# Update about me script to add a new line

about_me = open('about_me.txt', 'a')
about_me.write('''If you could do anything for your perfect night out, where would you go and what would you do?
I would have a banquet on Laugh Tale after I become KING OF THE PIRATES''')
about_me.close()