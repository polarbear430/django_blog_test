from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
# Create your models here.

#分类 类
@python_2_unicode_compatible
class Category(models.Model):
	"""docstring for Category
	django 模型要继承models.Model 类
	Category 表只需要 分类名 一列（id 自动生成）；
	CharField 是数据类型， 设置最大长度为 100
	"""
	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

#标签 类
@python_2_unicode_compatible
class Tag(models.Model):
	"""docstring for Tag"""
	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name
#文章 类
@python_2_unicode_compatible
class Post(models.Model):
	"""docstring for Post
	标题
	正文
	创建时间
	最后修改时间
	摘要 blank = True 参数可以取空值
	分类
	标签
	作者
	"""
	title = models.CharField(max_length = 70)

	body = models.TextField()
	#短的字符串用CharField，长的正文用TextField类型

	create_time = models.DateTimeField()

	modified_time = models.DateTimeField()

	excerpt = models.CharField(max_length = 200, blank = True)
	
	views =  models.PositiveIntegerField(default=0)
	#一篇文章只能有一个分类-> ForeignKey，
	#       但可以有多个标签->ManyToManyField
	category = models.ForeignKey(Category)

	tag = models.ManyToManyField(Tag, blank = True)

	author = models.ForeignKey(User)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:detail', kwargs={'pk':self.pk})
	def increase_views(self):
		self.views +=1
		self.save(update_fields=['views'])
	class Meta:
		ordering = ['-create_time']
