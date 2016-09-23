#Antifake-English-Translation

##EXPLAIN YOURSELF!

The antifake application is absolutely essential, even more so possibly for those of us not in Asia. Unfortunately, the application is not in English, just Chinese. I recently modified the APK to have roughly 50% in English, so it is easier to use for English speakers.

This is the second unofficial port. Hopefully this is slightly easier to use. If someone with a fake device can help with the sections which I cannot access (due to me having a real device) then please PM me.

##App info

**Software name**: Antifake English Translation

**Version information**: 1.2.2

**Version size**: 900KB

**Applicable Devices**: Xiaomi devices, Android 4 or above.

**Last Update**: 07th October 2014

**Play Store**: N/A, see below for APK

###How do I use this?

If you want to use this, just install the .apk file. If you want to compile the APK yourself you need to:

###I want to compile this myself - How?

1. First, acquire the original APK
2. Download apktool and decompile with the command "apktool d <<apk_name.apk>>"
3. Place the "values-en" folder in /res/

**OPTIONAL WHEN UPDATER IS BROKEN (CURRENTLY):** Open build\apk\AndroidManifest.xml and search for "1.0.22", change this number to something higher than the current build version (1.0.24)

4. Run the command "apktool b <<the_directory_of_files>>"
5. Sign the newly created apk with [signapk](https://code.google.com/p/signapk/), or download [APK multi tool](http://apkmultitool.com/?q=node/5)
6. Done!

**More information**: [MIUI.com thread here](http://en.miui.com/thread-51706-1-1.html)