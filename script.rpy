# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg blck = "images/pantai.jpg"
image bg cls = "images/cls1.jpg"
image bg kantin = "images/kantin.jpg"
image bg teras = "images/teras.jpg"
image bg ruang_guru = "images/ruang_guru.jpg"
image nanda biasa = "images/nandabiasa.png"
image nanda sedih = "images/MC_Unsure.png"
image nanda luka = "images/nandaluka.png"
image nanda kaget = "images/nandabiasa.png"
image azka kaget = "images/azka.png"
image nanda makan = "images/nandamakan.png"
image ibu khawatir = "images/ibubiasa.png"
image ibu biasa = "images/ibubiasa.png"
image ibu gembira = "images/ibubiasa.png"
image ayah biasa = "images/ayahnanda.png"
image classmates = "images/nandamirror.png"
image bg rumah = "images/rumah1.jpg"
image azka biasa = "images/azka.png"
image azka sedih = "images/azka.png"
image guru biasa = "images/guru.png"
image bg rumah_azka = "images/rumahazka.jpg"
image ayah_azka biasa = "images/ayahazka.png"
image ayah_azka tajam = "images/ayahazka.png"
image nanda diam = "images/nandabiasa.png"
image azka ragu = "images/azka.png"
image nanda berani = "images/nandabiasa.png"
image meja = "images/broketable.png"
image tv = "images/tv.png"
image azka khawatir = "images/azka.png"
image azka ragu = "images/azka.png"
image azka serius = "images/azka.png"
image azka tajam = "images/azka.png"
image ayah_azka menghela_napas = "images/ayahazka.png"
image ayah_azka tersenyum = "images/ayahazka.png"
image azka memohon = "images/azka.png"
image nanda tenang = "images/nandabiasa.png"
image nanda tersenyum = "images/nandagembira.png"
image bg aula_desa = "images/aula_desa.jpg"
image bg sekolah_hari = "images/sekolah_hari.jpg"
image bg sekolah= "images/sekolah.jpg"
image bg laut_senja = "images/laut_senja.jpg"


# Deklarasikan karakter yang digunakan di game.
define nanda = Character("Nanda", color="#eea8ea")
define azka = Character("Azka",color = "#62a0d2")
define teman = Character("Classmates", color = "#747171")
define ibu = Character("Ibu", color = "#0a0807")
define guru = Character("Guru", color = "#0a0807")
define ayah = Character("Ayah", color = "#0a0807")
define ayah_azka = Character("Ayah azka", color = "#0a0807")

# Game dimulai disini.
label start:
    scene bg blck   
    play music "orison.ogg" fadein 1 fadeout 1
    "Di suatu desa kecil di tepi pantai,..\ "
    "hidup seorang anak yang setiap harinya membantu kedua orang tuanya.."
    "ayah seorang nelayan, dan ibu seorang pedagang ikan."
    "Bagi mereka, laut adalah kehidupan."
    # stop music
    jump classroom1

label classroom1 :
    scene bg sekolah
    # play music "clas_music.ogg" fadeout 1 fadein 1
    
    pause
    "Classmates" "Bukankah dia anak nelayan itu? Orang-orang seperti mereka bau amis"
    pause
    show nanda biasa at left
    
    menu:
        "Hai,.. Selamat pagi":
            jump menyapa
        
        "...":
            jump tidak_menyapa 

    label menyapa:
        show nanda biasa at left
        nanda "Hai,.. Selamat pagi"
        jump menyapa_done

    label tidak_menyapa:
        show nanda biasa at left
        nanda "..."
        jump menyapa_done

    label menyapa_done:
        "Classmates" "..."

label kantin:
    scene bg kantin
    pause
    show nanda makan at left 
    nanda "Ikan bandeng masakan ibu tidak pernah mengecewakan"
    hide nanda makan
    show classmates at center
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
        teman "iihhhh, pantesan kamu bau amis"
        nanda "..."
        jump sepulang_sekolah

label sepulang_sekolah:
    scene bg rumah
    pause
    if nantang:
        show ibu khawatir at right
        ibu "Nanda, kamu pulang sih, tapi kenapa kamu kelihatan sedih?"
        hide ibu khawatir
        
        menu:
            "...":
                show nanda luka at left
                nanda "..."
                hide ibu khawatir
                hide nanda luka
                show tv at right 
                "TV dalam keadaan menyala, sedang menayangkan acara berita"
                "reporter" '"Sebuah organisasi yang bermotif dari kebencian akan makanan laut, Perkumpulan Warga Anti Seafood, PWAS, makin meresahkan warga setempat"'
                "reporter" '"kabarnya, pergerakan radikal organisasi ini mulai meluas pada tiap kalangan"'
                hide tv
                # show ibu khawatir at right 
                show nanda luka at left
                nanda "{i}Jadi ini alasan aku dirundung{/i}"
                $ tahu_alasan = True
                jump kamar_nanda

            
            "Tidak apa-apa bu":
                $ tahu_alasan = False
                show nanda luka at left
                nanda "Tidak apa-apa bu"
                hide ibu khawatir
                hide nanda luka
                
                jump kamar_nanda

    else :
        $ tahu_alasan = False
        show ibu gembira at right
        ibu "Bagaimana hari pertama sekolahmu, nak"
        hide ibu gembira
        show nanda sedih at left
        nanda "Tidak apa-apa, bu"
        hide nanda sedih
        jump kamar_nanda
    
    label kamar_nanda:
        scene bg rumah
        "Nanda masuk ke kamar"
        if nantang :
            show nanda luka at left
            nanda "(Menangis)"
            nanda "{i}Sepertinya aku harus lebih ramah kepada orang lain{i}"
            hide nanda luka
    
        else :
            show nanda sedih at left
            nanda "{i}Andaikan saja aku bisa tahu kenapa mereka memperlakukanku seperti itu..{/i}"

