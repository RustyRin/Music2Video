import sys

# Searches supported unicode characters

'''
This is a function that takes in a string and returns the name of an appropriate font name in the format that moviepy likes

'''

CJK = [  # FONT: NOTO SANS CJK JP
    {"from": ord(u"\u4e00"), "to": ord(u"\u9fff")},  # CJK Unified
    {"from": ord(u"\u3400"), "to": ord(u"\u4dbf")},  # CJK Extension-A
    {"from": ord(u"\U00020000"), "to": ord(u"\U0002a6df")},  # CJK Extension-B
    {"from": ord(u"\U0002a700"), "to": ord(u"\U0002b73f")},  # CJK Extension-C
    {"from": ord(u"\U0002b740"), "to": ord(u"\U0002b81f")},  # CJK Extension-D
    {"from": ord(u"\U0002b820"), "to": ord(u"\U0002ceaf")},  # CJK Extension-E
    {"from": ord(u"\U0002ceb0"), "to": ord(u"\U0002ebe0")},  # CJK Extension-F
    {"from": ord(u"\uf900"), "to": ord(u"\ufaff")},  # CJK Compatibility Ideographs
    {"from": ord(u"\U0002f800"), "to": ord(u"\U0002fa1f")},  # CJK Compatibility Ideographs Supplement
    {"from": ord(u"\u2f00"), "to": ord(u"\u2fdf")},  # CJK Radicals / KangXi Radicals
    {"from": ord(u"\u2e80"), "to": ord(u"\u2eff")},  # CJK Radicals Supplement
    {"from": ord(u"\u31c0"), "to": ord(u"\u31ef")},  # CJK Strokes
    {"from": ord(u"\u2ff0"), "to": ord(u"\u2fff")},  # Ideographs Description Characters
    {"from": ord(u"\u1100"), "to": ord(u"\u11ff")},  # Hangul Jamo (Not sure if in Noto CJK font)
    {"from": ord(u"\ua960"), "to": ord(u"\ua97f")},  # Hangul Jamo Extended-A
    {"from": ord(u"\ud7b0"), "to": ord(u"\ud7ff")},  # Hangul Jamo Extended-B
    {"from": ord(u"\u3130"), "to": ord(u"\u31bf")},  # Hangul Compatibility Jamo
    {"from": ord(u"\uffa0"), "to": ord(u"\uffdc")},  # Half-width Jamo
    {"from": ord(u"\uac00"), "to": ord(u"\ud7af")},  # Hangul Symbols
    {"from": ord(u"\u3040"), "to": ord(u"\u309f")},  # Japanese Hiragana
    {"from": ord(u"\U0001b100"), "to": ord(u"\U0001b12f")},  # Kana Extended-A
    {"from": ord(u"\U0001b000"), "to": ord(u"\U0001b0ff")},  # Kana Supplement
    {"from": ord(u"\u3190"), "to": ord(u"\u319f")},  # Kanbun
    {"from": ord(u"\u30a0"), "to": ord(u"\u30ff")},  # Katakana
    {"from": ord(u"\u31f0"), "to": ord(u"\u31ff")},  # Katakana Phonetic Extensions
    {"from": ord(u"\uff65"), "to": ord(u"\uff9f")}  # Half-width Katakana
    # Possible additions but idk:
    # Lisu, Miao, Nushu, Tangut, Tangut Components, Yi Syllabels, Yi Rabicals
]

Armenian = [  # FONT: NOTO SANS ARMENIAN
    {"from": ord(u"\u0530"), "to": ord(u"\u058f")},  # Armenian
    {"from": ord(u"\ufb13"), "to": ord(u"\ufb17")}  # Armenian Ligatures
]

Carian = [  # FONT: NOTO SANS CARIAN
    {"from": ord(u"\U000102a0"), "to": ord(u"\U000102df")}  # Carian
]

Cypriot_Syllabary = [  # FONT: NOTO SANS CYPRIOT
    {"from": ord(u"\U00010800"), "to": ord(u"\U0001083f")}  # Cypriot
]

Georgian = [  # FONT: NOTO SANS GEORGIAN
    {"from": ord(u"\u10a0"), "to": ord(u"\u10ff")},  # Georgian
    {"from": ord(u"\u1c90"), "to": ord(u"\u1cbf")},  # Georgian Extended
    {"from": ord(u"\u2d00"), "to": ord(u"\u2d2f")}  # Georgian Supplement
]

