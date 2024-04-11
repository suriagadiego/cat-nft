from django.urls import path
from .views import cat_mint_view, cat_list_view, cat_update_view
urlpatterns = [
    path(
        "list_all_cats/",
        cat_list_view.list_all_cats,
        name="list_all_cats"
    ),
    path(
        "list_my_cats/",
        cat_list_view.list_cats_by_owner,
        name="list_my_cats"
    ),
    path(
        "register_cat/",
        cat_mint_view.register_cat,
        name="register_cat",
    ),
    path(
        "update/<uuid:cat_uuid>/",
        cat_update_view.update_cat,
        name="update_cat"
    ),
]
