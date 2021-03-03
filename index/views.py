from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Template, Context  # 导入loader方法
from django.shortcuts import render  # 导入render 方法
from django.urls import reverse

from index.models import Author


def test(request, id):
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


def tag(request):
    t = Template("""
    {% load index_tags %}
    {% addstr_tag 'Django BookStore' %}
    """)
    html = t.render(Context())
    return HttpResponse(html)


def in_tag(request):
    t = Template("""
       {% load index_tags %}
       {% add_webname_tag 'C 语言中文网' %}

       """)
    html = t.render(Context({'varible': 'Hello'}))
    return HttpResponse(html)


def base_html(request):
    return render(request, 'base.html')


def index_html(request):
    name = 'xiaoming'
    course = ['python', 'django', 'flask']
    return render(request, 'base_test.html', locals())


def filter_tag(request):
    t = Template("""
        {% load index_tags %}
        <h1>:{{ Web|hello_my_filter }}</h1>
        """)
    html = t.render(Context({'Web': 'Web django Django'}))
    return HttpResponse(html)


def redict_url(request):
    return render(request, 'newtest.html')


def test_to_reverse(request):
    return HttpResponseRedirect(reverse
                                ('index:detail_hello', current_app=request.resolver_match.namespace))


def year_test(request, year):
    year = int(year)  # 转换整形


def num1_view(request, id):
    pass


def num2_view(request, id):
    pass


def num3_view(request, id):
    pass


def BookName(request):
    # books = Book.objects.raw("select * from index_book")  # 书写sql语句
    authors = Author.objects.raw("select id from index_author where name= %s", ['Tom'])
    return render(request, "allbook.html", locals())


# 在index/views.py 添加代码
from django.db.models import Count
from index.models import Book, PubName


def test_annotate(request):
    # 得到所有出版社的查询集合QuerySet
    bk_set = Book.objects.values('price')
    # bk=Book.objects.get(id=1)
    # print('书名:',bk.title,'出版社是:',bk.pub.pubname)
    # 根据出版社QuerySet查询分组，出版社和Count的分组聚合查询集合
    bk_count_set = bk_set.annotate(myCount=Count('price'))  # 返回查询集合
    for item in bk_count_set:  # 通过外键关联进行查询bk_set.pub.pubname
        print("价格是:", item['price'], "同等价格书籍数量：", item['myCount'])
        print(item)
    return HttpResponse('请在CMD命令行控制台查看结果')
# 路由配置为忘记:path('annotate/',views.test_annotate)
