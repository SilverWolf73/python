current_users = ['root', 'user_1', 'user_2', 'user_3', 'user_4']
new_users = ['kali', 'user_1','User_1']
if new_users :
    for user in new_users :
        for current_user in current_users :
            if user.upper() == current_user.upper():
                print("用户已经存在。")
                del new_users[0]
            else :
                print("欢迎新成员。",user)
                current_users.append(user)
                del new_users[0]
else :
    if current_users :
        for user in current_users :
            if user == 'root':
                print("你好管理员。")
            else :
                print("你好,",user)
    else :
        print("无用户登陆。")
