# from django.utils.deprecation import MiddlewareMixin
# from django.urls import resolve
# 
# class CSRFMiddleware(MiddlewareMixin):
#     def process_view(self, request, callback, callback_args, callback_kwargs):
#         # List of views to exempt from CSRF protection
#         exempt_views = [
#             'products.views.allProductList',
#             'products.views.allProductDetail'
#         ]
# 
#         if resolve(request.path_info).view_name in exempt_views:
#             setattr(request, '_dont_enforce_csrf_checks', True)
#         return None