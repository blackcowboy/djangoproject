from django.http import JsonResponse


class ResponseUtil():
    @staticmethod
    def __getResponse(code, msg, data):
        return JsonResponse({'code': code, 'msg': msg, 'data': data}, json_dumps_params={'ensure_ascii': False})

    @staticmethod
    def ResultOK(data=[], msg=''):
        return ResponseUtil.__getResponse(code='OK', msg=msg, data=data)

    @staticmethod
    def ResultError(msg, data=[]):
        return ResponseUtil.__getResponse(code='ERROR', msg=msg, data=data)