# SPDX-FileCopyrightText: 2025-2026 Samuel Moxham
# SPDX-License-Identifier: MIT
"""Authored website strings for every locale.

Leaf values are dicts keyed by locale code. English is the source of truth for
wording; other locales are filled by update_catalog.py (and never overwritten
while the English hash for that key is unchanged).

Te reo Māori should get native review.
"""

from __future__ import annotations

LOCALES = ("en", "mi", "es", "de", "ru", "ja", "ar", "hi")

LOCALE_META = {
    "en": {"name": "English", "og": "en_US", "dir": "ltr", "google": "en"},
    "mi": {"name": "Te reo Māori", "og": "mi_NZ", "dir": "ltr", "google": "mi"},
    "es": {"name": "Español", "og": "es_ES", "dir": "ltr", "google": "es"},
    "de": {"name": "Deutsch", "og": "de_DE", "dir": "ltr", "google": "de"},
    "ru": {"name": "Русский", "og": "ru_RU", "dir": "ltr", "google": "ru"},
    "ja": {"name": "日本語", "og": "ja_JP", "dir": "ltr", "google": "ja"},
    "ar": {"name": "العربية", "og": "ar", "dir": "rtl", "google": "ar"},
    "hi": {"name": "हिन्दी", "og": "hi_IN", "dir": "ltr", "google": "hi"},
}

# Keep product names, protocols, and version tags identical in every locale.
LANG_LIST = (
    "English, Te reo Māori, Español, Deutsch, Русский, 日本語, العربية, हिन्दी"
)


def S(en: str, mi: str, es: str, de: str, ru: str, ja: str, ar: str, hi: str) -> dict[str, str]:
    return {
        "en": en,
        "mi": mi,
        "es": es,
        "de": de,
        "ru": ru,
        "ja": ja,
        "ar": ar,
        "hi": hi,
    }


