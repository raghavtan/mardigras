from django.db import models

# Create your models here.
class category_list(models.Model):
    category_id = models.CharField(max_length=20, primary_key=True)
    category_name = models.CharField(max_length=60)
    category_desc = models.TextField(blank = True, null=True)
    icon_file_name = models.FilePathField(path="/categories/images",
                                          max_length=100, blank = True, null=True)
    def __str__(self):
        return self.category_name
    

class product_list(models.Model):
    product_id = models.CharField(max_length=20, primary_key=True)
    product_seq = models.CharField(max_length=20,blank = True, null=True)
    product_name = models.CharField(max_length=80,blank = True, null=True)
    product_s_desc = models.TextField(blank = True, null=True)
    product_colors = models.CharField(max_length=20,blank = True, null=True)
    product_sizes = models.CharField(max_length=60,blank = True, null=True)
    product_materials = models.CharField(max_length=20,blank = True, null=True)
    product_flavors = models.CharField(max_length=20,blank = True, null=True)
    product_thumbnail_url = models.FilePathField(path="/products/images/th",
                                                 max_length=100,blank = True, null=True)
    product_image_url = models.FilePathField(path="/products/images",
                                             max_length=100,blank = True, null=True)
    product_extra_flag = models.SmallIntegerField(blank = True, null=True)
    product_date_avail_from = models.DateField(auto_now=True,blank = True, null=True)
    product_date_avail_upto = models.CharField(max_length=20,blank = True, null=True)
    product_list_price = models.DecimalField(max_digits=10, decimal_places=2,
                                             blank = True, null=True)
    product_discount_id = models.CharField(max_length=10,blank = True, null=True)
    product_tax_id = models.CharField(max_length=20,blank = True, null=True)
    product_price_struct_id = models.CharField(max_length=20,blank = True, null=True)
    brand_id = models.CharField(max_length=20,blank = True, null=True)
    thumb_ok = models.NullBooleanField(blank = True, null=True)
    fullpic_ok = models.NullBooleanField(blank = True, null=True)
    def __str__(self):
        return self.product_id

class category_tree(models.Model):
    path_no = models.IntegerField(primary_key=True)
    parent_category = models.ForeignKey(category_list, related_name="parent")
    child_category = models.ForeignKey(category_list, related_name="child")
    def __str__(self):
        return str(self.path_no)

class category_table(models.Model):
    category_id = models.ForeignKey(product_list)
    product_id = models.ForeignKey(category_list)
    
