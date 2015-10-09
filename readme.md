# WeeChat Notification Center

![](screenshot.png)

> [WeeChat](http://www.weechat.org) script to pass highlights and private messages to the OS X 10.8+ Notification Center.


## Install

### Script center

- Install [pync](https://github.com/SeTeM/pync): `pip install pync`
- In WeeChat, type `/script` to open the script manager
- Find `notification_center` and type `i` then `Enter` to install

### Manually

- Install [pync](https://github.com/SeTeM/pync): `pip install pync`
- Copy or symlink `notification_center.py` into `~/.weechat/python/autoload/`

## Options

- show_highlights, defaults to on, valid values are on and off.
- show_private_message, defaults to on, valid values are on and off.
- show_message_text, defaults to on, valid values are on and off.
- sound, defaults to off, valid values are on and off.
- sound_name, defaults to Pong, valid values as of OS X 10.11 are Basso, Blow, Bottle, Frog, Funk, Glass, Hero, Morse, Ping, Pop, Purr, Sosumi, Submarine, Tink, but can really be anything that has an aptly named sound file in `/System/Library/Sounds/`, `/Library/Sounds/`, or `~/Library/Sounds/`.

## License

MIT © [Sindre Sorhus](http://sindresorhus.com)
