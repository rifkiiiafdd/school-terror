# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg blck = "images/pantai.jpg"
image bg cls = "images/cls1.jpg"
image bg kantin = "images/kantin.jpg"
image nanda biasa = "images/nanda.png"
image nanda makan = "images/gadismakan.png"
image classmates = "images/classmate.png"
image azka biasa = "images/azka.png"
image meja = "images/meja.png"

# Deklarasikan karakter yang digunakan di game.
define nanda = Character("Nanda", color="#eea8ea")
define azka = Character("Azka",color = "#62a0d2")
define teman = Character("Classmates", color = "#747171")

# Game dimulai disini.
label start:
    scene bg blck   
    play music "orison.ogg"
    "Di suatu desa kecil di tepi pantai,..\ "
    "hidup seorang anak yang setiap harinya membantu kedua orang tuanya.."
    "ayah seorang nelayan, dan ibu seorang pedagang ikan."
    "Bagi mereka, laut adalah kehidupan."
    stop music
    jump classroom1

label classroom1 :
    scene bg cls
    play music "clas_music.ogg" fadeout 1 fadein 1
    
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
        "Dan mereka pun berkelahi"
        jump masih_kantin
    
    label ikanlezat:
        teman "nyennyene"
        jump masih_kantin
    
    label masih_kantin :
        "Hubungan mereka semakin memburuk"
    stop music

label eskalasi:
    scene bg cls
    show nanda biasa at left 
    pause
    show meja at center
    pause
    nanda "Kenapa mereka membenci kami hanya karena kami dari keluarga nelayan?"
    hide meja
    "..."


    