Glogolitic = [  # FONT: NOTO SANS GLAGOLITIC
    {"from": ord(u"\u2c00"), "to": ord(u"\u2c5f")},  # Glagolitic
    {"from": ord(u"\U0001e000"), "to": ord(u"\U0001e02f")}  # Glagolitic Supplement
]

Gothic = [  # FONT: NOTO SANS GOTHIC
    {"from": ord(u"\U00010330"), "to": ord(u"\U0001034f")}  # Gothic
]

Linear_B = [  # FONT: NOTO SANS LINEAR B
    {"from": ord(u"\U00010000"), "to": ord(u"\U0001007f")},  # Linear B Syllabary
    {"from": ord(u"\U00010080"), "to": ord(u"\U000100ff")},  # Linear B Ideograms
    {"from": ord(u"\U00010100"), "to": ord(u"\U0001013f")}  # Aegean Numbers
]

Lycian = [  # FONT: NOTO SANS LYCIAN
    {"from": ord(u"\U00010280"), "to": ord(u"\U0001029f")}  # Lycian
]

Lydian = [  # FONT: NOTO SANS LYDIAN
    {"from": ord(u"\U00010920"), "to": ord(u"\U0001093f")}  # Lydian
]

Ogham = [  # FONT: NOTO SANS OGHAM
    {"from": ord(u"\u1980"), "to": ord(u"\u169f")}  # Ogham
]

Old_Italic = [  # FONT: NOTO SANS OLD ITALIC
    {"from": ord(u"\U00010300"), "to": ord(u"\U0001032f")}  # Old Italic
]

Runic = [  # FONT: NOTO SANS RUNIC
    {"from": ord(u"\u16a0"), "to": ord(u"\u16ff")}  # Runic
]

Shavian = [  # FONT: NOTO SANS SHAVIAN
    {"from": ord(u"\U00010450"), "to": ord(u"\U0001047f")}  # Shavian
]

Adlam = [  # FONT: NOTO SANS ADLAM
    {"from": ord(u"\U0001e900"), "to": ord(u"\U0001e95f")}  # Adlam
]

Bamum = [  # FONT: NOTO SANS BAMUM
    {"from": ord(u"\ua6a0"), "to": ord(u"\ua6ff")},  # Bamum
    {"from": ord(u"\U00016800"), "to": ord(u"\U00016a3f")}  # Bamum Supplement
]

Coptic = [  # FONT: NOTO SANS COPTIC
    {"from": ord(u"\u2c80"), "to": ord(u"\u2cff")},  # Coptic
    {"from": ord(u"\u03e2"), "to": ord(u"\u03ef")},  # Coptic in Greek Block
    {"from": ord(u"\U000102e0"), "to": ord(u"\U000102ff")}  # Coptic Epact Numbers
]

Egyptian_Hieroglyphs = [  # FONT: NOTO SANS EGYPTIAN HIEROGLYPHS
    {"from": ord(u"\U00013000"), "to": ord(u"\U0001342f")}  # Egyptian Hieroglyphs
]

Ethiopic = [  # FONT: NOTO SANS ETHIOPIC
    {"from": ord(u"\u1200"), "to": ord(u"\u137f")},  # Ethiopic
    {"from": ord(u"\u1380"), "to": ord(u"\u139f")},  # Ethiopic Supplement
    {"from": ord(u"\u2d80"), "to": ord(u"\u2ddf")},  # Ethiopic Extended
    {"from": ord(u"\uab00"), "to": ord(u"\uab2f")}  # Ethiopic Extended-A
]

NKo = [  # FONT: NOTO SANS NKO
    {"from": ord(u"\u07c0"), "to": ord(u"\u07ff")}  # N'Ko
]

Osmanya = [  # FONT: NOTO SANS OSMANYA
    {"from": ord(u"\U00010480"), "to": ord(u"\U000104af")}  # Osmanya
]

Tifinagh = [  # FONT: NOTO SANS TIFINAGH
    {"from": ord(u"\u2d30"), "to": ord(u"\u2d7f")}  # Tifinagh
]

Anatolian_Hieroglyphs = [  # FONT: ANATOLIAN HIEROGLYPHS
    {"from": ord(u"\U00014400"), "to": ord(u"\U0001467f")}  # Anatolian Hieroglyphs
]

