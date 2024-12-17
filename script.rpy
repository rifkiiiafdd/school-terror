# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg blck = "images/pantai.jpg"
image bg credits = "images/credits.jpg"
image bg cls = "images/cls1.jpg"
image bg kantin = "images/kantin.jpg"
image bg teras = "images/teras.jpg"
image bg ruang_guru = "images/ruang_guru.jpg"
image bg meja = "images/meja.jpg"
image bg makan = "images/makan.jpg"
image bg tv = 'images/tv.jpg'
image nanda biasa = "images/nandabiasa.png"
image nanda sedih = "images/MC_Unsure.png"
image nanda luka = "images/nandaluka.png"
image nanda kaget = "images/nandabiasa.png"
image azka kaget = "images/Azka_Agitated.png"
image nanda makan = "images/nandamakan.png"
image ibu khawatir = "images/Ibu_Wary.png"
image ibu biasa = "images/Ibu_Smilling.png"
image ibu gembira = "images/Ibu_Smilling.png"
image ayah biasa = "images/Ayah_Smiling.png"
image ayah khawatir = "images/Ayah_Wary.png"
image classmates = "images/nandamirror.png"
image bg kamar = "images/rumah1.jpg"
image bg rumah = "images/dirumah.jpg"
image azka biasa = "images/Azka_Neutral.png"
image azka sedih = "images/Azka_Neutral.png"
image guru biasa = "images/guru.png"
image bg rumah_azka = "images/rumahazka.jpg"
image ayah_azka biasa = "images/ayahazka.png"
image ayah_azka tajam = "images/ayahazka.png"
image nanda diam = "images/nandabiasa.png"
image azka ragu = "images/Azka_Neutral.png"
image nanda berani = "images/nandabiasa.png"
image meja = "images/broketable.png"
image tv = "images/tv.png"
image azka khawatir = "images/Azka_Neutral.png"
image azka ragu = "images/Azka_Neutral.png"
image azka serius = "images/Azka_Neutral.png"
image azka tajam = "images/Azka_Neutral.png"
image ayah_azka menghela_napas = "images/ayahazka.png"
image ayah_azka tersenyum = "images/ayahazka.png"
image azka memohon = "images/Azka_Neutral.png"
image nanda tenang = "images/nandabiasa.png"
image nanda tersenyum = "images/nandagembira.png"
image bg aula_desa = "images/aula_desa.jpg"
image bg sekolah_hari = "images/sekolah_hari.jpg"
image bg sekolah= "images/sekolah.jpg"
image bg laut_senja = "images/laut_senja.jpg"
image bg rumah_hancur = "images/rumah hancur.jpg"
image bg ending1 = "images/ending 1.jpg"
image bg ending2 = "images/ending 2.jpg"
image bg ending3 = "images/ending 3.jpg"


# Deklarasikan karakter yang digunakan di game.
define nanda = Character("Nanda", color="#ffddf2")
define azka = Character("Azka",color = "#ffffff")
define teman = Character("Classmates", color = "#ffffff")
define ibu = Character("Ibu", color = "#ffffff")
define guru = Character("Guru", color = "#ffe2d4")
define ayah = Character("Ayah", color = "#ffffdf")
define ayah_azka = Character("Ayah azka", color = "#d1ffdc")
define classmates = Character("Classmates", color = "#d6d5d5")

# Game dimulai disini.
label start:
    scene bg blck  
    play music "scene 1 pantai.ogg" fadein 1 fadeout 3
    play sound "scene 1 insturment.ogg" fadein 1 fadeout 1     


    "Di suatu desa kecil di tepi pantai,..\ "
    "hidup seorang anak yang setiap harinya membantu kedua orang tuanya.."
    "ayah seorang nelayan, dan ibu seorang pedagang ikan."
    "Bagi mereka, laut adalah kehidupan."
    stop music
    jump classroom1

