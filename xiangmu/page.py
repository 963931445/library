import math

def getpages(total, current, item,url):
    # item = 3
    str = "<ul class='pagination'>"
    str += "<li><a href='%s?page=0'>首页</a></li>" % (url)
    if current - 1 > 0:
        str += "<li><a href='%s?page=%s'>«</a></li>" % (url, current - 1)
    else:
        str += "<li><a href='%s?page=%s'>«</a></li>" % (url, 0)

    if current < (math.floor(total / 2)) and current != 0:
        for item1 in range(current, current - item, -1):
            before = current - item1 if (current - item1) > 0 else 0
            str += "<li><a href='%s?page=%s'>%s</a></li>" % (url, before, before + 1)

    else:
        str += "<li><a href='%s?page=%s'style='background:yellowgreen'>%s</a></li>" % (url, current, current + 1)
        for item1 in range(current + 1, total):
            after = item1 if item1 < total else total

            str += "<li><a href='%s?page=%s'>%s</a></li>" % (url, after, after + 1)
    if current + 1 < total:
        str += "<li><a href='%s?page=%s'>»</a></li>" % (url, current + 1)
        str += "<li><a href='%s?page=%s'>尾页</a></li>" % (url, total - 1)
    else:
        pass
        # str += "<li><a href='%s?page=%s'>»</a></li>" % (url, total-1)

    str += "</ul>"
    return str
