from datetime import datetime
from django.db import models
from django.contrib.auth.hashers import make_password,check_password
# Create your models here.

class mainuser(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_fname = models.CharField(max_length=35, null=False)
    user_lname = models.CharField(max_length=35, null=False)
    user_mail = models.EmailField(unique=True, null=False)
    user_password = models.CharField(max_length=128, null=False)
    user_dob = models.DateField( null=False)
    user_phonenumber = models.BigIntegerField( null=False)
    is_active = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)


    def check_password(self, raw_email,raw_password):
        # Implement password validation logic here
        if (self.user_mail == raw_email) and (self.user_password == raw_password):
            return True
        else:
            return False

    def check_mail(self, mail):
        if self.user_mail == mail:
            return True
        else:
            return False
    
    
    class Meta:
        db_table ="sm_app_mainuser"
        


# class shopowner(models.Model):
#     o_id=models.AutoField(primary_key=True)
#     o_name = models.CharField(max_length=35, null=False)
#     o_mail = models.EmailField(unique=True, null=False)
#     o_password = models.CharField(max_length=128, null=False)
#     o_dob = models.DateField( null=False)
#     o_phonenumber = models.BigIntegerField( null=False)
#     o_address = models.CharField(max_length=200,null=False)
    
    
#     class Meta:
#         db_table ="sm_app_shopowner"
        
        


class ShopOwner(models.Model):
    o_id = models.AutoField(primary_key=True)
    o_name = models.CharField(max_length=35, null=False)
    o_mail = models.EmailField(unique=True, null=False)
    o_password = models.CharField(max_length=128, null=False)
    o_dob = models.DateField(null=False)
    o_phonenumber = models.BigIntegerField(null=False)
    o_address = models.CharField(max_length=200, null=False)
    
    
    # def c_password(self,raw_password):
    #     # Implement password validation logic here
    #     if  (self.o_password == raw_password):
    #         return True
    #     else:
    #         return False
    
    class Meta:
        db_table = "sm_app_shopowner"



# class SuperMarket(models.Model):
#     s_id = models.AutoField(primary_key=True)
#     s_name = models.CharField(max_length=50, null=False)
#     s_mail = models.EmailField(unique=True, null=False)
#     s_phonenumber = models.BigIntegerField(null=False)
#     s_type = models.CharField(max_length=100, null=False)
#     s_address = models.CharField(max_length=200, null=False)
#     s_opentime=models.TimeField(null=False)
#     s_closetime=models.TimeField(null=False)
#     latitude = models.FloatField(default=0)
#     longitude = models.FloatField(default=0)
#     image = models.ImageField(upload_to='myapp/images/', null=True, blank=True)
#     owner = models.ForeignKey(ShopOwner, on_delete=models.CASCADE)
    
    
#     class Meta:
#         db_table = "sm_app_supermarket"
        
from django.db import models
from .models import ShopOwner

def supermarket_image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/myapp/images/<filename>
    return f'myapp/images/{filename}'

class SuperMarket(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=50, null=False)
    s_mail = models.EmailField(unique=True, null=False)
    s_phonenumber = models.BigIntegerField(null=False)
    s_type = models.CharField(max_length=100, null=False)
    s_address = models.CharField(max_length=200, null=False)
    s_opentime = models.TimeField(null=False)
    s_closetime = models.TimeField(null=False)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    image = models.ImageField(upload_to=supermarket_image_path, null=True, blank=True)
    owner = models.ForeignKey(ShopOwner, on_delete=models.CASCADE)
    
    
    class Meta:
        db_table = "sm_app_supermarket"

# def supermarket_image_path1(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/myapp/images/<filename>
#     return f'cate/{filename}'

