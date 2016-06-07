# -*- coding: UTF-8 -*-

import time
import random
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup
# En el fichero variables.py están las frases
from variables import *

def handle(msg):
  
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    # Dependiendo del tipo de contenido enviado al chat realizo una acción diferente
    
    if content_type == 'text':
      
      command = msg['text']
      print 'Comando leido: %s' % command
      
      """
      El @Motivationalbot es para cuando llaman al bot desde un grupo
      
      'Markdown' es para poder poner estilo al texto:
          *bold text*
          _italic text_
          [text](URL)
          `inline fixed-width code`
          ```pre-formatted fixed-width code block```
          
      Para enviar una imagen, primero enviarla al chat del bot para que nos diga
      el 'file_id', que es el que ponemos en sendPhoto, sendSticker
      o sendDocument (cuando es un gif)
      """
      
      # Comandos de ayuda
      if (command == '/ayudagifs') or (command == '/ayudagifs@Motivationalbot'):
          bot.sendMessage(chat_id, ayudagifs, 'Markdown')
      elif (command == '/ayudafrases') or (command == '/ayudafrases@Motivationalbot'):
          bot.sendMessage(chat_id, help, 'Markdown')
      elif (command == '/ayudafotos') or (command == '/ayudafotos@Motivationalbot'):
          bot.sendMessage(chat_id, ayudafotos, 'Markdown')
      elif (command == '/ayuda') or (command == '/ayuda@Motivationalbot'):
        # Teclado ajustado al tamaño del texto, se cierra al pulsar una opción
        markup = ReplyKeyboardMarkup(keyboard=[
                     ['/ayudafrases', '/ayudafotos', '/ayudagifs'],
                 ],
                 resize_keyboard=True,
                 one_time_keyboard=True)
        bot.sendMessage(chat_id, '*Selecciona un tipo de ayuda*', 'Markdown', reply_markup=markup)
      # Comandos para frases
      elif (command == '/fraseneruda') or (command == '/fraseneruda@Motivationalbot'):
          bot.sendMessage(chat_id, neruda[random.randint(0,len(neruda)-1)], 'Markdown')
      elif (command == '/frasefranklin') or (command == '/frasefranklin@Motivationalbot'):
          bot.sendMessage(chat_id, franklin[random.randint(0,len(franklin)-1)], 'Markdown')
      elif (command == '/frasebonnard') or (command == '/frasebonnard@Motivationalbot'):
          bot.sendMessage(chat_id, bonnard[random.randint(0,len(bonnard)-1)], 'Markdown')
      elif (command == '/frasepopular') or (command == '/frasepopular@Motivationalbot'):
          bot.sendMessage(chat_id, popular[random.randint(0,len(popular)-1)], 'Markdown')
      elif (command == '/frasedeportista') or (command == '/frasedeportista@Motivationalbot'):
          bot.sendMessage(chat_id, deportista[random.randint(0,len(deportista)-1)], 'Markdown')
      elif (command == '/frasecoelho') or (command == '/frasecoelho@Motivationalbot'):
          bot.sendMessage(chat_id, coelho[random.randint(0,len(coelho)-1)], 'Markdown')
      elif (command == '/frasegandhi') or (command == '/frasegandhi@Motivationalbot'):
          bot.sendMessage(chat_id, gandhi[random.randint(0,len(gandhi)-1)], 'Markdown')
      elif (command == '/fraserandom') or (command == '/fraserandom@FrasesRATbot'):
          bot.sendMessage(chat_id, todas[random.randint(0,len(todas)-1)], 'Markdown')
      # Comandos para imagenes
      elif (command == '/neruda') or (command == '/neruda@Motivationalbot'):
          bot.sendPhoto(chat_id, 'AgADBAADsacxGzUzbQxX2l2mzJvN1QMdQxkABKp9NOQsw5y_u8wAAgI')
      elif (command == '/franklin') or (command == '/franklin@Motivationalbot'):
          bot.sendPhoto(chat_id, 'AgADBAADsqcxGzUzbQx8UB2Le2KPtekgQxkABBOuVRKLlv0FnMsAAgI')
      elif (command == '/bonnard') or (command == '/bonnard@Motivationalbot'):
          bot.sendPhoto(chat_id, 'AgADBAADs6cxGzUzbQxexP2T2a-adBglKRkABMpEBOZWpCSM28kBAAEC')
      elif (command == '/coelho') or (command == '/coelho@Motivationalbot'):
          bot.sendPhoto(chat_id, 'AgADBAADtKcxGzUzbQwpIx2q-03yxxk1QxkABPZSrp_yb3SMsswAAgI')
      elif (command == '/gandhi') or (command == '/gandhi@Motivationalbot'):
          bot.sendPhoto(chat_id, 'AgADBAADtacxGzUzbQxsRS2Js6Ladr0SQxkABGT07dZpjudP9sgAAgI')
      # Comandos para gifs
      elif (command == '/deporte') or (command == '/deporte@Motivationalbot'):
          bot.sendDocument(chat_id, 'BQADBAADBwADNTNtDOE2DxhpS53PAg')
      elif (command == '/exito') or (command == '/exito@Motivationalbot'):
          bot.sendDocument(chat_id, 'BQADBAADCAADNTNtDNJ2addEMarKAg')
      elif (command == '/alimentacion') or (command == '/alimentacion@Motivationalbot'):
          bot.sendDocument(chat_id, 'BQADBAADCQADNTNtDBREjMrovML2Ag')
    elif content_type == 'sticker':
      sticker = msg['sticker']['file_id']
      print 'Sticker: %s' % sticker
    else:
      print 'Otros: %s' % msg

TOKEN = '225410833:AAEdA10qrm8IJ9ickhHTQK4VSsBdgb_NIxQ'
bot = telepot.Bot(TOKEN)
bot.message_loop({'chat': handle})

print 'Escuchando...'

while 1:
    time.sleep(10)
