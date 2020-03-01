from django.db import models

# 创建的表明为 模块名称_类名。如 userinfo_character
class Character(models.Model):
    name = models.CharField(max_length=200)
    # 用来说明对象的字符表达式。
    def __str__(self):
        return self.name