Arabic = [  # FONT: NOTO SANS ARABIC
    {"from": ord(u"\u0600"), "to": ord(u"\u06ff")},  # Arabic
    {"from": ord(u"\u0750"), "to": ord(u"\u077f")},  # Arabic Supplement
    {"from": ord(u"\u08a0"), "to": ord(u"\u08ff")},  # Arabic Extended-A
    {"from": ord(u"\ufb50"), "to": ord(u"\ufdff")},  # Arabic Presentation Forms-A
    {"from": ord(u"\ufe70"), "to": ord(u"\ufeff")}  # Arabic Presentation Forms-B
]

Arameric_Imperial = [  # FONT: NOTO SANS IMPERIAL ARAMAIC
    {"from": ord(u"\U00010840"), "to": ord(u"\U0001085f")}  # Aramaic, Imperial
]

Avestan = [  # FONT: NOTO SANS AVESTAN
    {"from": ord(u"\U00010b00"), "to": ord(u"\U00010b3f")}  # Avestan
]

Hebrew = [  # FONT: NOTO SANS HEBREW
    {"from": ord(u"\u0590"), "to": ord(u"\u05ff")},  # Hebrew
    {"from": ord(u"\ufb1d"), "to": ord(u"\ufb4f")}  # Hebrew Presentation Forms
]

Mandiac = [  # FONT: NOTO SANS MANDIAC
    {"from": ord(u"\u0840"), "to": ord(u"\u085f")}  # Mandiac
]

Pahlavi_Inscriptional = [  # FONT: NOTO SANS INSCRIPTIONAL PAHLAVI
    {"from": ord(u"\U00010b60"), "to": ord(u"\U00010b7f")}  # Pahlavi Inscriptional
]

Parthian_Inscriptional = [  # FONT: NOTO SANS INSCRIPTIONAL PARTHIAN
    {"from": ord(u"\U00010b40"), "to": ord(u"\U00010b5f")}  # Parthian, Inscriptional
]

Phoenician = [  # FONT: NOTO SANS PHOENICIAN
    {"from": ord(u"\U00010900"), "to": ord(u"\U0001091f")}  # Pheonician
]

Samaritan = [  # FONT: NOTO SANS SAMARITAN
    {"from": ord(u"\u0800"), "to": ord(u"\u083f")}  # Samaritan
]

Mongolian = [  # FONT: NOTO SANS MONGOLIAN
    {"from": ord(u"\u1800"), "to": ord(u"\u18af")},  # Mongolian
    {"from": ord(u"\U00011660"), "to": ord(u"\U0001167f")}  # Mongolian Supplement
]

Old_Turkic = [  # FONT: NOTO SANS OLD TURKIC
    {"from": ord(u"\U00010c00"), "to": ord(u"\U00010c4f")}  # Old Turkic
]

Phags_Pa = [  # FONT: NOTO SANS PHAGS PS
    {"from": ord(u"\ua840"), "to": ord(u"\ua87f")}  # Phags-Pa
]

Tibetan = [  # FONT: NOTO SANS TIBETAN
    {"from": ord(u"\u0f00"), "to": ord(u"\u0fff")}  # Tibetan
]

Bengali = [  # FONT: NOTO SANS BENGALI
    {"from": ord(u"\u0980"), "to": ord(u"\u09ff")}  # Bengali and Assamese
]

Brahmi = [  # FONT: NOTO SANS BRAHMI
    {"from": ord(u"\U00011000"), "to": ord(u"\U0001107f")}  # Brahmi
]

Chakma = [  # FONT: NOTO SANS CHAKMA
    {"from": ord(u"\U00011100"), "to": ord(u"\U0001114f")}  # Chakma
]

Devanagari = [  # FONT: NOTO SANS DEVANAGARI
    {"from": ord(u"\u0900"), "to": ord(u"\u097f")},  # Devanagari
    {"from": ord(u"\ua8e0"), "to": ord(u"\ua8ff")}  # Devanagari Extended
]

Gujarati = [  # FONT: NOTO SANS GUKARATI
    {"from": ord(u"\u0a80"), "to": ord(u"\u0aff")}  # Gujarati
]

Gurmukhi = [  # FONT: NOTO SANS GURMUKHI
    {"from": ord(u"\u0a00"), "to": ord(u"\u0a7f")}  # Gurmukhi
]