label eskalasi:
    scene bg cls
    pause
    show nanda biasa at left 
    pause
    show meja at center
    pause
    if tahu_alasan:
        nanda "(Menenangkan diri, Melihat sekitar)"
        hide nanda biasa
        hide meja
        nanda "(Keluar dari kelas)"

    else : 
        nanda "Kenapa mereka membenci kami hanya karena kami dari keluarga nelayan?"
        
        "..."

label ruangan_guru :
    scene bg ruang_guru
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
    scene bg teras
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
    scene bg rumah
    pause
    if azka_ikut :
        show nanda biasa at left
        nanda "Jadi, kamu mau ngobrolin apa?"
        hide nanda biasa
        show azka biasa at right
        azka "Aku mungkin tau sedikit hal tentang PWAS...."
        azka "..."
        hide azka biasa
        show nanda kaget at left
        show azka kaget at right 
        "DOR DOR DOR \n  (suara pintu diketuk)"
        "(Sebelum Azka dapat bercerita, tiba2 pintu depan rumah Nanda didobrak paksa)"
        "..." "Keluar kau nelayan bau amis"
        hide nanda kaget
        azka "Sial, mereka datang kesini"
        azka "ayo lari"
        hide azka kaget
        "(Nanda dan Azka berhasil menyelinap kabur melalui jendela)"
        "Mereka tak berhenti berlari ketakutan sampai tiba di suatu gubuk???? (cttn programmer : mau ngapain heyy, sus banget)"
    
    else :
        show nanda biasa at left
        nanda "Hari ini sungguh menyebalkan"
        nanda "..."
        pause 
        hide nanda biasa
        show nanda kaget at left 
        "DOR DOR DOR *\ (suara pintu diketuk)"
        "..." "Keluar kau nelayan bau amis"
        nanda "hah, apa yang terjadi?"
        nanda "aku tidak bisa menghadapi mereka"
        hide nanda kaget
        "(Nanda berhasil menyelinap kabur melalui jendela)"

label rumah_setelah_penyerangan:
    scene bg rumah with fade
    if azka_ikut:
        show nanda sedih at left
        show azka biasa at right
        nanda "Ibu! Ayah! Apakah kalian tidak apa-apa? Mereka melakukan apa??"
        hide nanda sedih
        show ibu khawatir at center
        ibu "Kami tidak apa-apa nak, untung saja mereka tidak mencarimu juga."
        show ayah biasa at left
        ayah "Iya nak, untung saja mereka tidak melakukan apa-apa ke kamu. Temanmu tidak apa-apa juga kan?"
        show azka biasa at right
        azka "Iya, Om, saya tidak apa-apa... Tapi... ada sesuatu yang ingin saya bicarakan."
        show azka sedih at right
        azka "{i}(Bagaimana cara saya menyampaikan hal ini pada mereka...){/i}"
        nanda "Azka? Apa yang ingin kamu bicarakan?"
        azka "Sebenarnya... Ketua PWAS adalah ayah kandung saya. Namun, saya tidak setuju dengan apa yang ayah saya lakukan. Itulah alasan kenapa saya ingin berteman denganmu, untuk menyelamatkan keluargamu dari ancamannya."
        nanda "Azka, aku tidak tahu harus berkata apa..."
        azka "Aku minta maaf tidak memberitahumu lebih awal" 
        azka "dan aku juga meminta maaf ayahku tega membuat keluargamu sengsara. Aku janji aku akan mencari cara untuk memperbaiki ini."
        show ibu biasa at center
        ibu "Azka... pesanku hanya satu, jaga keselamatanmu, ya?"
        hide ibu biasa
        show ayah biasa at center
        ayah "Iya nak, aku tahu itu ayahmu, namun kau harus tetap berhati-hati."
        azka "Baik tante, om."
        hide ayah biasa
        show azka biasa at right
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
    scene bg teras with fade
    pause
    menu:
        "Sebenarnya, aku masih ingin tinggal di sini.":
            show nanda biasa at left
            show ibu khawatir at right
            nanda "Sebenarnya, aku masih ingin tinggal di sini, Yah. Aku akan mencoba untuk menjauh dari orang-orang yang menindasku di kelas."
            ibu "Kalau itu keputusanmu, Nak, kami akan mendukungmu. Tapi ingat, tetaplah berhati-hati, ya?"
            hide ibu khawatir
            hide nanda biasa
            "Nanda dan keluarganya memutuskan untuk tetap tinggal di desa itu. Nanda memilih untuk tetap menjaga jarak, dengan fokus pada keluarganya dan persahabatan yang ia bangun di luar lingkungan kelas."
            return

        "Tidak yah, kebahagiaanku bukan apa-apa kalau dibandingkan dengan keselamatan kalian.":
            show nanda biasa at left
            show ayah biasa at right
            nanda "Tidak yah, kebahagiaanku bukan apa-apa kalau dibandingkan dengan keselamatan kalian. Aku tidak ingin hal buruk itu terjadi lagi. Aku ingin pindah dari sini."
            ayah "Baiklah, Nak. Kalau itu yang terbaik untuk kita semua, Ayah dan Ibu akan bersiap-siap."
            hide ayah biasa
            hide nanda biasa
            "Nanda dan keluarganya terpaksa pindah ke daerah lain karena Nanda gagal menghentikan teror yang menimpanya dan keluarganya."
            return

