from .swaggerExample import SwaggerDemo
from .authentication import UserValidate

def initialize_routes(api):
    api.add_resource(SwaggerDemo,'/api/details')
	
	#Authentication class routes
    api.add_resource(UserValidate,'/api/userAuth/validateOtp')