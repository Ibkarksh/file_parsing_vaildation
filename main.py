def id_email_validation(file_path):
    import re
    from dns.resolver import resolve
    data = open(file_path).readlines()
    separated_lines = []
    # Text Processing Stage
    for INDEX in range(len(data)):
        data[INDEX] = data[INDEX].split("\n")[0]
        separated_lines.append(data[INDEX].split(" "))
    #Looping over line by line
    for ELEMENT in separated_lines:
        #Add try catch to avoid int(non-integer) error
        try:
            int(ELEMENT[-1])
            regex_email = re.findall('^[A-Z a-z 0-9]+[\._]?[A-Z a-z 0-9]+[@]\w+[.]?\w{2,3}?$', ELEMENT[-2])
            if regex_email:
                domain = regex_email[0].split('@')[-1]
                bool(resolve(domain, 'MX'))
                if int(ELEMENT[-1]) % 2 == 0:
                    print(f"The {ELEMENT[-1]} of {ELEMENT[-2]} is even")
                else:
                    print(f"The {ELEMENT[-1]} of {ELEMENT[-2]} is odd")
        except:
            pass
#calling the function
id_email_validation("./data.txt")