label rumah_azka:
    scene bg rumah_azka with fade
    pause
    # Dialog awal kedatangan di rumah Azka
    show ayah_azka biasa at right
    ayah_azka "Oh, halo, Nak! Apa kabar? Ada sesuatu yang ayah ingin bicarakan—eh, siapa ini? Kamu membawa teman? Halo, Nak, sini, masuk saja."
    show azka biasa at left
    azka "Em, ayah, kenalkan ini Nanda, teman baruku."
    show nanda diam at center
    nanda "(Diam, merasa tidak nyaman dengan situasi ini.)"
    hide nanda diam
    show azka ragu at left
    azka "Yah... Nanda itu, dia anak seorang nelayan."
    # Reaksi Ayah Azka
    show ayah_azka tajam at right
    ayah_azka "(Tatapannya tajam) Nelayan? Maksudmu keluarganya cari nafkah dari laut? Dari seafood?"
    show azka khawatir at left
    azka "Iya, Yah."
    ayah_azka "Kamu nggak tahu, Nak. Dulu waktu Ayah kecil, Ayah tinggal di pinggir pantai. Setiap hari rumah kita bau amis karena pasar ikan ada di dekat situ. Orang-orang di sana nggak pernah peduli sama kebersihan."
    ayah_azka "Setiap kali Ayah jalan ke sekolah, Ayah selalu dihina sama anak-anak nelayan karena keluarga kita nggak kerja di laut. Ayah dibully cuma karena nggak makan ikan. Itu kenangan yang nggak bisa Ayah lupain."

    show azka serius at left
    azka "Yah, aku ngerti kalau pengalaman Ayah dulu nggak enak. Tapi Nanda dan keluarganya nggak ada hubungannya sama itu. Mereka nggak salah cuma karena mereka kerja di laut. Mereka juga manusia, Yah."
    show ayah_azka tajam at right
    ayah_azka "Tapi mereka tetap bagian dari kelompok itu, Azka."

    show nanda berani at center
    nanda "Om, keluarga saya memang nelayan, itu benar. Tapi kami nggak cuma kerja untuk cari uang, kami juga jaga laut yang kami andalkan untuk hidup."
    nanda "Ayah saya ikut gerakan pembersihan pantai, kami nggak pernah ambil ikan secara berlebihan, dan kami ngajarin anak-anak di desa untuk nggak buang sampah ke laut."
    show ayah_azka tajam at right
    ayah_azka "Kamu tahu, Nanda? Dulu hidup saya pernah sulit karena orang-orang nelayan di kampung saya. Tapi mungkin... saya sudah terlalu lama menyimpan kebencian itu."

    show nanda tenang at center
    nanda "Saya nggak tahu apa yang Om alami dulu, tapi satu hal yang saya tahu, kebencian itu nggak akan membuat Om lebih bahagia. Kita cuma ingin hidup, Om, sama seperti semua orang."
    show azka memohon at left
    azka "Ayah, aku mohon. Kita bisa belajar lihat orang dari hatinya, bukan dari pekerjaannya."
    show ayah_azka menghela_napas at right
    ayah_azka "(Menghela napas panjang) Kamu benar, Azka... Nanda. Mungkin saya salah selama ini."

    show nanda tersenyum at center
    nanda "(Tersenyum, lega) Terima kasih, Om. Saya harap ke depannya, Om bisa melihat kami sebagai teman, bukan musuh."
    hide ayah_azka menghela_napas
    hide azka memohon
    hide nanda tersenyum
    show ayah_azka tersenyum at right
    ayah_azka "(Tersenyum)Terima kasih, Nanda. Saya harus keluar sebentar untuk mengurus sesuatu."
    hide ayah_azka tersenyum
    show azka biasa at left
    azka "Ayah, mau ke mana?"
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
    return

        

    
