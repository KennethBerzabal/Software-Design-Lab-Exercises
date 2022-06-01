a="pots&pans"
b=a.split("&")
c=[]
c=list(b)
def reverse(data,leng,leng2,index,count):
    rev=(leng-1)-count
    if count<leng/2:
        temp=data[index][count]
        data[index][count]=data[index][rev]
        data[index][rev]=temp
    if index==leng2:
        print(data[index-1]+"&"+data[index])
    return reverse(data,leng,leng2,index+1,count)
reverse(c,4,2,0,0)