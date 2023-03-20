def simple_middleware(get_response):
    def MW(request):
        response = get_response(request)
        print("oooookkkkk")
        return response
    return MW


class MiddlewareSet:
    def __init__(self,get_response):
        self.get_response = get_response
        
    def __call__(self,request):
        response = self.get_response(request)
        print("class level middleware")
        return response