STRINGS: dict = {
    "nav": {
        "download": S("Download", "Tikiake", "Descargar", "Herunterladen", "Скачать", "ダウンロード", "تنزيل", "डाउनलोड"),
        "documentation": S("Documentation", "Tuhinga", "Documentación", "Dokumentation", "Документация", "ドキュメント", "التوثيق", "दस्तावेज़"),
        "about": S("About", "Mō", "Acerca de", "Über", "О проекте", "概要", "حول", "परिचय"),
        "github": S("GitHub", "GitHub", "GitHub", "GitHub", "GitHub", "GitHub", "GitHub", "GitHub"),
        "home": S("Home", "Kāinga", "Inicio", "Start", "Главная", "ホーム", "الرئيسية", "होम"),
        "language": S("Language", "Reo", "Idioma", "Sprache", "Язык", "言語", "اللغة", "भाषा"),
    },
    "footer": {
        "copyright_before": S(
            "© 2025–2026 Samuel Moxham. Cue2 is open source under the MIT License. Website source on",
            "© 2025–2026 Samuel Moxham. He pūmana MIT a Cue2. Kei",
            "© 2025–2026 Samuel Moxham. Cue2 es código abierto bajo la licencia MIT. Código del sitio en",
            "© 2025–2026 Samuel Moxham. Cue2 ist Open Source unter der MIT-Lizenz. Website-Quellcode auf",
            "© 2025–2026 Samuel Moxham. Cue2 — открытое ПО по лицензии MIT. Исходный код сайта на",
            "© 2025–2026 Samuel Moxham. Cue2 は MIT ライセンスのオープンソースです。サイトのソースは",
            "© 2025–2026 Samuel Moxham. Cue2 برنامج مفتوح المصدر برخصة MIT. مصدر الموقع على",
            "© 2025–2026 Samuel Moxham. Cue2 MIT लाइसेंस के तहत ओपन सोर्स है। साइट स्रोत:",
        ),
        "copyright_after": S(".", ".", ".", ".", ".", "。", ".", "।"),
    },
    "download": {
        "aria": S("Download Cue2", "Tikiake Cue2", "Descargar Cue2", "Cue2 herunterladen", "Скачать Cue2", "Cue2 をダウンロード", "تنزيل Cue2", "Cue2 डाउनलोड करें"),
        "windows": S("Download Cue2 for Windows", "Tikiake Cue2 mō Windows", "Descargar Cue2 para Windows", "Cue2 für Windows herunterladen", "Скачать Cue2 для Windows", "Windows 用 Cue2 をダウンロード", "تنزيل Cue2 لـ Windows", "Windows के लिए Cue2 डाउनलोड करें"),
        "macos": S("Download Cue2 for macOS", "Tikiake Cue2 mō macOS", "Descargar Cue2 para macOS", "Cue2 für macOS herunterladen", "Скачать Cue2 для macOS", "macOS 用 Cue2 をダウンロード", "تنزيل Cue2 لـ macOS", "macOS के लिए Cue2 डाउनलोड करें"),
        "linux": S("Download Cue2 for Linux", "Tikiake Cue2 mō Linux", "Descargar Cue2 para Linux", "Cue2 für Linux herunterladen", "Скачать Cue2 для Linux", "Linux 用 Cue2 をダウンロード", "تنزيل Cue2 لـ Linux", "Linux के लिए Cue2 डाउनलोड करें"),
        "windows_x64": S("Windows x64", "Windows x64", "Windows x64", "Windows x64", "Windows x64", "Windows x64", "Windows x64", "Windows x64"),
        "windows_arm64": S("Windows ARM64", "Windows ARM64", "Windows ARM64", "Windows ARM64", "Windows ARM64", "Windows ARM64", "Windows ARM64", "Windows ARM64"),
        "macos_arm64": S("macOS (Apple Silicon)", "macOS (Apple Silicon)", "macOS (Apple Silicon)", "macOS (Apple Silicon)", "macOS (Apple Silicon)", "macOS (Apple Silicon)", "macOS (Apple Silicon)", "macOS (Apple Silicon)"),
        "linux_x64": S("Linux x64", "Linux x64", "Linux x64", "Linux x64", "Linux x64", "Linux x64", "Linux x64", "Linux x64"),
        "linux_arm64": S("Linux ARM64", "Linux ARM64", "Linux ARM64", "Linux ARM64", "Linux ARM64", "Linux ARM64", "Linux ARM64", "Linux ARM64"),
        "all_releases": S("All releases on GitHub", "Ngā putanga katoa i GitHub", "Todas las versiones en GitHub", "Alle Versionen auf GitHub", "Все выпуски на GitHub", "GitHub 上のすべてのリリース", "كل الإصدارات على GitHub", "GitHub पर सभी रिलीज़"),
    },
    "home": {
        "title": S(
            "Cue2 — Open-source live media playback and show control",
            "Cue2 — Purei pāpāho ora pūmana me te whakahaere whakaaturanga",
            "Cue2 — Reproducción de medios en vivo y control de espectáculo de código abierto",
            "Cue2 — Open-Source-Live-Medienwiedergabe und Showsteuerung",
            "Cue2 — открытое ПО для живого медиавоспроизведения и управления шоу",
            "Cue2 — オープンソースのライブメディア再生とショーコントロール",
            "Cue2 — تشغيل وسائط حيّة مفتوح المصدر وتحكم بالعرض",
            "Cue2 — ओपन-सोर्स लाइव मीडिया प्लेबैक और शो नियंत्रण",
        ),
        "description": S(
            "Cue2 is free, open-source cue-based playback for live events. Run audio, video, text, OSC and MIDI from a cuelist on Windows, macOS and Linux.",
            "He pūmana, he kore utu a Cue2 mō te purei tohu i ngā kaupapa ora. Whakahaerea te oro, ataata, kupu, OSC me te MIDI i tētahi rārangi tohu i Windows, macOS me Linux.",
            "Cue2 es reproducción gratuita y de código abierto basada en cues para eventos en vivo. Audio, vídeo, texto, OSC y MIDI desde una cuelist en Windows, macOS y Linux.",
            "Cue2 ist kostenlose, quelloffene cue-basierte Wiedergabe für Live-Events. Audio, Video, Text, OSC und MIDI aus einer Cuelist auf Windows, macOS und Linux.",
            "Cue2 — бесплатное открытое cue-воспроизведение для живых событий. Аудио, видео, текст, OSC и MIDI из cuelist на Windows, macOS и Linux.",
            "Cue2 はライブイベント向けの無料オープンソースのキュー再生です。Windows、macOS、Linux のキューリストから音声、映像、テキスト、OSC、MIDI を実行します。",
            "Cue2 تشغيل مجاني ومفتوح المصدر قائم على الإشارات للفعاليات الحية. شغّل الصوت والفيديو والنص وOSC وMIDI من قائمة إشارات على Windows وmacOS وLinux.",
            "Cue2 लाइव इवेंट के लिए मुफ़्त, ओपन-सोर्स क्यू-आधारित प्लेबैक है। Windows, macOS और Linux पर क्यूलिस्ट से ऑडियो, वीडियो, टेक्स्ट, OSC और MIDI चलाएँ।",
        ),
        "hero_h1": S(
            "Open-source media playback for live events",
            "Purei pāpāho pūmana mō ngā kaupapa ora",
            "Reproducción de medios de código abierto para eventos en vivo",
            "Open-Source-Medienwiedergabe für Live-Events",
            "Открытое медиавоспроизведение для живых событий",
            "ライブイベント向けオープンソースメディア再生",
            "تشغيل وسائط مفتوح المصدر للفعاليات الحية",
            "लाइव इवेंट के लिए ओपन-सोर्स मीडिया प्लेबैक",
        ),
        "hero_lede": S(
            "A lightweight and versatile app to run audio, video, text, OSC and MIDI from a cuelist on Windows, macOS and Linux.",
            "He taupānga māmā, whaikiko hoki hei whakahaere oro, ataata, kupu, OSC me te MIDI i tētahi rārangi tohu i Windows, macOS me Linux.",
            "Una app ligera y versátil para reproducir audio, vídeo, texto, OSC y MIDI desde una cuelist en Windows, macOS y Linux.",
            "Eine schlanke, vielseitige App für Audio, Video, Text, OSC und MIDI aus einer Cuelist auf Windows, macOS und Linux.",
            "Лёгкое и гибкое приложение: аудио, видео, текст, OSC и MIDI из cuelist на Windows, macOS и Linux.",
            "Windows、macOS、Linux のキューリストから音声、映像、テキスト、OSC、MIDI を実行する、軽量で汎用的なアプリです。",
            "تطبيق خفيف ومتعدد الاستخدامات لتشغيل الصوت والفيديو والنص وOSC وMIDI من قائمة إشارات على Windows وmacOS وLinux.",
            "Windows, macOS और Linux पर क्यूलिस्ट से ऑडियो, वीडियो, टेक्स्ट, OSC और MIDI चलाने वाला हल्का, बहुउपयोगी ऐप।",
        ),
        "screenshot_alt": S(
            "Cue2 0.1 showing a theatre cuelist, active cues, and an audio waveform",
            "Cue2 0.1 e whakaatu ana i tētahi rārangi tohu whare tapere, ngā tohu hohe, me tētahi ngaru oro",
            "Cue2 0.1 mostrando una cuelist de teatro, cues activas y una forma de onda de audio",
            "Cue2 0.1 mit einer Theater-Cuelist, aktiven Cues und einer Audio-Wellenform",
            "Cue2 0.1: театральный cuelist, активные cues и звуковая волна",
            "劇場のキューリスト、アクティブなキュー、音声波形を示す Cue2 0.1",
            "Cue2 0.1 يعرض قائمة إشارات مسرحية وإشارات نشطة وموجة صوت",
            "Cue2 0.1 थिएटर क्यूलिस्ट, सक्रिय क्यू और ऑडियो वेवफ़ॉर्म दिखाता हुआ",
        ),
        "release_note": S(
            "Cue2 <strong>0.1.0 StripyHat</strong> is the first public alpha. Download the archive for your OS, unpack it, and run Cue2. A great deal of care has gone into making it reliable, but you should still treat it with the caution appropriate to alpha software.",
            "Ko Cue2 <strong>0.1.0 StripyHat</strong> te arpha tūmatanui tuatahi. Tikiakehia te pūranga mō tō pūnaha, wewetehia, ka whakahaere i a Cue2. Kua nui te atawhai kia pono, engari me āta whakamahi tonu nā te mea he pūmana arpha.",
            "Cue2 <strong>0.1.0 StripyHat</strong> es la primera alfa pública. Descarga el archivo para tu sistema, descomprímelo y ejecuta Cue2. Se ha cuidado mucho la fiabilidad, pero trátalo con la cautela propia de un software alfa.",
            "Cue2 <strong>0.1.0 StripyHat</strong> ist die erste öffentliche Alpha. Laden Sie das Archiv für Ihr Betriebssystem herunter, entpacken Sie es und starten Sie Cue2. Es wurde mit viel Sorgfalt zuverlässig gemacht, bleibt aber Alpha-Software — entsprechend vorsichtig einsetzen.",
            "Cue2 <strong>0.1.0 StripyHat</strong> — первая публичная альфа. Скачайте архив для своей ОС, распакуйте и запустите Cue2. Надёжности уделено много внимания, но это всё ещё альфа — используйте с соответствующей осторожностью.",
            "Cue2 <strong>0.1.0 StripyHat</strong> は初の公開アルファです。お使いの OS 用アーカイブをダウンロードし、展開して Cue2 を実行してください。信頼性には十分配慮していますが、アルファ版として慎重に扱ってください。",
            "Cue2 <strong>0.1.0 StripyHat</strong> هي أول ألفا عامة. نزّل الأرشيف لنظامك، فكّه، وشغّل Cue2. بُذل جهد كبير لجعله موثوقاً، لكن تعامل معه بحذر يليق ببرمجيات ألفا.",
            "Cue2 <strong>0.1.0 StripyHat</strong> पहला सार्वजनिक अल्फा है। अपने OS का आर्काइव डाउनलोड करें, खोलें, और Cue2 चलाएँ। विश्वसनीयता पर काफ़ी ध्यान दिया गया है, फिर भी अल्फा सॉफ़्टवेयर की तरह सावधानी से इस्तेमाल करें।",
        ),
        "about_h2": S("About Cue2", "Mō Cue2", "Acerca de Cue2", "Über Cue2", "О Cue2", "Cue2 について", "حول Cue2", "Cue2 के बारे में"),
        "about_p1": S(
            "Cue2 is a desktop application for <strong>sequenced playback of audio, video, text overlays, and show-control messages</strong>. Cues consist of a shell and components. The shell is the playback instructions for the cue. The components are the actions the cue is to make. The cuelist is also loosely structured: any cue can be assigned as a child of another cue at will, to be played together. This allows complex sequence structures while remaining easy to program.",
            "He taupānga rorohiko a Cue2 mō te <strong>purei raupapa o te oro, ataata, kupu takatika, me ngā karere whakahaere whakaaturanga</strong>. He anga me ngā waehanga ō ngā tohu. Ko te anga ngā tohutohu purei. Ko ngā waehanga ngā mahi a te tohu. He hanganga ngāwari te rārangi tohu: ka taea te whakamōtū i tētahi tohu hei tamaiti nō tētahi atu, kia purei ngātahi. He raupapa uaua, he māmā tonu te papatono.",
            "Cue2 es una aplicación de escritorio para <strong>reproducción secuenciada de audio, vídeo, superposiciones de texto y mensajes de control de espectáculo</strong>. Las cues tienen una cáscara y componentes. La cáscara son las instrucciones de reproducción. Los componentes son las acciones de la cue. La cuelist es flexible: cualquier cue puede ser hija de otra y reproducirse juntas. Así se arman secuencias complejas sin dejar de ser fáciles de programar.",
            "Cue2 ist eine Desktop-Anwendung für <strong>sequenzielle Wiedergabe von Audio, Video, Text-Overlays und Show-Control-Nachrichten</strong>. Cues bestehen aus einer Hülle und Komponenten. Die Hülle sind die Wiedergabeanweisungen. Die Komponenten sind die Aktionen der Cue. Die Cuelist ist locker strukturiert: Jede Cue kann nach Belieben Kind einer anderen sein und gemeinsam abgespielt werden. So entstehen komplexe Abläufe, die sich trotzdem leicht programmieren lassen.",
            "Cue2 — настольное приложение для <strong>последовательного воспроизведения аудио, видео, текстовых наложений и сообщений управления шоу</strong>. Cue состоит из оболочки и компонентов. Оболочка — инструкции воспроизведения. Компоненты — действия cue. Cuelist устроен свободно: любую cue можно сделать дочерней другой, чтобы играть вместе. Так получаются сложные последовательности, которые всё ещё просто программировать.",
            "Cue2 は<strong>音声、映像、テキストオーバーレイ、ショーコントロールメッセージのシーケンス再生</strong>向けデスクトップアプリです。キューはシェルとコンポーネントでできています。シェルは再生の指示、コンポーネントはキューが行う動作です。キューリストはゆるい構造で、任意のキューを別のキューの子にして一緒に再生できます。複雑なシーケンスでも、プログラミングは簡単です。",
            "Cue2 تطبيق سطح مكتب لـ<strong>تشغيل متسلسل للصوت والفيديو وطبقات النص ورسائل تحكم العرض</strong>. تتكون الإشارة من غلاف ومكوّنات. الغلاف تعليمات التشغيل. المكوّنات هي أفعال الإشارة. قائمة الإشارات مرنة: يمكن جعل أي إشارة ابناً لأخرى لتعمل معاً. يتيح ذلك تراكيب تسلسل معقّدة مع بقاء البرمجة سهلة.",
            "Cue2 <strong>ऑडियो, वीडियो, टेक्स्ट ओवरले और शो-कंट्रोल संदेशों के अनुक्रमित प्लेबैक</strong> के लिए एक डेस्कटॉप ऐप है। क्यू में शेल और कंपोनेंट होते हैं। शेल प्लेबैक निर्देश हैं। कंपोनेंट वे क्रियाएँ हैं जो क्यू करेगा। क्यूलिस्ट ढीली संरचना वाली है: किसी भी क्यू को दूसरी क्यू का चाइल्ड बनाकर साथ चलाया जा सकता है। जटिल सीक्वेंस भी प्रोग्राम करना आसान रहता है।",
        ),
        "about_p2": S(
            "Cue2 was made with love for community performing arts around the world. But it can also be used in many more settings, and in any workflow that needs reliable triggering of media and network commands. Media decode uses <strong>FFmpeg</strong>, allowing a wide range of supported formats. Audio I/O uses <strong>SDL3</strong>. The application is <strong>MIT-licensed</strong> and free to use, modify, and redistribute.",
            "I hangaia a Cue2 ki te aroha mō ngā mahi whakaari hapori o te ao. Engari ka taea hoki i ētahi atu wāhi, i ngā mahi rānei e hiahia ana ki te pūrena pono o te pāpāho me ngā whakahau whatunga. Ka whakamahi te wetewete pāpāho i a <strong>FFmpeg</strong>, he maha ngā hōputu. Ko <strong>SDL3</strong> te I/O oro. He raihana <strong>MIT</strong> te taupānga — wātea te whakamahi, te whakarerekē, te tohatoha.",
            "Cue2 nació con cariño por las artes escénicas comunitarias de todo el mundo. También sirve en muchos otros contextos y en cualquier flujo que necesite disparar medios y comandos de red con fiabilidad. La decodificación usa <strong>FFmpeg</strong>, con una amplia gama de formatos. El I/O de audio usa <strong>SDL3</strong>. La aplicación tiene <strong>licencia MIT</strong>: úsala, modifícala y redistribúyela.",
            "Cue2 entstand aus Liebe zur darstellenden Community-Kunst weltweit. Es eignet sich aber auch für viele andere Kontexte und jeden Ablauf, der zuverlässiges Auslösen von Medien und Netzwerkbefehlen braucht. Die Dekodierung nutzt <strong>FFmpeg</strong> und damit viele Formate. Audio-I/O nutzt <strong>SDL3</strong>. Die Anwendung steht unter der <strong>MIT-Lizenz</strong> — nutzen, ändern, weitergeben.",
            "Cue2 сделан с любовью к любительскому сценическому искусству по всему миру. Его можно применять и в других местах — везде, где нужно надёжно запускать медиа и сетевые команды. Декодирование через <strong>FFmpeg</strong> даёт широкий набор форматов. Аудио I/O — <strong>SDL3</strong>. Приложение под <strong>лицензией MIT</strong>: можно использовать, менять и распространять.",
            "Cue2 は世界のコミュニティ舞台芸術への愛から生まれました。メディアとネットワークコマンドを確実にトリガーしたい、ほかの現場やワークフローでも使えます。デコードは <strong>FFmpeg</strong> で、多くの形式に対応します。音声 I/O は <strong>SDL3</strong>。アプリは <strong>MIT ライセンス</strong>で、利用・改変・再配布が自由です。",
            "صُنع Cue2 بحب لفنون الأداء المجتمعية حول العالم. ويمكن استخدامه في سياقات كثيرة أخرى، وفي أي سير عمل يحتاج إطلاقاً موثوقاً للوسائط وأوامر الشبكة. فكّ الوسائط عبر <strong>FFmpeg</strong> يدعم نطاقاً واسعاً من الصيغ. دخل/خرج الصوت عبر <strong>SDL3</strong>. التطبيق بـ<strong>رخصة MIT</strong> ومجاني للاستخدام والتعديل وإعادة التوزيع.",
            "Cue2 दुनिया भर की सामुदायिक प्रदर्शन कला के लिए प्यार से बना है। और भी कई जगहों पर, और किसी भी वर्कफ़्लो में जहाँ मीडिया और नेटवर्क कमांड विश्वसनीय रूप से ट्रिगर हों, इसका उपयोग हो सकता है। डिकोड <strong>FFmpeg</strong> से होता है, इसलिए कई फ़ॉर्मैट चलते हैं। ऑडियो I/O <strong>SDL3</strong> है। ऐप <strong>MIT-लाइसेंस</strong> है — उपयोग, बदलाव और पुनर्वितरण मुक्त है।",
        ),
        "features_h2": S("What you can do", "Ngā mahi ka taea", "Qué puedes hacer", "Was Sie tun können", "Что можно делать", "できること", "ما يمكنك فعله", "आप क्या कर सकते हैं"),
        "feature_audio_h3": S("Audio playback", "Purei oro", "Reproducción de audio", "Audiowiedergabe", "Воспроизведение аудио", "音声再生", "تشغيل الصوت", "ऑडियो प्लेबैक"),
        "feature_audio_p": S(
            "Play sound files from the cuelist with patches, a per-cue routing matrix, levels, pan, and fades.",
            "Pureia ngā kōnae oro i te rārangi tohu, me ngā pātene, he mātiti ararere ia tohu, ngā taumata, te pan, me ngā memeha.",
            "Reproduce archivos de sonido desde la cuelist con parches, una matriz de enrutado por cue, niveles, paneo y fundidos.",
            "Spielen Sie Tondateien aus der Cuelist mit Patches, einer Routing-Matrix pro Cue, Pegeln, Pan und Fades.",
            "Воспроизводите звуковые файлы из cuelist: патчи, матрица маршрутизации на cue, уровни, панорама и фейды.",
            "キューリストから音声ファイルを再生。パッチ、キューごとのルーティングマトリクス、レベル、パン、フェードに対応。",
            "شغّل ملفات الصوت من قائمة الإشارات مع باتشات ومصفوفة توجيه لكل إشارة ومستويات وبان وفيد.",
            "क्यूलिस्ट से साउंड फ़ाइलें चलाएँ — पैच, प्रति-क्यू राउटिंग मैट्रिक्स, लेवल, पैन और फ़ेड के साथ।",
        ),
        "feature_audio_link": S("Zero to audio", "Kore ki te oro", "De cero a audio", "Von null zu Audio", "С нуля до аудио", "ゼロから音声へ", "من الصفر إلى الصوت", "शून्य से ऑडियो तक"),
        "feature_video_h3": S("Video and displays", "Ataata me ngā whakaatu", "Vídeo y pantallas", "Video und Displays", "Видео и экраны", "映像とディスプレイ", "الفيديو والشاشات", "वीडियो और डिस्प्ले"),
        "feature_video_p": S(
            "Put movies, stills, and text on a multi-screen canvas with layers.",
            "Whakanohoia ngā kiriata, pikitia, me ngā kupu ki tētahi kānawe mata-maha, me ngā paparanga.",
            "Pon películas, imágenes y texto en un lienzo multi-pantalla con capas.",
            "Filme, Standbilder und Text auf einer Mehrschirm-Leinwand mit Ebenen.",
            "Фильмы, кадры и текст на многоэкранном холсте со слоями.",
            "複数画面キャンバスのレイヤーに動画、静止画、テキストを出せます。",
            "ضع أفلاماً وصوراً ونصاً على لوحة متعددة الشاشات بطبقات.",
            "मल्टी-स्क्रीन कैनवस पर लेयर के साथ फ़िल्में, स्टिल और टेक्स्ट रखें।",
        ),
        "feature_video_link": S("Zero to video", "Kore ki te ataata", "De cero a vídeo", "Von null zu Video", "С нуля до видео", "ゼロから映像へ", "من الصفر إلى الفيديو", "शून्य से वीडियो तक"),
        "feature_show_h3": S("Show control", "Whakahaere whakaaturanga", "Control de espectáculo", "Showsteuerung", "Управление шоу", "ショーコントロール", "تحكم العرض", "शो नियंत्रण"),
        "feature_show_p": S(
            "Listen and send OSC and MIDI. Drive Cue2 from the network, or fire other devices from a cue. Cue lights are in the box.",
            "Whakarongo, tuku OSC me te MIDI. Whakahaerea a Cue2 i te whatunga, tūwhera rānei ētahi atu pūrere i tētahi tohu. Kei roto ngā rama tohu.",
            "Escucha y envía OSC y MIDI. Controla Cue2 por red o dispara otros dispositivos desde una cue. Las cue lights van incluidas.",
            "OSC und MIDI empfangen und senden. Cue2 übers Netzwerk steuern oder andere Geräte aus einer Cue feuern. Cue-Lights sind dabei.",
            "Приём и отправка OSC и MIDI. Управляйте Cue2 по сети или запускайте другие устройства из cue. Cue-lights уже в комплекте.",
            "OSC と MIDI の受信・送信。ネットワークから Cue2 を操作したり、キューから他機器を発火できます。キューライトも同梱です。",
            "استمع وأرسل OSC وMIDI. شغّل Cue2 من الشبكة، أو أطلق أجهزة أخرى من إشارة. أضواء الإشارات مضمّنة.",
            "OSC और MIDI सुनें और भेजें। नेटवर्क से Cue2 चलाएँ, या क्यू से दूसरे डिवाइस फायर करें। क्यू लाइट बॉक्स में शामिल हैं।",
        ),
        "feature_show_link": S("OSC command reference", "Tohutoro whakahau OSC", "Referencia de comandos OSC", "OSC-Befehlsreferenz", "Справка по командам OSC", "OSC コマンドリファレンス", "مرجع أوامر OSC", "OSC कमांड संदर्भ"),
        "feature_seq_h3": S("Sequences and groups", "Raupapa me ngā rōpū", "Secuencias y grupos", "Sequenzen und Gruppen", "Последовательности и группы", "シーケンスとグループ", "التسلسلات والمجموعات", "सीक्वेंस और ग्रुप"),
        "feature_seq_p": S(
            "Pre-wait, post-wait, Continue, Follow, nested groups, and a playhead that operators already understand.",
            "Tataritanga-mua, tataritanga-muri, Haere tonu, Whai, ngā rōpū kōpūpū, me te upoko-purei e mōhio kē ana ngā kaiwhakahaere.",
            "Preespera, postespera, Continue, Follow, grupos anidados y un playhead que los operadores ya entienden.",
            "Pre-Wait, Post-Wait, Continue, Follow, verschachtelte Gruppen und ein Playhead, den Operatoren schon kennen.",
            "Pre-wait, post-wait, Continue, Follow, вложенные группы и playhead, который операторы уже понимают.",
            "プリウェイト、ポストウェイト、Continue、Follow、入れ子グループ、オペレーターが既に知っているプレイヘッド。",
            "انتظار مسبق ولاحق، Continue وFollow، مجموعات متداخلة، ورأس تشغيل يفهمه المشغّلون مسبقاً.",
            "प्री-वेट, पोस्ट-वेट, Continue, Follow, नेस्टेड ग्रुप, और एक प्लेहेड जिसे ऑपरेटर पहले से समझते हैं।",
        ),
        "feature_seq_link": S("Cue sequences", "Raupapa tohu", "Secuencias de cues", "Cue-Sequenzen", "Последовательности cue", "キューシーケンス", "تسلسلات الإشارات", "क्यू सीक्वेंस"),
        "feature_cross_h3": S("Cross-platform", "Tū-papa-maha", "Multiplataforma", "Plattformübergreifend", "Кроссплатформенность", "クロスプラットフォーム", "متعدد المنصات", "क्रॉस-प्लेटफ़ॉर्म"),
        "feature_cross_p": S(
            "Windows 10+, macOS, and Linux, including x64 and ARM where we ship builds.",
            "Windows 10+, macOS, me Linux, tae atu ki te x64 me te ARM kei reira ngā hanga.",
            "Windows 10+, macOS y Linux, incluyendo x64 y ARM donde publicamos builds.",
            "Windows 10+, macOS und Linux, inklusive x64 und ARM, wo wir Builds ausliefern.",
            "Windows 10+, macOS и Linux, включая x64 и ARM там, где есть сборки.",
            "Windows 10+、macOS、Linux。ビルドを出す x64 と ARM に対応。",
            "Windows 10+ وmacOS وLinux، بما في ذلك x64 وARM حيث نوفّر بناءات.",
            "Windows 10+, macOS, और Linux — जहाँ हम बिल्ड देते हैं वहाँ x64 और ARM सहित।",
        ),
        "feature_cross_link": S("System requirements", "Ngā whakaritenga pūnaha", "Requisitos del sistema", "Systemanforderungen", "Системные требования", "システム要件", "متطلبات النظام", "सिस्टम आवश्यकताएँ"),
        "feature_oss_h3": S("Open source", "Pūmana", "Código abierto", "Open Source", "Открытый исходный код", "オープンソース", "مفتوح المصدر", "ओपन सोर्स"),
        "feature_oss_p": S(
            "Read the code, file issues, and build from source. No license key.",
            "Pānuitia te waehere, tukuna ngā take, hangaia mai i te pūtake. Kāore he kī raihana.",
            "Lee el código, abre incidencias y compila desde el origen. Sin clave de licencia.",
            "Code lesen, Issues öffnen, aus dem Quellcode bauen. Kein Lizenzschlüssel.",
            "Читайте код, открывайте задачи, собирайте из исходников. Без лицензионного ключа.",
            "コードを読み、Issue を出し、ソースからビルドできます。ライセンスキーは不要です。",
            "اقرأ الشفرة، سجّل المشاكل، وابنِ من المصدر. بلا مفتاح ترخيص.",
            "कोड पढ़ें, इश्यू दर्ज करें, स्रोत से बिल्ड करें। कोई लाइसेंस कुंजी नहीं।",
        ),
        "feature_oss_link": S("Licensing", "Raihana", "Licencias", "Lizenzierung", "Лицензии", "ライセンス", "الترخيص", "लाइसेंसिंग"),
        "who_h2": S("Who it is for", "Mō wai", "Para quién es", "Für wen", "Для кого", "誰向けか", "لمن هو", "यह किसके लिए है"),
        "who_p1": S(
            "Sound, video, and show-control operators who want a cuelist on the machine they already have. Typical uses are theatre and live performance, concerts, galleries and installations, and houses of worship. If you think in cues, GO, and standby, Cue2 is aimed at you.",
            "Ngā kaiwhakahaere oro, ataata, whakahaere-whakaaturanga e hiahia ana ki tētahi rārangi tohu i te rorohiko kei a rātou kē. Ko ngā whare tapere, ngā whakaaturanga ora, ngā konohete, ngā taiwhanga, ngā whare karakia. Mēnā ko ngā tohu, te GO, me te tū rite ōu whakaaro, mōu a Cue2.",
            "Operadores de sonido, vídeo y control de espectáculo que quieren una cuelist en la máquina que ya tienen. Usos típicos: teatro y directo, conciertos, galerías e instalaciones, y lugares de culto. Si piensas en cues, GO y standby, Cue2 va dirigido a ti.",
            "Ton-, Video- und Showsteuerungs-Operatoren, die eine Cuelist auf dem Rechner haben wollen, den sie schon haben. Typisch: Theater und Live-Performance, Konzerte, Galerien und Installationen, Gotteshäuser. Wer in Cues, GO und Standby denkt, ist die Zielgruppe.",
            "Звукорежиссёры, видеооператоры и show-control, которым нужен cuelist на уже имеющейся машине. Типичные места: театр и живое выступление, концерты, галереи и инсталляции, храмы. Если вы мыслите cues, GO и standby — Cue2 для вас.",
            "すでに持っているマシンでキューリストを使いたい音響・映像・ショーコントロールのオペレーター向け。劇場やライブ、コンサート、ギャラリーやインスタレーション、礼拝堂など。キュー、GO、スタンバイで考える人のための Cue2 です。",
            "مشغّلو الصوت والفيديو وتحكم العرض الذين يريدون قائمة إشارات على الجهاز لديهم أصلاً. الاستخدامات الشائعة: المسرح والأداء الحي، الحفلات، المعارض والتجهيزات، ودور العبادة. إن كنت تفكّر بإشارات وGO واستعداد، فـ Cue2 موجّه لك.",
            "साउंड, वीडियो और शो-कंट्रोल ऑपरेटर जो अपनी मौजूदा मशीन पर क्यूलिस्ट चाहते हैं। आम उपयोग: थिएटर और लाइव प्रदर्शन, कॉन्सर्ट, गैलरी और इंस्टॉलेशन, पूजा स्थल। अगर आप क्यू, GO और स्टैंडबाय में सोचते हैं, तो Cue2 आपके लिए है।",
        ),
        "who_p2": S(
            f"Cue2 is currently testing multiple translations. With each release we will improve coverage and accuracy. Currently supported languages: {LANG_LIST}.",
            f"Kei te whakamātau a Cue2 i ētahi whakamāoritanga. Ia putanga ka pai ake te kapi me te tika. Ngā reo ināianei: {LANG_LIST}.",
            f"Cue2 está probando varias traducciones. Con cada versión mejoraremos cobertura y precisión. Idiomas actuales: {LANG_LIST}.",
            f"Cue2 testet derzeit mehrere Übersetzungen. Mit jeder Version werden Abdeckung und Genauigkeit besser. Derzeit unterstützt: {LANG_LIST}.",
            f"Cue2 сейчас проверяет несколько переводов. С каждым выпуском покрытие и точность вырастут. Сейчас поддерживаются: {LANG_LIST}.",
            f"Cue2 は複数の翻訳を試験中です。リリースごとにカバー範囲と精度を上げます。現在の対応言語: {LANG_LIST}。",
            f"يختبر Cue2 حالياً ترجمات متعددة. مع كل إصدار نحسّن التغطية والدقة. اللغات المدعومة حالياً: {LANG_LIST}.",
            f"Cue2 कई अनुवादों का परीक्षण कर रहा है। हर रिलीज़ में कवरेज और सटीकता सुधरेगी। वर्तमान भाषाएँ: {LANG_LIST}.",
        ),
        "start_h2": S("Get started", "Tīmata", "Empezar", "Loslegen", "Начать", "はじめに", "ابدأ", "शुरू करें"),
        "start_install": S("Install and first launch", "Tāuta me te whakarewa tuatahi", "Instalación y primer arranque", "Installation und erster Start", "Установка и первый запуск", "インストールと初回起動", "التثبيت والإطلاق الأول", "इंस्टॉल और पहला लॉन्च"),
        "start_concepts": S("Concepts in five minutes", "Ngā ariā i te rima meneti", "Conceptos en cinco minutos", "Konzepte in fünf Minuten", "Концепции за пять минут", "5分でわかる概念", "المفاهيم في خمس دقائق", "पाँच मिनट में अवधारणाएँ"),
        "start_audio": S("Play your first audio file", "Pureia tō kōnae oro tuatahi", "Reproduce tu primer archivo de audio", "Erste Audiodatei abspielen", "Воспроизведите первый аудиофайл", "最初の音声ファイルを再生", "شغّل أول ملف صوت", "अपनी पहली ऑडियो फ़ाइल चलाएँ"),
        "start_osc": S("OSC command reference", "Tohutoro whakahau OSC", "Referencia de comandos OSC", "OSC-Befehlsreferenz", "Справка по командам OSC", "OSC コマンドリファレンス", "مرجع أوامر OSC", "OSC कमांड संदर्भ"),
        "start_manual": S("The full manual lives at", "Kei konei te pukapuka katoa", "El manual completo está en", "Das vollständige Handbuch steht unter", "Полное руководство:", "完全なマニュアルは", "الدليل الكامل على", "पूरी मैनुअल यहाँ है"),
    },
    "about": {
        "title": S("About Cue2", "Mō Cue2", "Acerca de Cue2", "Über Cue2", "О Cue2", "Cue2 について", "حول Cue2", "Cue2 के बारे में"),
        "description": S(
            "Cue2 is MIT-licensed show-control and media playback software by Samuel Moxham. Version 0.1 StripyHat is the first public alpha.",
            "He pūmana raihana MIT a Cue2 nā Samuel Moxham, mō te whakahaere whakaaturanga me te purei pāpāho. Ko 0.1 StripyHat te arpha tūmatanui tuatahi.",
            "Cue2 es software de control de espectáculo y reproducción de medios con licencia MIT, de Samuel Moxham. La versión 0.1 StripyHat es la primera alfa pública.",
            "Cue2 ist MIT-lizenzierte Showsteuerungs- und Medienwiedergabe-Software von Samuel Moxham. Version 0.1 StripyHat ist die erste öffentliche Alpha.",
            "Cue2 — ПО для управления шоу и воспроизведения медиа с лицензией MIT, автор Samuel Moxham. Версия 0.1 StripyHat — первая публичная альфа.",
            "Cue2 は Samuel Moxham による MIT ライセンスのショーコントロール／メディア再生ソフトです。0.1 StripyHat が初の公開アルファです。",
            "Cue2 برنامج تحكم بالعرض وتشغيل وسائط برخصة MIT من Samuel Moxham. الإصدار 0.1 StripyHat هو أول ألفا عامة.",
            "Cue2 Samuel Moxham का MIT-लाइसेंसी शो-कंट्रोल और मीडिया प्लेबैक सॉफ़्टवेयर है। संस्करण 0.1 StripyHat पहला सार्वजनिक अल्फा है।",
        ),
        "h1": S("About Cue2", "Mō Cue2", "Acerca de Cue2", "Über Cue2", "О Cue2", "Cue2 について", "حول Cue2", "Cue2 के बारे में"),
        "intro": S(
            "Cue2 is free and open-source software for cue-based playback of audio, video, text overlays, and show-control messages. It runs on Windows, macOS, and Linux.",
            "He pūmana, he kore utu a Cue2 mō te purei tohu o te oro, ataata, kupu takatika, me ngā karere whakahaere whakaaturanga. Ka rere i Windows, macOS, me Linux.",
            "Cue2 es software libre y de código abierto para reproducción basada en cues de audio, vídeo, texto y mensajes de control de espectáculo. Funciona en Windows, macOS y Linux.",
            "Cue2 ist freie Open-Source-Software für cue-basierte Wiedergabe von Audio, Video, Text-Overlays und Show-Control-Nachrichten. Läuft auf Windows, macOS und Linux.",
            "Cue2 — бесплатное открытое ПО для cue-воспроизведения аудио, видео, текста и сообщений управления шоу. Работает на Windows, macOS и Linux.",
            "Cue2 は音声、映像、テキストオーバーレイ、ショーコントロールメッセージのキュー再生向け無料オープンソースです。Windows、macOS、Linux で動作します。",
            "Cue2 برمجيات حرة ومفتوحة المصدر لتشغيل قائم على الإشارات للصوت والفيديو وطبقات النص ورسائل تحكم العرض. يعمل على Windows وmacOS وLinux.",
            "Cue2 ऑडियो, वीडियो, टेक्स्ट ओवरले और शो-कंट्रोल संदेशों के क्यू-आधारित प्लेबैक के लिए मुफ़्त ओपन-सोर्स सॉफ़्टवेयर है। यह Windows, macOS और Linux पर चलता है।",
        ),
        "project_h2": S("Project", "Kaupapa", "Proyecto", "Projekt", "Проект", "プロジェクト", "المشروع", "परियोजना"),
        "project_p": S(
            "Cue2 is written and maintained by <strong>Samuel Moxham</strong>. The first public alpha is <strong>0.1.0 StripyHat</strong>, released in 2026. The application is under active development. A great deal of work has gone into making it reliable, but you should still treat it with the caution appropriate to alpha software.",
            "Nā <strong>Samuel Moxham</strong> a Cue2 i tuhi, i tiaki. Ko <strong>0.1.0 StripyHat</strong> te arpha tūmatanui tuatahi, i 2026. Kei te whanake tonu. Kua nui te mahi kia pono, engari me āta whakamahi nā te mea he arpha.",
            "Cue2 lo escribe y mantiene <strong>Samuel Moxham</strong>. La primera alfa pública es <strong>0.1.0 StripyHat</strong>, de 2026. Sigue en desarrollo activo. Se ha trabajado mucho la fiabilidad, pero trátalo con la cautela de un software alfa.",
            "Cue2 wird von <strong>Samuel Moxham</strong> geschrieben und gepflegt. Die erste öffentliche Alpha ist <strong>0.1.0 StripyHat</strong> (2026). Die Anwendung wird aktiv weiterentwickelt. Viel Arbeit steckt in der Zuverlässigkeit — trotzdem Alpha, entsprechend vorsichtig nutzen.",
            "Cue2 пишет и сопровождает <strong>Samuel Moxham</strong>. Первая публичная альфа — <strong>0.1.0 StripyHat</strong>, 2026 год. Приложение активно развивается. Надёжности уделено много труда, но это альфа — используйте осторожно.",
            "Cue2 の開発と保守は <strong>Samuel Moxham</strong> です。初の公開アルファは 2026 年の <strong>0.1.0 StripyHat</strong>。現在も活発に開発中です。信頼性には多くの労力を割いていますが、アルファ版として慎重に使ってください。",
            "يكتب Cue2 ويصونه <strong>Samuel Moxham</strong>. أول ألفا عامة هي <strong>0.1.0 StripyHat</strong> الصادرة عام 2026. التطبيق قيد التطوير النشط. بُذل عمل كبير لجعله موثوقاً، لكن تعامل معه بحذر ألفا.",
            "Cue2 को <strong>Samuel Moxham</strong> लिखते और संभालते हैं। पहला सार्वजनिक अल्फा <strong>0.1.0 StripyHat</strong> है, 2026 में जारी। ऐप सक्रिय विकास में है। विश्वसनीयता पर काफ़ी काम हुआ है, फिर भी अल्फा की सावधानी से इस्तेमाल करें।",
        ),
        "license_h2": S("License", "Raihana", "Licencia", "Lizenz", "Лицензия", "ライセンス", "الترخيص", "लाइसेंस"),
        "license_p1": S(
            "Cue2 application code is released under the MIT License. You are free to use, modify, and redistribute it under those terms. The software is provided as-is, without warranty.",
            "Ka tukuna te waehere Cue2 i raro i te Raihana MIT. Wātea koe ki te whakamahi, whakarerekē, tohatoha i runga i aua tikanga. Ka tukuna te pūmana i a ia, kāore he taunaki.",
            "El código de Cue2 se publica bajo la licencia MIT. Puedes usarlo, modificarlo y redistribuirlo bajo esos términos. El software se ofrece tal cual, sin garantía.",
            "Der Cue2-Anwendungscode steht unter der MIT-Lizenz. Nutzung, Änderung und Weitergabe sind unter diesen Bedingungen frei. Die Software wird ohne Gewähr bereitgestellt.",
            "Код приложения Cue2 выпускается под лицензией MIT. Его можно использовать, изменять и распространять на этих условиях. ПО поставляется «как есть», без гарантий.",
            "Cue2 のアプリケーションコードは MIT ライセンスです。その条件の下で利用・改変・再配布できます。ソフトウェアは無保証で提供されます。",
            "يُصدر كود تطبيق Cue2 برخصة MIT. لك حرية الاستخدام والتعديل وإعادة التوزيع وفق تلك البنود. يُقدَّم البرنامج كما هو بلا ضمان.",
            "Cue2 ऐप कोड MIT लाइसेंस के तहत जारी है। उन शर्तों पर उपयोग, बदलाव और पुनर्वितरण मुक्त है। सॉफ़्टवेयर जैसा है वैसा, बिना वारंटी।",
        ),
        "license_p2": S(
            "Bundled FFmpeg libraries are distributed under LGPLv2.1 or later. MIDI uses RtMidi (MIT-style). Details are in the",
            "Ka tohatohatia ngā pūmanawa FFmpeg i raro i te LGPLv2.1, i muri mai rānei. Ko RtMidi (ahu MIT) te MIDI. Kei ngā",
            "Las bibliotecas FFmpeg incluidas se distribuyen bajo LGPLv2.1 o posterior. MIDI usa RtMidi (estilo MIT). Detalles en las",
            "Mitgelieferte FFmpeg-Bibliotheken stehen unter LGPLv2.1 oder neuer. MIDI nutzt RtMidi (MIT-ähnlich). Details in den",
            "Поставляемые библиотеки FFmpeg — под LGPLv2.1 или новее. MIDI использует RtMidi (в духе MIT). Подробности в",
            "同梱の FFmpeg ライブラリは LGPLv2.1 以降です。MIDI は RtMidi（MIT 系）です。詳細は",
            "مكتبات FFmpeg المضمّنة تُوزَّع برخصة LGPLv2.1 أو أحدث. MIDI يستخدم RtMidi (بأسلوب MIT). التفاصيل في",
            "बंडल FFmpeg लाइब्रेरी LGPLv2.1 या बाद के तहत वितरित हैं। MIDI RtMidi (MIT-शैली) इस्तेमाल करता है। विवरण:",
        ),
        "license_link": S("licensing notes", "tuhipoka raihana", "notas de licencia", "Lizenzhinweisen", "заметках о лицензиях", "ライセンス注記", "ملاحظات الترخيص", "लाइसेंस नोट्स"),
        "links_h2": S("Links", "Hononga", "Enlaces", "Links", "Ссылки", "リンク", "روابط", "लिंक"),
        "download_cue2": S("Download Cue2", "Tikiake Cue2", "Descargar Cue2", "Cue2 herunterladen", "Скачать Cue2", "Cue2 をダウンロード", "تنزيل Cue2", "Cue2 डाउनलोड करें"),
        "documentation": S("Documentation", "Tuhinga", "Documentación", "Dokumentation", "Документация", "ドキュメント", "التوثيق", "दस्तावेज़"),
        "app_source": S("Application source", "Pūtake taupānga", "Código de la aplicación", "Anwendungsquellcode", "Исходный код приложения", "アプリケーションのソース", "مصدر التطبيق", "ऐप स्रोत"),
        "issues": S("Issues and feedback", "Ngā take me ngā urupare", "Incidencias y comentarios", "Issues und Feedback", "Задачи и отзывы", "Issue とフィードバック", "المشاكل والملاحظات", "इश्यू और फ़ीडबैक"),
        "website_source": S("Website source", "Pūtake pae tukutuku", "Código del sitio", "Website-Quellcode", "Исходный код сайта", "サイトのソース", "مصدر الموقع", "वेबसाइट स्रोत"),
        "docs_source": S("Documentation source", "Pūtake tuhinga", "Código de la documentación", "Dokumentationsquellcode", "Исходный код документации", "ドキュメントのソース", "مصدر التوثيق", "दस्तावेज़ स्रोत"),
    },
}


def is_leaf(node: object) -> bool:
    return isinstance(node, dict) and "en" in node and set(node).issubset(LOCALES)


def walk(node: dict, prefix: str = ""):
    for key, value in node.items():
        path = f"{prefix}.{key}" if prefix else key
        if is_leaf(value):
            yield path, value
        elif isinstance(value, dict):
            yield from walk(value, path)


def tree_for(lang: str) -> dict:
    def convert(node):
        if is_leaf(node):
            return node.get(lang) or node["en"]
        return {k: convert(v) for k, v in node.items()}

    return convert(STRINGS)