label classroom1 :
    stop music
    stop sound
    scene bg sekolah with fade
    play music "scene 2 & 5 (kelas kantin).ogg" fadein 0.5 fadeout 1 volume 0.1
    show nanda biasa at left
    with moveinleft
    pause
    classmates "Bukankah dia anak nelayan itu? Orang-orang seperti mereka bau amis"
    
    
    menu:
        "Hai,.. Selamat pagi":
            jump menyapa
        
        "...":
            jump tidak_menyapa 

    label menyapa:
        hide nanda biasa
        show nanda tersenyum at left
        with dissolve
        nanda "Hai,.. Selamat pagi"
        classmates "Eh, kamu yang anak nelayan ya?? Kamu bau amis habisnya!"
        jump menyapa_done

    label tidak_menyapa:
        hide nanda biasa
        show nanda biasa at left
        nanda "..."
        hide nanda biasa
        classmates "“eh anak nelayannya dateng, tuh”"
        jump menyapa_done

    label menyapa_done:
        play sound "scene 2 abis dikatain bau ikan.ogg" fadein 1 fadeout 6
        show nanda biasa at left
        with dissolve
        nanda "Hah,..."
        nanda "Apa yang salah dengan aku?"
        
        pause

label kantin:
    scene bg kantin with fade
    stop sound
    show nanda makan at left 
    with moveinbottom
    pause
    scene makan with dissolve
    pause
    scene bg kantin 
    with dissolve
    show nanda makan at left 
    nanda "Ikan bandeng masakan ibu tidak pernah mengecewakan"
    with dissolve

    hide nanda makan
    show classmates at center
    with moveinright
    play sound "scene 3 (berantem).ogg" fadein 1 fadeout 7
    teman "Lah, kenapa kamu makan ikan? Itu menjijikkan, mana mungkin kamu makan makhluk hidup dari laut."
    hide classmates
    hide nanda makan

    menu:
        "Kenapa memangnya? ":
            show nanda berani at left
            nanda "Kenapa memangnya?"
            hide nanda berani
            jump nantang

        "Ikan itu lezat dan sehat tau!":
            show nanda biasa at left
            nanda "Ikan itu lezat dan sehat tau!"
            hide nanda biasa
            jump ikanlezat
    
    label nantang:
        show classmates at center
        teman "Lah? Nantangin?"
        hide classmates 
        $ nantang = True
        "Lalu mereka pun berkelahi hebat"
        jump sepulang_sekolah
    
    label ikanlezat:
        $ nantang = False
        show classmates at center
        teman "iihhhh, pantesan kamu bau amis"
        nanda "..."
        jump sepulang_sekolah


label sepulang_sekolah:
    scene bg rumah with fade
    stop music
    stop sound
    play music "scene 4 (rumah nanda).ogg" fadein 1 fadeout 1
    pause
    if nantang:
        show ibu khawatir at right
        with moveinright
        ibu "Nanda, kamu pulang sih, tapi kenapa kamu kelihatan sedih?"
        hide ibu khawatir
        
        menu:
            "...":
                show nanda luka at left

                nanda "..."
                hide ibu khawatir
                hide nanda luka
                scene bg tv with fade
                play sound "scene 4 (baca berita).ogg" fadein 1 fadeout 1
                "TV dalam keadaan menyala, sedang menayangkan acara berita"
                "reporter" '"Sebuah organisasi yang bermotif dari kebencian akan makanan laut, Perkumpulan Warga Anti Seafood, PWAS, makin meresahkan warga setempat"'
                "reporter" '"kabarnya, pergerakan radikal organisasi ini mulai meluas pada tiap kalangan"'
                scene bg rumah with dissolve
                # show i bu khawatir at right 
                show nanda luka at left
                stop sound
                nanda "{i}Jadi ini alasan aku dirundung{/i}"
                $ tahu_alasan = True
                hide nanda luka
                with moveoutleft
                jump kamar_nanda

            
            "Tidak apa-apa bu":
                $ tahu_alasan = False
                show nanda luka at left
                nanda "Tidak apa-apa bu"
                hide nanda luka
                with moveoutleft
                
                jump kamar_nanda

    else :
        $ tahu_alasan = False
        show ibu gembira at right
        ibu "Bagaimana hari pertama sekolahmu, nak"
        hide ibu gembira
        show nanda sedih at left 
        nanda "Tidak apa-apa, bu"
        
        hide nanda sedih
        with moveoutleft
        jump kamar_nanda
    
    label kamar_nanda:
        "Nanda masuk ke kamar"
        scene bg kamar with fade
        if nantang :
            show nanda luka at left
            with moveinleft
            nanda "(Menangis)"
            nanda "{i}Sepertinya aku harus lebih ramah kepada orang lain{i}"
            hide nanda luka
    
        else :
            show nanda sedih at left
            with moveinleft
            nanda "{i}Andaikan saja aku bisa tahu kenapa mereka memperlakukanku seperti itu..{/i}"
            hide nanda sedih 

