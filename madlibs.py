# This game shows the use of string concatenation

# print("Enter an adjective :")
# phrase = input()
#
# #listed are few ways by which concatenations are done
# # 1
# print(" My heart is " + phrase)
# # 2
# print(" I have a {} cow".format(phrase))
# # 3
# print(f" Today was a {phrase} day!")
#
# """
# Output:
# Enter an adjective :
# red
#  My heart is red
#  I have a red cow
#  Today was a red day!
# """

verb = input("Verb: ")
a_person = input("Anyone you know: ")
adj = input("Adjective: ")

madlib = f"I like to {verb} alot. I have liked it({verb}) since i was a child. My {a_person} says that I could {verb} all day, just too {adj} at it! "

print(madlib)
