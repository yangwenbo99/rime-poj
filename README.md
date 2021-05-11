Type POJ (Pe̍h-Ōe-Ji, Church Romanisation) in RIME. 

用 RIME 拍白話字。

Ing RIME phah Pe̍h-ōe-li.

For the Chinese version of the README file, please see `README.zh.md`. 

Tiong-bûn pan-pún tī-leh  `README.zh.md`. 

中文版本佇咧 `README.zh.md`. 


## Setup

Put files in the `im` directory into your RIME configuration directory, i.e. 
-  `~/.config/ibus/rime/` or `~/.config/fcitx/rime/` on Linux, 
- `%APPDATA%\Rime` on Windows, or
- `~/Library/Rime/` on Mac OS. 

## How to use? 

- Vowel: Type a vowel and then press the numeric key corresponding to its tone.
- Complex vowel (diphthongs and tripthones): either type them in one-by-one or type the whole vowel and choose at the end
- o͘: press w
- ⁿ: press v
- Toned n (like the one in n̂g): press x
- Toned m (like the one in ḿ): press z

For the best experience, please install Wenquanyi Zen Hei.


## Tech details

We use the Normal form C (NFC, the "combining form") whenever possible.  This is achievable by Python's  `unicodedata.normalize(form, unistr)` function. 

