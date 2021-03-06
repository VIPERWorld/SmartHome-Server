#! /usr/bin/env python
# coding:utf-8

import handler

urls = [
    (r'/', handler.index.IndexHandler),
    (r'/test/device', handler.index.Testhandler),
    (r'/test/chart', handler.index.Charthandler),
    (r'/error/(\d+)', handler.index.ErrorHandler),
    (r'/weixin', handler.weixin.WechatHandler),
    (r'/weixin/oauth', handler.oauth.OauthHandler),
    (r'/weixin/auth', handler.oauth.AuthHandler),
    # (r'/user/(\d+)/own', handler.user.DeviceHandler),
    (r'/device/qr', handler.qr.QrcodeHandler),
    (r'/device/(\d+)', handler.device.DeviceHandler),
    (r'/device/(\d+)/sensor/(\d+)', handler.sensor.SensorHandler),
    # (r'/device/sensor/data', handler.device.DataHandler),
    # (r'/device/new', handler.device.DeviceInfoHandler),
    # (r'/device/own', handler.device.DeviceMangaerHandler),
    # (r'/device/info/(\d+)', handler.device.DeviceInfoHandler),
]
