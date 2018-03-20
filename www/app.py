#/usr/bin/env/python3
# -*- coding: utf-8 -*-

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
	return web.Response(body = b'<h1>Awesome</h1>', headers = {'content-type': 'text/html'})

@asyncio.coroutine #协程
def init(loop):
	app = web.Application(loop = loop)
	app.router.add_route('GET', '/', index)
	#在coroutine内部用yield from调用另一个coroutine实现异步操作
	#create_server创建TCP服务
	srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
	logging.info('server started at http://127.0.0.1:9000...')
	return srv

#创建一个事件循环
loop = asyncio.get_event_loop()
#将协程注册到事件循环并启动事件循环
loop.run_until_complete(init(loop))
loop.run_forever()

