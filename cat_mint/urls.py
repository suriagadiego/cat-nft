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
    # path(
    #     "<uuid:product_uuid>/",
    #     product_detail_view.get_product_by_uuid,
    #     name="product_detail_view",
    # ),
    # path(
    #     "id/<int:product_id>/",
    #     product_detail_view.get_product_by_id,
    #     name="product_detail_view_id",
    # ),
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
    # path(
    #     "delete/<uuid:product_uuid>/",
    #     product_delete_view.delete_product,
    #     name="delete_product"
    # )
]
# path('part/<int:pk>/', rest_part_no.part_no_detail_view,  name='part_no-detail'),
# path('part/create/', rest_part_no.part_no_create_view, name='part_no_create'),
# path('part/update/<int:pk>/', rest_part_no.part_no_update_view, name='part_no_update'),
# path('part/search/', rest_part_no.part_no_search_view, name='part_no_search'),
# path('part/batch_delete/', rest_part_no.part_delete_apiview, name='part_no_delete'),
# path('part/bulk/create/', rest_part_no.bulk_create_parts , name='part_bulk_create'),