class categories(models.Model):
    category_id=models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to=supermarket_image_path, null=True, blank=True)
    template_name = models.CharField(max_length=100, default='checkboxproducts.html')
    extemplate_name = models.CharField(max_length=100, default='existing_products.html')
    # image = models.ImageField(upload_to=supermarket_image_path1, null=True, blank=True)
    shop = models.ForeignKey(SuperMarket, on_delete=models.CASCADE)
 
    
    
    class Meta:
        db_table = "sm_app_categories"


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_price=models.FloatField(default=0.0, null=True)
    quantity = models.IntegerField(default=1) 
    product_image = models.ImageField(upload_to=supermarket_image_path, null=True, blank=True)
    product_staus=models.BooleanField(default=True)
    category = models.ForeignKey(categories, on_delete=models.CASCADE)
    shop = models.ForeignKey(SuperMarket, on_delete=models.CASCADE)
    
    
    
    class Meta:
        db_table = "sm_app_product"



class DeliveryBoy(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        db_table = "sm_app_deliveryboy"


class Order(models.Model):
    STATUS_CHOICES = [
        ('PLACED', 'Placed'),
        ('ORDERCOMMITTED', 'OrderCommitted' ),
        ('PACKED', 'Packed'),
        ('DISPATCHED', 'Dispatched'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]

    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(mainuser, on_delete=models.CASCADE)
    shop_owner = models.ForeignKey(ShopOwner, on_delete=models.CASCADE)
    supermarket = models.ForeignKey(SuperMarket, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField()
    payment_status = models.CharField(max_length=50, default="PENDING")
    order_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='PLACED')
    is_new = models.BooleanField(default=True)  # New field
    order_deliverysoc=models.CharField(max_length=100, default="none")
    order_deliverydec=models.CharField(max_length=100, default="none")
    delivery_boy = models.ForeignKey(DeliveryBoy, on_delete=models.SET_NULL, null=True, blank=True)
    # deliveryed_date=models.DateTimeField(auto_now_add=True)
    delivered_date = models.DateField(default=datetime.now)

    def __str__(self):
        return f"Order ID: {self.order_id}, User: {self.user.user_mail}, Total Price: {self.total_price}, Payment Status: {self.payment_status}"

    def update_status_to_next(self):
        status_sequence = ['PLACED', 'ORDERCOMMITTED','PACKED', 'DISPATCHED', 'DELIVERED']
        current_index = status_sequence.index(self.order_status)
        if current_index < len(status_sequence) - 1:
            self.order_status = status_sequence[current_index + 1]
            self.save()
    
    def cancel_order(self):
        if self.order_status not in ['Delivered', 'Canceled']:
            self.order_status = 'Canceled'
            self.save()
            return True
        return False
    
    def update_payment_status(self, new_status):
        self.payment_status = new_status
        self.save()

    class Meta:
        db_table = "sm_app_order"


class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField()

    def __str__(self):
        return f"Order Item ID: {self.order_item_id}, Order ID: {self.order.order_id}, Product: {self.product.product_name}"

    class Meta:
        db_table = "sm_app_orderitem"



class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)
    amount = models.FloatField()
    payment_status = models.CharField(max_length=50 , default='PENDING')
    razorpay_order_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_payment_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_signature = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"Payment ID: {self.payment_id}, Order ID: {self.order.order_id}, Amount: {self.amount}, Status: {self.payment_status}"

    def update_order_payment_status(self, new_status):
        self.payment_status = new_status
        self.save()
        self.order.update_payment_status(new_status)

    class Meta:
        db_table = "sm_app_Payment"

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    update_desc = models.CharField(max_length=500)
    update_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Update ID: {self.update_id}, Order ID: {self.order.order_id}, Timestamp: {self.update_timestamp}"

    class Meta:
        db_table = "sm_app_OrderUpdate"
# class Payment(models.Model):
#     payment_id = models.AutoField(primary_key=True)
#     order = models.OneToOneField(Order, on_delete=models.CASCADE)
#     payment_date = models.DateTimeField(auto_now_add=True)
#     payment_method = models.CharField(max_length=50)  # e.g., 'Paytm'
#     amount = models.FloatField()
#     payment_status = models.CharField(max_length=50)  # e.g., 'Pending', 'Completed'
#     transaction_id = models.CharField(max_length=100, null=True, blank=True)  # Paytm transaction ID

#     class Meta:
#         db_table = "sm_app_Payment"



# # class Order(models.Model):
# #     order_id = models.AutoField(primary_key=True)
# #     user = models.ForeignKey(mainuser, on_delete=models.CASCADE)
# #     shop_owner = models.ForeignKey(ShopOwner, on_delete=models.CASCADE)
# #     supermarket = models.ForeignKey(SuperMarket, on_delete=models.CASCADE)
# #     order_date = models.DateTimeField(auto_now_add=True)
# #     total_price = models.FloatField()
    
# #     # Payment-related fields
# #     payment_date = models.DateTimeField(auto_now_add=True)
# #     payment_method = models.CharField(max_length=50)  # e.g., 'Paytm'
# #     amount = models.FloatField()
# #     PAYMENT_STATUS_CHOICES = [
# #         ('Pending', 'Pending'),
# #         ('Completed', 'Completed'),
# #         ('Failed', 'Failed'),
# #     ]
# #     payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS_CHOICES)  # e.g., 'Pending', 'Completed'
# #     transaction_id = models.CharField(max_length=100, null=True, blank=True)  # Paytm transaction ID

# #     class Meta:
# # #         db_table = "sm_app_Order"

# class Order(models.Model):
#     order_id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(mainuser, on_delete=models.CASCADE)
#     shop_owner = models.ForeignKey(ShopOwner, on_delete=models.CASCADE)
#     supermarket = models.ForeignKey(SuperMarket, on_delete=models.CASCADE)
#     order_date = models.DateTimeField(auto_now_add=True)
#     total_price = models.FloatField()
#     payment_status = models.CharField(max_length=50, default="PENDING")

#     def __str__(self):
#         return f"Order ID: {self.order_id}, User: {self.user.user_mail}, Total Price: {self.total_price}, Payment Status: {self.payment_status}"

#     class Meta:
#         db_table = "sm_app_Order"

#     def update_payment_status(self, new_status):
#         self.payment_status = new_status
#         self.save()


# class OrderItem(models.Model):
#     order_item_id = models.AutoField(primary_key=True)
#     order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#     price = models.FloatField()

#     def __str__(self):
#         return f"Order Item ID: {self.order_item_id}, Order ID: {self.order.order_id}, Product: {self.product.product_name}"

#     class Meta:
#         db_table = "sm_app_OrderItem"


# class Payment(models.Model):
#     payment_id = models.AutoField(primary_key=True)
#     order = models.OneToOneField(Order, on_delete=models.CASCADE)
#     payment_date = models.DateTimeField(auto_now_add=True)
#     payment_method = models.CharField(max_length=50)  # e.g., 'Credit Card', 'PayPal'
#     amount = models.FloatField()
#     payment_status = models.CharField(max_length=50)  # e.g., 'Pending', 'Completed'

#     def __str__(self):
#         return f"Payment ID: {self.payment_id}, Order ID: {self.order.order_id}, Amount: {self.amount}, Status: {self.payment_status}"

#     class Meta:
#         db_table = "sm_app_Payment"

#     def update_order_payment_status(self, new_status):
#         self.payment_status = new_status
#         self.save()
#         # Update associated order's payment status
#         self.order.update_payment_status(new_status)


# class OrderUpdate(models.Model):
#     update_id = models.AutoField(primary_key=True)
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     update_desc = models.CharField(max_length=500)
#     update_timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Update ID: {self.update_id}, Order ID: {self.order.order_id}, Timestamp: {self.update_timestamp}"

#     class Meta:
#         db_table = "sm_app_OrderUpdate"

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "Feedback"