current_users = ['fiosvaio', 'cath_bro', 'notahero99', 'cocodraco', 'ntsyaad']
new_users = ['fiolisyafa', 'cath_bro', 'queen_ger', 'cocodraco', 'tea_coops']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("This username has already been taken. Please choose a different username.")
    else:
        print("This username is avaliable.")