Kaithi = [  # FONT: NOTO SANS KAITHI
    {"from": ord(u"\U00011080"), "to": ord(u"\U000110cf")}  # Kaithi
]

Kannada = [  # FONT: NOTO SANS KANNADA
    {"from": ord(u"\u0c80"), "to": ord(u"\u0cff")}  # Kannada
]

Kharoshthi = [  # FONT: NOTO SANS KHAROSHTHI
    {"from": ord(u"\U00010a00"), "to": ord(u"\U00010a5f")}  # Kharoshthi
]

Lepcha = [  # FONT: NOTO SANS LEPCHA
    {"from": ord(u"\u1c00"), "to": ord(u"\u1c4f")}  # Lepcha
]

Limbu = [  # FONT: NOTO SANS LIMBU
    {"from": ord(u"\u1900"), "to": ord(u"\u194f")}  # Limbu
]

Malayalam = [  # FONT: NOTO SANS MALAYALAM
    {"from": ord(u"\u0d00"), "to": ord(u"\u0d7f")}  # Malayalam
]

Meetei_Mayek = [  # FONT: NOTO SANS MAYEK
    {"from": ord(u"\uabc0"), "to": ord(u"\uabff")},  # Meetei Mayek
    {"from": ord(u"\uaae0"), "to": ord(u"\uaaff")}  # Meetei Mayek Extensions
]

Ol_Chiki = [  # FONT: NOTO SANS OL CHIKI
    {"from": ord(u"\u1c50"), "to": ord(u"\u1c7f")}  # Ol Chiki
]

Oriya = [  # FONT: NOTO SANS ORIYA
    {"from": ord(u"\u0b00"), "to": ord(u"\u0b7f")}  # Oriya
]

Saurashtra = [  # FONT: NOTO SANS SAURASHTRA
    {"from": ord(u"\ua880"), "to": ord(u"\ua8df")}  # Saurashtra
]

Sinhala = [  # FONT: NOTO SANS SINHALA
    {"from": ord(u"\u0d80"), "to": ord(u"\u0dff")},  # Sinhala
    {"from": ord(u"\U000111e0"), "to": ord(u"\U000111ff")}  # Sinhala Archaic Numbers
]

Syloti_Nagri = [  # FONT: NOTO SANS SYLOTI NAGRI
    {"from": ord(u"\ua800"), "to": ord(u"\ua82f")}  # Syloti Nagri
]

Tamil = [  # FONT: NOTO SANS TAMIL
    {"from": ord(u"\u0b80"), "to": ord(u"\u0bff")}  # Tamil
]

Telugu = [  # FONT: NOTO SANS TELUGU
    {"from": ord(u"\u0c00"), "to": ord(u"\u0c7f")}  # Telugu
]

Thaana = [  # FONT: NOTO SANS THAANA
    {"from": ord(u"\u0780"), "to": ord(u"\u07bf")}  # Thaana
]

Cham = [  # FONT: NOTO SANS CHAM
    {"from": ord(u"\uaa00"), "to": ord(u"\uaa5f")}  # Cham
]

Kayah_Li = [  # FONT: NOTO SANS KAYAH LI
    {"from": ord(u"\ua900"), "to": ord(u"\ua92f")}  # Kaya Li
]

Khmer = [  # FONT: NOTO SANS KHMER
    {"from": ord(u"\u1780"), "to": ord(u"\u17ff")},  # Khmer
    {"from": ord(u"\u19e0"), "to": ord(u"\u19ff")}  # Khmer Symbols
]

Lao = [  # FONT: NOTO SANS LAO
    {"from": ord(u"\u0e80"), "to": ord(u"\u0eff")}  # Lao
]

Myanmar = [  # FONT: NOTO SANS MYANMAR
    {"from": ord(u"\u1000"), "to": ord(u"\u109f")},  # Myanmar
    {"from": ord(u"\uaa60"), "to": ord(u"\uaa7f")},  # Myanmar Extended-A
    {"from": ord(u"\ua9e0"), "to": ord(u"\ua9ff")}  # Myanmar Extended-B
]

New_Tai_Lue = [  # FONT: NOTO SANS NEW TAI LUE
    {"from": ord(u"\u1980"), "to": ord(u"\u19df")}  # New Tai Lue
]

