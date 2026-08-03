# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from criteo_api_api_experimental.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from criteo_api_api_experimental.model.base_type import BaseType
from criteo_api_api_experimental.model.base_type_list_request import BaseTypeListRequest
from criteo_api_api_experimental.model.base_type_list_response import BaseTypeListResponse
from criteo_api_api_experimental.model.base_type_request import BaseTypeRequest
from criteo_api_api_experimental.model.base_type_resource import BaseTypeResource
from criteo_api_api_experimental.model.base_type_response import BaseTypeResponse
from criteo_api_api_experimental.model.common_problem import CommonProblem
from criteo_api_api_experimental.model.derived_type_one import DerivedTypeOne
from criteo_api_api_experimental.model.derived_type_one_request import DerivedTypeOneRequest
from criteo_api_api_experimental.model.derived_type_one_resource import DerivedTypeOneResource
from criteo_api_api_experimental.model.derived_type_one_response import DerivedTypeOneResponse
from criteo_api_api_experimental.model.derived_type_two import DerivedTypeTwo
