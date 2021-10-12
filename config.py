import os
import logging
import time
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

class Config:
    
    # eğer heroku gibi bir bulut platformunda çalışıyorsa enviroment variables kullanabilirsiniz.
    # enviroment variables kullanırsanız bu dosyada bir değişiklik yapmamalısınız.
    # gömülü konfig için ne yapman gerektiğini anlatmayacağım. python öğren gel

    # requireds +
    BOT_TOKEN = os.environ.get('BOT_TOKEN', '')
    APP_ID = int(os.environ.get('APP_ID', 1111111))
    API_HASH = os.environ.get('API_HASH', '')
    BOT_USERNAME = os.environ.get('BOT_USERNAME','')
    if not BOT_USERNAME.startswith('@'): BOT_USERNAME = '@' + BOT_USERNAME # bu satıra dokunmayın.
    FORCE_SUBSCRIBE_CHANNEL = os.environ.get('FORCE_SUBSCRIBE_CHANNEL','') # force subscribe channel link.
    if FORCE_SUBSCRIBE_CHANNEL == "" or FORCE_SUBSCRIBE_CHANNEL == " " or FORCE_SUBSCRIBE_CHANNEL == None: FORCE_SUBSCRIBE_CHANNEL = None # bu satıra dokunmayın.
    LOGGER.info(f"FORCE_SUBSCRIBE_CHANNEL: {FORCE_SUBSCRIBE_CHANNEL}") # debug
    # requireds -

    # commands +
    UNZIP_COMMAND = os.environ.get('UNZIP_COMMAND','unzip')
    UNZIP_COMMAND = [UNZIP_COMMAND, UNZIP_COMMAND+BOT_USERNAME] # bu satıra dokunmayın.
    STATS_COMMAND = os.environ.get('STATS_COMMAND','stats')
    STATS_COMMAND = [STATS_COMMAND, STATS_COMMAND+BOT_USERNAME] # bu satıra dokunmayın.
    SHELL_COMMAND = os.environ.get('SHELL_COMMAND','shell')
    SHELL_COMMAND = [SHELL_COMMAND, SHELL_COMMAND+BOT_USERNAME] # bu satıra dokunmayın.
    CLEARME_COMMAND = os.environ.get('CLEARME_COMMAND', "clearme")
    CLEARME_COMMAND = [CLEARME_COMMAND, CLEARME_COMMAND+BOT_USERNAME] # bu satıra dokunmayın.
    SAVE_THUMB_COMMAND = os.environ.get('SAVE_THUMB_COMMAND', "save")
    SAVE_THUMB_COMMAND = [SAVE_THUMB_COMMAND, SAVE_THUMB_COMMAND+BOT_USERNAME] # bu satıra dokunmayın.
    CLEAR_THUMB_COMMAND = os.environ.get('CLEAR_THUMB_COMMAND', "clear")
    CLEAR_THUMB_COMMAND = [CLEAR_THUMB_COMMAND, CLEAR_THUMB_COMMAND+BOT_USERNAME] # bu satıra dokunmayın.
    SHOW_THUMB_COMMAND = os.environ.get('SHOW_THUMB_COMMAND','show')
    SHOW_THUMB_COMMAND = [SHOW_THUMB_COMMAND, SHOW_THUMB_COMMAND+BOT_USERNAME] # bu satıra dokunmayın.
    # commands -
    
    # non-required +
    SORT_FILES_BEFORE_SEND = int(os.environ.get('SORT_FILES_BEFORE_SEND', 1)) # sorting for upload files
    USE_NATSORT = int(os.environ.get('USE_NATSORT', 1)) # sort 10 2 20 1 60 6 to 1, 2, 6, 10, 20, 60
    OWNER_ID = int(os.environ.get('OWNER_ID', 0)) # give your owner id # if given 0 shell will not works
    AUTH_IDS = [int(x) for x in os.environ.get("AUTH_IDS", "0").split()] # if open to everyone give 0
    DOWNLOAD_DIR = os.environ.get('DOWNLOAD_DIR', 'downloads')
    FINISHED_PROGRESS_STR = os.environ.get('FINISHED_PROGRESS_STR','●')
    UN_FINISHED_PROGRESS_STR = os.environ.get('UN_FINISHED_PROGRESS_STR','○')
    PROGRESS = "`🔥 Biten Yüzde / Percent: % {0}\n📀 Toplam Boyut / Total Size: {1}\n📤 Biten Boyut / Finished: {2}\n" + \
        "📥 Kalan Boyut / Remaining: {3}\n⚡️ Anlık Hız / Speed: {4}/s\n⌛️ Geçen Süre / Passed: {5}\n⏳ Kalan Süre / Remaining: {6}`"
    FORCE_DOC_UPLOAD = int(os.environ.get('FORCE_DOC_UPLOAD', 0))
    ONE_PROCESS_PER_USER = int(os.environ.get('ONE_PROCESS_PER_USER', 1)) # for stability
    UNAUTHORIZED_TEXT_STR = os.environ.get('UNAUTHORIZED_TEXT_STR', "🇹🇷 Bu bot senin için değil ezik.\n🇬🇧 This bot not for you.")
    PROGRESSBAR_LENGTH = int(os.environ.get('PROGRESSBAR_LENGTH', 25))
    ONE_PROCESS_PER_USER_STR = os.environ.get('ONE_PROCESS_PER_USER_STR',
        f"🇬🇧 1 user = 1 process.\nYou can clear your all files with /{CLEARME_COMMAND[0]}," + \
        " Your process quee will be cleared. If anything is uploading at now, it will be cleared. Be careful." + \
        f"\n\n🇹🇷 1 kullanıcı = 1 işlem.\nTüm dosyalarınızı /{CLEARME_COMMAND[0]} ile temizleyebilirsiniz." + \
        " İşlem sıranız temizlenir. Şu an yüklenen bir şey varsa temizlenir. Dikkatli olun.")
    CHANNEL_OR_CONTACT = os.environ.get('CHANNEL_OR_CONTACT', "HuzunluArtemis") # give your public channel or contact username
    SLEEP_TIME_BETWEEN_SEND_FILES = int(os.environ.get('SLEEP_TIME_BETWEEN_SEND_FILES', 2)) 
    SHOW_PROGRESS_MIN_SIZE_DOWNLOAD = int(os.environ.get('SHOW_PROGRESS_MIN_SIZE_DOWNLOAD', 12*1024*1024)) # for speedy
    DOWNLOADING_STR = os.environ.get('DOWNLOADING_STR',
        "**🇹🇷 İndiriliyor / 🇬🇧 Downloading:**\n\n🎯 Name / Ad: `{}`\n❄️ Size / Boyut: `{}`\n🔑 Password / Parola: {}")
    UPLOADING_STR = os.environ.get('UPLOADING_STR',
        "**🇹🇷 Yükleniyor / 🇬🇧 Uploading:**\n\n🎯 Kaynak / Source: `{}`\n" + \
        "🍌 Kaynak Boyutu / Source Size: `{}`\n🔑 Password / Parola: {}\n\n🦋 Anlık Dosya / File Now: `{}`\n" + \
        "❄️ Size Now / Anlık Boyut: `{}`\n🥕 File Turn / Dosya Sırası: `{}`")
    DOWNLOAD_SUCCESS = os.environ.get('DOWNLOAD_SUCCESS',
        "🇹🇷 Dosya indirildi! / 🇬🇧 File downloaded.\n🇹🇷 Geçen Süre / 🇬🇧 Time: `{}`" + \
        "\n\n🇹🇷 Arşivden çıkarılıyor lütfen bekleyin.\n🇬🇧 Extracting please wait.")
    EXTENSIONS = [str(x) for x in os.environ.get("EXTENSIONS",
        "7z apm arj bz2 bzip2 cab chm cpio cramfs deb dmg fat gz gzip hfs iso lzh lzma lzma2 mbr msi mslz nsis ntfs rar"+
        " rpm squashfs tar tar.bz2 tar.gz tar.xz tbz2 tgz udf vhd wim xar z zip").split()]
    all_supported_extensions_with_comma = ", ".join(EXTENSIONS).upper() # dont change config order.
    START_TEXT_STR = os.environ.get('START_TEXT_STR',"🇬🇧 Send archive and reply with `/" + UNZIP_COMMAND[0] + "`" + \
        " (if passworded: Leave a space after the command and enter the password.) " + \
        f"You can clear your all files with `/{CLEARME_COMMAND[0]}`," + \
        " Your process quee will be cleared. If anything is uploading at now, it will be cleared. Be careful.\n\n" + \
        "🇹🇷 Arşivi gönderin ve `/" + UNZIP_COMMAND[0] + "` ile yanıtlayın." + \
        " (parolalıysa: komutunuzdan sonra bir boşluk bırakıp parolayı girin.) " + \
        f"Tüm dosyalarınızı `/{CLEARME_COMMAND[0]}` ile temizleyebilirsiniz." + \
        " İşlem sıranız temizlenir. Şu an yüklenen bir şey varsa temizlenir. Dikkatli olun.\n\n"
        "🍓 Örnekler / Samples:\n\n✅ `/" + UNZIP_COMMAND[0] + "`" + \
        "\n✅ `/" + UNZIP_COMMAND[0] + " Hunhj887ZunLudArt87emiS`" + \
        "\n✅ `/" + UNZIP_COMMAND[0] + " HEreis8yorupassword-parolaizZBuraya`" + \
        "\n✅ `/" + UNZIP_COMMAND[0] + " anoTherSampLe-bAskABirorNek`" + \
        "\n\n🖼 Set thumbnail / Küçük resim ayarlama: `/" + SAVE_THUMB_COMMAND[0] + "`" + \
        "\n❌ Clear thumbnail / Küçük resmi temizle: `/" + CLEAR_THUMB_COMMAND[0] + "`" + \
        "\n🌆 Show thumbnail / Küçük resmi göster: `/" + SHOW_THUMB_COMMAND[0] + "`" + \
        "\n🌿 Server stats / Sunucu istatistikleri: `/" + STATS_COMMAND[0] + "`" + \
        f"\n\n🍒 Supported / Destekler: `{all_supported_extensions_with_comma}`")
    UPLOAD_SUCCESS = os.environ.get('UPLOAD_SUCCESS',
        "🇹🇷 Dosyalar yüklendi! / 🇬🇧 Files uploaded!\n🇹🇷 Geçen Süre / 🇬🇧 Time: `{}`\n\n🍇 Yüklenen / Uploaded: `{}`\n" + \
        "🍎 Boyut / Size: `{}`\n🔥 [Kaynak / Source]({})\n✅ Başarılı / Success: `{}`\n❌ Başarısız / Unsucces: `{}`")
    CLEAR_STR = os.environ.get('CLEAR_STR',
        "🇬🇧 You\'re clean like a baby now. I deleted your files.\n🇹🇷 Şimdi bebek gibi tertemizsin. Dosyalarını sildim.")
    JOIN_CHANNEL_STR = os.environ.get('JOIN_CHANNEL_STR',
        "Merhaba / Hi {}\n\n" + \
        "🇬🇧 First subscribe my channel from button, then send /start again.\n" + \
        "🇹🇷 Önce butondan kanala abone ol, sonra bana /start yaz.")
    YOU_ARE_BANNED_STR = os.environ.get('YOU_ARE_BANNED_STR',
        "🇬🇧 You are Banned to use me.\n🇹🇷 Banlanmışsın ezik.\n\nDestek / Support: {}")
    JOIN_BUTTON_STR = os.environ.get('JOIN_BUTTON_STR', "🇬🇧 Join / 🇹🇷 Katıl")
    # non-required -

    botStartTime = time.time() # dont touch
    
    # elleme:
    if CHANNEL_OR_CONTACT is not None:
        if not CHANNEL_OR_CONTACT.startswith('@'):
            CHANNEL_OR_CONTACT = '@' + CHANNEL_OR_CONTACT
        PROGRESS += "\n\n💎 " + CHANNEL_OR_CONTACT
        DOWNLOAD_SUCCESS += "\n\n💎 " + CHANNEL_OR_CONTACT
        UPLOAD_SUCCESS += "\n\n💎 " + CHANNEL_OR_CONTACT
        START_TEXT_STR += "\n\n💎 " + CHANNEL_OR_CONTACT
    
    # geliştiriciyseniz elleyebilirsiniz:
    HELP_COMMANDS = ['start', 'help','yardim', "yardım", "y","h"]

    # hiç ellemeyin:
    HELP_COMMANDSR = []
    HELP_COMMANDSR = HELP_COMMANDS.copy()
    for x in HELP_COMMANDS:
        HELP_COMMANDSR.append(x + BOT_USERNAME)
    HELP_COMMANDS = HELP_COMMANDSR
    del HELP_COMMANDSR
    # dont touch
    if ONE_PROCESS_PER_USER == 1:
        LOGGER.info("ONE_PROCESS_PER_USER was true")
        del ONE_PROCESS_PER_USER
        ONE_PROCESS_PER_USER = True
    else:
        LOGGER.info("ONE_PROCESS_PER_USER was false")
        del ONE_PROCESS_PER_USER
        ONE_PROCESS_PER_USER = False
    #
    if FORCE_DOC_UPLOAD == 1:
        LOGGER.info("FORCE_DOC_UPLOAD was true")
        del FORCE_DOC_UPLOAD
        FORCE_DOC_UPLOAD = True
    else:
        LOGGER.info("FORCE_DOC_UPLOAD was false")
        del FORCE_DOC_UPLOAD
        FORCE_DOC_UPLOAD = False
    #
    if SORT_FILES_BEFORE_SEND == 1:
        LOGGER.info("SORT_FILES_BEFORE_SEND was true")
        del SORT_FILES_BEFORE_SEND
        SORT_FILES_BEFORE_SEND = True
    else:
        LOGGER.info("SORT_FILES_BEFORE_SEND was false")
        del SORT_FILES_BEFORE_SEND
        SORT_FILES_BEFORE_SEND = False
    #
    if USE_NATSORT == 1:
        LOGGER.info("USE_NATSORT was true")
        del USE_NATSORT
        USE_NATSORT = True
    else:
        LOGGER.info("USE_NATSORT was false")
        del USE_NATSORT
        USE_NATSORT = False
