# str = "Apple,Banana"
# lst = str.split(',')
# print(lst)

# str = "lalllbl"
# print(str.strip('l'))

# str = "Apple is red"
# sub = "m"
# print(str.find(sub,6,10))

# s = "abc 123 456 def"
# split_val = s.split(' ')
# for i in range(len(split_val)):
#     if split_val[i].isdigit():
#         print(split_val[i])

# s = "  abc123 !@# 456  "
# strip_val = s.strip()
# split_val = strip_val.split(' ')
# for i in range(len(split_val)):
#     if split_val[i].isalnum():
#         print(split_val[i])

# s = "Hello world this is test"
# print(s[s.find(' ')+1::])

# Str = "John 85, Alice 90, Bob abc, Mike 78"
# split_val = Str.split(',')
# for i in range(len(split_val)):
#     val = split_val[i].replace(" ","")
#     if not (val.isalpha()):
#         print(split_val[i].strip())

# Input = "   john@123   "
# split_val = Input.strip()
# print(split_val.isalnum())

# Input = "run --file=report.txt"
# print(Input[Input.find('--file=')+7::])

# Input = " 123, Gandhi Street, Chennai, 600001 "
# split_val = Input.split(",")
# for i in range(len(split_val)):
#     space_clean = split_val[i].strip()
#     split_val[i] = space_clean
# print(split_val)

# lines = ["This is line 1", "   ", "Second line", "\t  "]
# for i in range(len(lines)):
#     if lines[i].isspace():
#         print(f"Line {i+1} is empty")


# s = "abc 123 456 def"
# s_split = s.split()
# for i in range(len(s_split)):
#     if s_split[i].isdigit():
#         print(s_split[i])

# s = "  abc123 !@# 456  "
# s_strip = s.strip()
# s_splite = s_strip.split()
# for i in range(len(s_splite)):
#     if s_splite[i].isalnum():
#         print(s_splite[i])

# s = "Hello world this is test"
# s_space = s[s.find(" ")+1::]
# print(s_space)

# s = "apple,banana,grape"
# s_split = s.split(",")
# print(s_split)

# s = "   Hello World   "
# s_strip = s.strip()
# print(s_strip)

# s = "This is a test string"
# s_find = s.find("test")
# print(s_find)

# s = "12345"
# print(s.isdigit())

# s = "   "
# print(s.isspace())

# s = "abc123"
# print(s.isalnum())

# Input = "John 85, Alice 90, Bob abc, Mike 78"
# inp_split = Input.split(",")
# for i in range(len(inp_split)):
#     inp_repla = inp_split[i].replace(" ","")
#     if not (inp_repla.isalpha()):
#         print(inp_split[i].strip())