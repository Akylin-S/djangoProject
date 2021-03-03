from django.db import models
from django.db.models import F

# 新建出版社表
class PubName(models.Model):
    pubname = models.CharField('名称', max_length=255, unique=True)


# Create your models here.
class Book(models.Model):  # 创建 book 表
    title = models.CharField(max_length=30, unique=True, verbose_name='书名')
    public = models.CharField(max_length=50, verbose_name='出版社')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='定价')

    def default_price(self):
        return '￥30'

    retail_price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='零售价', default=default_price)
    pub = models.ForeignKey(to=PubName, on_delete=models.CASCADE, null=True)  # 创建Foreign外键关联pub,以pub_id关联

    def __str__(self):
        return "title:%s pub:%s price:%s" % (self.title, self.public, self.price)


class BookExtend(Book):
    """
    BOOK代理模型
    """

    class Meta:
        ordering = ['id']  # 定义Meta选项顺序排序按照id字段
        proxy = True  # 设置代理模型

    def __str__(self):
        return "title:%s pub:%s price:%s" % (self.title, self.pub, self.price)  # 定义方法


class Author(models.Model):  # 创建作者表
    name = models.CharField(max_length=30, verbose_name='姓名')
    email = models.EmailField(verbose_name='邮箱')
    books = models.ManyToManyField(to="Book")

    def __str__(self):
        return '作者：%s' % self.name


class UserInfo(models.Model):  # 创建用户信息表
    username = models.CharField(max_length=24, verbose_name='用户注册')
    password = models.CharField(max_length=24, verbose_name='密码')
    choices = (
        ('male', '男性'),
        ('female', '女性'),
    )
    gender = models.CharField(max_length=6, choices=choices, default='male')


# 新建一对一关用户信息表拓展表,添加完成后执行数据库迁移同步操作
class ExtendUserinfo(models.Model):
    user = models.OneToOneField(to=UserInfo, on_delete=models.CASCADE)
    signature = models.CharField(max_length=255, verbose_name='用户签名', help_text='自建签名')
    nickname = models.CharField(max_length=255, verbose_name='昵称', help_text='自建昵称')


class AbstractBase(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=100)
    username = models.CharField(max_length=80)
    nowday = models.DateTimeField()

    class Meta:
        abstract = True


class SomeThing(AbstractBase):
    testexams = models.CharField(max_length=50)


class SomeComment(AbstractBase):
    level = models.CharField(max_length=20)


