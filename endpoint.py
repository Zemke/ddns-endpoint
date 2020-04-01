import os
import sys

import web

urls = ('/.*', 'index')


def do_the_boogy():
  os.system(" ".join(sys.argv[2:]))


class index:
  def GET(self):
    do_the_boogy()
    return "yeah, you're here"
    pass

  def POST(self):
    do_the_boogy()
    return "yeah, you're here POST"
    pass


if __name__ == "__main__":
  app = web.application(urls, globals())
  app.run()
