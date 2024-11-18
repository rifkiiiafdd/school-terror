# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg blck = "images/pantai.jpg"
image bg cls = "images/cls1.jpg"
image bg kantin = "images/kantin.jpg"
image bg teras = "images/teras.jpg"
image bg ruang_guru = "images/ruang_guru.jpg"
image nanda biasa = "images/nanda.png"
image nanda sedih = "images/nanda.png"
image nanda kaget = "images/nanda.png"
image azka kaget = "images/nanda.png"
image nanda makan = "images/gadismakan.png"
image ibu khawatir = "images/nanda.png"
image ibu gembira = "images/nanda.png"
image classmates = "images/classmate.png"
image bg rumah = "images/rumah1.jpg"
image azka biasa = "images/azka.png"
image meja = "images/meja.png"
image tv = "images/tv.png"

# Deklarasikan karakter yang digunakan di game.
define nanda = Character("Nanda", color="#eea8ea")
define azka = Character("Azka",color = "#62a0d2")
define teman = Character("Classmates", color = "#747171")
define ibu = Character("Ibu", color = "#0a0807")
define guru = Character("Guru", color = "#0a0807")

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
    scene bg cls
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
    pause
    show classmates at right
    teman "Lah, kenapa kamu makan ikan? Itu menjijikkan, mana mungkin kamu makan makhluk hidup dari laut."
    menu:
        "Kenapa memangnya? ":
            nanda "Kenapa memangnya?"
            jump nantang

        "Ikan itu lezat dan sehat tau!":
            nanda "Ikan itu lezat dan sehat tau!"
            jump ikanlezat
    
    label nantang:
        teman "Lah? Nantangin?"
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
    show nanda sedih at left
    pause
    if nantang:
        show ibu khawatir at right
        ibu "Nanda, kamu pulang sih, tapi kenapa kamu masih sedih?"
        
        menu:
            "...":
                nanda "..."
                hide ibu khawatir
                show tv at right 
                "TV dalam keadaan menyala, sedang menayangkan acara berita"
                "reporter" '"Sebuah organisasi yang bermotif dari kebencian akan makanan laut, Perkumpulan Warga Anti Seafood, PWAS, makin meresahkan warga setempat"'
                "reporter" '"kabarnya, pergerakan radikal organisasi ini mulai meluas pada tiap kalangan"'
                hide tv
                show ibu khawatir at right 
                nanda "{i}Jadi ini alasan aku dirundung{/i}"
                $ tahu_alasan = True
                jump kamar_nanda

            
            "Tidak apa-apa bu":
                $ tahu_alasan = False
                nanda "Tidak apa-apa bu"
                hide ibu khawatir
                hide nanda sedih
                
                jump kamar_nanda

    else :
        $ tahu_alasan = False
        show ibu gembira at right
        ibu "Bagaimana hari pertama sekolahmu, nak"
        nanda "Tidak apa-apa, bu"
        hide nanda sedih
        hide ibu gembira
        jump kamar_nanda
    
    label kamar_nanda:
        scene bg rumah
        "Nanda masuk ke kamar"
        if nantang :
            show nanda sedih at left
            nanda "(Menangis)"
            nanda "{i}Sepertinya aku harus lebih ramah kepada orang lain{i}"
    
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
    show guru biasa at right
    guru "Ada apa, Nanda? Kamu terlihat sedih."
    nanda "Bu, aku selalu dibully oleh teman-teman di sekolah."
    guru "Oh tidak, siapa yang melakukan itu?"
    nanda "Aku tidak tahu nama mereka, tapi mereka selalu mengejek dan menghinaku."
    guru "Itu tidak bisa dibiarkan. Ibu akan mencari tahu siapa mereka. Tapi kamu juga harus berani, Nanda."
    nanda "Berani bagaimana, Bu?"
    guru "Berani untuk tidak membiarkan mereka merendahkanmu. Tunjukkan bahwa kamu kuat dan tidak takut."
    nanda "Tapi, Bu, itu sulit..."
    guru "Ibu tahu, tapi kamu tidak sendiri. Ibu dan teman-teman yang baik akan selalu mendukungmu."

    if tahu_alasan:
        nanda "Terima kasih, Bu. Aku akan mencoba."
        hide guru biasa
        nanda "pasti tidak semua orang membenci keluarga nelayan sepertiku"
        nanda "Aku harus mencari teman seperti itu"
        hide nanda sedih
    else :
        nanda "Mereka.."
        nanda "Mereka semua tanpa alasan membully ku karena aku anak nelayan"
        nanda "Aku benci itu"
        guru "Nanda, jangan berkata seperti itu. Semua pekerjaan itu mulia"
        guru "jangan khawatir, ibu akan memarahi mereka"
        hide guru biasa
        nanda "{i}Ibu tidak mengerti{/i}"
        nanda "{i}Ku rasa tidak ada yang bisa kupercaya{/i}"
        hide nanda sedih
    jump di_teras_sekolah

