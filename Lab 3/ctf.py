flag = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ'
new_flag = []
for i in range(len(flag)):
    new_flag.append(chr(ord(flag[i]) >> 8))
print(new_flag)
