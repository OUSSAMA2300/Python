# Start with users that need to be verified
# and an empty list to hold confirmed users. 
unconfirmed_users = ['alice', 'brian', 'candace']
confriemd_users = []

# Verfiy each user untill there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.

while unconfirmed_users:
    currnet_users = unconfirmed_users.pop()

    print("Verfying user:", currnet_users.title())
    confriemd_users.append(currnet_users)

# Display all confirmed users.
print("\nThe following users have been confiremd: ")
for confirmed_user in confriemd_users:
    print(confirmed_user.title())