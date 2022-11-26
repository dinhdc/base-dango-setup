from drf_yasg import openapi


list_address_params = [
    openapi.Parameter("limit", openapi.IN_QUERY, type=openapi.TYPE_NUMBER,
                      description="Number of results to return per page."),
    openapi.Parameter("offset", openapi.IN_QUERY, type=openapi.TYPE_NUMBER,
                      description="The initial index from which to return the results."),
    openapi.Parameter("parent", openapi.IN_QUERY, type=openapi.TYPE_STRING,
                      description="Filter results by uid of parent"),
]
