from django.shortcuts import render  #渲染
from django.http import HttpResponse  #导入包，必须项

# Create your views here.
def Game(request,path):
    st=path.split('/')
    html=int(st[0])+int(st[2]) if st[1]=="add" else int(st[0])-int(st[2])
    return HttpResponse({
        html})

def compute(request):
    x = int(request.POST.get("x")) if request.POST.get("x") else 1
    y = int(request.POST.get("y")) if request.POST.get("y") else 1
    op = request.POST.get("op") if request.POST.get("op") else "add"
    z = {}
    z["x"] = x
    z["y"] = y
    z["op"] = op
    if op == "add":
        z["val"] = x + y
    elif op == "sub":
        z["val"] = x -y
    elif op == "mul":
        z["val"] = x * y
    else:
        z["val"] = x / y
    if request.method == "POST":
        return render(request, "game.html", z)
    else:
        return render(request, "game.html")
        

def test(a):

    return a*a

class person():

    def myname(name,age):
        return strcat(self.name,self.age)
    

def Test_Flitter(request):
    
    dist={}
    dist["dint"] = 1
    dist["dtuple"] = (1, 2, 3)
    dist["dlist"] = [4, 5, 6]
    dist["dmap"] = {"name":"tt", "age":"24",}
    dist["dfunc"] = test   #这里传入参数名，不加括号，加括号表示执行结果。
    dist["dobj"] = person() #实例化
    dist["script"] = "<script>alert('111')</script>"
    print(dist["dlist"][1])
    return render(request, 'test_flitter.html', dist) #渲染html页面，注意一定打引号，否则被视为变量，而这里需要变量render(request, html文件地址)默认是在templates下查找,render()中第三个参数为视图views传给模板也就是html页面的字典，第三个参数只能为字典。

def Test_If_For(request):
    
    dist = {}
    dist["number"] = [1, 2 ,3]
    return render(request, "test_if_for.html", dist)
