with open("writing_file.txt", mode='w') as f:
    # truncateされる :byte=0に切り詰める
    f.write("You can write contents here\nuse 'backslash' to break the row")
    f.write("new write() doesn't break row")

    print("You can add a new row using 'file' parameter", file=f)
    print("new print() method breaks the row for you!!", file=f)
   