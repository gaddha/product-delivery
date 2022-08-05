from django.db import models
from django.db.models.signals import pre_save
from .utils import slug_pre_save_receiver
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class productsProductModel(models.Model):
    title = models.CharField(max_length=55,null=True)
    description = models.CharField(max_length=55)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, blank=True, null=True, unique=True)


    def __str__(self):
        return str(self.title)


pre_save.connect(slug_pre_save_receiver,sender=productsProductModel)



class produtsCategoryModel(models.Model):
    product = models.ForeignKey(productsProductModel,related_name='produtsCategoryModel_product',on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=55)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, blank=True, null=True, unique=True)


    def __str__(self):
        return self.title


pre_save.connect(slug_pre_save_receiver,sender=produtsCategoryModel)

class  productSubCategoryModel(models.Model):
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=55)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, blank=True, null=True, unique=True)

    def __str__(self):
        return self.title


pre_save.connect(slug_pre_save_receiver,sender=productSubCategoryModel)



class productsBrandModel(models.Model):
    title = models.CharField(max_length=55,unique=True)
    description = models.CharField(max_length=55)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, blank=True, null=True, unique=True)

    def __str__(self):
        return self.title


pre_save.connect(slug_pre_save_receiver,sender=productsBrandModel)



class productsAttributeModel(models.Model):
    product = models.ForeignKey(productsProductModel,related_name='productsAttributeModel_product',on_delete=models.CASCADE)
    category = models.ForeignKey(produtsCategoryModel,related_name='productsAttributeModel_category',on_delete=models.CASCADE,null=True)
    sub_category = models.ForeignKey(productSubCategoryModel, related_name='productsAttributeModel_sub_category',on_delete=models.CASCADE)
    brand = models.ForeignKey(productsBrandModel,related_name='productsAttributeModel_brand',on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(default=1.0)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, blank=True, null=True, unique=True)

    def __str__(self):
        return str(self.product)

pre_save.connect(slug_pre_save_receiver,sender=productsAttributeModel)

class productsCartModel(models.Model):
    user = models.OneToOneField(User,related_name='productsCartModel_user',on_delete=models.CASCADE)
    product = models.ManyToManyField(productsAttributeModel,related_name ='productsCartModel_product',blank=True)
    total = models.FloatField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250,blank=True, null=True, unique=True)


pre_save.connect(slug_pre_save_receiver,sender=productsCartModel)


class productsOrderModel(models.Model):

    user = models.ForeignKey(User,related_name='productsOrderModel_user',on_delete=models.CASCADE)
    products = models.ForeignKey(productsCartModel,related_name ='productsOrderModel_products',on_delete=models.CASCADE)
    STATUS=(
        ('IN PROGRESS','in progress'),
        ('IN TRANSIT','in transit'),
        ('DELIVERED','delivered')
    )
    status = models.CharField(max_length=12, choices=STATUS, default='IN PROGRESS')
    total = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, blank=True, null=True, unique=True)

    def __str__(self):
        return str(self.user)


pre_save.connect(slug_pre_save_receiver,sender=productsOrderModel)




class productpaymentsModel(models.Model):
    user = models.ForeignKey(User, related_name='paymentsModel_user', on_delete=models.CASCADE)
    product = models.ForeignKey(productsOrderModel, related_name='paymentsModel_products',
                                 on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    upin = models.CharField(max_length=3)
    STaTUS = (
        ('IN PROGRESS', 'in progress'),
        ('SUCCESS', 'success'),
    )
    payment_status = models.CharField(max_length=12, choices=STaTUS, default='IN PROGRESS')
    total_amount = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, blank=True, null=True, unique=True)

    def __str__(self):
        return str(self.products)


pre_save.connect(slug_pre_save_receiver, sender=productpaymentsModel)


