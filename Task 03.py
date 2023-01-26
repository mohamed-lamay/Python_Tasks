def is_balanced(s):
    brackets = ['()', '[]', '{}']
    while any(x in s for x in brackets):
        for br in brackets:
            s = s.replace(br, '')
        print("s ",s)
        if s in brackets or s == '':
            print ("yes")
        else:
            print ("no")
is_balanced('([{}])')