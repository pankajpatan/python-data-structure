# First Question
print('hello world'[8])


# second question
print('tinker'[1:4])

# third question
print(set('Mississippi'))

# four question
Samplelist= [(10, 20, 30), (40, 50, 90), (70, 80, 60)]
for i in range(len(Samplelist)):
    Samplelist[i]=list(Samplelist[i])
    Samplelist[i][-1]=100
    Samplelist[i]=tuple(Samplelist[i])
print(Samplelist)



# FIVE QUESTION 
Sampledata = {'1':['a','b'], '2':['c','d']}
Data1= Sampledata.get("1")
Data2=Sampledata.get('2')
def combine(x,y):
    for i in range(len(x)):
        for j in range(len(y)):
            print(x[i]+y[j])

combine(Data1,Data2)
