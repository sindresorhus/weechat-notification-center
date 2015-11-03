# WeeChat Notification Center

![](screenshot.png)

> [WeeChat](http://www.weechat.org) script to pass highlights and private messages to the OS X 10.8+ Notification Center.


## Install

### Script center

- Install [pync](https://github.com/SeTeM/pync): `pip install pync`
- Download [the WeeChat icon](https://weechat.org/media/images/weechat_logo_small.png) to `~/.weechat/weechat.png`
- In WeeChat, type `/script` to open the script manager
- Find `notification_center` and type `i` then `Enter` to install

### Manually

- Install [pync](https://github.com/SeTeM/pync): `pip install pync`
- Download [the WeeChat icon](https://weechat.org/media/images/weechat_logo_small.png) to `~/.weechat/weechat.png`
- Copy or symlink `notification_center.py` into `~/.weechat/python/autoload/`


## Options

### show_highlights

Default: `'on'`  
Values: `'on'`, `'off'`

### show_private_message

Default: `'on'`  
Values: `'on'`, `'off'`

### show_message_text

Default: `'on'`  
Values: `'on'`, `'off'`

### sound

Default: `'off'`  
Values: `'on'`, `'off'`

### sound_name

Default: `'Pong'`  
Values: `'Basso'`, `'Blow'`, `'Bottle'`, `'Frog'`, `'Funk'`, `'Glass'`, `'Hero'`, `'Morse'`, `'Ping'`, `'Pop'`, `'Purr'`, `'Sosumi'`, `'Submarine'`, `'Tink'`, but can really be anything that has an aptly named sound file in `/System/Library/Sounds/`, `/Library/Sounds/`, or `~/Library/Sounds/`.


## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
