from django.http import JsonResponse
import hashlib
import time

API_KEY = '456kbasdcy9lansdeeefasdfl.{004kk;'
AUTH_TIME = 30
AUTH_LIST = [
    # {"key":, "time":}
]


def auth_status(request):
    if request.method == "POST":
        tm_key = request.META['HTTP_AUTH_KEY']
        if not tm_key:
            return False
        tm_list = tm_key.split('|')
        if len(tm_list) != 2:
            return False
        auth_key, time_stamp=tm_list

        limit_time = time.time() - AUTH_TIME
        print(limit_time, time_stamp)
        # key will be invalid after 30 seconds, time validation
        if limit_time > float(time_stamp):
            return False

        h = hashlib.md5()
        h.update(bytes("%s|%s"%(API_KEY, time_stamp), encoding='utf-8'))
        h_key = h.hexdigest()
        # valid key with server key
        if auth_key != h_key:
            return False

        exist = False
        del_keys=[]
        # validate the key if the key is used before, if it pass the time validation, but the key is used again
        for k, v in enumerate(AUTH_LIST):
            v_key = v['key']
            v_time = v['time']
            if v_time < limit_time:
                del_keys.append(k)
            if v_key == auth_key:
                exist = True
        for k in del_keys:
            del AUTH_LIST[k]
        if exit:
            return False
        AUTH_LIST.append({"key": auth_key, "time": time_stamp})
    return True


def auth_api(func):
    def inner(request):
        if not auth_status(request):
            return JsonResponse({
                'status_code': 10001,
                'message': " API refuse to connect",
            }, json_dumps_params={'ensure_ascii': False})

        return func(request)
    return inner
