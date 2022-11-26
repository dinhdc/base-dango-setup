from drf_yasg.inspectors import SwaggerAutoSchema

# custom tag schema for swagger models


class CustomAutoSchema(SwaggerAutoSchema):

    def get_tags(self, operation_keys=None):
        tags = self.overrides.get('tags', None) or getattr(
            self.view, 'module', [])
        if not tags:
            tags = [operation_keys[0]]

        return tags
