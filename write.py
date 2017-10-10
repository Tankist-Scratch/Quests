import data, os

def write(name, text, buttons):
    page = """<!DOCTYPE html>
             <html lang="en">
                 <head>
                 <meta charset="UTF-8">
                 <title>%s</title>
             </head>
             <body>
             """ % name #<iframe width='100%s' src='pages/index.html' frameborder='0' height='100%s'>
    page += text + "<br/>\n"
    for link in buttons:
        page += "<a href='%s.html'><button>%s</button></a><br/>\n" % (link[1], link[0])
    page += "</body></html>"
    return page


# page = open("wiki/index.html", "w", encoding="utf-8")
# page.write(write(data.main, True, "Главная"))
# page.close()

# page = open("wiki/all/index.html", "w", encoding="utf-8")
# page.write(write("".join(["""
#       {{tree|%s}}
#       """ % i for i in data.all]), True, "Все создания"))
# page.close()

for np in data.pages.keys():
    page = open("pages/%s.html" % np, "w", encoding="utf-8")
    page.write(write("", *data.pages[np]))
    page.close()