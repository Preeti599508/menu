# from openai import OpenAI

# client = OpenAI()
# response = client.chat.completions.with_raw_response.create(
#     messages=[{
#         "role": "user",
#         "content": "Say this is a test",
#     }],
#     model="gpt-4o-mini",
# )
# print(response.headers.get('x-request-id'))

# # get the object that `chat.completions.create()` would have returned
# completion = response.parse()
# print(completion)

dist={
    "name":[],
    "age":[]
}
n=[]
a=[]

yn=input("do you want to visit data(y/n): ")
while yn=="y":
    op=int(input("1 for enter data \n 2 for show data \n enter your choice :"))
    if op==1:
        l=int(input("enter the len of data :"))
        for i in range(l):
            name=input("enter the name : ")
            age=int(input("enter the age : "))
            n.append(name)
            a.append(age)
            
    if op==2:
        for i in range(0,len(n)):
            print(n[i],a[i])
        yn=(input("do you want more : "))