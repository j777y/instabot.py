#!/usr/bin/env python
# -*- coding: utf-8 -*-

from instabot import InstaBot

bot = InstaBot(login="contro_versial", password="Jehovah3167",
               like_per_day=1000,
               comments_per_day=50,
               tag_list=['followforfollow', 'lol', 'omg', 'beautiful'],
               max_like_for_one_tag=100,
               follow_per_day=150,
               follow_time=5*60*60,
               unfollow_per_day=150,
               unfollow_break_min=15,
               unfollow_break_max=30,
               log_mod=0)

bot.new_auto_mod()