label eskalasi:
    scene bg cls with fade
    stop music
    
    show nanda biasa at left 
    with moveinleft
    nanda "apa yang terjadi dengan meja ku?"    
    scene bg meja with fade
    play music "meja.ogg"
    pause
    scene bg cls with fade
    show nanda sedih at left 
    with dissolve

    pause
    if tahu_alasan:
        nanda "(Menenangkan diri, Melihat sekitar)"
        hide nanda sedih
        with moveoutleft
        nanda "(Keluar dari kelas)"

    else : 
        nanda "Kenapa mereka membenci kami hanya karena kami dari keluarga nelayan?"
        
        "..."
        hide nanda sedih
        with moveoutleft
        nanda "(Keluar dari kelas)"

label ruangan_guru :
    stop music
    play music "scene 5 dan 6.ogg" fadein 0.1 fadeout  0.1
    scene bg ruang_guru with fade
    pause
    show nanda sedih at left
    nanda "Selamat pagi bu, maaf mengganggu"
    hide nanda sedih
    show guru biasa at right
    guru "Ada apa, Nanda? Kamu terlihat sedih."
    hide guru biasa
    show nanda biasa at left
    nanda "Bu, aku selalu dibully oleh teman-teman di sekolah."
    hide nanda biasa
    show guru biasa at right 
    guru "Oh tidak, siapa yang melakukan itu?"
    hide guru biasa
    show nanda sedih at left
    nanda "Aku tidak tahu nama mereka, tapi mereka selalu mengejek dan menghinaku."
    hide nanda sedih
    show guru biasa at right
    guru "Itu tidak bisa dibiarkan. Ibu akan mencari tahu siapa mereka. Tapi kamu juga harus berani, Nanda."
    hide guru biasa
    show nanda sedih at left
    nanda "Berani bagaimana, Bu?"
    hide nanda sedih
    show guru biasa at right
    guru "Berani untuk tidak membiarkan mereka merendahkanmu. Tunjukkan bahwa kamu kuat dan tidak takut."
    hide guru biasa
    show nanda sedih at left
    nanda "Tapi, Bu, itu sulit..."
    hide nanda sedih
    show guru biasa at right
    guru "Ibu tahu, tapi kamu tidak sendiri. Ibu dan teman-teman yang baik akan selalu mendukungmu."

    if tahu_alasan:
        hide guru biasa 
        show nanda sedih at left
        nanda "Terima kasih, Bu. Aku akan mencoba."
        nanda "pasti tidak semua orang membenci keluarga nelayan sepertiku"
        nanda "Aku harus mencari teman seperti itu"
        hide nanda sedih
    else :
        hide guru biasa
        show nanda sedih at left
        nanda "Mereka.."
        nanda "Mereka semua tanpa alasan membully ku karena aku anak nelayan"
        nanda "Aku benci itu"
        hide nanda sedih
        show guru biasa at right
        guru "Nanda, jangan berkata seperti itu. Semua pekerjaan itu mulia"
        guru "jangan khawatir, ibu akan memarahi mereka"
        hide guru biasa
        show nanda sedih at left
        nanda "{i}Ibu tidak mengerti{/i}"
        nanda "{i}Ku rasa tidak ada yang bisa kupercaya{/i}"
        hide nanda sedih
    jump di_teras_sekolah

