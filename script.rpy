# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg blck = "images/pantai.jpg"
image bg cls = "images/cls1.jpg"
image bg kantin = "images/kantin.jpg"
image nanda biasa = "images/nanda.png"
image nanda sedih = "images/nanda.png"
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
        show nanda biasa at left

label kantin:
    scene bg kantin
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


    










