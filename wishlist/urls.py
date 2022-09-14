from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_wishlist_xml
from wishlist.views import show_wishlist_json 
from wishlist.views import show_wishlist_json_filtered
from wishlist.views import show_wishlist_xml_filtered

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_wishlist_xml, name='show_wishlist_xml'),
    path('json/', show_wishlist_json, name='show_wishlist_json'),
    path('json/<int:id>', show_wishlist_json_filtered, name='show_wishlist_json_filtered'),
    path('xml/<int:id>', show_wishlist_xml_filtered, name='show_wishlist_xml_filtered'),
]