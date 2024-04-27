with open("api.txt", "r") as f:
    lines = f.readlines()

for company in lines:
    if company['name'] == 'Warner Bros. Pictures':
        print(company)

























# f = open("api.txt", "r")
# print(f.readline()[20:30])
# f.close()
