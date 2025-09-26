# user_word = "moaiah"
# test_word = "mosiah"

# # for index_u in range(len(user_word)):
# #     letter_u = user_word[index_u]
# #     print(f"\nIndex: {index_u} Letter: {letter_u}")

# # for index_t in range(len(test_word)):
# #     letter_t = test_word[index_t]
# #     print(f"\nIndex: {index_t} Letter: {letter_t}")


# # for i, letter in enumerate(user_word):
# #     print(f"position{i} and letter {letter}")
# # for i, letter in enumerate(test_word):
# #     print(f"position{i} and letter {letter}")

# word = "book"

# for index in range(len(word)):
#     letter = word[index]
#     print(f"Index: {index} Letter: {letter}")


# while True:
#     fav_word = "commitment"
#     fav_letter = input("What letter? ")

#     for letter in fav_word:
#         if letter == fav_letter:
#             print(letter.upper(), end="")
#         else:
#             print(letter, end="")
        
#     print("")

#     for letter in fav_word:    
#         if letter == fav_letter:
#             print("_", end="")
#         else:
#             print(letter, end="")
#     print("")



user_word = "mormon"
test_word = "mosiah"


for letter in test_word:
    if letter in user_word:
        print(letter.upper(), end="")
    else:
        print("_")