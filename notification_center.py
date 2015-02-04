# https://github.com/sindresorhus/weechat-notification-center
# Requires `pip install pync`
#
# Updated by Gianni Van Hoecke:
#  - Option to show all messages
#  - Updated titles to be more clear
#

import weechat
from pync import Notifier


SCRIPT_NAME = 'notification_center'
SCRIPT_AUTHOR = 'Sindre Sorhus <sindresorhus@gmail.com>'
SCRIPT_VERSION = '0.3.0'
SCRIPT_LICENSE = 'MIT'
SCRIPT_DESC = 'Pass highlights and private messages to the OS X 10.8+ Notification Center'

weechat.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE, SCRIPT_DESC, '', '')

DEFAULT_OPTIONS = {
	'show_highlights': 'on',
	'show_private_message': 'on',
	'show_message_text': 'on',
	'show_other_message': 'on',
	'sound': 'on',
	'sound_on_other_message': 'off'
}

for key, val in DEFAULT_OPTIONS.items():
	if not weechat.config_is_set_plugin(key):
		weechat.config_set_plugin(key, val)

def notify(data, buffer, date, tags, displayed, highlight, prefix, message):

	#If own nickname is sender, ignore
	mynick = weechat.buffer_get_string(buffer,'localvar_nick')
	if prefix == mynick or prefix == ('@%s' % mynick):
		return weechat.WEECHAT_RC_OK

	#Format message
	message = repr(message.encode('string-escape'))

	#Passing `None` or `''` still plays the default sound so we pass a lambda instead
	sound = 'Pong' if weechat.config_get_plugin('sound') == 'on' else lambda:_
	sound_on_other_message = 'Pong' if weechat.config_get_plugin('sound_on_other_message') == 'on' else lambda:_

	channel = weechat.buffer_get_string(buffer, 'localvar_channel')

	#Send notification
	if weechat.config_get_plugin('show_highlights') == 'on' and int(highlight):
		if weechat.config_get_plugin('show_message_text') == 'on':
			Notifier.notify(message, title='Highlighted by %s in %s' % (prefix, channel), sound=sound)
		else:
			Notifier.notify('In %s by %s' % (channel, prefix), title='Highlighted Message', sound=sound)
	elif weechat.config_get_plugin('show_private_message') == 'on' and 'notify_private' in tags:
		if weechat.config_get_plugin('show_message_text') == 'on':
			Notifier.notify(message, title='%s [private]' % prefix, sound=sound)
		else:
			Notifier.notify('From %s' % prefix, title='Private Message', sound=sound)
	elif weechat.config_get_plugin('show_other_message') == 'on':
		if weechat.config_get_plugin('show_message_text') == 'on':
			Notifier.notify(message, title='By %s in %s' % (prefix, channel), sound=sound_on_other_message)
		else:
			Notifier.notify('In %s by %s' % (channel, prefix), title='New Message', sound=sound_on_other_message)
	return weechat.WEECHAT_RC_OK
  
weechat.hook_print('', 'irc_privmsg', '', 1, 'notify', '')