label di_teras_sekolah:
    stop music
    play music "scene 7.ogg" fadein 1 fadeout 1
    scene bg teras with fade
    # pause
    # show nanda biasa at left 
    pause
    show azka biasa at right
    pause
    azka "Hai, apakah kamu tidak apa-apa?"
    $ azka_berteman = True
    hide azka biasa
    show nanda biasa at left
    nanda "..."
    hide nanda biasa
    show azka biasa at right
    azka "Aku sering melihat apa yang mereka lakukan padamu. Tenang saja, aku tidak sama seperti mereka, ayahku juga sering memancing."
    hide azka biasa
    if tahu_alasan:
        show nanda biasa at left
        nanda "Aku tidak apa-apa, kok, terima kasih ya."
        hide nanda biasa
        show azka biasa at right
        azka "aku tahu kok, berita tentang organisasi itu"
        hide azka biasa
        show nanda kaget at left
        nanda "ehh, benarkah?"
        hide nanda kaget
        show azka biasa at right
        azka "iya, aku sebenarnya juga melihat kalau organisasi itu bisa saja ikut andil dalam perlakuan buruk yang teman-teman sekelasmu lakukan di sini"
        hide azka biasa
        show nanda biasa at left
        nanda "aku juga menduga seperti itu.."
        "(Nanda mendapat teman pertamanya)"
        jump azka_ngobrol
    
    else :
        menu :
            "ramah":
                show nanda biasa at left
                nanda "aku tidak apa-apa, kok, terima kasih"
                nanda  "aku sering merasa sendirian di sini, nama kamu siapa?"
                hide nanda biasa
                show azka biasa at right
                azka "Namaku azka, senang berkenalan denganmu!"
                azka "aku tahu kok, berita tentang organisasi itu"
                hide azka biasa
                show nanda kaget at left
                nanda "oh ya.."
                hide nanda kaget
                show azka biasa at right
                azka " iya, aku sebenarnya juga melihat kalau organisasi itu bisa saja ikut andil dalam perlakuan buruk yang teman-teman sekelasmu lakukan di sin"
                hide azka biasa
                show nanda biasa at left
                nanda "begitu ya.."
                nanda "aku juga menduga seperti itu"
                hide nanda biasa
                jump azka_ngobrol
        
            "dingin" :
                show nanda biasa at left
                nanda "Oh iya, aku tidak apa-apa, senang bertemu kamu, tapi aku ada urusan, aku pergi dulu ya"
                hide nanda biasa
                show azka biasa at right
                azka "Oh, baik, sampai bertemu, ya!"
                hide azka biasa
                "(Dan begitulah Nanda kehilangan satu-satunya kesempatan mendapatkan teman baru)"
                $ azka_ikut = False
                $ azka_berteman = False
                jump rumah2
           
label azka_ngobrol :
    show azka biasa at right
    azka " lengkapnya, mau ngobrol tentang itu gak sehabis sekolah?"
    hide azka biasa
    menu :
        "Terima Ajakan":
            show nanda biasa at left
            nanda "Boleh"
            nanda "aku juga ingin tahu lebih banyak tentang organisasi itu"
            hide nanda biasa
            $ azka_ikut = True
            jump rumah2
        
        "Tolak Ajakan":
            show nanda biasa at left
            nanda "Maaf, aku ada urusan"
            hide nanda biasa
            $ azka_ikut = False
            jump rumah2

