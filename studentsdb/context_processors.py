# -*- coding: utf-8 -*-

def students_proc(request):
    PORTAL_URL = request.scheme + '://' + request.get_host()
    groups = (
        {'id': 1, 'title': 'МтМ - 21', 'leader': u'Ячменев Олег'},
        {'id': 2, 'title': 'МтМ - 22', 'leader': u'Віталій Подоба'},
        {'id': 3, 'title': 'МтМ - 23', 'leader': u'Корост Андрій'},
        )
    return {'PORTAL_URL': PORTAL_URL, 'groups_select': groups}
