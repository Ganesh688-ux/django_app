class CustomHeaderMiddleware:
    def __init__(self,get_response):
        # print('CustomHeader__init__')
        self.get_response = get_response
    def __call__(self,request):
        #  print('CustomHeader __call__')
        response = self.get_response(request)
        response['X-Custom-Header'] = 'My custom Value'
        return response