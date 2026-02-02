# WeeChat Notification Center

![](screenshot.png)

> [WeeChat](https://weechat.org) script to pass highlights and private messages to the macOS Notification Center

## Install

### Script center

- Install [pync](https://github.com/SeTeM/pync): `pip install pync`
- Copy `weechat.png` from this repository to `~/.weechat/weechat.png`
- In WeeChat, type `/script` to open the script manager
- Find `notification_center` and type `i` then `Enter` to install

### Manually

- Install [pync](https://github.com/SeTeM/pync): `pip install pync`
- Copy or symlink `weechat.png` to `~/.weechat/weechat.png`
- Copy or symlink `notification_center.py` into `~/.weechat/python/autoload/`

## Options

### enabled

Default: `'on'`\
Values: `'on'` `'off'`

Temporarily disable all notifications.

### show_highlights

Default: `'on'`\
Values: `'on'` `'off'`

### show_private_message

Default: `'on'`\
Values: `'on'` `'off'`

### show_message_text

Default: `'on'`\
Values: `'on'` `'off'`

### sound

Default: `'off'`\
Values: `'on'` `'off'`

### sound_name

Default: `'Pong'`\
Values: `'Basso'` `'Blow'` `'Bottle'` `'Frog'` `'Funk'` `'Glass'` `'Hero'` `'Morse'` `'Ping'` `'Pop'` `'Purr'` `'Sosumi'` `'Submarine'` `'Tink'`, but can really be anything that has an aptly named sound file in `/System/Library/Sounds/`, `/Library/Sounds/`, or `~/Library/Sounds/`.

### activate_bundle_id

Default: `com.apple.Terminal`\
Values: `'com.apple.Terminal'` `'com.googlecode.iterm2'` (or any bundle ID that your terminal uses)

App to activate when the notification is clicked.

The app bundle ID can be found in `/Applications/<MyTerminal>.app/Contents/Info.plist`, right below the `CFBundleIdentifier` key.

### ignore_old_messages

Default: `'off'`\
Values: `'on'` `'off'`

Determines whether old messages, such as log playbacks, will trigger notifications or not.

### ignore_current_buffer_messages

Default: `'off'`\
Values: `'on'` `'off'`

Determines whether messages from the current buffer should trigger notifications or not. This is especially useful if you use [wee-slack](https://github.com/wee-slack/wee-slack) and receive notifications for messages they send, as discussed in [#22](https://github.com/sindresorhus/weechat-notification-center/issues/22).

### channels

Default: `''`\
Values: Comma-separated list of channel names

Channels in this list will trigger a notification on every message received.

### tags

Default: `''`\
Values: Comma-separated list of tags

Additional [message tags](https://weechat.org/files/doc/stable/weechat_user.en.html#lines_tags) that can trigger notifications. This can be used in combination with [`weechat.look.highlight_tags`](https://weechat.org/files/doc/stable/weechat_user.en.html#option_weechat.look.highlight_tags) to generate custom notifications.

For example, to get notifications when `<nick>` joins or parts `<server>`:

```
/notify add <nick> <server>
/set weechat.look.highlight_tags "irc_notify_join,irc_notify_quit"
/set plugins.var.notification_center.tags "irc_notify"
```