label rumah2:
    hide azka biasa
    hide nanda biasa
    scene bg rumah with fade
    pause
    if azka_ikut :
        show nanda biasa at left
        with moveinleft
        nanda "Jadi, kamu mau ngobrolin apa?"
        hide nanda biasa
        show azka biasa at right
        with moveinright
        azka "Aku mungkin tau sedikit hal tentang PWAS...."
        azka "..."
        hide azka biasa
        show nanda kaget at left
        show azka kaget at right 
        stop music
        stop sound
        play music "scene 8 (ada pwas).ogg" fadein 1 fadeout 1
        play sound "door.ogg" fadein 1 fadeout 1 
        "DOR DOR DOR \n (suara pintu diketuk)"
        "(Sebelum Azka dapat bercerita, tiba-tiba pintu depan rumah Nanda didobrak paksa)"
        "..." "Keluar kau nelayan bau amis"
        
        azka "Sial, mereka datang kesini"
        azka "ayo lari"
        hide nanda kaget
        with moveoutleft
        hide azka kaget
        with moveoutright
        "(Nanda dan Azka berhasil menyelinap kabur melalui jendela)"
        "Mereka tak berhenti berlari ketakutan sampai tiba di suatu gubuk"
    else :
        show nanda biasa at left
        nanda "Hari ini sungguh menyebalkan"
        pause 
        stop music
        hide nanda biasa
        show nanda kaget at left
        stop music
        play music "scene 8 (ada pwas).ogg" fadein 1 fadeout 1
        play sound "door.ogg" fadein 1 fadeout 1 
        "DOR DOR DOR *\ (suara pintu diketuk)"
        "..." "Keluar kau nelayan bau amis"
        nanda "hah, apa yang terjadi?"
        nanda "aku tidak bisa menghadapi mereka"
        hide nanda kaget
        "(Nanda berhasil menyelinap kabur melalui jendela)"

label rumah_setelah_penyerangan:
    scene bg rumah with fade
    stop sound
    if azka_ikut:
        show nanda sedih at left
        
        nanda "Ibu! Ayah! Apakah kalian tidak apa-apa? Mereka melakukan apa??"
        hide nanda sedih
        show ibu khawatir at center
        ibu "Kami tidak apa-apa nak, untung saja mereka tidak mencarimu juga."
        show ayah biasa at left
        ayah "Iya nak, untung saja mereka tidak melakukan apa-apa ke kamu. Temanmu tidak apa-apa juga kan?"
        hide ayah biasa
        hide ibu khawatir

        show azka biasa at right
        azka "Iya, Om, saya tidak apa-apa... Tapi... ada sesuatu yang ingin saya bicarakan."
        hide azka biasa
        show azka sedih at right
        azka "{i}(Bagaimana cara saya menyampaikan hal ini pada mereka...){/i}"
        hide azka sedih
        show nanda biasa at left
        nanda "Azka? Apa yang ingin kamu bicarakan?"
        hide nanda biasa
        show azka sedih at right
        azka "Sebenarnya... Ketua PWAS adalah ayah kandung saya. Namun, saya tidak setuju dengan apa yang ayah saya lakukan. Itulah alasan kenapa saya ingin berteman denganmu, untuk menyelamatkan keluargamu dari ancamannya."
        hide azka sedih

        show nanda biasa at left
        nanda "Azka, aku tidak tahu harus berkata apa..."
        hide nanda biasa
        show azka sedih at right
        azka "Aku minta maaf tidak memberitahumu lebih awal" 
        azka "dan aku juga meminta maaf ayahku tega membuat keluargamu sengsara. Aku janji aku akan mencari cara untuk memperbaiki ini."
        show ibu biasa at center
        ibu "Azka... pesanku hanya satu, jaga keselamatanmu, ya?"
        hide ibu biasa
        show ayah khawatir at center
        ayah "Iya nak, aku tahu itu ayahmu, namun kau harus tetap berhati-hati."
        azka "Baik tante, om."
        hide ayah khawatir
        hide azka sedih

        "Azka dan Nanda pergi ke rumah Azka untuk menemui ayah Azka."
        jump rumah_azka
    else:
        show nanda sedih at left
        nanda "Ibu! Ayah! Apakah kalian tidak apa-apa? Mereka melakukan apa??"
        hide nanda sedih
        show ibu khawatir at center
        ibu "Kami tidak apa-apa nak, untung saja mereka tidak mencarimu juga."
        show ayah biasa at left
        ayah "Iya nak, untung saja mereka tidak melakukan apa-apa ke kamu."
        nanda "Bu, Yah, aku rasa sudah waktunya kita pindah dari sini. Lingkungannya sudah tidak aman, aku khawatir mereka akan kembali dan melakukan hal yang lebih buruk dari tadi. Aku tidak mau Ibu dan Ayah kenapa-napa."
        ayah "Tidak usah mengkhawatirkan Ayah dan Ibu, kami bisa melapor ke pihak yang berwenang. Tapi bagaimana dengan kamu? Bukankah kamu sudah bahagia di sini?"
        nanda "..."
        jump rencana_pindah

