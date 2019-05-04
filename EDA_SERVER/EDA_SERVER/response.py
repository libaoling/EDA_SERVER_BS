#!/usr/bin/env python
# -*- encoding: utf-8 -*-


def r(success=True, result=''):
    _r = dict()
    if success is True:
        _r['status_code'] = 200
    else:
        _r['status_code'] = 400
    _r['result'] = result

    return _r

