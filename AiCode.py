from numpy import *

#get the accuracy level
alpha = double(input("select the accurecy level: "))

#is acc decimal?
if alpha % 1 == 0:
    int(alpha)

#training model data
dataset = [[2,2],[4,4],[1.5,1.5],[7,7]]

#prediction to make
prediction = [3,6,11,14,0]

#error saving
dserror = []
texample= [] # items look like [w,b]

#weight and bias
w = 0.01 
b = 0.01

#Calculation process
def fun(x,weight,bias):
    y = (x*weight)+bias
    return y

#define the error cost
def CostF(data,weight,bias,ErrorSaver,WBSaver):
    listitem = []
    avg = 0
    for li in data:
        x = li[0]
        y = li[1]
        yh=fun(x,weight,bias)
        listitem.append((yh - y)**2)
    for i in listitem:
        avg += i
    avg /= len(listitem)*2
    store(avg,weight,bias,ErrorSaver,WBSaver)
    return avg

#store the important data at the moment 
def store(inp,weight,bias,ErrorSaver,WBSaver):
    ErrorSaver.append(inp)
    WBSaver.append([weight,bias])

#look for the minimum error cost
def look(weight,bias,ErrorSaver,WBSaver):
    prediction = 0
    for i in range(len(ErrorSaver)):
        if ErrorSaver[i] == 0:
            prediction = ErrorSaver[i]
            return i
        elif i != 0:
            if ErrorSaver[i] < ErrorSaver[prediction]:
                prediction = i
    return ErrorSaver.index(ErrorSaver[prediction])

#take the minumum error cost and finds the optimal weight and bias
def MinimumErrorCost(weight,bias,ErrorSaver,WBSaver):
    a = look(weight,bias,ErrorSaver,WBSaver)
    weight,bias = texample[a][0] , texample[a][1]
    return weight,bias

#define the proper weight and bias
def GradientDecesnt(alpha,Data,weight,bias,ErrorSaver,WBSaver):
    #NewW = weight
    #NewB = bias
    weight, bias = 0, 0
    #AverageVarW, AverageVarB = 0, 0
    iii = 0
    while iii < 100/alpha:
        """ if CostF(Data,NewW,NewB,ErrorSaver,WBSaver) < CostF(Data,weight,bias,ErrorSaver,WBSaver):
                Mass = len(Data)
                for i in range(len(Data)):
                    AverageVarW += (Data[i][0]*(fun(Data[i][0],weight,bias)-Data[i][1]))
                for i in Data:
                    AverageVarB += (fun(Data[i][0],weight,bias)-Data[i][1])
                NewW += w - AverageVarW*(alpha/Mass)
                NewB += b - AverageVarB*(alpha/Mass)
                store(CostF(Data,NewW,NewB,ErrorSaver,WBSaver),NewW,NewB,ErrorSaver,WBSaver)
            else:
                store(CostF(Data,NewW,NewB,ErrorSaver,WBSaver),NewW,NewB,ErrorSaver,WBSaver)
            iii += 1"""
        bbb = 0
        while bbb < 100/alpha:
            store(CostF(Data,weight,bias,ErrorSaver,WBSaver),weight,bias,ErrorSaver,WBSaver)
            bias += alpha
            bbb += 1 
        store(CostF(Data,weight,bias,ErrorSaver,WBSaver),weight,bias,ErrorSaver,WBSaver)
        weight += alpha
        bias = 0
        iii += 1

#runs a test
def TestAi(predict,weight,bias):
    res = []
    for inp in predict:
        SaveRes = int(fun(inp,weight,bias)*100000)/100000
        if SaveRes % 1 == 0:
            res.append(int(SaveRes))
        else:
            res.append(SaveRes)
    return res

#Runs indefinetly till the program reaches a fault
def NewTest():
    NewVar = 0
    while True:
        SaveRes = fun(NewVar,w,b)
        if SaveRes != NewVar:
            print(f"failure at calculating {NewVar} and got {SaveRes} instead of {(NewVar*2)+1}")
        NewVar += 1

#pieces of the puzzle together. printing result of the test above
def main(Alpha,weight,bias,ErrorSaver,WBSaver,Data,Input):
    GradientDecesnt(Alpha,Data,weight,bias,ErrorSaver,WBSaver)
    weight, bias = MinimumErrorCost(weight,bias,ErrorSaver,WBSaver)
    MainRes = TestAi(Input,weight,bias)
    for i in range(len(MainRes)):
        print(f"{MainRes[i]} \n")
    #NewTest()

main(alpha,w,b,dserror,texample,dataset,prediction)
