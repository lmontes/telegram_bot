#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import subprocess
import os
import signal
from telebot import types
from config import BotConfiguration


config = BotConfiguration("/etc/bot.conf")

if not config.isValid():
  config = BotConfiguration("conf/bot.conf")
  
if not config.isValid():
  print("Config file does not exist")
  exit(1)
  

token = config.value("token")

gitUser = config.value("git_user")
gitRepo = config.value("git_repo")
gitPass = config.value("git_pass")
command = config.value("command")

logName = "process.log"

proc = None

bot = telebot.TeleBot(token)

def listener(messages):
  for m in messages:
    cid = m.chat.id
    if m.content_type == "text":       
      print("[" + str(cid) + "]: " + m.text)


bot.set_update_listener(listener)


@bot.message_handler(commands = ["update"])
def command_update(m):
    url = "https://" + gitUser + ":" + gitPass + "@bitbucket.org/" + gitUser + "/" + gitRepo
    bot.send_message(m.chat.id, "Updating git repository ...")
    subprocess.Popen(["git", "pull", url])


@bot.message_handler(commands = ["stop"])
def command_stop(m):
    global proc    
    if proc != None:
        bot.send_message(m.chat.id, "Stopping process " + str(proc.pid))
        proc.kill()
        proc = None


@bot.message_handler(commands = ["start"])
def command_start(m):
    global proc    

    f = open(logName, "w")
    
    proc = subprocess.Popen(command.split(" "), stderr = f)
    bot.send_message(m.chat.id, "The pid is " + str(proc.pid))


@bot.message_handler(commands = ["status"])
def command_status(m):
    global proc    

    if proc != None:
        if proc.poll() == None:
            bot.send_message(m.chat.id, "Running with pid " + str(proc.pid))
        else:
            bot.send_message(m.chat.id, "Stopped")
    else: 
        bot.send_message(m.chat.id, "Stopped")  


@bot.message_handler(commands = ["log"])
def command_log(m):
    f = open(logName, "r")
    log = f.read()
    if len(log) > 0:
        bot.send_message(m.chat.id, log)
    else:
        bot.send_message(m.chat.id, "Log is empty")


bot.polling(none_stop = True)
