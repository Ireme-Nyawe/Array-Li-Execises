# Program to merge two lists of friends and remove duplicate names

friends_list_1 = ["Mucyo", "Muhire", "Mukiza"]
friends_list_2 = ["Muhire", "Mugisha", "Muhoza"]

merged_friends = list(set(friends_list_1 + friends_list_2))

print("Merged list of friends:")
for friend in merged_friends:
    print(friend)
