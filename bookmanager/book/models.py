from django.db import models

"""
1. Our model class needs to inherit from `models.Model`.

2. The system will automatically add a primary key for us: `id`.

3. Fields

   `field_name = models.Type(options)`

   The field name is actually the column name in the database table.

   Do not use Python, MySQL, or other reserved keywords as field names.

   `char(M)`

   `varchar(M)`

   `M` is the option/parameter.
"""
class BookInfo(models.Model):
    #id
    name=models.CharField(max_length=80, unique=True)
    pub_date=models.DateField(null=True)
    readcount=models.IntegerField(default=0)
    commentcount=models.IntegerField(default=0)
    is_delete=models.BooleanField(default=False)

    class Meta:
        db_table = "BookInfo"
        verbose_name = "Books"
    # Override the __str__ method so that the admin site displays the book name
    def __str__(self):
        return self.name

# Characters/people: copy it over first. Explain the principle later.
class PeopleInfo(models.Model):
    name = models.CharField(max_length=80)
    gender = models.BooleanField()
    # Foreign key constraint: which book the character belongs to.
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)