label di_teras_sekolah:
    scene bg teras
    pause
    show nanda biasa at left 
    pause
    show azka biasa at right
    pause
    azka "Hai, apakah kamu tidak apa-apa?"
    $ azka_berteman = True
    nanda "..."
    azka "Aku sering melihat apa yang mereka lakukan padamu. Tenang saja, aku tidak sama seperti mereka, ayahku juga sering memancing."
    if tahu_alasan:
        nanda "Aku tidak apa-apa, kok, terima kasih ya."
        azka "aku tahu kok, berita tentang organisasi itu"
        nanda "ehh, benarkah?"
        azka "iya, aku sebenarnya juga melihat kalau organisasi itu bisa saja ikut andil dalam perlakuan buruk yang teman-teman sekelasmu lakukan di sini"
        nanda "aku juga menduga seperti itu.."
        "(Nanda mendapat teman pertamanya)"
        jump azka_ngobrol
    
    else :
        menu :
            "ramah":
                nanda "aku tidak apa-apa, kok, terima kasih"
                nanda  "aku sering merasa sendirian di sini, nama kamu siapa?"
                azka "Namaku azka, senang berkenalan denganmu!"
                azka "aku tahu kok, berita tentang organisasi itu"
                nanda "oh ya.."
                azka " iya, aku sebenarnya juga melihat kalau organisasi itu bisa saja ikut andil dalam perlakuan buruk yang teman-teman sekelasmu lakukan di sin"
                nanda "begitu ya.."
                nanda "aku juga menduga seperti itu"
                jump azka_ngobrol
        
            "dingin" :
                nanda "Oh iya, aku tidak apa-apa, senang bertemu kamu, tapi aku ada urusan, aku pergi dulu ya"
                azka "Oh, baik, sampai bertemu, ya!"
                "(Dan begitulah Nanda kehilangan satu-satunya kesempatan mendapatkan teman baru)"
                $ azka_ikut = False
                $ azka_berteman = False
                jump rumah2

            
label azka_ngobrol :
    azka " lengkapnya, mau ngobrol tentang itu gak sehabis sekolah?"
    menu :
        "Terima Ajakan":
            nanda "Boleh"
            $ azka_ikut = True
            jump rumah2
        
        "Tolak Ajakan":
            nanda "Maaf, aku ada urusan"
            $ azka_ikut = False
            jump rumah2
    


label rumah2:
    hide azka biasa
    hide nanda biasa
    pause
    scene bg rumah
    pause
    if azka_ikut :
        show nanda biasa at left
        pause
        show azka biasa at right
        pause
        nanda "Jadi, kamu mau ngobrolin apa?"
        pause 
        azka "Aku mungkin tau sedikit hal tentang PWAS...."
        azka "..."
        pause
        hide azka biasa
        hide nanda biasa
        show nanda kaget at left
        show azka kaget at right 
        "DOR DOR DOR *\ (suara pintu diketuk)"
        "(Sebelum Azka dapat bercerita, tiba2 pintu depan rumah Nanda didobrak paksa)"
        "..." "Keluar kau nelayan bau amis"
        azka "Sial, mereka datang kesini"
        azka "ayo lari"
        hide nanda kaget
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

    

        

    