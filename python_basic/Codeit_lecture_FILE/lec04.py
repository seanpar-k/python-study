with open('new_file.txt', 'w') as f:
    f.write("hello world\n")
    f.write("haneol babo\n")

with open('new_file.txt', 'a') as f:     # append의 줄임말
    f.write("TRUE")