from django.db import models


# Create your models here.
class ArticleType(models.Model):
    """
    博客类别实体
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField('', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "博客类别管理"
        verbose_name_plural = "博客类别管理"