Tai_Le = [  # FONT: NOTO SANS TAI LE
    {"from": ord(u"\u1950"), "to": ord(u"\u197f")}  # Tai Le
]

Tai_Viet = [  # FONT: NOTO SANS TIA VIET
    {"from": ord(u"\uaa80"), "to": ord(u"\uaadf")}  # Tai Viet
]

Thai = [  # FONT: NOTO SANS THAI
    {"from": ord(u"\u0e00"), "to": ord(u"\u0e7f")}  # Thai
]

Balinese = [  # FONT: NOTO SANS BALINESE
    {"from": ord(u"\u1b00"), "to": ord(u"\u1b7f")}  # Balinese
]

Batak = [  # FONT: NOTO SANS BATAK
    {"from": ord(u"\u1bc0"), "to": ord(u"\u1bff")}  # Batak
]

Buginese = [  # FONT: NOTO SANS BUGINESE
    {"from": ord(u"\u1a00"), "to": ord(u"\u1a1f")}  # Buginese
]

Buhid = [  # NOTO SANS BUHID
    {"from": ord(u"\u1740"), "to": ord(u"\u175f")}  # Buhid
]

Hanunoo = [  # FONT: NOTO SANS HANUNOO
    {"from": ord(u"\u1720"), "to": ord(u"\u173f")}  # Hanunoo
]

Javanese = [  # FONT: NOTO SANS JAVANESE
    {"from": ord(u"\ua980"), "to": ord(u"\ua9df")}  # Javanese
]

Rejang = [  # FONT: REJANG
    {"from": ord(u"\ua930"), "to": ord(u"\ua95f")}  # Rejang
]

Tagalong = [  # FONT: NOTO SANS TAGALONG
    {"from": ord(u"\u1700"), "to": ord(u"\u171f")}  # Tagalong
]

Tagbanwa = [  # FONT: NOTO SANS TAGBANWA
    {"from": ord(u"\u1760"), "to": ord(u"\u177f")}  # Tagbanwa
]

Cherokee = [  # FONT: NOTO SANS CHEROKEE
    {"from": ord(u"\u13a0"), "to": ord(u"\u13ff")},  # Cherokee
    {"from": ord(u"\uab70"), "to": ord(u"\uabbf")}  # Cherokee Supplement
]

Deseret = [  # FONT: NOTO SANS DESERET
    {"from": ord(u"\U00010400"), "to": ord(u"\U0001044f")}  # Deseret
]

Osage = [  # FONT: NOTO SANS OSAGE
    {"from": ord(u"\U000104b0"), "to": ord(u"\U000104ff")}  # Osage
]

UCAS = [  # FONT: NOTO SANS CANADIAN ABORIGIANAL
    {"from": ord(u"\u1400"), "to": ord(u"\u167f")}  # Unified Canadian Aboriginal Syllabics
]

Emoji = [  # FONT: SEGOE UI EMOJI
    {"from": ord(u"\U0001f600"), "to": ord(u"\U0001f64f")},  # Emoticons
    {"from": ord(u"\u2600"), "to": ord(u"\u26ff")},  # Miscellaneous Symbols
    {"from": ord(u"\U0001f300"), "to": ord(u"\U0001f5ff")},  # Miscellaneous Symbols And Pictographs
    {"from": ord(u"\U0001f900"), "to": ord(u"\U0001f9ff")},  # Supplemental Symbols And Pictographs
    {"from": ord(u"\U0001f680"), "to": ord(u"\U0001f6ff")}  # Transport and Map Symbols
]

