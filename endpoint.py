import os
import re
import sys

import web

urls = ('/.*', 'index')


def do_the_boogy(pp):
  #  todo pass pp
  os.system(" ".join(sys.argv[2:]))


p_compile = re.compile("^.+=()$")


def parse_params(params):
  addr = re.compile("addr=(.+?)(?:&|\?|$)").search(params).group(1)
  secret = re.compile("secret=(.+?)(?:&|\?|$)").search(params).group(1)
  domain = re.compile("domain=(.+?)(?:&|\?|$)").search(params).group(1)
  return {"addr": addr, "secret": secret, "domain": domain}


class index:
  def GET(self):
    do_the_boogy(parse_params(web.ctx.query))
    return "yeah, you're here"
    pass


def POST(self):
  do_the_boogy(parse_params(web.ctx.query))
  return "yeah, you're here POST"
  pass


if __name__ == "__main__":
  app = web.application(urls, globals())
  app.run()
