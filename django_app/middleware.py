class CustomHeaderMiddleware:

    def _init_(self,get_response):
        print('CustomHeader _init_ ')
        self.get_response = get_response

    def _call_(self, request):
        print('CustomHeader _call_ ')
        response = self.get_response(request)
        response['X-Custom-Header'] = 'My Custom Value'
        return response