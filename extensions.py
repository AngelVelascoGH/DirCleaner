IMAGE_EXTENSIONS = {
    '.jpg', '.jpeg',
    '.png',
    '.gif',
    '.bmp',
    '.webp',
    '.svg',
    '.ico',
    '.tiff', '.tif',
    '.heic', '.heif',
    '.raw',
    '.cr2', '.nef', '.arw',
    '.psd',
    '.ai',
}

AUDIO_EXTENSIONS = {
    '.flac',
    '.wav',
    '.aiff', '.aif',
    '.alac',
    '.ape',
    '.wv',
    '.mp3',
    '.m4a',
    '.aac',
    '.ogg', '.oga',
    '.opus',
    '.wma',
    '.mid', '.midi',
    '.amr',
    '.3gp',
}

DOCUMENT_EXTENSIONS = {
    '.txt',
    '.rtf',
    '.doc', '.docx',
    '.xls', '.xlsx',
    '.ppt', '.pptx',
    '.odt',
    '.ods',
    '.odp',
    '.pdf',
    '.epub',
    '.mobi',
    '.azw', '.azw3',
    '.pages',
    '.numbers',
    '.key',
    '.csv',
    '.md',
}

VIDEO_EXTENSIONS = {
    '.mp4',
    '.mov',
    '.avi',
    '.mkv',
    '.wmv',
    '.flv',
    '.webm',
    '.mpeg', '.mpg',
    '.m4v',
    '.3gp', '.3g2',
    '.mts', '.m2ts',
    '.vob',
    '.ts',
    '.mxf',
    '.ogv',
    '.f4v',
    '.rm', '.rmvb',
    '.asf',
}

EXECUTABLE_EXTENSIONS = {
    '.exe',
    '.msi',
    '.bat',
    '.cmd',
    '.com',
    '.dmg',
    '.app',
    '.pkg',
    '.deb',
    '.rpm',
    '.sh',
    '.run',
    '.appimage',
    '.snap',
    '.flatpak',
    '.jar',
    '.apk',
    '.ipa',
}

EXTRACTABLES = {
    '.zip',
    '.rar',
    '.7z',
    '.tar',
    '.tar.gz', '.tgz',
    '.tar.bz2',
    '.tar.xz',
    '.gz',
}

TEMP_DOWNLOAD = {
    '.crdownload',
    '.download',
    '.part',
    '.partial',
    '.tmp',
    '.temp',
    '.filepart',
}

DIRECTORIES = {
    "Pictures": IMAGE_EXTENSIONS,
    "Documents":DOCUMENT_EXTENSIONS,
    "Music": AUDIO_EXTENSIONS,
    "Videos": VIDEO_EXTENSIONS,
    "Executables": EXECUTABLE_EXTENSIONS 
}