label rencana_pindah:
    scene bg rumah_hancur with fade
    pause
    menu:
        "Sebenarnya, aku masih ingin tinggal di sini.":
            show nanda biasa at left
            
            nanda "Sebenarnya, aku masih ingin tinggal di sini, Yah. Aku akan mencoba untuk menjauh dari orang-orang yang menindasku di kelas."
            hide nanda biasa
            show ibu khawatir at right
            ibu "Kalau itu keputusanmu, Nak, kami akan mendukungmu. Tapi ingat, tetaplah berhati-hati, ya?"
            hide ibu khawatir
            "Nanda dan keluarganya memutuskan untuk tetap tinggal di desa itu. Nanda memilih untuk tetap menjaga jarak, dengan fokus pada keluarganya dan persahabatan yang ia bangun di luar lingkungan kelas."
            jump ed2

        "Tidak yah, kebahagiaanku bukan apa-apa kalau dibandingkan dengan keselamatan kalian.":
            show nanda biasa at left
            
            nanda "Tidak yah, kebahagiaanku bukan apa-apa kalau dibandingkan dengan keselamatan kalian. Aku tidak ingin hal buruk itu terjadi lagi. Aku ingin pindah dari sini."
            show ayah biasa at right
            ayah "Baiklah, Nak. Kalau itu yang terbaik untuk kita semua, Ayah dan Ibu akan bersiap-siap."
            hide ayah biasa
            hide nanda biasa
            "Nanda dan keluarganya terpaksa pindah ke daerah lain karena Nanda gagal menghentikan teror yang menimpanya dan keluarganya."
            jump ed3