Default_Unicode = [  # FONT: NOTO SANS
    {"from": ord(u"\u0400"), "to": ord(u"\u04ff")},  # Cyrillic
    {"from": ord(u"\u0500"), "to": ord(u"\u052f")},  # Cyrillic Supplement
    {"from": ord(u"\u2de0"), "to": ord(u"\u2dff")},  # Cyrillic Extended-A
    {"from": ord(u"\ua640"), "to": ord(u"\u169f")},  # Cyrillic Extended-B
    {"from": ord(u"\u1c80"), "to": ord(u"\u1c8f")},  # Cyrillic Extended-C
    {"from": ord(u"\u0370"), "to": ord(u"\u03ff")},  # Greek
    {"from": ord(u"\u1f00"), "to": ord(u"\u1fff")},  # Greek Extended
    {"from": ord(u"\u0000"), "to": ord(u"\u007f")},  # Latin
    {"from": ord(u"\u0080"), "to": ord(u"\u00ff")},  # Latin-1 Supplement
    {"from": ord(u"\u0100"), "to": ord(u"\u017f")},  # Latin Extended-A
    {"from": ord(u"\u0180"), "to": ord(u"\u024f")},  # Latin Extended-B
    {"from": ord(u"\u2c60"), "to": ord(u"\u2c7f")},  # Latin Extended-C
    {"from": ord(u"\ua720"), "to": ord(u"\ua7ff")},  # Latin Extended-D
    {"from": ord(u"\uab30"), "to": ord(u"\uab6f")},  # Latin Extended-E
    {"from": ord(u"\u1e00"), "to": ord(u"\u1eff")},  # Latin Extended Additional
    {"from": ord(u"\ufb00"), "to": ord(u"\ufb06")},  # Latin Ligatures
    {"from": ord(u"\uff00"), "to": ord(u"\uff5e")},  # Full-width Latin Letters
    {"from": ord(u"\u0250"), "to": ord(u"\u02af")},  # IPA Extensions
    {"from": ord(u"\u1d00"), "to": ord(u"\u1d7f")},  # Phonetic Extensions
    {"from": ord(u"\u1d80"), "to": ord(u"\u1dbf")}  # Phonetic Extensions Supplement

]


# Noy Yet Supported:
# Elbasan
# Linear A
# Old Hungarian
# Old Permic
# Bassa Vah
# Medefaidrin
# Mende Kikakui
# Meroitic
# Cuniform
# Hatran
# Nabataean
# Old North Arabian
# Old South Arabian
# Psalter Pahlavi
# Palmyrene
# Manichaean
# Marchen
# Old Sogdian
# Sogdian
# Soyombo
# Zanabazar Square
# Ahom
# Braiksuki
# Dogra
# Grantha
# Gunjala Gondi
# Khojki
# Khundawadi
# Mahajani
# Masaram Gondi
# Modi
# Mro
# Multani
# Newa
# Sharada
# Siddham
# Sora Sompeng
# Takri
# Tirhuta
# Verdic Extensions
# Warang Citi
# Hanifi Rohingya
# Pahawh Hmong
# Pau Cin Hau
# Makasar
# Sudanese
# Bofomofo


