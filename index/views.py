from django.http import HttpResponse
from django.template import loader, Template, Context  # 导入loader方法
from django.shortcuts import render  # 导入render 方法


def test(request):
    t = loader.get_template('test.html')
    html = t.render({'name': 'c语言中文网'})  # 以字典形式传递数据并生成html
    return HttpResponse(html)  # 以 HttpResponse方式响应html


# Create your views here.
def hello(request):
    a = {'vaule': 'hello my django'}
    return render(request, "hello.html", a)


def test_html(request):
    a = {'name': 'C语言中文网', 'course': ["Python", "C", "C++", "Java"],
         'b': {'name': 'C语言中文网', 'address': 'http://c.biancheng.net/'}, 'test_hello': test_hello,
         'class_obj': Website()}  # 创建空字典，模板必须以字典的形式进行传参
    return render(request, 'test_html.html', a)


def test_hello():
    return '欢迎来到C语言中文网'


class Website:
    def Web_name(self):
        return 'Hello，C语言中文网!'
    # Web_name.alters_data=True #不让Website()方法被模板调用


def test_for(request):
    # 调用template()方法生成模板
    t1 = Template("""
                    {% for item in list %}
                        <li>{{ item }}</li>
                    {% empty %}
                        <h1>如果找不到你想要，可以来C语言中文网(网址：http://c.biancheng.net/)</h1>
                    {% endfor %}
                              """)
    # 调用 Context()方法
    c1 = Context({'list': ['Python', 'Java', 'C', 'Javascript', 'C++']})
    html = t1.render(c1)
    return HttpResponse(html)


def test_if(request):
    dic = {'x': 2 ** 4}
    return render(request, 'test_if.html', dic)


def test01_for(request):
    # 使用嵌套for标签依次遍历列表取值
    website = Template("""
     {% for course in list01 %}
     <div>
        {% for coursename in course %}
        <p><b>{{ coursename }}</b></p>
        {% endfor %}
     </div>
     {% endfor %}
     """)
    webname = Context({'list01': [['Django', 'Flask', 'Tornado'], ['c语言中网', 'Django官网', 'Pytho官网']]})
    html = website.render(webname)
    return HttpResponse(html)


def test_forloop(request):
    a = Template("""
     {% for item in lists %}
     <div>
        <p><b>{{ forloop.counter }}:{{ item }}</b></p>
     </div>
     {% endfor %}
     """)
    b = Context({'lists': ['c语言中网', 'Django官网', 'Python官网']})
    html = a.render(b)
    return HttpResponse(html)  # 数字与元素以 1:'c语言中文网' 的形式出现


def test_url(request):
    return render(request, 'test_url.html')
