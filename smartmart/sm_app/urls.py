from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from .views import user_form_view
from . import views

urlpatterns = [
   
    path('openwindow',views.openwindow, name='openwindow'),
    path('signup/', views.signup, name='signup'),
    path('login/',views.login, name='login'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('about/', views.about, name='about'),
    path('aboutusshopowner/',views.aboutusshopowner,name='aboutusshopowner'),
    path('forgotpassword/',views.forgotpass, name='forgotpassword'),
     path('forgotpassshopowner/',views.forgotpassshopowner, name='forgotpassshopowner'),
    path('user_form/', views.user_form_view, name='user_form_submit'),
    path('login_operations/',views.login_operation, name='login_operation'),
    path('logout/',views.user_logout, name="user_logout"),
    
   path('activate/<uidb64>/<token>/', views.activate, name='activate'),
   
   
    path('home/',views.home, name='home'),
   path('profile/', views.profile, name='profile'),
   
    path('shopowner_reg_form', views.shopowner_reg_form, name='shopowner_reg_form'),
    path('shop_owner_details',views.shop_owner_details, name='shop_owner_details'),
    #  path('show_owner/',views.show_owner, name='show_owner'),
    # path('show_owner/<str:email>/', views.show_owner, name='show_owner'),
   
    path('register_shop', views.register_shop, name='register_shop'),
     path('shopowner_reg/',views.shopowner_reg, name='shopowner_reg'),
      path('shopreg/', views.shopreg, name='shopreg'),

   
    
    
    # path('shopor_reg/', viewswne.shopowner_reg, name='shopowner_reg'),
    # path('welcome_page_to_owner/', views.welcome_page_to_owner, name='welcome_page_to_owner'),  --------------
    #  path('welcome_page_to_owner/<str:shop_mail>/', views.welcome_page_to_owner, name='welcome_page_to_owner'),
      path('success_page/',views.success_page, name='success_page'),
    # path('register_shop/', views.register_shop, name='register_shop'),
    # path('success_page/', views.success_page, name='success_page'),
    
 


    # path('shopowner_reg/', views.shopowner_reg, name='shopowner_reg'),
    # path('welcome_page_to_owner/<str:email>/', views.welcome_page_to_owner, name='welcome_page_to_owner'),
    # path('shopreg/', views.register_shop, name='register_shop'),
    # path('success/', views.success_page, name='success_page'),
    path("shopowner_login", views.shopowner_login, name="shopowner_login"),
    path('ownerwelcome/',views.ownerwelcome, name='ownerwelcome'),
    path('shopowner_login_operation/',views.shopowner_login_operation , name='shopowner_login_operation'),
  path('maps/', views.maps, name='maps'),
  path('fgpm/', views.fgpm, name='fgpm'),
  path('fgpmshopowner/', views.fgpmshopowner, name='fgpmshopowner'),
  path('deliveryboyfgp/',views.deliveryboyfgp,name='deliveryboyfgp'),
  #  path('maps/', views.maps, name='maps'),
   path('forgotpasssucces/',views.forgotpasssucces,name='forgotpasssucces'),
   path('nearby-shops/', views.nearby_shops, name='nearby_shops'),
    # path('shopownerprofile/<int:owner_id>/', views.shopownerprofile, name='shopownerprofile'),
    path('shopownerprofile_op/', views.shopownerprofile_op, name='shopownerprofile_op'),
      path('orders/<int:shop_id>/', views.order_list_view, name='order_list_view'),
      path('update_order/<int:order_id>/', views.update_order_view, name='update_order_view'),
 path('shop_owner_profile/', views.shop_owner_profile, name='shop_owner_profile'),
 path('shopowner_onlyprofile/', views.shopowner_onlyprofile, name='shopowner_onlyprofile'),
      path('store-categories/', views.store_categories, name='store_categories'),  
       path('checkboxcategory/', views.checkboxcategory, name='checkboxcategory'),
       path('display_categories/',views.display_categories,name='display_categories'),
       path('display_categoriesshopowner/',views.display_categoriesshopowner,name="display_categoriesshopowner"),
        path('store_products/', views.store_products, name='store_products'),  
         path('checkboxproducts/', views.checkboxproducts, name='checkboxproducts'),
           path('add_products_view/<int:cid>/', views.add_products_view, name='add_products_view'),
         path('showcataddproducts/',views.showcataddproducts,name='showcataddproducts'),
           path('select-category/', views.select_category, name='select_category'),
    path('select-products/', views.select_products, name='select_products'),
    path('shopcatalog/', views.shopcatalog, name='shopcatalog'),
    # path('userselect_category/',views.userselect_category,name='userselect_category'),
    path('display_products/', views.display_products, name='display_products'),
    path('display_productsatshopowner/',views.display_productsatshopowner,name='display_productsatshopowner'),
     path('backdisplay_categories/',views.backdisplay_categories,name='backdisplay_categories'),
      path('add_to_list/', views.add_to_list, name='add_to_list'),
    path('display_selected_products/', views.display_selected_products, name='display_selected_products'),
    path('generate_invoice/', views.generate_invoice, name='generate_invoice'),
 path('remove_product_from_selection/', views.remove_product_from_selection, name='remove_product_from_selection'),
  path('generate_invoice_and_redirect/', views.generate_invoice_and_redirect, name='generate_invoice_and_redirect'),
 path('order/',views.order, name='order'),
  path('create_order/', views.create_order, name='create_order'),
    path('order_success/<int:order_id>/', views.order_success, name='order_success'),
         path('user_orders/', views.user_orders, name='user_orders'), 
         path('order_items/<int:order_id>/', views.order_items, name='order_items'),
          path('track-order/', views.track_order, name='track_order'),
            path('cancleorder/', views.cancleorder, name='cancleorder'),
            path('cancel_order/', views.cancel_order, name='cancel_order'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
          path('update-order-status/', views.update_order_status, name='update_order_status'),
          # path('checkout/<int:order_id>/', views.checkout, name='checkout'),  # Add this line
            # path('create_payment/', views.create_payment, name='create_payment'),
    # path('paymenthandler/', views.payment_handler, name='paymenthandler'),
          # path('initiate_payment/', views.initiate_payment, name='initiate_payment'),
    # path('paytm/response/', views.payment_response, name='payment_response'),
#  path('initiate_payment/', views.initiate_payment, name="initiate_payment"),
    # path('handlerequest/', views.handlerequest, name="HandleRequest"),

#  path('payment/', views.initiate_payment, name='initiate_payment'),
    # path('payment/callback/', views.payment_callback, name='payment_callback'),
    
    
    # path('checkout/', views.checkout, name="checkout"),
    # path('handlerequest/', views.handlerequest, name="HandleRequest"),
# Payment APIs

    path('payment/', views.payment, name = 'payment'),
    path('handlerequest/', views.handlerequest, name = 'handlerequest'),
    # path('typesofpayments/',views.typesofpayments, name='typesofpayments'),
    # path('cashondelivery/',views.cashondelivery,name="cashondelivery"), *****
    # path('orderdone',views.orderdone,name="orderdone"),***
    path('typesofpayments/',views.typesofpayments, name="typesofpayments"),
    path('cashondelivery/',views.cashondelivery,name="cashondelivery"),
    path('onlinepayment/',views.onlinepayment,name="onlinepayment"),
    path('cashoncollect/',views.cashoncollect,name="cashoncollect"),
    
    
    # path('delivery_boys/register/', views.delivery_boy_register, name='delivery_boy_register'),
    # path('orders/packed/',views.packed_orders, name='packed_orders'),
    # path('orders/pick/<int:order_id>/', views.pick_order, name='pick_order'),
    # path('deliver_order<int:order_id>/', views.deliver_order, name='deliver_order'),
    
    path('delivery_boy_register/', views.delivery_boy_register, name='delivery_boy_register'),
    path('delivery_boy_login/', views.delivery_boy_login, name='delivery_boy_login'),
    path('delivery_boy_logout/', views.delivery_boy_logout, name='delivery_boy_logout'),
    path('orders/packed/', views.packed_orders, name='packed_orders'),
    path('orders/pick/<int:order_id>/', views.pick_order, name='pick_order'),
    path('orders/deliver/<int:order_id>/', views.deliver_order, name='deliver_order'),
    path('dispatched_orders/', views.dispatched_orders, name='dispatched_orders'),
    path('delivery_boy_home/', views.delivery_boy_home, name='delivery_boy_home'),
    path('delivery_boy/profile/', views.delivery_boy_profile, name='delivery_boy_profile'),
    path('delivery_boy/orders/', views.delivery_boy_orders, name='delivery_boy_orders'),
    
    path('picked_order_route/<int:order_id>/', views.picked_order_route, name='picked_order_route'),
    
    
    path('payment_success/',views.payment_success,name="payment_success"),
  
  
  path('update_price/<int:product_id>/', views.update_price, name='update_price'),
   path('edit_profile/', views.edit_profile, name='edit_profile'),
   path('edit_ownerprofile/',views.edit_ownerprofile,name='edit_ownerprofile'),
   path('edit_deliveryprofile/',views.edit_deliveryprofile,name='edit_deliveryprofile'),
   
   
   path('feedback_view/', views.feedback_view, name='feedback_view'),
   path('feedback_owner/', views.feedback_owner, name='feedback_owner'),
   
   path('services_view/', views.services_view, name='services_view'),
   
   path('shopownerlogout/',views.shopownerlogout,name="shopownerlogout"),
   
   path('smart/',views.smart, name='smart'),
   
   path('password_options/',views.password_options,name="password_options"),


path('password_reset/', views.password_reset_request, name='password_reset'),
    path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', views.password_reset_complete, name='password_reset_complete'),
    path('reset/invalid/', views.password_reset_invalid, name='password_reset_invalid'),
    path('toggle_product_status/<int:product_id>/', views.toggle_product_status, name='toggle_product_status'),

    
    #  path('toggle_product_status/<int:product_id>/', views.toggle_product_status, name='toggle_product_status'),
    # Generating Invoice
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)