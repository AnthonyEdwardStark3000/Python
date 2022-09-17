class About_me:
    name = 'suresh'

    def about_me():
        print('I love to code.')


print(type(About_me))
print(About_me.name)

# creating objects
suresh = About_me()

print(type(suresh))
suresh.about_me()