label rumah_azka:
    scene bg rumah_azka with fade
    pause
    # Dialog awal kedatangan di rumah Azka
    show ayah_azka biasa at right
    ayah_azka "Oh, halo, Nak! Apa kabar? Ada sesuatu yang ayah ingin bicarakan—eh, siapa ini? Kamu membawa teman? Halo, Nak, sini, masuk saja."
    hide ayah_azka biasa
    show azka biasa at left
    azka "Em, ayah, kenalkan ini Nanda, teman baruku."
    show nanda diam at center
    nanda "(Diam, merasa tidak nyaman dengan situasi ini.)"
    hide nanda diam
    hide azka biasa
    show azka ragu at left
    azka "Yah... Nanda itu, dia anak seorang nelayan."
    hide aska ragu
    # Reaksi Ayah Azka
    show ayah_azka tajam at right
    ayah_azka "(Tatapannya tajam) Nelayan? Maksudmu keluarganya cari nafkah dari laut? Dari seafood?"
    hide ayah_azka tajam
    show azka khawatir at left
    azka "Iya, Yah."
    hide azka khawatir
    show ayah_azka tajam at right
    ayah_azka "Kamu nggak tahu, Nak. Dulu waktu Ayah kecil, Ayah tinggal di pinggir pantai. Setiap hari rumah kita bau amis karena pasar ikan ada di dekat situ. Orang-orang di sana nggak pernah peduli sama kebersihan."
    ayah_azka "Setiap kali Ayah jalan ke sekolah, Ayah selalu dihina sama anak-anak nelayan karena keluarga kita nggak kerja di laut. Ayah dibully cuma karena nggak makan ikan. Itu kenangan yang nggak bisa Ayah lupain."
    hide ayah_azka tajam


    show azka serius at left
    azka "Yah, aku ngerti kalau pengalaman Ayah dulu nggak enak. Tapi Nanda dan keluarganya nggak ada hubungannya sama itu. Mereka nggak salah cuma karena mereka kerja di laut. Mereka juga manusia, Yah."
    hide azka serius
    show ayah_azka tajam at right
    ayah_azka "Tapi mereka tetap bagian dari kelompok itu, Azka."
    hide ayah_azka tajam

    show nanda berani at center
    nanda "Om, keluarga saya memang nelayan, itu benar. Tapi kami nggak cuma kerja untuk cari uang, kami juga jaga laut yang kami andalkan untuk hidup."
    nanda "Ayah saya ikut gerakan pembersihan pantai, kami nggak pernah ambil ikan secara berlebihan, dan kami ngajarin anak-anak di desa untuk nggak buang sampah ke laut."
    hide nanda berani
    show ayah_azka tajam at right
    ayah_azka "Kamu tahu, Nanda? Dulu hidup saya pernah sulit karena orang-orang nelayan di kampung saya. Tapi mungkin... saya sudah terlalu lama menyimpan kebencian itu."
    hide ayah_azka tajam

    show nanda tenang at center
    nanda "Saya nggak tahu apa yang Om alami dulu, tapi satu hal yang saya tahu, kebencian itu nggak akan membuat Om lebih bahagia. Kita cuma ingin hidup, Om, sama seperti semua orang."
    hide nanda tenang
    show azka memohon at left
    azka "Ayah, aku mohon. Kita bisa belajar lihat orang dari hatinya, bukan dari pekerjaannya."
    hide azka memohon
    show ayah_azka menghela_napas at right
    ayah_azka "(Menghela napas panjang) Kamu benar, Azka... Nanda. Mungkin saya salah selama ini."
    hide ayah_azka menghela_napas

    show nanda tersenyum at center
    nanda "(Tersenyum, lega) Terima kasih, Om. Saya harap ke depannya, Om bisa melihat kami sebagai teman, bukan musuh."
    hide nanda tersenyum
    hide ayah_azka menghela_napas
    hide azka memohon
    hide nanda tersenyum
    show ayah_azka tersenyum at right
    ayah_azka "(Tersenyum)Terima kasih, Nanda. Saya harus keluar sebentar untuk mengurus sesuatu."
    hide ayah_azka tersenyum
    show azka biasa at left
    azka "Ayah, mau ke mana?"   
    hide azka biasa
    show ayah_azka biasa at right
    ayah_azka "Ada sesuatu yang perlu saya lakukan. Kamu akan mengerti nanti."
    hide ayah_azka biasa
    pause

    scene bg aula_desa with fade
    "Ayah Azka kemudian mengurus pembubaran kelompok PWAS, yang selama ini mengganggu ketenangan para nelayan di desa."


    scene bg sekolah_hari with fade
    "Di sekolah, Nanda berhasil mengubah persepsi teman-temannya tentang keluarga nelayan. Perlahan, kelas menjadi lebih toleran terhadap mereka yang sebelumnya dianggap berbeda."

    scene bg laut_senja with fade
    "Keluarga Nanda akhirnya terbebas dari ancaman dan teror. Mereka dapat hidup dengan tenang, menjaga laut dengan penuh cinta seperti yang selalu mereka lakukan."
    jump ed1

label ed1:
    scene bg ending1 with fade
    
    menu :
        "Ya" :
            jump start

        
        "Tidak" :
            jump credit

label ed3:
    scene bg ending3 with fade
    
    menu :
        "Ya" :
            jump start

        
        "Tidak" :
            jump credit
label ed2:
    scene bg ending2 with fade
    
    menu :
        "Ya" :
            jump start

        
        "Tidak" :
            jump credit

label credit:
    scene bg credits with fade 
    pause
    return


    
