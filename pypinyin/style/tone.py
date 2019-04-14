# -*- coding: utf-8 -*-
"""TONE 相关的几个拼音风格实现:

Style.TONE
Style.TONE2
Style.TONE3
Style.TONE4

"""
from __future__ import unicode_literals

from pypinyin.constants import Style
from pypinyin.style import register
from pypinyin.style._constants import RE_TONE3
from pypinyin.style._utils import (
    replace_symbol_to_number,
    get_initials,
    get_finals)


class ToneConverter(object):
    def to_tone(self, pinyin, **kwargs):
        return pinyin

    def to_tone2(self, pinyin, **kwargs):
        # 用数字表示声调
        pinyin = replace_symbol_to_number(pinyin)
        return pinyin

    def to_tone3(self, pinyin, **kwargs):
        pinyin = self.to_tone2(pinyin, **kwargs)
        # 将声调数字移动到最后
        return RE_TONE3.sub(r'\1\3\2', pinyin)

    def to_tone4(self, pinyin, **kwargs):
        pinyin = self.to_tone3(pinyin, **kwargs)
        # 将声母韵母空格分开
        strict = kwargs.get('strict', False)
        print(kwargs, strict)
        initials = get_initials(pinyin, strict)
        finals = get_finals(pinyin, strict)
        return (initials + ' ' + finals).strip()


converter = ToneConverter()
register(Style.TONE, func=converter.to_tone)
register(Style.TONE2, func=converter.to_tone2)
register(Style.TONE3, func=converter.to_tone3)
register(Style.TONE4, func=converter.to_tone4)
