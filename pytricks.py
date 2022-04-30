# 1 The walrus operator; --> :=

my_blog = "blog.octachart.com"

# blog_len = len(my_blog)
# if blog_len > 10:
#     print(True)

if blog_len := len(my_blog) > 10:
    pass
    # print(True)

# 2 The dir() 
    
import pip
# print(dir(pip))

# 3 The * operator

num = [1,2,3,4,5]
# print(*num)

num2 = [7,8,9,10]
# print([*num, *num2])

new = []
for n in num:
    new.append(n)
    
for n in num2:
    new.append(n)
# print(new)

# *args...
def names(*name_tuples):
    return name_tuples

# print(names("Ronnie", "AfroBoy", "Youtuber" , "...."))

# **kwargs...
def names_(**kwargs):
    return kwargs
# print(names_(first = "Ronnie", lastname= "Atuhaire", blog = "octachart"))

# 4 The breakpoint()

x = 10
y = "Hi"
z = "World"

# print(y)
# breakpoint()
# print(z)

# The zip() function

# zip(*iterables)

words = ["one", "two", "three"]
figs = [1,2,3]

for word, fig in zip(words, figs):
    pass
    # print(fig ,"---> ", word)

mapper = [["one", "two", "three"], [1,2,3]]
print([n for n in zip(*mapper)])



    