def search(input_string):
    input_string = str(input_string)
    input_string = list(input_string)
    for i in range(len(input_string)):

        # CJK
        current_range = CJK
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            print('Font range: CJK')
            return "NotoSansCJKjp"

        # Armenian
        current_range = Armenian
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            print('Font range: Armenian')
            return "NotoSansArmenian"

        # Carian
        current_range = Carian
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansCarian"

        # Cypriot
        current_range = Cypriot_Syllabary
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "Noto-SansSypriot"

        # Georgian
        current_range = Georgian
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansGeogian"

        # Glogolitic
        current_range = Glogolitic
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansGlogolitic"

        # Gothic
        current_range = Gothic
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansGothic"

        # Linear B
        current_range = Linear_B
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansLinearB"

        # Lycian
        current_range = Lycian
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansLycian"

        # Lydian
        current_range = Lydian
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansLydian"

        # Ogham
        current_range = Ogham
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansOgham"

        # Old Italic
        current_range = Old_Italic
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansOldItalic"

        # Runic
        current_range = Runic
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansRunic"

        # Shavian
        current_range = Shavian
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansShavian"

        # Adlam
        current_range = Adlam
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansAdlam"

        # Bamum
        current_range = Bamum
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansBamum"

        # Coptic
        current_range = Coptic
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansCoptic"

        # Egyption Hieroglyphs
        current_range = Egyptian_Hieroglyphs
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansEgptianHieroglyphs"

        # Ethiopic
        current_range = Ethiopic
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansEthiopic"

        # N'Ko
        current_range = NKo
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansNKo"

        # Osmanya
        current_range = Osmanya
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansOsmanya"

        # Tifinagh
        current_range = Tifinagh
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansTifinagh"

        # Anatolian Heiroglphys
        current_range = Anatolian_Hieroglyphs
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansAnatolianHieroglyphs"

        # Arabic
        current_range = Arabic
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansArabic"

        # Arameric Imperial
        current_range = Arameric_Imperial
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansImperialAramaic"

        # Avestan
        current_range = Avestan
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansAvestan"

        # Hebrew
        current_range = Hebrew
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansHebrew"

        # Mandiac
        current_range = Mandiac
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansMandiac"

        # Pahlavi Inscriptional
        current_range = Pahlavi_Inscriptional
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "Noto-SansInscriptionalPahlavi"

        # Parthian Inscriptional
        current_range = Parthian_Inscriptional
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansInscriptionalParthian"

        # Phoenician
        current_range = Phoenician
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansPhoenician"

        # Samaritan
        current_range = Samaritan
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansSamaritan"

        # Mongolian
        current_range = Mongolian
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansMongolian"

        # Old Turkic
        current_range = Old_Turkic
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansOldTurkic"

        # Phags_Pa
        current_range = Phags_Pa
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansPhagsPa"

        # Tibetan
        current_range = Tibetan
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansTibetan"

        # Bengali
        current_range = Bengali
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansBengali"

        # Brahmi
        current_range = Brahmi
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansBrahmi"

        # Chakma
        current_range = Chakma
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansChakma"

        # Devanagari
        current_range = Devanagari
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansDevanagari"

        # Gujarati
        current_range = Gujarati
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansGujarati"

        # Gurmukhi
        current_range = Gurmukhi
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansGurmukhi"

        # Kaithi
        current_range = Kaithi
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansKaithi"

        # Kannada
        current_range = Kannada
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansKannada"

        # Kharoshthi
        current_range = Kharoshthi
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansKharoshthi"

        # Lepcha
        current_range = Lepcha
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansLepcha"

        # Limbu
        current_range = Limbu
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansLimbu"

        # Malayakan
        current_range = Malayalam
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansMalayalam"

        # Meetei Mayek
        current_range = Meetei_Mayek
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansMayek"

        # Ol Chiki
        current_range = Ol_Chiki
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansOlChiki"

        # Oriya
        current_range = Oriya
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansOriya"

        # Saurashtra
        current_range = Saurashtra
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansSaurashtraa"

        # Sinhala
        current_range = Sinhala
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansSinhala"

        # Syloti Nagri
        current_range = Syloti_Nagri
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansSylotiNagri"

        # Tamil
        current_range = Tamil
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansTamil"

        # Telugu
        current_range = Telugu
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansTelugu"

        # Thaana
        current_range = Thaana
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansThaana"

        # Cham
        current_range = Cham
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansCham"

        # Kayah Li
        current_range = Kayah_Li
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansKayahLi"

        # Khmer
        current_range = Khmer
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansKhmen"

        # Lao
        current_range = Lao
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansLao"

        # Myanmar
        current_range = Myanmar
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansMyanmar"

        # New Tai Lue
        current_range = New_Tai_Lue
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansNewTaiLue"

        # Tai Le
        current_range = Tai_Le
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansTaiLe"

        # Tai Viet
        current_range = Tai_Viet
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansTaiViet"

        # Thai
        current_range = Thai
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansThai"

        # Balinese
        current_range = Balinese
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansBalinese"

        # Batak
        current_range = Batak
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansBatak"

        # Buginese
        current_range = Buginese
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansBuginese"

        # Buhid
        current_range = Buhid
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansBuhid"

        # Hanunoo
        current_range = Hanunoo
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansHanunoo"

        # Javanese
        current_range = Javanese
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansJavanese"

        # Rejang
        current_range = Rejang
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansRejang"

        # Tagalong
        current_range = Tagalong
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansTagalong"

        # Tagbanwa
        current_range = Tagbanwa
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansTagbanwa"

        # Cherokee
        current_range = Cherokee
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansCherokee"

        # Deseret
        current_range = Deseret
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansDeseret"

        # Osage
        current_range = Osage
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansOsage"

        # United Canadian Aborigional Syllabics
        current_range = UCAS
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return "NotoSansCanadianAborigianal"

        # Emoji
        current_range = Emoji
        if any([range["from"] <= ord(input_string[i]) <= range["to"] for range in current_range]):
            return 'NotoEmoji'

        return ('NotoSans')
