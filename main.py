import telebot
import time

TOKEN = "5384352973:AAEz0Ipmmm_hZXtEqBDWipUWMxxy8LoVs_Y"

bot = telebot.TeleBot(TOKEN)

start = " Selamat Datang Di Layanan LKM FIT BOT. \n" \
 \
 \
        "\n" \
 \
 \
        "Untuk mengetahui informasi mengenai Layanan KP & Magang, silahkan ketik atau klik Kode Sesuai dengan Opsi Kategori Di bawah ini:  \n" \
 \
 \
        "\n" \
 \
 \
        "\n" \
 \
 \
        "/A. Sosialisasi dan Seputar Magang\n" \
 \
 \
        "/B. Pendaftaran Magang\n" \
 \
 \
        "/C. Pelaksanaan Magang\n" \
 \
 \
        "/D. Presentasi Magang\n" \
 \
 \
        "/E. Pengumpulan Berkas Magang\n" \
 \
 \
        "/F. Penilaian\n" \
 \
 \
        "/G. Media Informasi/Kontak LKM FIT  \n" \
 \
 \
        "\n" \
 \
 \
        "\n" \
 \
 \
        "Apabila, Ingin ada yang ditanyakan lebih lanjut atau kendala, silahkan chat whatsapp kami  : \n" \
 \
 \
        "\n" \
 \
 \
        "https://wa.me/6285161415115"


A = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Sub Kategori Di bawah ini :\n" \
 \
 \
    "\n" \
 \
 \
    "/AA. MK Magang\n" \
 \
 \
    "/AB. Seputar Magang\n" \
 \
 \
    "/AC. Agenda Magang\n" \
 \
 \
    "/AD. Jenis Magang yang Diakui LKM FIT \n" \
 \
 \
    "/AE. Syarat Perusahaan Magang \n" \
 \
 \
    "/AF. Lowongan Magang \n" \
 \
 \
    "/AG. Info Sosialisasi Magang \n" \
 \
 \
    "\n" \
 \
 \
    "\n" \
 \
 \
    "ketik atau klik   \"/start\" untuk kembali ke menu sebelumnya. \n"


AA = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
     "\n" \
 \
 \
     "/AA001 Kapan ambil MK Magang?\n" \
 \
 \
     "/AA002 Bagaimana jika belum ambil MK Magang?\n" \
 \
 \
     "/AA003 Bagaimana jika mengulang Magang?\n" \
 \
 \
     "/AA004 Bagaimana jika magang di luar agenda magang?\n" \
 \
 \
     "\n" \
 \
 \
     "ketik atau klik \"/A\" untuk kembali ke menu sebelumnya. "\
\
"\nketik atau klik \"/start\" untuk kembali ke menu utama. "

AA001 = "Kapan ambil MK Magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Mahasiswa mengambil MK MAGANG pada semester dimana magang akan dilaksanakan dan laporan akan dikumpulkan juga. " \
 \
 \
"Bukan saat semester pendaftaran magang (semester sebelum magang)."\
\
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/AA\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

AA002 = "Bagaimana jika belum ambil MK Magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Kegiatan magang masih bisa dilakukan, tetapi nilai untuk MK Magang tidak bisa dikeluarkan." \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/AA\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

AA003 = "Bagaimana jika mengulang Magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Mahasiswa wajib mengambil MK MAGANG lagi pada semester dimana kegiatan magang dilaksanakan." \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/AA\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

AA004 = "Bagaimana jika magang di luar agenda magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Jika pelaksanaan magang diluar agenda magang, akan ditinjau secara case per case. Silahkan  Hubungi Admin untuk informasi lebih lanjut."\
\
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/AA\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "


AB = "Silahkan ketik atau klik  Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
     "\n" \
 \
 \
     "/AB001. Apa itu magang?\n" \
 \
 \
     "/AB002. Siapa yang harus daftar magang?\n" \
 \
 \
     "/AB003. Kenapa harus daftar magang?\n" \
 \
 \
     "/AB004. Dimana mahasiswa dapat bertanya atau konsultasi terkait magang?\n" \
 \
 \
     "\n" \
 \
 \
     "ketik atau klik \"/A\" untuk kembali ke menu sebelumnya. "\
\
"\nketik atau klik atau klik  \"/start\" untuk kembali ke menu utama. "

AB001 = "Apa itu magang?\t\n" \
 \
 \
        "\n" \
 \
 \
        "Magang merupakan bagian dari salah satu pelatihan kerja yang terselenggara di sebuah perusahaan untuk menerapkan keilmuan atau kompetensi yang didapat selama menjalani masa pendidikan, di dunia kerja secara langsung.\n" \
 \
 \
        "\n" \
 \
 \
        "Info Lebih Lanjut Seputar Magang : https://drive.google.com/drive/folders/1AfGRIQ63gOpFuROueOajDFSlmFmHd1Yl\n"\
\
"\n" \
 \
 \
"ketik atau klik \"/AB\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

AB002 = "Siapa yang harus daftar magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Seluruh Mahasiswa Telkom University" \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/AB\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

AB003 = "Kenapa harus daftar magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Karena magang termasuk salah satu mata kuliah wajib " \
 \
 \
"bagi mahasiswa diploma Telkom University yang bertujuan untuk mengimplementasikan " \
 \
 \
"ilmu yang didapat selama kuliah ke dunia kerja.\n" \
 \
 \
"\n" \
 \
 \
"Info Lebih Lanjut Seputar Magang : https://drive.google.com/drive/folders/1AfGRIQ63gOpFuROueOajDFSlmFmHd1Yl\n"\
\
"\n" \
 \
 \
"ketik atau klik \"/AB\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik  \"/start\" untuk kembali ke menu utama. "

AB004 = "Dimana mahasiswa dapat bertanya atau konsultasi terkait magang? \n\n" \
 \
 \
        "Pertanyaan seputar Magang dapat hubungi LKM dengan cara :\n" \
 \
 \
        "1. Email\n" \
 \
 \
        "( magang@tass.telkomuniversity.ac.id )\n" \
 \
 \
        "2. Official WhatsApp\n" \
 \
 \
        "( https://wa.me/6285161415115 )\n" \
 \
 \
        "3. Instagram\n" \
 \
 \
        "( https://www.instagram.com/magang.fit/ )\n"\
\
"\n" \
 \
 \
"ketik atau klik \"/AB\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "


AC = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
     "\n" \
 \
 \
     "/AC001 Apa itu agenda magang?\n" \
 \
 \
"AC002 Dimana mahasiswa dapat melihat agenda magang? \n" \
 \
 \
     "/AC003 Bagaimana jika magang di luar agenda magang? \n" \
 \
 \
     "\n" \
 \
 \
     "ketik atau klik \"/A\" untuk kembali ke menu sebelumnya. " \
 \
 \
     "\nketik atau klik \"/start\" untuk kembali ke menu utama. "

AC001 = "Apa itu agenda magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Agenda magang dibuat oleh LKM untuk menjadi patokan bagi mahasiswa selama melaksanakan magang, agenda magang merupakan " \
 \
 \
"rekomendasi tanggal bagi mahasiswa yang dibuat LKM agar bisa menyelesaikan magang tepat waktu dan sesuai dengan" \
 \
 \
" kalender akademik Telkom University.\n" \
 \
 \
"\n" \
 \
 \
"Info Lebih Lanjut Seputar Agenda Magang : " \
 \
 \
"https://drive.google.com/drive/folders/0Bw6KX-QlpggQMlVBbEZHOENwem8?resourcekey=0-FU9KV_wCdgD9-dsADC0HIA " \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/AC\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

AC002 = "Dimana mahasiswa dapat melihat agenda magang? \n" \
 \
 \
        "\n" \
 \
 \
        "Info Lebih Lanjut Agenda Magang : https://drive.google.com/drive/folders/1AfGRIQ63gOpFuROueOajDFSlmFmHd1Yl \n" \
 \
        "\n" \
 \
 \
        "Cari Sesuai Dengan Tahun Ajaran Masing-Masing \n \n" \
 \
 \
        "ketik atau klik \"/AC\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
        "ketik atau klik \"/start\" untuk kembali ke menu utama. "

AC003 = "Bagaimana jika magang di luar agenda magang? \n" \
 \
 \
        "\n" \
 \
 \
        "Jika pelaksanaan magang diluar agenda magang, akan ditinjau secara case per case. Silahkan Hubungi Admin untuk informasi lebih lanjut.\n" \
 \
 \
        "\n" \
 \
 \
        "Kontak Admin Kami :\n" \
 \
 \
        "1. Email\n" \
 \
 \
        "(magang@tass.telkomuniversity.ac.id)\n" \
 \
 \
        "2. Official WhatsApp\n" \
 \
 \
        "(https://wa.me/6285161415115)\n" \
 \
 \
        "3. Instagram\n" \
 \
 \
        "(https://www.instagram.com/magang.fit/) \n" \
 \
        "\n" \
 \
 \
        "ketik atau klik \"/AC\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
        "ketik atau klik \"/start\" untuk kembali ke menu utama. "

AD = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
     "\n" \
 \
 \
     "/ADA. Magang Fakultas\n" \
 \
 \
     "/ADB. Magang Mandiri \n" \
 \
 \
     "/ADC. Magang StartUp \n" \
 \
 \
     "/ADD. Magang Kerja \n" \
 \
 \
     "/ADE. Magang MBKM \n" \
 \
 \
     "/ADF. Magang UMKM \n" \
 \
 \
     "\n" \
 \
 \
     "ketik atau klik \"/A\" untuk kembali ke menu sebelumnya. "\
\
"\nketik atau klik \"/start\" untuk kembali ke menu utama. "


ADA = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
      "\n" \
 \
 \
      "/ADA001. Apa itu Magang Fakultas?\n\n" \
 \
 \
      "/ADA002. Apa saja aturan pendokumentasian Magang Fakultas?\n \n" \
 \
 \
      "/ADA003. Kapan batas pendaftaran Magang Fakultas?\n \n" \
 \
 \
      "/ADA004. Bagaimana proses pendaftaran Magang Fakultas?\n \n" \
 \
 \
      "/ADA005. Bagaimana alur Magang Fakultas?\n \n" \
 \
 \
      "\n" \
 \
 \
      "ketik atau klik \"/AD\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
      "ketik atau klik \"/start\" untuk kembali ke menu utama. "

ADA001 = " Apa itu Magang Fakultas? \n" \
 \
 \
         "\n" \
 \
 \
         "Magang di perusahaan yang disediakan oleh LKM FIT dan bersifat terbuka untuk seluruh mahasiswa FIT.\n \n" \
 \
 \
         "(lihat lowongan di https://bit.ly/LowonganKPMagangFIT)\n \n \n" \
 \
 \
         "ketik atau klik \"/ADA\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
         "ketik atau klik \"/start\" untuk kembali ke menu utama. "

ADA002 = " Apa saja aturan pendokumentasian Magang Fakultas? \n" \
 \
 \
         "\n" \
 \
 \
         "1. Dokumen Sebelum Magang\n" \
 \
 \
         " \na) Form pendaftaran online skema fakultas\n" \
 \
 \
         " \nb) Surat Pengantar dibuat LKM\n" \
 \
 \
         " \nc) Surat Penerimaan dari perusahaan (dilaporkan oleh LKM ke mahasiswa)\n\n" \
 \
 \
         " \n" \
 \
 \
         " 2. Dokumen Setelah Magang\n" \
 \
 \
         " \na) Laporan Akhir (terdapat lembar pengesahan yang ditanda-tangan pembimbing lapangan dan dose pembimbing akademik)\n" \
 \
 \
         " \nb) Sertifikat / Surat Selesa Magang\n" \
 \
 \
         " \nc) Lembar Aktivitas Haria Magang\n" \
 \
 \
         " \nd) Nilai Pembimbing Lapangan\n" \
 \
 \
         " \ne) Nilai Akhir Magang (oleh dosen pembimbing akademik)\n\n" \
 \
 \
         "\nInfo aturan pendokumentasian Magang Fakultas dapat diakses di https://magang-sas.telkomuniversity.ac.id/jenis-jenis-magang/  \n \n" \
 \
         "\n" \
 \
 \
         "ketik atau klik \"/ADA\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
         "ketik atau klik \"/start\" untuk kembali ke menu utama. "

ADA003 = " Kapan batas pendaftaran Magang Fakultas? \n" \
 \
 \
         "\n" \
 \
 \
         "Batas pendaftaran Magang Fakultas mengikuti agenda magang yang telah ditetapkan LKM FIT\n" \
 \
 \
         "\n" \
 \
 \
         "Info Lebih Lanjut Agenda Magang : https://drive.google.com/drive/folders/0Bw6KX-QlpggQMlVBbEZHOENwem8?resourcekey=0-FU9KV_wCdgD9-dsADC0HIA \n\n \n" \
 \
 \
         "ketik atau klik \"/ADA\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
         "ketik atau klik \"/start\" untuk kembali ke menu utama. "

ADA004 = " Bagaimana proses pendaftaran Magang Fakultas? " \
 \
 \
         "\n" \
 \
 \
         "\nProses pendaftaran magang fakultas dibantu oleh LKM FIT, sehingga mahasiswa hanya daftar magang di form ( https://bit.ly/PendaftaranMagangFIT ) , proses seleksi dan penerimaan selanjutnya dibantu oleh LKM. \n" \
        "\n\n[ Jangan lupa menggunakan akun SSO ] \n"\
         " \n \n" \
 \
 \
         "\nketik atau klik \"/ADA\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
         "ketik atau klik \"/start\" untuk kembali ke menu utama. "

ADA005 = " Bagaimana alur Magang Fakultas? \n" \
 \
 \
         "\n" \
 \
 \
         "Alur Magang Fakultas Dapat Diakses di : \n" \
 \
 \
         "https://magang-sas.telkomuniversity.ac.id/aturan-magang/  \n \n" \
 \
 \
         "\nketik atau klik \"/ADA\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
         "ketik atau klik \"/start\" untuk kembali ke menu utama. "


ADB = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
      "\n" \
 \
 \
      "/ADB001. Apa itu Magang Mandiri?\n\n" \
 \
 \
      "/ADB002. Apa saja aturan pendokumentasian Magang Mandiri?\n \n" \
 \
 \
      "/ADB003. Kapan batas pendaftaran Magang Mandiri?\n \n" \
 \
 \
      "/ADB004. Bagaimana alur Magang Mandiri? \n\n" \
 \
 \
      "\n" \
 \
 \
      "ketik atau klik \"/AD\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
      "ketik atau klik \"/start\" untuk kembali ke menu utama. "

ADB001 = " Apa itu Magang Mandiri? \n" \
 \
 \
         "\n" \
 \
 \
         "Magang Mandiri adalah magang pada perusahaan di luar yang disediakan oleh LKM FIT. Proses administrasi dari magang ini bersifat mandiri sejak pendaftaran hingga pengumpulan berkas. \n \n" \
 \
 \
         "\nketik atau klik \"/ADB\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
         "ketik atau klik \"/start\" untuk kembali ke menu utama. "

ADB002 = " Apa saja aturan pendokumentasian Magang Mandiri? \n" \
 \
 \
         "\n" \
 \
 \
         "1. Dokumen Sebelum Magang\n\n" \
 \
 \
         "\na) Form pendaftaran online skema mandiri\n" \
 \
 \
         "\nb) Surat Pengantar dibuat LKM\n" \
 \
 \
         "\nc) Surat Penerimaan dari perusahaan (dilaporkan oleh LKM ke mahasiswa)\n\n" \
 \
 \
         " \n" \
 \
 \
         " 2. Dokumen Setelah Magang\n\n" \
 \
 \
         "\na) Laporan Akhir (terdapat lembar pengesahan yang ditanda-tangani pembimbing lapangan dan dosen pembimbing akademik)\n" \
 \
 \
         "\nb) Sertifikat / Surat Selesai Magang\n" \
 \
 \
         "\nc) Lembar Aktivitas Harian Magang\n" \
 \
 \
         "\nd) Nilai Pembimbing Lapangan\n" \
 \
 \
         " \ne) Nilai Akhir Magang (oleh dosen pembimbing akademik)\n" \
 \
 \
         "\n" \
 \
 \
         "\nInfo aturan pendokumentasian Magang Mandiri dapat diakses di https://magang-sas.telkomuniversity.ac.id/jenis-jenis-magang/   \n" \
 \
         "\n" \
 \
 \
         "\nketik atau klik \"/ADB\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
         "ketik atau klik \"/start\" untuk kembali ke menu utama. "

ADB003 = " Kapan batas pendaftaran Magang Mandiri? \n" \
 \
 \
         "\n" \
 \
 \
         "Batas pendaftaran Magang Mandiri mengikuti agenda magang yang telah ditetapkan LKM FIT\n" \
 \
 \
         "\n" \
 \
 \
         "Info Lebih Lanjut Agenda Magang : https://drive.google.com/drive/folders/0Bw6KX-QlpggQMlVBbEZHOENwem8?resourcekey=0-FU9KV_wCdgD9-dsADC0HIA \n\n \n" \
 \
 \
         "\nketik atau klik \"/ADB\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
         "ketik atau klik \"/start\" untuk kembali ke menu utama. "

ADB004 = " Bagaimana Alur Magang Mandiri? " \
 \
 \
         "\n\n" \
 \
 \
         "Alur Magang Mandiri Dapat Diakses di : https://magang-sas.telkomuniversity.ac.id/aturan-magang/  \n \n" \
 \
 \
         "\nketik atau klik \"/ADB\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
         "ketik atau klik \"/start\" untuk kembali ke menu utama. "


ADC = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
      "\n" \
 \
 \
      "/ADC001. Apa itu Magang StartUp?\n\n" \
 \
 \
      "/ADC002. Apa saja aturan pendokumentasian Magang StartUp?\n \n" \
 \
 \
      "/ADC003. Kapan batas pendaftaran Magang StartUp? \n\n" \
 \
 \
      "/ADC004. Bagaimana alur Magang StartUp? \n\n" \
 \
 \
      "\n" \
 \
 \
      "ketik atau klik \"/AD\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
      "ketik atau klik \"/start\" untuk kembali ke menu utama. "

ADC001 = " Apa itu Magang StartUp? \n" \
 \
 \
         "\n" \
 \
 \
         "Magang StartUp adalah magang pada StartUp yang dikelola Inkubator atau Pengelola StartUp di Telkom University.\n\nMagang ini tidak melakukan pekerjaan pada umumnya di perusahaan, namun membangun dan mengelola perusahaan untuk menghasilkan pendapatan perusahaan. \n \n" \
 \
 \
         "\nketik atau klik \"/ADC\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
         "ketik atau klik \"/start\" untuk kembali ke menu utama. "

ADC002 = " Apa saja aturan pendokumentasian Magang StartUp? \n" \
 \
 \
         "\n" \
 \
 \
         "1. Dokumen Sebelum Magang\n" \
 \
 \
         " \na) Form pendaftaran skema StartUp\n" \
 \
 \
         " \nb) Tidak dibuat Surat Pengantar, LKM menerima daftar mahasiswa dari Kaprodi\n" \
 \
 \
         " \nc) Lembar Lulus Evaluasi Magang dari Inkubator atau Pengelol StartUp (dilaporkan dari mahasiswa ke LKM)\n" \
 \
 \
         " \n" \
 \
 \
         " \n2. Dokumen Setelah Magang\n" \
 \
 \
         " \na) Laporan Akhir (terdapat lemba pengesahan yang ditanda-tangan pendamping StartUp dan dosen pembimbing akademik)\n" \
 \
 \
         " \nb) Surat Selesai Magang denga rekomendasi nilai dari pembimbing StartUp\n" \
 \
 \
         " \nc) Pitchdesk Inkubasi StartUp\n" \
 \
 \
         " \nd) Nilai Dosen Pembimbing\n" \
 \
 \
         "\n" \
 \
 \
         "\nInfo aturan pendokumentasian Magang StartUp dapat diakses di https://magang-sas.telkomuniversity.ac.id/jenis-jenis-magang/ \n" \
 \
         "\n" \
 \
 \
         "\nketik atau klik \"/ADC\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
         "ketik atau klik \"/start\" untuk kembali ke menu utama. "

ADC003 = " Kapan batas pendaftaran Magang StartUp? \n" \
 \
 \
         "\n" \
 \
 \
         "Info Lebih Lanjut Agenda Magang : https://drive.google.com/drive/folders/0Bw6KX-QlpggQMlVBbEZHOENwem8?resourcekey=0-FU9KV_wCdgD9-dsADC0HIA \n\n \n" \
 \
 \
         "ketik atau klik \"/ADC\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
         "ketik atau klik \"/start\" untuk kembali ke menu utama. "

ADC004 = " Bagaimana Alur Magang StartUp? " \
 \
 \
         "\n" \
 \
 \
         "\nAlur Magang StartUp Dapat Diakses di : https://magang-sas.telkomuniversity.ac.id/aturan-magang/  \n \n" \
 \
 \
         "\nketik atau klik \"/ADC\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
         "ketik atau klik \"/start\" untuk kembali ke menu utama. "


ADD = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
      "\n" \
 \
 \
      "/ADD001. Apa itu Magang Kerja?\n\n" \
 \
 \
      "/ADD002. Apa saja aturan pendokumentasian Magang Kerja?\n \n" \
 \
 \
      "/ADD003. Kapan batas pendaftaran Magang Kerja?\n \n" \
 \
 \
      "/ADD004. Bagaimana alur Magang Kerja? \n\n" \
 \
 \
      "\n" \
 \
 \
      "ketik atau klik \"/AD\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
      "ketik atau klik \"/start\" untuk kembali ke menu utama. "

ADD001 = " Apa itu Magang Kerja? \n" \
 \
 \
         "\n" \
 \
 \
         "Magang Kerja adalah kegiatan magang bagi mahasiswa yang telah bekerja dapat diakui pengalaman kerjanya sebagai kegiatan Magang dan Proyek Akhir. Perusahaan tempat kerja harus berfirma (CV atau PT) dan sudah berjalan selama minimal 3 tahun. \n \n" \
 \
 \
         "\nketik atau klik \"/ADD\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
         "ketik atau klik \"/start\" untuk kembali ke menu utama. "

ADD002 = " Apa saja aturan pendokumentasian Magang Kerja? \n" \
 \
 \
         "\n" \
 \
 \
         "Info aturan pendokumentasian Magang Kerja dapat diakses di https://magang-sas.telkomuniversity.ac.id/jenis-jenis-magang/  \n" \
 \
         "\n" \
 \
 \
         "\nketik atau klik \"/ADD\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
         "ketik atau klik \"/start\" untuk kembali ke menu utama. "

ADD003 = " Kapan batas pendaftaran Magang Kerja? \n" \
 \
 \
         "\n" \
 \
 \
         "Info Lebih Lanjut Agenda Magang : https://drive.google.com/drive/folders/0Bw6KX-QlpggQMlVBbEZHOENwem8?resourcekey=0-FU9KV_wCdgD9-dsADC0HIA \n\n \n" \
 \
 \
         "\nketik atau klik \"/ADD\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
         "ketik atau klik \"/start\" untuk kembali ke menu utama. "

ADD004 = " Bagaimana Alur Magang Kerja? " \
 \
 \
         "\n" \
 \
 \
         "\nAlur Magang Kerja Dapat Diakses di : https://magang-sas.telkomuniversity.ac.id/aturan-magang/  \n \n" \
 \
 \
         "\nketik atau klik \"/ADD\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
         "ketik atau klik \"/start\" untuk kembali ke menu utama. "


ADE = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
      "\n" \
 \
 \
      "/ADE001. Apa itu Magang MBKM?\n\n" \
 \
 \
      "/ADE002. Apa saja aturan pendokumentasian Magang MBKM? \n\n" \
 \
 \
      "/ADE003. Kapan batas pendaftaran Magang MBKM?\n \n" \
 \
 \
      "/ADE004. Dimana mahasiswa dapat melihat informasi magang MBKM dari Kemendikbud?\n \n" \
 \
 \
      "/ADE005. Bagaimana alur Magang MBKM? \n\n" \
 \
 \
      "\n" \
 \
 \
      "ketik atau klik \"/AD\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
      "ketik atau klik \"/start\" untuk kembali ke menu utama. "

ADE001 = " Apa itu Magang MBKM? \n" \
 \
 \
         "\n" \
 \
 \
         "Magang MBKM adalah magang yang dilaksanakan oleh Kemendikbud dan Bagian Perkuliahan Universitas dan Luar Prodi Studi (BPUPLS dahulu PPDU) Universitas Telkom guna mendukung program Merdeka Belajar Kampus Merdeka (MBKM).\n\nInformasi selanjutnya mengenai program magang MBKM dan lowongan Magang MBKM dapat dilihat di kampusmerdeka.kemdikbud.go.id/program/magang atau di ppdu - internship.telkomuniversity.ac.id / \n \n"\
\

"\nketik atau klik \"/ADE\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

ADE002 = " Apa saja aturan pendokumentasian Magang MBKM? \n" \
 \
 \
         "\n" \
 \
 \
         "\n1. Dokumen Sebelum Magang\n" \
 \
 \
         "\n a) Form pendaftaran skema MBKM\n" \
 \
 \
         "\n b) Surat Pengantar dibuat oleh LKM\n" \
 \
 \
         "\n c) Surat Penerimaan dari perusahaan atau kemendikbud (dilaporkan dari mahasiswa ke LKM)\n" \
 \
 \
         " \n" \
 \
 \
         " \n2. Dokumen Setelah Magang\n" \
 \
 \
         "\n a) Laporan Akhir (terdapat lembar pengesahan yang ditanda-tangani pembimbing lapangan dan dosen pembimbing akademik)\n" \
 \
 \
         "\n b) Sertifikat / Surat Selesai Magang\n" \
 \
 \
         "\n c) Lembar Aktifitas Harian\n" \
 \
 \
         "\n d) Nilai Pembimbing Lapangan\n" \
 \
 \
         "\n e) Nilai Akhir Magang (oleh dosen pembimbing akademik)\n" \
 \
 \
         "\n" \
 \
 \
         "\nInfo aturan pendokumentasian Magang MBKM dapat diakses di https://magang-sas.telkomuniversity.ac.id/jenis-jenis-magang/ \n" \
 \
         "\n" \
 \
 \
         "\nketik atau klik \"/ADE\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
         "ketik atau klik \"/start\" untuk kembali ke menu utama. "

ADE003 = " Kapan batas pendaftaran Magang MBKM? \n" \
 \
 \
         "\n" \
 \
 \
         "Info Lebih Lanjut Agenda Magang : https://drive.google.com/drive/folders/0Bw6KX-QlpggQMlVBbEZHOENwem8?resourcekey=0-FU9KV_wCdgD9-dsADC0HIA \n\n \n" \
 \
 \
         "\nketik atau klik \"/ADE\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
         "ketik atau klik \"/start\" untuk kembali ke menu utama. "

ADE004 = " Dimana mahasiswa dapat melihat informasi magang MBKM dari Kemendikbud? " \
 \
 \
         "\n" \
 \
 \
         "\nSilakan mengunjungi situs Kemendikbud dengan link di bawah ini: https://kampusmerdeka.kemdikbud.go.id/program/magang  \n \n" \
 \
 \
         "\nketik atau klik \"/ADE\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
         "ketik atau klik \"/start\" untuk kembali ke menu utama. "

ADE005 = " Bagaimana Alur Magang MBKM? " \
 \
 \
         "\n" \
 \
 \
         "\nAlur Magang MBKM Dapat Diakses di : https://magang-sas.telkomuniversity.ac.id/aturan-magang/  \n \n" \
 \
 \
         "\nketik atau klik \"/ADE\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
         "ketik atau klik \"/start\" untuk kembali ke menu utama. "


ADF = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
      "\n" \
 \
 \
      "/ADF001. Apa itu Magang UMKM?\n\n" \
 \
 \
      "/ADF002. Apa saja aturan pendokumentasian Magang UMKM? \n\n" \
 \
 \
      "/ADF003. Kapan batas pendaftaran Magang UMKM? \n\n" \
 \
 \
      "/ADF004. Bagaimana alur Magang UMKM?\n \n" \
 \
 \
      "\n" \
 \
 \
      "ketik atau klik \"/AD\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
      "ketik atau klik \"/start\" untuk kembali ke menu utama. "

ADF001 = "Apa itu Magang UMKM? \n" \
 \
 \
         "\n" \
 \
 \
         "Magang UMKM adalah magang pada UMKM yang menjadi mitra Fakultas Ilmu Terapan. Ruang lingkup magang adalah pembuatan konten digital untuk pemasaran dan pengelolaan media sosial guna perluasan pelanggan dan peningkatan bisnis UMKM. Magang UMKM hanya tersedia untuk prodi D3 Manajemen Pemasaran. \n \n" \
 \
 \
         "\nketik atau klik \"/ADF\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
         "ketik atau klik \"/start\" untuk kembali ke menu utama. "

ADF002 = " Apa saja aturan pendokumentasian Magang UMKM? \n" \
 \
 \
         "\n" \
 \
 \
         "\n1. Dokumen Sebelum Magang\n" \
 \
 \
         "\n a) Form pendaftaran skema mandiri (khusus untuk D3 Manajemen Pemasaran)\n" \
 \
 \
         "\n b) Surat Pengantar dibuat LKM\n" \
 \
 \
         "\n c) Surat Penerimaan dari perusahaan (dilaporkan oleh mahasiswa ke LKM)\n" \
 \
 \
         " \n" \
 \
 \
         "\n 2. Dokumen Setelah Magang\n" \
 \
 \
         "\n a) Laporan Akhir (terdapat lembar pengesahan yang ditanda-tangani pembimbing lapangan dan dosen pembimbing akademik)\n" \
 \
 \
         "\n b) Sertifikat / Surat Selesai Magang\n" \
 \
 \
         "\n c) Lembar Aktivitas Harian Magang\n" \
 \
 \
         "\n d) Nilai Pembimbing Lapangan\n" \
 \
 \
         "\n e) Nilai Akhir Magang (oleh dosen pembimbing akademik)\n" \
 \
 \
         "\n" \
 \
 \
         "\nInfo aturan pendokumentasian Magang UMKM dapat diakses di https://magang-sas.telkomuniversity.ac.id/jenis-jenis-magang/ \n" \
 \
         "\n" \
 \
 \
         "\nketik atau klik \"/ADF\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
         "ketik atau klik \"/start\" untuk kembali ke menu utama. "

ADF003 = " Kapan batas pendaftaran Magang UMKM? \n" \
 \
 \
         "\n" \
 \
 \
         "Info Lebih Lanjut Agenda Magang : https://drive.google.com/drive/folders/0Bw6KX-QlpggQMlVBbEZHOENwem8?resourcekey=0-FU9KV_wCdgD9-dsADC0HIA \n\n \n" \
 \
 \
         "\nketik atau klik \"/ADF\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
         "ketik atau klik \"/start\" untuk kembali ke menu utama. "

ADF004 = " Bagaimana Alur Magang UMKM? " \
 \
 \
         "\n" \
 \
 \
         "\nAlur Magang UMKM Dapat Diakses di : https://magang-sas.telkomuniversity.ac.id/aturan-magang/  \n \n" \
 \
 \
         "\nketik atau klik \"/ADF\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
         "ketik atau klik \"/start\" untuk kembali ke menu utama. "


AE = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
     "\n" \
 \
 \
     "/AE001. Apa syarat perusahaan yang bisa diajukan untuk magang? \n" \
 \
 \
     "\n\n" \
 \
 \
     "ketik atau klik \"/A\" untuk kembali ke menu sebelumnya. "\
\
"\nketik atau klik \"/start\" untuk kembali ke menu utama. "

AE001 = "Apa syarat perusahaan yang bisa diajukan untuk magang?\n\n" \
 \
 \
        "\n" \
 \
 \
        "Syarat Perusahaan magang diantarnya adalah:\n\n" \
 \
 \
        "1. Perusahaan tersebut memiliki sistem administrasi (cap dan penomoran dokumen)\n\n" \
 \
 \
        "2. Perusahaan memiliki lokasi kerja (kantor)\n\n" \
 \
 \
        "3. Perusahaan memiliki struktur organisasi\n\n" \
 \
 \
        "4. Perusahaan memiliki pekerjaan yang bisa dikerjakan oleh mahasiwa magang\n"\
\
"\n\n" \
 \
 \
"ketik atau klik \"/AE\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

AF = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
     "\n" \
 \
 \
     "/AF001. Apa itu lowongan magang? \n\n" \
 \
 \
     "/AF002. Dimana mahasiswa dapat melihat Lowongan Magang yang disediakan oleh Falkutas Ilmu Terapan? \n\n" \
 \
 \
     "/AF003. Dimana mahasiswa dapat melihat perusahaan yang bekerja sama dengan Telkom University?\n \n" \
 \
 \
     "/AF004. Bagaimana melakukan pendaftaran Magang di lowongan yang disediakan oleh Fakultas Ilmu Terapan? \n" \
 \
 \
     "\n\n" \
 \
 \
     "ketik atau klik \"/A\" untuk kembali ke menu sebelumnya. "\
\
"\nketik atau klik \"/start\" untuk kembali ke menu utama. "

AF001 = "Apa itu lowongan magang?\n\n" \
 \
 \
        "\n" \
 \
 \
        "Lowongan magang adalah tersedianya posisi jabatan atau pekerjaan yang terbuka di suatu perusahaan untuk mahasiswa yang akan melakukan magang \n"\
\
"\n\n" \
 \
 \
"ketik atau klik \"/AF\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

AF002 = " Dimana mahasiswa dapat melihat Lowongan Magang yang disediakan oleh Falkutas Ilmu Terapan? \n\n" \
 \
 \
        "\n" \
 \
 \
        "Lowongan Magang dapat di akses melalui :\nhttps://magang-sas.telkomuniversity.ac.id/lowongan-magang/ \n"\
\
"\n\n" \
 \
 \
"ketik atau klik \"/AF\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

AF003 = " Dimana mahasiswa dapat melihat perusahaan yang bekerja sama dengan Telkom University? \n\n" \
 \
 \
        "\n" \
 \
 \
        "Daftar perusahaan yang bekerja sama dengan Telkom University dapat di akses di https://magang-sas.telkomuniversity.ac.id/perusahaan/  \n"\
\
"\n\n" \
 \
 \
"ketik atau klik \"/AF\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

AF004 = " Bagaimana melakukan pendaftaran Magang di lowongan yang disediakan oleh Fakultas Ilmu Terapan? \n\n" \
 \
 \
        "\n" \
 \
 \
        "Pendaftaran Magang dapat diakses melalui https://bit.ly/PendaftaranMagangFIT \n\n" \
 \
 \
        "[ Jangan lupa menggunakan akun SSO ] \n"\
\
"\n\n" \
 \
 \
"ketik atau klik \"/AF\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "


AG = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
     "\n" \
 \
 \
     "/AG001. Dimana info terkait sosialisasi magang dapat diakses? \n" \
 \
 \
     "\n\n" \
 \
 \
     "ketik atau klik \"/A\" untuk kembali ke menu sebelumnya. "\
\
"\nketik atau klik \"/start\" untuk kembali ke menu utama. "

AG001 = "Dimana info terkait sosialisasi magang dapat diakses??\n\n" \
 \
 \
        "\n" \
 \
 \
        "Info terkait pelaksanaan sosialisasi magang dapat diakses di \n" \
 \
 \
        "https://magang-sas.telkomuniversity.ac.id/ \n" \
 \
 \
        "\n" \
 \
 \
        "Materi Sosialisasi Magang dapat diakses di\n" \
 \
 \
        "https://drive.google.com/drive/folders/1AfGRIQ63gOpFuROueOajDFSlmFmHd1Yl \n"\
\
"\n\n" \
 \
 \
"ketik atau klik \"/AG\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "



B = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Sub Kategori Di bawah ini :\n" \
 \
 \
    "\n" \
 \
 \
    "/BA. Alur Magang Online\n" \
 \
 \
    "/BB. Pendaftaran Magang\n" \
 \
 \
    "/BC. Persetujuan Magang dari Dosen Wali\n" \
 \
 \
    "/BD. Dosen Pembimbing Akademik Magang\n" \
 \
 \
    "/BE. Surat Pengantar Magang\n" \
 \
 \
    "/BF. Penerimaan / Diterima\n" \
 \
 \
    "/BG. Penolakan / DItolak\n" \
 \
 \
    "/BH. Pengunduran diri / Dipulangkan\n" \
 \
 \
    "/BI. KEPO MAGANG FIT\n" \
 \
 \
    "\n" \
 \
 \
    "\n" \
 \
 \
    "ketik atau klik \"/start\" untuk kembali ke menu sebelumnya. \n"

BA = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
     "\n" \
 \
 \
     "/BA001. Bagaimana alur pendaftaran magang secara online? \n" \
 \
 \
     "\n" \
 \
 \
     "\n" \
 \
 \
     "ketik atau klik \"/B\" untuk kembali ke menu sebelumnya. "\
\
"\nketik atau klik \"/start\" untuk kembali ke menu utama. "

BA001 = "Bagaimana alur pendaftaran magang secara online??"\
\
"\n" \
 \
"\n" \
 \
 \
"Info alur pendaftaran magang secara online dapat diakses di https://magang-sas.telkomuniversity.ac.id/aturan-magang/"\
\
"\n" \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/BA\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "


BB = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
     "\n" \
 \
 \
     "/BB001. Kapan periode pendaftaran magang? \n \n" \
 \
 \
     "/BB002. Dimana mahasiswa dapat mengakses form pendaftaran magang online? \n \n" \
 \
 \
     "/BB003. Bagaimana cara mendaftar magang? \n \n" \
 \
 \
     "/BB004. Bagaimana jika daftar magangnya terlambat? \n \n" \
 \
 \
     "\n" \
 \
 \
     "ketik atau klik \"/B\" untuk kembali ke menu sebelumnya. "

BB001 = "Kapan periode pendaftaran magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Periode Pendaftaran Magang dapat diakses di: https://drive.google.com/drive/folders/14w639_FFKyF1_HMfV3IhhzQQjRpqNOwf \n" \
 \
 \
"\n" \
 \
 \
"[ Sesuai Dengan Tahun Ajaran Yang Berlaku ]"\
\
"\n" \
 \
"\n"\
\
"\n" \
 \
 \
"ketik atau klik \"/BB\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BB002 = " Dimana mahasiswa dapat mengakses form pendaftaran magang online?"\
\
"\n" \
 \
"\n" \
 \
 \
"Klik tautan dibawah ini: \n https://docs.google.com/forms/d/e/1FAIpQLScYTvWtp0HKlkQdkAzID6ANJu711KQMfrLwQX6AfZm8Tqk6_w/viewform \n \n" \
 \
 \
"(gunakan email SSO/student)\n" \
 \
 \
"\n" \
 \
 \
"\n" \
 \
 \
"Pendaftaran Magang dapat di akses melalui : bit.ly/PendaftaranMagangFIT  \n \n(jangan lupa menggunakan akun SSO)"\
\
"\n \n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/BB\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BB003 = "Bagaimana cara mendaftar magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Tata cara mendaftar magang dapat diakses di https://magang-sas.telkomuniversity.ac.id/aturan-magang/"\
\
"\n" \
 \
"\n\n" \
 \
 \
"ketik atau klik \"/BB\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BB004 = "Bagaimana jika daftar magangnya terlambat?"\
\
"\n" \
 \
"\n" \
 \
 \
"Apabila terlambat daftar magang, " \
 \
 \
"maka konsekuensinya adalah waktu " \
 \
 \
"pelaksanaan magang yang " \
 \
 \
"mundur. dikarenakan tanggal input " \
 \
 \
"nilai tidak bisa diundur, maka " \
 \
 \
"mahasiswa perlu menyesuaikan diri " \
 \
 \
"saat presentasi/audiensi magang " \
 \
 \
"dan pengumpulan berkas magang. " \
 \
 \
"Poinnya kumpulkan berkas magang " \
 \
 \
"sesuai tenggat input nilai ke " \
 \
 \
"igracias, jika tidak maka nilai " \
 \
 \
"magang tidak bisa kami input."\
\
"\n" \
 \
"\n\n" \
 \
 \
"ketik atau klik \"/BB\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BC = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
     "\n" \
 \
 \
     "/BC001. Apa itu persetujuan magang? \n \n" \
 \
 \
     "/BC002. Kapan persetujuan magang diminta? \n \n" \
 \
 \
     "/BC003. Kenapa harus ada persetujuan magang? \n\n" \
 \
 \
     "/BC004. Dimana dosen wali melaporkan persetujuan magang mahasiswa?\n \n" \
 \
 \
     "/BC005. Bagaimana cara mendapatkan persetujuan magang? \n\n" \
 \
 \
     "/BC006. Bagaimana menyampaikan rencana magang ke dosen wali?\n\n" \
 \
 \
     "/BC007. Bagaimana jika dosen wali tidak menyetujui pendaftaran magang mahasiswa? \n" \
 \
 \
     "\n\n" \
 \
 \
     "ketik atau klik \"/B\" untuk kembali ke menu sebelumnya. "\
\
"\nketik atau klik \"/start\" untuk kembali ke menu utama. "

BC001 = "Apa itu persetujuan magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Persetujuan magang adalah hal yang perlu dilakukan oleh dosen wali sebagai tanda bahwa kegiatan magang yang mahasiswa daftarkan sudah sesuai dengan aturan prodi dan tidak menganggu kegiatan akademik lainnya.  \n" \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/BC\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BC002 = " Kapan persetujuan magang diminta?"\
\
"\n" \
 \
"\n" \
 \
 \
"Persetujuan magang diminta dari mahasiswa langsung kepada dosen wali melalui email, persetujuan pengajuan magang bisa diajukan mahasiswa kepada dosen wali setelah mahasiswa mengisi form pendaftaran magang.\n" \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/BC\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BC003 = "Kenapa harus ada persetujuan magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Agar dosen wali bisa mengetahui record magang mahasiswanya dan mengirimkan persetujuan magang ke LKM (rekomendasi kami mahasiswa menghubungi dosen wali melalui email, dengan template email terdapat di artikel aturan magang). \n" \
 \
 \
"\n" \
 \
 \
"Link Artikel Aturan Magang : https://magang-sas.telkomuniversity.ac.id/aturan-magang/  \n" \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/BC\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BC004 = "Dimana dosen wali melaporkan persetujuan magang mahasiswa?"\
\
"\n" \
 \
"\n" \
 \
 \
"Dosen wali wajib memberikan persetujuan magang ke LKM, agar LKM bisa membuat surat pengantar magang. Dosen wali bisa memberikan persetujuan dengan mengisi form konfirmasi persetujuan magang dengan tautan berikut:\nhttps://bit.ly/KonfirmasiMagangFIT  \n" \
        "\n\n[ Jangan lupa menggunakan akun SSO ] \n" \
 \
\
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/BC\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BC005 = " Bagaimana cara mendapatkan persetujuan magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Persetujuan magang diberikan oleh dosen wali. Apabila mahasiswa sudah mengisi form " \
 \
 \
"pendaftaran magang, maka mahasiswa harus menghubungi dosen wali supaya dosen wali bisa " \
 \
 \
"mengetahui record magang mahasiswanya dan mengirimkan persetujuan magang ke LKM (rekomendasi " \
 \
 \
"kami mahasiswa menghubungi dosen wali melalui email, dengan template email terdapat di artikel aturan magang). \n" \
 \
 \
"\n" \
 \
 \
"Info lebih lanjut tata cara mendapatkan persetujuan magang : https://magang-sas.telkomuniversity.ac.id/aturan-magang/ " \
 \
 \
"\n" \
 \
"\n \n" \
 \
 \
"ketik atau klik \"/BC\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BC006 = " Bagaimana menyampaikan rencana magang ke dosen wali?"\
\
"\n" \
 \
"\n" \
 \
 \
"Info lebih lanjut tata cara menyampaikan rencana magang ke dosen wali : https://magang-sas.telkomuniversity.ac.id/aturan-magang/  \n" \
 \
 \
"\n" \
 \
 \
"[ Artikel Aturan Magang Pada Poin Mahasiswa Menyampaikan Rencana Magang ke Dosen Wali ] \n" \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/BC\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BC007 = "Bagaimana jika dosen wali tidak menyetujui pendaftaran magang mahasiswa?"\
\
"\n" \
 \
"\n" \
 \
 \
"Dosen wali memiliki hak untuk menolak pengajuan magang mahasiswa dengan berbagai alasan akademik. Apabila mahasiswa dianggap belum bisa melaksanakan magang, maka dosen wali wajib memberitahukan kepada mahasiswa secara detail alasan pengajuan magang ditolak (bisa melalui email, verbal, atau aplikasi pesan instan). \n" \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/BC\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BD = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
     "\n" \
 \
 \
     "/BD001. Kapan dosen pembimbing diumumkan? \n\n" \
 \
 \
     "/BD002. Kenapa belum dapat dosen pembimbing?\n \n" \
 \
 \
     "/BD003. Dimana mahasiswa melihat data Rekap Penerimaan dan Dosen Pembimbing Magang?\n \n" \
 \
 \
     "\n" \
 \
 \
     "ketik atau klik \"/B\" untuk kembali ke menu sebelumnya. "\
\
"\nketik atau klik \"/start\" untuk kembali ke menu utama. "

BD001 = " Kapan dosen pembimbing diumumkan?"\
\
"\n" \
 \
"\n" \
 \
 \
"Dosen pembimbing akademik diumumkan pada awal semester setelah masa PRS dilakukan."\
\
"\n" \
 \
"\n\n" \
 \
 \
"ketik atau klik \"/BD\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BD002 = "Kenapa belum dapat dosen pembimbing?"\
\
"\n" \
 \
"\n" \
 \
 \
"Ada kemungkinan mahasiswa belum mengambil MK Magang di semester berjalan."\
\
"\n" \
 \
"\n\n" \
 \
 \
"ketik atau klik \"/BD\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BD003 = "Dimana mahasiswa melihat data Rekap Penerimaan dan Dosen Pembimbing Magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Silakan klik link berikut ini :\n" \
 \
 \
"https://magang-sas.telkomuniversity.ac.id/rekap-penerimaan-dan-dosen-pembimbing-magang/ "\
\
"\n" \
 \
"\n\n" \
 \
 \
"ketik atau klik \"/BD\" untuk kembali ke menu sebelumnya. \n"\
\
"\nketik atau klik \"/start\" untuk kembali ke menu utama. "


BE = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
     "\n" \
 \
 \
     "/BE001. Apa itu Surat Pengantar Magang? \n\n" \
 \
 \
     "/BE002. Kapan surat pengantar dibuat dan didapat oleh mahasiswa?\n \n" \
 \
 \
     "/BE003. Siapa yang membuat surat pengantar magang? Dan dikirim kemana?\n \n" \
 \
 \
     "/BE004. Kenapa harus ada surat pengantar magang? \n\n" \
 \
 \
     "/BE005. Kenapa mahasiswa belum dapat surat pengantar? \n\n" \
 \
 \
     "/BE006. Dimana mahasiswa mendapatkan surat pengantar magang?\n \n" \
 \
 \
     "/BE007. Bagaimana persyaratan membuat Surat pengantar magang? \n\n" \
 \
 \
     "/BE008. Bagaimana apabila mahasiswa belum menerima Surat pengantar dalam waktu 7 hari (sejak dosen wali mengirim konfirmasi)? \n\n" \
 \
 \
     "/BE009. Bagaimana cara memberikan Surat Pengantar ke Perusahaan? \n\n" \
 \
 \
     "/BE010. Bagaimana cara revisi surat pengantar? \n\n" \
 \
 \
     "\n" \
 \
 \
     "ketik atau klik \"/B\" untuk kembali ke menu sebelumnya. "\
\
"\nketik atau klik \"/start\" untuk kembali ke menu utama. "

BE001 = "Apa itu Surat Pengantar Magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Surat Pengantar Magang adalah Surat permohonan izin kepada pimpinan perusahaan supaya berkenan menerima mahasiswa untuk magang di perusahaan tersebut."\
\
"\n" \
 \
"\n\n" \
 \
 \
"ketik atau klik \"/BE\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BE002 = "Kapan surat pengantar dibuat dan didapat oleh mahasiswa?"\
\
"\n" \
 \
"\n" \
 \
 \
"Surat pengantar dibuat disetiap hari senin dan rabu.\n" \
 \
 \
"\n" \
 \
 \
"Surat pengantar diberikan maksimal 3 hari kerja setelah mengajukan pembuatan surat"\
\
"\n" \
 \
"\n\n" \
 \
 \
"ketik atau klik \"/BE\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BE003 = "Siapa yang membuat surat pengantar magang? Dan dikirim kemana?"\
\
"\n" \
 \
"\n" \
 \
 \
"Surat Pengantar Magang dibuat oleh LKM dan dikirim ke perusahaan magang yang dituju"\
\
"\n" \
 \
"\n\n" \
 \
 \
"ketik atau klik \"/BE\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BE004 = "Kenapa harus ada surat pengantar magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Agar perusahaan bersedia menerima mahasiswa untuk magang di perusahaan mereka."\
\
"\n\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/BE\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BE005 = "Kenapa mahasiswa belum dapat surat pengantar?"\
\
"\n" \
 \
"\n" \
 \
 \
"Ada kemungkinan salah satu persyaratan pembuatan surat pengantar magang belum dilengkapi atau dilaksanakan oleh mahasiswa."\
\
"\n\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/BE\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BE006 = "Dimana mahasiswa mendapatkan surat pengantar magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Dikirim LKM ke email mahasiswa."\
\
"\n\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/BE\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BE007 = "Bagaimana persyaratan membuat Surat pengantar magang??"\
\
"\n" \
 \
"\n" \
 \
 \
"Surat pengantar magang akan dibuat oleh LKM apabila telah memenuhi kondisi berikut:\n\n" \
 \
 \
"1. Mahasiswa telah mengisi form pendafaran magang online melalui tautan: https://bit.ly/PengajuanPengantarMagangFITTelU \n \n" \
 \
 \
"2. Mahasiswa telah menghubungi dosen wali terkait persetujuan pengajuan magang \n\n" \
 \
 \
"3. Dosen wali telah menyetujui dan mengirimkan persetujuan magang ke LKM melalui tautan https://bit.ly/KonfirmasiMagangFIT\n\n" \
 \
 \
"4. Sudah mengikuti kuis KEPO MAGANG FIT\n \n"\
\
"Info lebih lanjut persyaratan membuat surat pengantar magang : https://magang-sas.telkomuniversity.ac.id/aturan-magang/ \n" \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/BE\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BE008 = "Bagaimana apabila mahasiswa belum menerima Surat pengantar dalam waktu 7 hari (sejak dosen wali mengirim konfirmasi)?"\
\
"\n" \
 \
"\n" \
 \
 \
"Silakan bertanya ke LKM Email:\n" \
 \
 \
"magang@tass.telkomuniversity.ac.id \n\n" \
 \
 \
"WA: https://wa.me/6285161415115"\
\
"\n\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/BE\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BE009 = "Bagaimana cara memberikan Surat Pengantar ke Perusahaan?"\
\
"\n" \
 \
"\n" \
 \
 \
"Surat pengantar diberikan kepada perusahaan dengan 3 cara:\n\n" \
 \
 \
"1. [direkomendasikan LKM]\nMahasiswa memberikan langsung ke perusahaan dengan membuat janji dengan tim HR atau tim unit yang dituju untuk memberikan surat pengantar magang yang dilampirkan dengan CV dan Transkrip Nilai\n\n" \
 \
 \
"2. [kurang direkomendasikan]\nMahasiswa memberikan melalui email ke perusahaan dengan menghubungi dan mengingatkan tim HR atau tim unit yang dituju untuk membaca email berisi surat pengantar magang yang dilampirkan dengan CV dan Transkrip Nilai\n\n" \
 \
 \
"3. [tidak direkomendasikan]\nMahasiswa memberikan melalui perusahaan pengiriman surat dan menghubungi tim HR atau tim unit yang dituju untuk menunggu paket berisi surat pengantar magang yang dilampirkan dengan CV dan Transkrip Nilai\n"\
\
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/BE\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BE010 = "Bagaimana cara revisi surat pengantar?"\
\
"\n" \
 \
"\n" \
 \
 \
"Apabila ada kekeliruan atau perubahan yang diinginkan perusahaan di dalam surat pengantar yang telah dikirim oleh LKM ke email mahasiswa, maka mahasiswa diperkenankan mengajukan revisi surat dengan cara membalas (reply) email yang berisi surat pengantar magang.\n\n" \
 \
 \
"Jelaskan dengan detail bagian surat yang perlu dihilangkan dan diganti, yang perlu ditambahkan atau dikurangi serta bagian yang perlu disesuaikan. Hasil revisi surat akan LKM FIT kirim melalui email kembali."\
\
"\n\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/BE\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "


BF = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
     "\n" \
 \
 \
     "/BF001. Apa itu penerimaan/diterima? \n\n" \
 \
 \
     "/BF002. Apa yang harus dilakukan mahasiswa setelah perusahaan menerima pengajuan magang? \n\n" \
 \
 \
     "/BF003. Apa yang harus dilakukan setelah memberikan/melaporkan penerimaan? \n\n" \
 \
 \
     "/BF004. Kapan mahasiswa melaporkan penerimaan? \n\n" \
 \
 \
     "/BF005. Dimana mahasiswa melaporkan bukti penerimaan magang?\n \n" \
 \
 \
     "/BF006. Bagaimana format bukti penerimaan dari perusahaan?\n \n" \
 \
 \
     "/BF007. Bagaimana jika diterima magang kurang dari 6 bulan?\n \n" \
 \
 \
     "\n" \
 \
 \
     "ketik atau klik \"/B\" untuk kembali ke menu sebelumnya. "\
\
"\nketik atau klik \"/start\" untuk kembali ke menu utama. "

BF001 = "Apa itu penerimaan/diterima?"\
\
"\n" \
 \
"\n" \
 \
 \
"Penerimaan magang adalah status yang diberikan oleh perusahaan/industri sebagai tanda " \
 \
 \
"bahwa mahasiswa diperkenankan melakukan magang di perusahaan tersebut."\
\
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/BF\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BF002 = "Apa yang harus dilakukan mahasiswa setelah perusahaan menerima pengajuan magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Mahasiswa melaporkan bukti penerimaan magang dengan mengisi link google form berikut ini:\nhttps://bit.ly/PenerimaanMagangFIT \n" \
        "\n\n[ Jangan lupa menggunakan akun SSO ] \n" \
 \
\
 \
" \n" \
 \
 \
"Setelah mengisi form penerimaan magang, mahasiswa melanjutkan magang dan bukti penerimaan dari perusahaan dikirim ke dosen wali (email/WA) sebagai informasi."\
\
"\n" \
 \
"\n\n" \
 \
 \
"ketik atau klik \"/BF\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BF003 = "Apa yang harus dilakukan setelah memberikan/melaporkan penerimaan?"\
\
"\n" \
 \
"\n" \
 \
 \
"Apabila mahasiswa sudah memberikan penerimaan ke LKM, maka mahasiswa diperkenankan untuk magang dan mendapatkan dosen pembimbing magang."\
\
"\n" \
 \
"\n\n" \
 \
 \
"ketik atau klik \"/BF\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BF004 = "Kapan mahasiswa melaporkan penerimaan?"\
\
"\n" \
 \
"\n" \
 \
 \
"Segera setelah mendapatkan jawaban penerimaan dari perusahaan yang dituju."\
\
"\n" \
 \
"\n\n" \
 \
 \
"ketik atau klik \"/BF\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BF005 = "Dimana mahasiswa melaporkan bukti penerimaan magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Mahasiswa dapat melaporkan bukti penerimaan dan penolakan magang dengan mengisi link google form berikut ini:  \nhttps://bit.ly/PenerimaanMagangFIT " \
        "\n\n[ Jangan lupa menggunakan akun SSO ] \n" \
 \
 \
        "\n" \
 \
"\n\n" \
 \
 \
"ketik atau klik \"/BF\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BF006 = "Bagaimana format bukti penerimaan dari perusahaan?"\
\
"\n" \
 \
"\n" \
 \
 \
"Penerimaan magang adalah status yang diberikan oleh perusahaan/industri sebagai tanda " \
 \
 \
"bahwa mahasiswa diperkenankan melakukan magang di perusahaan tersebut. Berbentuk tertulis yang diperoleh dari sumber-sumber berikut (pilih 1):\n\n" \
 \
 \
" - Situs Web perusahaan (pdf)\n" \
 \
 \
" - Email perusahaan (pdf)\n" \
 \
 \
" - Aplikasi perusahaan (Screenshoot-JPG/PNG)"\
\
"\n" \
 \
"\n\n" \
 \
 \
"ketik atau klik \"/BF\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BF007 = "Bagaimana jika diterima magang kurang dari 6 bulan?"\
\
"\n" \
 \
"\n" \
 \
 \
"Apabila magang kurang dari 6 bulan, kami rekomendasikan hal berikut:\n\n" \
 \
 \
"1. Silakan untuk mengajukan kembali magang di tempat yang sama hingga genap 6 bulan (LKM bersedia membantu membuat kembali surat pengantar)\n \n" \
 \
 \
"2. Apabila perusahaan tidak bersedia, silakan cari lokasi magang di tempat lain yang bersedia menerima magang selama sisa bulan yang kamu butuhkan agar genap menjadi 6 bulan. (LKM bersedia membantu membuat kembali surat pengantar) \n\n" \
 \
 \
"3. Apabila sulit mendaptkan perusahaannya, silakan untuk mengajukan magang di prodi ya (lapor ke kaprodi dan dosen wali. LKM bersedia membantu membuat kembali surat pengantar)\n\n" \
 \
 \
"Dari seluruh rekomendasi tersebut, kerena magang di 2 perusahaan, maka dokumen magang dari perusahaan (laporan dengan ttd pengesahan pbb lapangan ada 2, presensi perusahaan ada 2, nilai pembimbing lapangan ada 2, dan sertifikat magang ada 2). \n \n"\
\
"Semoga lancar magangnya...  \n" \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"Info lebih lanjut jika diterima magang kurang dari 6 bulan : https://magang-sas.telkomuniversity.ac.id/jenis-jenis-magang/ \n"\
\
"\n" \
 \
"\n\n" \
 \
 \
"ketik atau klik \"/BF\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "



BG = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
     "\n" \
 \
 \
     "/BG001. Apa itu penolakan/ditolak? \n\n" \
 \
 \
     "/BG002. Apa yang harus dilakukan setelah ditolak oleh perusahaan? \n\n" \
 \
 \
     "/BG003. Apa yang harus dilakukan setelah melaporkan penolakan magang?\n \n" \
 \
 \
     "/BG004. Kapan mahasiswa melaporkan penolakan magang?\n \n" \
 \
 \
     "/BG005. Dimana mahasiswa melaporkan bukti penolakan magang? \n\n" \
 \
 \
     "/BG006. Bagaimana format bukti penolakan dari perusahaan? \n\n" \
 \
 \
     "/BG007. Bagaimana saat perusahaan menolak permintaan magang?\n \n" \
 \
 \
     "\n" \
 \
 \
     "ketik atau klik \"/B\" untuk kembali ke menu sebelumnya. "\
\
"\nketik atau klik \"/start\" untuk kembali ke menu utama. "

BG001 = "Apa itu penolakan/ditolak?"\
\
"\n" \
 \
"\n" \
 \
 \
"Penolakan magang adalah status yang diberikan oleh perusahaan/industri sebagai tanda bahwa " \
 \
 \
"mahasiswa tidak diperkenankan melakukan magang dengan alasan tertentu."\
\
"\n" \
 \
"\n\n" \
 \
 \
"ketik atau klik \"/BG\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BG002 = "Apa yang harus dilakukan setelah ditolak oleh perusahaan?"\
\
"\n" \
 \
"\n" \
 \
 \
"Apabila mahasiswa ditolak oleh perusahaan, silakan untuk melaporkan penolakan ke LKM melalui" \
 \
 \
" tautan berikut:\nhttps://bit.ly/PenerimaanMagangFIT " \
        "\n\n[ Jangan lupa menggunakan akun SSO ] \n" \
 \
 \
        "\n" \
 \
"\n\n" \
 \
 \
"ketik atau klik \"/BG\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BG003 = "Apa yang harus dilakukan setelah melaporkan penolakan magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Apabila mahasiswa sudah memberikan penolakan ke LKM, silakan untuk mengulangi proses pendaftaran dari awal."\
\
"\n" \
 \
"\n\n" \
 \
 \
"ketik atau klik \"/BG\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BG004 = "Kapan mahasiswa melaporkan penolakan magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Segera setelah mendapatkan jawaban penolakan magang dari perusahaan yang dituju."\
\
"\n" \
 \
"\n\n" \
 \
 \
"ketik atau klik \"/BG\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BG005 = "Dimana mahasiswa melaporkan bukti penolakan magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Mahasiswa dapat melaporkan bukti penerimaan dan penolakan magang dengan mengisi link google form berikut ini:\nhttps://bit.ly/PenerimaanMagangFIT " \
        "\n\n[ Jangan lupa menggunakan akun SSO ] \n" \
 \
 \
        "\n" \
 \
"\n\n" \
 \
 \
"ketik atau klik \"/BG\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BG006 = "Bagaimana format bukti penolakan dari perusahaan?"\
\
"\n" \
 \
"\n" \
 \
 \
"Berbentuk tertulis yang diperoleh dari sumber-sumber berikut (pilih 1):\n\n" \
 \
 \
" - Situs Web perusahaan (pdf)\n" \
 \
 \
" - Email perusahaan (pdf)\n" \
 \
 \
" - Aplikasi perusahaan (Screenshoot-JPG/PNG)"\
\
"\n" \
 \
"\n\n" \
 \
 \
"ketik atau klik \"/BG\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BG007 = "Bagaimana saat perusahaan menolak permintaan magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Setelah mengisi form penerimaan/penolakan magang, mahasiswa harus mengulang proses pengajuan magang dari tahap ke-1. Bukti penolakan dari perusahaan dikirim ke dosen wali (email/WA) sebagai informasi."\
\
"\n" \
 \
"\n\n" \
 \
 \
"ketik atau klik \"/BG\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "


BH = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
     "\n" \
 \
 \
     "/BH001. Apa itu pengunduran diri/dipulangkan? \n\n" \
 \
 \
     "/BH002. Apa yang harus dilakukan setelah undur diri/dipulangkan oleh perusahaan?\n \n" \
 \
 \
     "/BH003. Apa yang harus dilakukan setelah melaporkan undur diri/dipulangkan? \n\n" \
 \
 \
     "/BH004. Kapan mahasiswa melaporkan undur diri/dipulangkan? \n\n" \
 \
 \
     "/BH005. Bagaimana format bukti undur diri/dipulangkan dari perusahaan? \n\n" \
 \
 \
     "/BH006. Bagaimana saat mahasiswa dipulangkan dari perusahaan? \n\n" \
 \
 \
     "/BH007. Bagaimana saat mahasiswa mengundurkan diri dari perusahaan?\n \n" \
 \
 \
     "\n" \
 \
 \
     "ketik atau klik \"/B\" untuk kembali ke menu sebelumnya. "\
\
"\nketik atau klik \"/start\" untuk kembali ke menu utama. "

BH001 = "Apa itu pengunduran diri/dipulangkan?"\
\
"\n" \
 \
"\n" \
 \
 \
"Undur diri adalah status dimana mahasiswa menyatakan undur diri baik dari tahap pendaftaran atau di saat pelaksanaan magang di perusahaan.\n" \
 \
 \
"\n" \
 \
 \
"Sedangkan dipulangkan adalah status dimana mahasiswa dipulangkan oleh perusahaan ke pihak kampus atas dasar alasan tertentu."\
\
"\n" \
 \
"\n\n" \
 \
 \
"ketik atau klik \"/BH\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BH002 = "Apa yang harus dilakukan setelah undur diri/dipulangkan oleh perusahaan?"\
\
"\n" \
 \
"\n" \
 \
 \
"Apabila mahasiswa undur diri/dipulangkan oleh perusahaan, silakan untuk melaporkan ke " \
 \
 \
"LKM melalui tautan berikut: https://bit.ly/PenerimaanMagangFIT " \
        "\n\n[ Jangan lupa menggunakan akun SSO ] \n" \
 \
 \
        "\n" \
 \
"\n\n" \
 \
 \
"ketik atau klik \"/BH\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BH003 = "Apa yang harus dilakukan setelah melaporkan undur diri/dipulangkan?"\
\
"\n" \
 \
"\n" \
 \
 \
"Apabila mahasiswa sudah memberikan undur diri/dipulangkan ke LKM, silakan untuk mengulangi proses pendaftaran dari awal."\
\
"\n" \
 \
"\n\n" \
 \
 \
"ketik atau klik \"/BH\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BH004 = "Kapan mahasiswa melaporkan undur diri/dipulangkan?"\
\
"\n" \
 \
"\n" \
 \
 \
"Segera setelah mendapatkan pemberitahuan jika dipulangkan magang oleh perusahaan yang terkait atau mengundurkan diri dari perusahaan yang dituju. "\
\
"\n" \
 \
"\n\n" \
 \
 \
"ketik atau klik \"/BH\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BH005 = "Bagaimana format bukti undur diri/dipulangkan dari perusahaan?"\
\
"\n" \
 \
"\n" \
 \
 \
"Berbentuk tertulis yang diperoleh dari sumber-sumber berikut (pilih 1):\n\n" \
 \
 \
" - Situs Web perusahaan (pdf)\n" \
 \
 \
" - Email perusahaan (pdf)\n" \
 \
 \
" - Aplikasi perusahaan (Screenshoot-JPG/PNG) "\
\
"\n" \
 \
"\n\n" \
 \
 \
"ketik atau klik \"/BH\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BH006 = "Bagaimana saat mahasiswa dipulangkan dari perusahaan?"\
\
"\n" \
 \
"\n" \
 \
 \
"Setelah mengisi form penerimaan magang, mahasiswa harus mengulang proses pengajuan magang dari tahap ke-1. Bukti persetujuan dipulangkan dari perusahaan dikirim ke dosen wali (email/WA) sehingga dosen wali dapat mengirim konfirmasi persetujuan magang berikutnya."\
\
"\n" \
 \
"\n\n" \
 \
 \
"ketik atau klik \"/BH\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BH007 = "Bagaimana saat mahasiswa mengundurkan diri dari perusahaan?"\
\
"\n" \
 \
"\n" \
 \
 \
"Setelah mengisi form penerimaan magang, mahasiswa harus mengulang proses pengajuan magang dari tahap ke-1. Bukti persetujuan undur diri dari perusahaan dikirim ke dosen wali (email/WA) sehingga dosen wali dapat mengirim konfirmasi persetujuan magang berikutnya. "\
\
"\n" \
 \
"\n\n" \
 \
 \
"ketik atau klik \"/BH\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "


BI = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
     "\n" \
 \
 \
     "/BI001. Kapan kuis “KEPO MAGANG FIT” dapat diakses? \n\n" \
 \
 \
     "/BI002. Dimana dapat mengakses kuis “KEPO MAGANG FIT”? \n\n" \
 \
 \
     "\n" \
 \
 \
     "ketik atau klik \"/B\" untuk kembali ke menu sebelumnya. "\
\
"\nketik atau klik \"/start\" untuk kembali ke menu utama. "

BI001 = "Kapan kuis “KEPO MAGANG FIT” dapat diakses?"\
\
"\n" \
 \
"\n" \
 \
 \
"Kuis “KEPO MAGANG FIT” dapat diakses Setelah mahasiswa mendapatkan materi sosialisasi magang.\n"\
\
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/BI\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

BI002 = "Dimana dapat mengakses kuis “KEPO MAGANG FIT”?"\
\
"\n" \
 \
"\n" \
 \
 \
"Kuis dapat diakses di Google Classroom yang diambil oleh mahasiswa di semester berjalan magang.\n" \
 \
 \
"\n" \
 \
 \
"Google Classroom (Tahun Ajaran Masing-Masing):\n" \
 \
 \
"( https://magang-sas.telkomuniversity.ac.id/en/lkm-google-classroom )\n\n\n" \
 \
 \
"ketik atau klik \"/BI\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "


C = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
    "\n" \
 \
 \
    "\n/C001. Apa yang mahasiswa lakukan selama magang selain melakukan pekerjaan magang itu sendiri? \n" \
 \
 \
    "\n/C002. Apakah ada aturan khusus dalam menyusun pelaporan aktivitas harian magang? \n" \
 \
 \
    "\n/C003. Dimana mahasiswa dapat mengakses inforrmasi terbaru apabila terdapat perubahan aturan? \n" \
 \
 \
    "\n/C004. Bagaimana saat mahasiswa dipulangkan dari perusahaan? \n" \
 \
 \
    "\n/C005. Bagaimana jika magang dilaksanakan kurang dari 6 bulan akibat dari aturan perusahaan? \n" \
 \
 \
    "\n/C006. Bagaimana jika magang dilaksanakan selama 12 bulan? \n" \
 \
 \
    "\n/C007. Bagaimana jika mahasiswa sudah lulus kuliah namun masih magang? \n" \
 \
 \
    "\n/C008. Bagaimana jika dalam waktu 1 minggu, Daftar Rekap Kegiatan Magang masih belum ter-update? \n" \
 \
 \
    "\n" \
 \
 \
    "\nketik atau klik \"/start\" untuk kembali ke menu utama."

C001 = "Apa yang mahasiswa lakukan selama magang selain melakukan pekerjaan magang itu sendiri? "\
\
"\n" \
 \
"\n" \
 \
 \
"Mahasiswa harus melengkapi lembar aktivitas harian magang dan membuat laporan. \n" \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/C\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

C002 = "Apakah ada aturan khusus dalam menyusun pelaporan aktivitas harian magang? "\
\
"\n" \
 \
"\n" \
 \
 \
"Ya, silakan klik tautan dibawah ini:\n \n" \
 \
 \
" https://bit.ly/AktifitasHarianMagangFIT " \
       "\n\n[ Jangan lupa menggunakan akun SSO ] \n" \
 \
 \
 \
       "\n" \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/C\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

C003 = "Dimana mahasiswa dapat mengakses inforrmasi terbaru apabila terdapat perubahan aturan?  \n\n" \
 \
 \
       "1. Website:  \n" \
 \
 \
       "( http://magang-sas.telkomuniversity.ac.id ) \n" \
 \
 \
       "\n 2. Instagram:\n" \
 \
 \
       "( https://www.instagram.com/magang.fit )\n" \
 \
 \
       "\n 3. Google Classroom (Tahun Ajaran Masing-Masing):\n" \
 \
 \
       "( https://magang-sas.telkomuniversity.ac.id/en/lkm-google-classroom )\n"\
\
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/C\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

C004 = "Bagaimana saat mahasiswa dipulangkan dari perusahaan? "\
\
"\n" \
 \
"\n" \
 \
 \
"Setelah mengisi form penerimaan/penolakan magang, mahasiswa harus mengulang proses pengajuan magang dari tahap ke-1. \n \nBukti persetujuan dipulangkan dari perusahaan dikirim ke dosen wali (email/WA) sehingga dosen wali dapat mengirim konfirmasi persetujuan magang berikutnya. \n " \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/C\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

C005 = "Bagaimana jika magang dilaksanakan kurang dari 6 bulan akibat dari aturan perusahaan?  "\
\
"\n" \
 \
"\n" \
 \
 \
"Bila magang dilaksanakan kurang dari 6 bulan akibat dari aturan perusahaan, maka mahasiswa direkomendasikan melanjutkan magang di FIT untuk menggenapkan magang menjadi 6 bulan. \n \n" \
 \
 \
"\n" \
 \
 \
"ketik atau klik \"/C\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

C006 = "Bagaimana jika magang dilaksanakan selama 12 bulan? \n\n" \
 \
 \
       "Bila magang dilaksanakan 12 bulan di perusahaan, maka :  \n\n" \
 \
 \
       "1. Prodi akan melakukan ekivalensi semua nilai mata kuliah sama dengan nilai magang pada 2 semester, yakni semester 5 dan 6  (untuk D3), atau semester 7 dan 8 (untuk Sarjana Terapan)\n" \
 \
 \
       "\n2. Perusahaan harus mengeluarkan 2 kali nilai yakni nilai_1 (untuk 6 bulan pertama) dan nilai_2 (untuk 6 bulan terakhir).\n\n" \
 \
 \
       "\n" \
 \
 \
       "ketik atau klik \"/C\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
       "ketik atau klik \"/start\" untuk kembali ke menu utama. "

C007 = "Bagaimana jika mahasiswa sudah lulus kuliah namun masih magang? \n\n" \
 \
 \
       "Apabila mahasiswa sudah lulus kuliah namun masih magang, maka: \n\n" \
 \
 \
       "1. Nilai yang dimasukkan ke igracias diambil dari Nilai Pembimbing Lapangan saja\n" \
 \
 \
       "\n2. Mahasiswa harus melanjutkan magang walau sudah lulus kuliah dengan catatan : ijazah dan berkas kelulusan lainnya diberikan setelah selesai magang 12 bulan. Selesai magang ditandai dengan adanya Sertifikat / Surat Selesai magang dari perusahaan. \n\n" \
 \
 \
       "\n" \
 \
 \
       "ketik atau klik \"/C\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
       "ketik atau klik \"/start\" untuk kembali ke menu utama. "

C008 = "Bagaimana jika dalam waktu 1 minggu, Daftar Rekap Kegiatan Magang masih belum ter-update? \n"\
\
"\n" \
 \
"\n" \
 \
 \
"Apabila dalam waktu 1 minggu masih belum ter-update silakan melakukan konfirmasi kepada LKM melalui email ke magang@tass.telkomuniversity.ac.id atau pesan WA https://wa.me/6285161415115 \n \n" \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/C\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "


D = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Sub Kategori Di bawah ini :\n \n" \
 \
 \
    "/DA. Pembimbing Lapangan \n" \
 \
 \
    "\n/DB. Pembimbing Akademik \n" \
 \
 \
    "\n" \
 \
 \
    "\n" \
 \
 \
    "ketik atau klik \"/start\" untuk kembali ke menu sebelumnya. \n"


DA = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
     "\n" \
 \
 \
     "/DA001. Dimana pembimbing lapangan menginput nilai untuk mahasiswa magang?  \n" \
 \
 \
     "\n/DA002. Bagaimana alur presentasi online kepada pembimbing lapangan?  \n" \
 \
 \
     "\n/DA003. Bagaimana alur presentasi onsite kepada pembimbing lapangan?  \n" \
 \
 \
     "\n" \
 \
 \
     "\nketik atau klik \"/D\" untuk kembali ke menu sebelumnya."\
\
"\nketik atau klik \"/start\" untuk kembali ke menu utama. "

DA001 = "Dimana pembimbing lapangan menginput nilai untuk mahasiswa magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Pembimbing lapangan dapat menginput nilai magang mahasiswa jika berhalangan memberikan nilai secara tertulis" \
 \
 \
" di form nilai dengan mengakses link google form berikut :   \n\n" \
 \
 \
"https://bit.ly/NilaiMagangOnlineFIT" \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"Form tersebut diisi oleh pembimbing lapangan. Setelah form terisi, maka akan ada respon ke email pembimbing lapangan. " \
 \
 \
"Silakan pembimbing lapangan untuk meneruskan (forward) email tersebut kepada mahasiswa yang dinilai. \n\n" \
 \
 \
 \
"ketik atau klik \"/DA\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

DA002 = "Bagaimana alur presentasi online kepada pembimbing lapangan? "\
\
"\n" \
 \
"\n" \
 \
 \
"1. Mahasiswa persentasi melalui aplikasi online meeting (Google Meet, Zoom, Skype) \n \n" \
 \
 \
"2. Pembimbing lapangan mengisi nilai pada tautan : bit.ly/NilaiMagangOnlineFIT \n \n" \
 \
 \
"3. Pembimbing lapangan membubuhkan tandatangan dan cap digital perusahaan pada lembar pengesahan magang dan lembar aktivitas harian. \n \n" \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/DA\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

DA003 = "Bagaimana alur presentasi onsite kepada pembimbing lapangan? "\
\
"\n" \
 \
"\n" \
 \
 \
"1. Mahasiswa persentasi secara tatap muka (langsung)  \n \n" \
 \
 \
"2. Pembimbing lapangan mengisi dokumen nilai magang dan membubuhkan tanda tangan dan cap. Form dapat diunduh di http://bit.ly/DokumenKpMagangFIT \n \n" \
 \
 \
"3. Pembimbing lapangan membubuhkan tandatangan dan cap perusahaan pada lembar pengesahan magang dan lembar aktivitas harian.  \n \n" \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/DA\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "



DB = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
     "\n" \
 \
 \
     "/DB001. Dimana pembimbing akademik menginput nilai untuk mahasiswa?   \n" \
 \
 \
     "\n/DB002. Bagaimana alur presentasi online pembimbing akademik? \n" \
 \
 \
     "\n/DB003. Bagaimana alur presentasi onsite pembimbing akademik?   \n" \
 \
 \
     "\n" \
 \
 \
     "\nketik atau klik \"/D\" untuk kembali ke menu sebelumnya."\
\
"\nketik atau klik \"/start\" untuk kembali ke menu utama. "

DB001 = "Dimana pembimbing akademik menginput nilai untuk mahasiswa?  "\
\
"\n" \
 \
"\n" \
 \
 \
"Pembimbing akademik dapat menginput nilai magang mahasiswa jika berhalangan memberikan nilai secara tertulis " \
 \
 \
"di form nilai dengan mengakses link google form berikut:   \n\n" \
 \
 \
"https://bit.ly/NilaiMagangDosenOnline" \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"Form tersebut diisi oleh pembimbing akademik. Setelah form terisi, maka akan ada respon ke email pembimbing akademik. " \
 \
 \
"Silakan pembimbing akademik untuk meneruskan (forward) email tersebut kepada mahasiswa yang dinilai.  \n\n" \
 \
 \
 \
"ketik atau klik \"/DB\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

DB002 = "Bagaimana alur presentasi online pembimbing akademik?  "\
\
"\n" \
 \
"\n" \
 \
 \
"1. Mahasiswa persentasi melalui aplikasi online meeting (Google Meet, Zoom, Skype) \n \n" \
 \
 \
"2. Pembimbing memberikan nilai ke tautan: bit.ly/NilaiMagangDosenOnline serta mengirim ke mahasiswa ybs\n \n" \
 \
 \
"3. Pembimbing akademik membubuhkan tanda tangan pada lembar pengesahan magang \n \n" \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/DB\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

DB003 = "Bagaimana alur presentasi online pembimbing akademik?  "\
\
"\n" \
 \
"\n" \
 \
 \
"1. Mahasiswa persentasi secara tatap muka (langsung)\n \n" \
 \
 \
"2. Pembimbing akademik mengisi dokumen lembar penilaian akhir magang dan membubuhkan tanda tangan. Form dapat diunduh di http://bit.ly/DokumenKpMagangFIT  \n \n" \
 \
 \
"3. Pembimbing lapangan membubuhkan tandatangan pada lembar pengesahan magang  \n \n" \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/DB\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "



E = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Sub Kategori Di bawah ini :\n \n" \
 \
 \
    "/EA. Prosedur Pengumpulan Berkas Magang \n" \
 \
 \
    "\n/EB. Lokasi Pengumpulan Berkas Magang\n" \
 \
 \
    "\n/EC. Batas Waktu Pengumpulan Berkas Magang \n" \
 \
 \
    "\n/ED. Sanksi Keterlambatan Pengumpulan Berkas Magang\n" \
 \
 \
    "\n/EE. Berkas/Dokumen Magang\n" \
 \
 \
    "\n" \
 \
 \
    "\n" \
 \
 \
    "ketik atau klik \"/start\" untuk kembali ke menu sebelumnya. \n"



EA = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
     "\n" \
 \
 \
     "/EA001. Bagaimana prosedur pengumpulan berkas akhir magang? \n" \
 \
 \
     "\n" \
 \
 \
     "\nketik atau klik \"/E\" untuk kembali ke menu sebelumnya."\
\
"\nketik atau klik \"/start\" untuk kembali ke menu utama. "

EA001 = "Bagaimana prosedur pengumpulan berkas akhir magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Info Lebih Lanjut Tentang Prosedur pengumpulan berkas akhir magang : \n\n" \
 \
 \
"http://bit.ly/KumpulBerkasAkhirKpMagangFIT  " \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/EA\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "



EB = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
     "\n" \
 \
 \
     "/EB001. Dimana lokasi pengumpulan berkas akhir magang? \n" \
 \
 \
     "\n" \
 \
 \
     "\nketik atau klik \"/E\" untuk kembali ke menu sebelumnya."\
\
"\nketik atau klik \"/start\" untuk kembali ke menu utama. "

EB001 = "Dimana lokasi pengumpulan berkas akhir magang?  "\
\
"\n" \
 \
"\n" \
 \
 \
"Lokasi Pengumpulan berkas akhir magang, dikumpulkan di classroom magang tahun ajaran masing-masing dan Untuk Kode Kelas Classroom dapat dilihat di: \n\n" \
 \
 \
"https://magang-sas.telkomuniversity.ac.id/en/lkm-google-classroom" \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/EB\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "



EC = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
     "\n" \
 \
 \
     "/EC001. Kapan batas pengumpulan berkas akhir magang? \n" \
 \
 \
     "\n" \
 \
 \
     "\nketik atau klik \"/E\" untuk kembali ke menu sebelumnya."\
\
"\nketik atau klik \"/start\" untuk kembali ke menu utama. "

EC001 = "Kapan batas pengumpulan berkas akhir magang? "\
\
"\n" \
 \
"\n" \
 \
 \
"Batas pengumpulan berkas hingga pada akhir periode magang, dapat dilihat pada agenda magang di link berikut : \n\n" \
 \
 \
"https://drive.google.com/drive/folders/14w639_FFKyF1_HMfV3IhhzQQjRpqNOwf" \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/EC\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "



ED = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
     "\n" \
 \
 \
     "/ED001. Apakah ada sanksi keterlambatan pengumpulan berkas akhir magang?  \n" \
 \
 \
     "\n" \
 \
 \
     "\nketik atau klik \"/E\" untuk kembali ke menu sebelumnya."\
\
"\nketik atau klik \"/start\" untuk kembali ke menu utama. "

ED001 = "Apakah ada sanksi keterlambatan pengumpulan berkas akhir magang?  "\
\
"\n" \
 \
"\n" \
 \
 \
"Sebagai sanksi keterlambatan, nilai yang diupload di google classroom dan igracias dikurangi 20 poin. \n\n" \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/ED\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "



EE = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
     "\n" \
 \
 \
     "/EE001. Apa saja berkas yang dikumpulkan ke Google Classroom? \n" \
 \
 \
     "\n /EE002. Apakah ada aturan untuk penyusunan laporan magang? \n" \
 \
 \
     "\n /EE003. Apa saja status keterangan yang akan diberikan di Classroom? \n" \
 \
 \
     "\n /EE004. Apakah tanda tangan wajib basah? \n" \
 \
 \
     "\n /EE005. Dimana mahasiswa dapat mengunduh berkas magang? \n" \
 \
 \
     "\n /EE006. Bagaimana bentuk perusahaan mengeluarkan sertifikat? \n" \
 \
 \
     "\n /EE007. Bagaimana mahasiswa tahu berkas sudah lengkap? \n " \
 \
 \
     "\nketik atau klik \"/E\" untuk kembali ke menu sebelumnya."\
\
"\nketik atau klik \"/start\" untuk kembali ke menu utama. "

EE001 = "Apa saja berkas yang dikumpulkan ke Google Classroom?  "\
\
"\n" \
 \
"\n" \
 \
 \
"Info lebih lanjut pengumpulan berkas pada Google Classroom :  \n\n" \
 \
 \
"https://magang-sas.telkomuniversity.ac.id/cara-pengumpulan-berkas-kp-dan-magang-melalui-classroom-lkm/ " \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"Unduh dokumen magang di tautan:\n\n " \
 \
 \
"http://bit.ly/DokumenKpMagangFIT" \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/EE\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

EE002 = "Apakah ada aturan untuk penyusunan laporan magang?  "\
\
"\n" \
 \
"\n" \
 \
 \
"Silakan klik tautan dibawah ini:  \n\n" \
 \
 \
"https://bit.ly/LaporanMagangFIT  " \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/EE\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

EE003 = "Apa saja status keterangan yang akan diberikan di Classroom? "\
\
"\n" \
 \
"\n" \
 \
 \
"1. Belum lengkap (revisi): memperbaiki berkas yang kurang lengkap dan memperbaiki sesuai keterangan revisi di kolom komentar \n \n" \
 \
 \
"2. Lengkap: mahasiswa menunggu nilai keluar di google classroom dan igracias \n \n" \
 \
 \
"3. Lengkap terlambat. \n \n" \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/EE\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

EE004 = "Apakah tanda tangan wajib basah?"\
\
"\n" \
 \
"\n" \
 \
 \
"Tidak, bisa tanda tangan digital " \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/EE\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

EE005 = "Dimana mahasiswa dapat mengunduh berkas magang? "\
\
"\n" \
 \
"\n" \
 \
 \
"Klik tautan dibawah ini:   \n\n" \
 \
 \
"http://bit.ly/DokumenKpMagangFIT  " \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/EE\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

EE006 = "Bagaimana bentuk perusahaan mengeluarkan sertifikat? "\
\
"\n" \
 \
"\n" \
 \
 \
"1. Sertifikat asli (hardfile)   \n\n" \
 \
 \
"2. E-sertifikat   \n \n" \
 \
 \
"3. Surat asli/scan\n \n" \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/EE\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

EE007 = "Bagaimana mahasiswa tahu berkas sudah lengkap?   "\
\
"\n" \
 \
"\n" \
 \
 \
"1. LKM memeriksa kelengkapan berkas   \n \n" \
 \
 \
"2. LKM memberi keterangan pada comment di Google Classroom  \n \n" \
 \
 \
"3. LKM menginput nilai di Google Classroom \n \n" \
 \
 \
"4. Assignment di-return oleh LKM \n \n" \
 \
 \
"5. Mahasiswa tidak diperkenankan untuk resubmit berkas jika sudah dinyatakan lengkap \n" \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/EE\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "


F = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Sub Kategori Di bawah ini :\n \n" \
 \
 \
    "/FA. Nilai Magang \n" \
 \
 \
    "/FB. Sanksi\n" \
 \
 \
    "/FC. Kuesioner Magang\n" \
 \
 \
    "\n" \
 \
 \
    "\n" \
 \
 \
    "ketik atau klik \"/start\" untuk kembali ke menu sebelumnya. \n"



FA = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
     "\n" \
 \
 \
     "/FA001. Apa isi dari lembar penilaian akhir magang?\n" \
 \
 \
     "\n/FA002. Kapan pemberitahuan nilai magang?\n" \
 \
 \
     "\n/FA003. Kapan batas input nilai magang?\n" \
 \
 \
     "\n/FA004. Dimana nilai magang diinputkan?\n" \
 \
 \
     "\n" \
 \
 \
     "\nketik atau klik \"/F\" untuk kembali ke menu sebelumnya."\
\
"\nketik atau klik \"/start\" untuk kembali ke menu utama. "

FA001 = "Apa isi dari lembar penilaian akhir magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Akumulasi nilai pembimbing lapangan dan pembimbing akademik." \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/FA\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

FA002 = "Kapan pemberitahuan nilai magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Nilai magang diberitahukan di Classroom saat berkas yang dikumpulkan sudah lengkap tidak ada revisi. Lalu akan di-submit di igracias setelahnya oleh LAA." \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/FA\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

FA003 = " Kapan batas input nilai magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Batas input nilai magang dapat dilihat di agenda magang dan akan diberitahukan batas akhirnya di pengumuman Classroom." \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/FA\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

FA004 = "Dimana nilai magang diinputkan?"\
\
"\n" \
 \
"\n" \
 \
 \
"Google Classroom LKM FIT:\n https://bit.ly/GoogleClassroomGenap21-22 " \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"Igracias:\n https://igracias.telkomuniversity.ac.id" \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/FA\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "



FB = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
     "\n" \
 \
 \
     "/FB001. Apa saja sanksi magang?\n" \
 \
 \
     "\n" \
 \
 \
     "\nketik atau klik \"/F\" untuk kembali ke menu sebelumnya."\
\
"\nketik atau klik \"/start\" untuk kembali ke menu utama. "

FB001 = "Apa saja sanksi magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Sanksi keterlambatan pengumpulan berkas magang adalah nilai yang diupload di Google Classroom dan igracias dikurangi 20 poin." \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/FB\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "



FC = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
     "\n" \
 \
 \
     "/FC001. Apa itu kuesioner magang? \n" \
 \
 \
     "\n/FC002. Dimana pengisian kuesioner magang?\n" \
 \
 \
     "\n" \
 \
 \
     "\nketik atau klik \"/F\" untuk kembali ke menu sebelumnya."\
\
"\nketik atau klik \"/start\" untuk kembali ke menu utama. "

FC001 = "Apa itu kuesioner magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Kuesioner evaluasi magang adalah dokumen yang bertujuan untuk mengetahui kepuasan perusahaan terhadap kinerja alumni atau mahasiswa Fakultas Ilmu Terapan selama kerja dan magang di perusahaan." \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/FC\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

FC002 = "Dimana pengisian kuesioner magang?"\
\
"\n" \
 \
"\n" \
 \
 \
"Kuesioner dapat di akses melalui akun SSO dan berikut link Kuesioner : \nbit.ly/evaluasikuesionermagang-fit-telu " \
 \
 \
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/FC\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "



G = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Sub Kategori Di bawah ini :\n \n" \
 \
 \
    "/GA. Website LKM FIT\n" \
 \
 \
    "/GB. Instagram LKM FIT\n" \
 \
 \
    "/GC. Email LKM FIT\n" \
 \
 \
    "/GD. Whatsapp Chat LKM FIT\n" \
 \
 \
    "/GE. Google Classroom LKM FIT \n" \
 \
 \
    "\n" \
 \
 \
    "\n" \
 \
 \
    "ketik atau klik \"/start\" untuk kembali ke menu sebelumnya. \n"



GA = "Website LKM FIT :\n https://magang-sas.telkomuniversity.ac.id/"\
\
"\n" \
 \
 \
"\n" \
 \
 \
"ketik atau klik \"/G\" untuk kembali ke menu sebelumnya. "\
\
"\nketik atau klik \"/start\" untuk kembali ke menu utama. "



GB = "Instagram LKM FIT :\n https://www.instagram.com/magang.fit/"\
\
"\n" \
 \
 \
"\n" \
 \
 \
"ketik atau klik \"/G\" untuk kembali ke menu sebelumnya. "\
\
"\nketik atau klik \"/start\" untuk kembali ke menu utama. "


GC = "Email LKM FIT :\n magang@tass.telkomuniversity.ac.id"\
\
"\n" \
 \
 \
"\n" \
 \
 \
"ketik atau klik \"/G\" untuk kembali ke menu sebelumnya. "\
\
"\nketik atau klik \"/start\" untuk kembali ke menu utama. "


GD = "Whatsapp LKM FIT :\n \n 085161415115 atau klik dibawah ini :\n https://wa.me/6285161415115"\
\
"\n" \
 \
 \
"\n" \
 \
 \
"ketik atau klik \"/G\" untuk kembali ke menu sebelumnya. "\
\
"\nketik atau klik \"/start\" untuk kembali ke menu utama. "



GE = "Silahkan ketik atau klik Kode Sesuai dengan Opsi Pertanyaan yang ingin diinformasikan Di bawah ini :\n" \
 \
 \
     "\n" \
 \
 \
     "/GE001 Apakah kegunaan Google Classroom LKM?\n" \
 \
 \
     "\n/GE002 Apa kode kelas untuk join ke Google Classroom LKM?\n" \
 \
 \
     "\n/GE003 Bagaimana cara bergabung dengan Google Classroom LKM?\n" \
 \
 \
     "\n/GE004 Bagaimana jika terdapat kendala dalam membuka classroom di situs sso.telkomuniversity.ac.id ?\n" \
 \
 \
     "\n/GE005 Bagaimana jika terdapat kendala untuk login ke situs sso.telkomuniversity.ac.id ? \n" \
 \
 \
     "\n" \
 \
 \
     "\nketik atau klik \"/G\" untuk kembali ke menu sebelumnya."

GE001 = "Apakah kegunaan Google Classroom LKM?"\
\
"\n" \
 \
"\n" \
 \
 \
"Google Classroom LKM digunakan untuk mendukung proses pengumpulan berkas laporan Akhir Magang." \
 \
 \
" Setiap mahasiswa yang sedang mengambil Magang wajib bergabung pada classroom."\
\
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/GE\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

GE002 = "Apa kode kelas untuk join ke Google Classroom LKM?"\
\
"\n" \
 \
"\n" \
 \
 \
"Info Lebih Lanjut Kode kelas untuk join ke Google Classroom LKM FIT : \n" \
 \
 \
"https://magang-sas.telkomuniversity.ac.id/en/lkm-google-classroom"\
\
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/GE\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

GE003 = "Bagaimana cara bergabung dengan Google Classroom LKM?"\
\
"\n" \
 \
"\n" \
 \
 \
"Info lebih lanjut cara bergabung dengan Google Classroom LKM:   \n" \
 \
 \
"https://magang-sas.telkomuniversity.ac.id/en/lkm-google-classroom"\
\
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/GE\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

GE004 = "Bagaimana jika terdapat kendala dalam membuka classroom di situs sso.telkomuniversity.ac.id ?"\
\
"\n" \
 \
"\n" \
 \
 \
"Bagi mahasiswa yang mengalami kendala dalam membuka Classroom atau email students, " \
 \
 \
"silakan ajukan ticketing sisfo melalui igracias pada menu : \n \n" \
 \
 \
"Helpdesk SISFO > Ticketing > Input Tiket."\
\
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/GE\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

GE005 = " Bagaimana jika terdapat kendala untuk login ke situs sso.telkomuniversity.ac.id ?"\
\
"\n" \
 \
"\n" \
 \
 \
"Bagi mahasiswa yang mengalami kendala dalam membuka Classroom atau email students, " \
 \
 \
"silakan ajukan ticketing sisfo melalui igracias pada menu : \n \n" \
 \
 \
"Helpdesk SISFO > Ticketing > Input Tiket."\
\
"\n" \
 \
"\n" \
 \
 \
"ketik atau klik \"/GE\" untuk kembali ke menu sebelumnya. \n" \
 \
 \
"ketik atau klik \"/start\" untuk kembali ke menu utama. "

response = "Harap Untuk Mengklik Kode Yang Sudah Disediakan Secara Benar\n \n - LKM FIT BOT -"








@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, start)


@bot.message_handler(commands=['hey'])
def send_welcome(message):
    bot.send_message(message.chat.id, response)



@bot.message_handler(commands=["A"])
def send_welcome(message):bot.send_message(message.chat.id, A)


@bot.message_handler(commands=["AA"])
def send_welcome(message):


    bot.send_message(message.chat.id, AA)


@bot.message_handler(commands=["AA001"])
def send_welcome(message):


    bot.send_message(message.chat.id, AA001)


@bot.message_handler(commands=["AA002"])
def send_welcome(message):


    bot.send_message(message.chat.id, AA002)


@bot.message_handler(commands=["AA003"])
def send_welcome(message):


    bot.send_message(message.chat.id, AA003)


@bot.message_handler(commands=["AA004"])
def send_welcome(message):


    bot.send_message(message.chat.id, AA004)




@bot.message_handler(commands=["AB"])
def send_welcome(message):


    bot.send_message(message.chat.id, AB)


@bot.message_handler(commands=["AB001"])
def send_welcome(message):


    bot.send_message(message.chat.id, AB001)


@bot.message_handler(commands=["AB002"])
def send_welcome(message):


    bot.send_message(message.chat.id, AB002)


@bot.message_handler(commands=["AB003"])
def send_welcome(message):


    bot.send_message(message.chat.id, AB003)


@bot.message_handler(commands=["AB004"])
def send_welcome(message):


    bot.send_message(message.chat.id, AB004)



@bot.message_handler(commands=["AC"])
def send_welcome(message):


    bot.send_message(message.chat.id, AC)


@bot.message_handler(commands=["AC001"])
def send_welcome(message):


    bot.send_message(message.chat.id, AC001)


@bot.message_handler(commands=["AC002"])
def send_welcome(message):


    bot.send_message(message.chat.id, AC002)


@bot.message_handler(commands=["AC003"])
def send_welcome(message):


    bot.send_message(message.chat.id, AC003)




@bot.message_handler(commands=["AD"])
def send_welcome(message):


    bot.send_message(message.chat.id, AD)




@bot.message_handler(commands=["ADA"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADA)


@bot.message_handler(commands=["ADA001"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADA001)


@bot.message_handler(commands=["ADA002"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADA002)


@bot.message_handler(commands=["ADA003"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADA003)


@bot.message_handler(commands=["ADA004"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADA004)


@bot.message_handler(commands=["ADA005"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADA005)



@bot.message_handler(commands=["ADB"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADB)


@bot.message_handler(commands=["ADB001"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADB001)


@bot.message_handler(commands=["ADB002"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADB002)


@bot.message_handler(commands=["ADB003"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADB003)


@bot.message_handler(commands=["ADB004"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADB004)


@bot.message_handler(commands=["ADC"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADC)


@bot.message_handler(commands=["ADC001"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADC001)


@bot.message_handler(commands=["ADC002"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADC002)


@bot.message_handler(commands=["ADC003"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADC003)


@bot.message_handler(commands=["ADC004"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADC004)




@bot.message_handler(commands=["ADD"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADD)


@bot.message_handler(commands=["ADD001"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADD001)


@bot.message_handler(commands=["ADD002"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADD002)


@bot.message_handler(commands=["ADD003"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADD003)


@bot.message_handler(commands=["ADD004"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADD004)



@bot.message_handler(commands=["ADE"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADE)


@bot.message_handler(commands=["ADE001"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADE001)


@bot.message_handler(commands=["ADE002"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADE002)


@bot.message_handler(commands=["ADE003"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADE003)


@bot.message_handler(commands=["ADE004"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADE004)


@bot.message_handler(commands=["ADE005"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADE005)

@bot.message_handler(commands=["ADF"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADF)


@bot.message_handler(commands=["ADF001"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADF001)


@bot.message_handler(commands=["ADF002"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADF002)


@bot.message_handler(commands=["ADF003"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADF003)


@bot.message_handler(commands=["ADF004"])
def send_welcome(message):


    bot.send_message(message.chat.id, ADF004)



@bot.message_handler(commands=["AE"])
def send_welcome(message):


    bot.send_message(message.chat.id, AE)


@bot.message_handler(commands=["AE001"])
def send_welcome(message):


    bot.send_message(message.chat.id, AE001)



@bot.message_handler(commands=["AF"])
def send_welcome(message):


    bot.send_message(message.chat.id, AF)


@bot.message_handler(commands=["AF001"])
def send_welcome(message):


    bot.send_message(message.chat.id, AF001)


@bot.message_handler(commands=["AF002"])
def send_welcome(message):


    bot.send_message(message.chat.id, AF002)


@bot.message_handler(commands=["AF003"])
def send_welcome(message):


    bot.send_message(message.chat.id, AF003)


@bot.message_handler(commands=["AF004"])
def send_welcome(message):


    bot.send_message(message.chat.id, AF004)



@bot.message_handler(commands=["AG"])
def send_welcome(message):


    bot.send_message(message.chat.id, AG)


@bot.message_handler(commands=["AG001"])
def send_welcome(message):


    bot.send_message(message.chat.id, AG001)



@bot.message_handler(commands=["B"])
def send_welcome(message):


    bot.send_message(message.chat.id, B)



@bot.message_handler(commands=["BA"])
def send_welcome(message):


    bot.send_message(message.chat.id, BA)


@bot.message_handler(commands=["BA001"])
def send_welcome(message):


    bot.send_message(message.chat.id, BA001)




@bot.message_handler(commands=["BB"])
def send_welcome(message):


    bot.send_message(message.chat.id, BB)


@bot.message_handler(commands=["BB001"])
def send_welcome(message):


    bot.send_message(message.chat.id, BB001)


@bot.message_handler(commands=["BB002"])
def send_welcome(message):


    bot.send_message(message.chat.id, BB002)


@bot.message_handler(commands=["BB003"])
def send_welcome(message):


    bot.send_message(message.chat.id, BB003)


@bot.message_handler(commands=["BB004"])
def send_welcome(message):


    bot.send_message(message.chat.id, BB004)



@bot.message_handler(commands=["BC"])
def send_welcome(message):


    bot.send_message(message.chat.id, BC)


@bot.message_handler(commands=["BC001"])
def send_welcome(message):


    bot.send_message(message.chat.id, BC001)


@bot.message_handler(commands=["BC002"])
def send_welcome(message):


    bot.send_message(message.chat.id, BC002)


@bot.message_handler(commands=["BC003"])
def send_welcome(message):


    bot.send_message(message.chat.id, BC003)


@bot.message_handler(commands=["BC004"])
def send_welcome(message):


    bot.send_message(message.chat.id, BC004)


@bot.message_handler(commands=["BC005"])
def send_welcome(message):


    bot.send_message(message.chat.id, BC005)


@bot.message_handler(commands=["BC006"])
def send_welcome(message):


    bot.send_message(message.chat.id, BC006)


@bot.message_handler(commands=["BC007"])
def send_welcome(message):


    bot.send_message(message.chat.id, BC007)


@bot.message_handler(commands=["BD"])
def send_welcome(message):


    bot.send_message(message.chat.id, BD)


@bot.message_handler(commands=["BD001"])
def send_welcome(message):


    bot.send_message(message.chat.id, BD001)


@bot.message_handler(commands=["BD002"])
def send_welcome(message):


    bot.send_message(message.chat.id, BD002)


@bot.message_handler(commands=["BD003"])
def send_welcome(message):


    bot.send_message(message.chat.id, BD003)


@bot.message_handler(commands=["BE"])
def send_welcome(message):


    bot.send_message(message.chat.id, BE)


@bot.message_handler(commands=["BE001"])
def send_welcome(message):


    bot.send_message(message.chat.id, BE001)


@bot.message_handler(commands=["BE002"])
def send_welcome(message):


    bot.send_message(message.chat.id, BE002)


@bot.message_handler(commands=["BE003"])
def send_welcome(message):


    bot.send_message(message.chat.id, BE003)


@bot.message_handler(commands=["BE004"])
def send_welcome(message):


    bot.send_message(message.chat.id, BE004)


@bot.message_handler(commands=["BE005"])
def send_welcome(message):


    bot.send_message(message.chat.id, BE005)


@bot.message_handler(commands=["BE006"])
def send_welcome(message):


    bot.send_message(message.chat.id, BE006)


@bot.message_handler(commands=["BE007"])
def send_welcome(message):


    bot.send_message(message.chat.id, BE007)


@bot.message_handler(commands=["BE008"])
def send_welcome(message):


    bot.send_message(message.chat.id, BE008)


@bot.message_handler(commands=["BE009"])
def send_welcome(message):


    bot.send_message(message.chat.id, BE009)


@bot.message_handler(commands=["BE010"])
def send_welcome(message):


    bot.send_message(message.chat.id, BE010)



@bot.message_handler(commands=["BF"])
def send_welcome(message):


    bot.send_message(message.chat.id, BF)


@bot.message_handler(commands=["BF001"])
def send_welcome(message):


    bot.send_message(message.chat.id, BF001)


@bot.message_handler(commands=["BF002"])
def send_welcome(message):


    bot.send_message(message.chat.id, BF002)


@bot.message_handler(commands=["BF003"])
def send_welcome(message):


    bot.send_message(message.chat.id, BF003)


@bot.message_handler(commands=["BF004"])
def send_welcome(message):


    bot.send_message(message.chat.id, BF004)


@bot.message_handler(commands=["BF005"])
def send_welcome(message):


    bot.send_message(message.chat.id, BF005)


@bot.message_handler(commands=["BF006"])
def send_welcome(message):


    bot.send_message(message.chat.id, BF006)


@bot.message_handler(commands=["BF007"])
def send_welcome(message):


    bot.send_message(message.chat.id, BF007)



@bot.message_handler(commands=["BG"])
def send_welcome(message):


    bot.send_message(message.chat.id, BG)


@bot.message_handler(commands=["BG001"])
def send_welcome(message):


    bot.send_message(message.chat.id, BG001)


@bot.message_handler(commands=["BG002"])
def send_welcome(message):


    bot.send_message(message.chat.id, BG002)


@bot.message_handler(commands=["BG003"])
def send_welcome(message):


    bot.send_message(message.chat.id, BG003)


@bot.message_handler(commands=["BG004"])
def send_welcome(message):


    bot.send_message(message.chat.id, BG004)


@bot.message_handler(commands=["BG005"])
def send_welcome(message):


    bot.send_message(message.chat.id, BG005)


@bot.message_handler(commands=["BG006"])
def send_welcome(message):


    bot.send_message(message.chat.id, BG006)


@bot.message_handler(commands=["BG007"])
def send_welcome(message):


    bot.send_message(message.chat.id, BG007)


@bot.message_handler(commands=["BH"])
def send_welcome(message):


    bot.send_message(message.chat.id, BH)


@bot.message_handler(commands=["BH001"])
def send_welcome(message):


    bot.send_message(message.chat.id, BH001)


@bot.message_handler(commands=["BH002"])
def send_welcome(message):


    bot.send_message(message.chat.id, BH002)


@bot.message_handler(commands=["BH003"])
def send_welcome(message):


    bot.send_message(message.chat.id, BH003)


@bot.message_handler(commands=["BH004"])
def send_welcome(message):


    bot.send_message(message.chat.id, BH004)


@bot.message_handler(commands=["BH005"])
def send_welcome(message):


    bot.send_message(message.chat.id, BH005)


@bot.message_handler(commands=["BH006"])
def send_welcome(message):


    bot.send_message(message.chat.id, BH006)


@bot.message_handler(commands=["BH007"])
def send_welcome(message):


    bot.send_message(message.chat.id, BH007)


@bot.message_handler(commands=["BI"])
def send_welcome(message):


    bot.send_message(message.chat.id, BI)


@bot.message_handler(commands=["BI001"])
def send_welcome(message):


    bot.send_message(message.chat.id, BI001)


@bot.message_handler(commands=["BI002"])
def send_welcome(message):


    bot.send_message(message.chat.id, BI002)


@bot.message_handler(commands=["C"])
def send_welcome(message):


    bot.send_message(message.chat.id, C)


@bot.message_handler(commands=["C001"])
def send_welcome(message):


    bot.send_message(message.chat.id, C001)


@bot.message_handler(commands=["C002"])
def send_welcome(message):


    bot.send_message(message.chat.id, C002)


@bot.message_handler(commands=["C003"])
def send_welcome(message):


    bot.send_message(message.chat.id, C003)


@bot.message_handler(commands=["C004"])
def send_welcome(message):


    bot.send_message(message.chat.id, C004)


@bot.message_handler(commands=["C005"])
def send_welcome(message):


    bot.send_message(message.chat.id, C005)


@bot.message_handler(commands=["C006"])
def send_welcome(message):


    bot.send_message(message.chat.id, C006)


@bot.message_handler(commands=["C007"])
def send_welcome(message):


    bot.send_message(message.chat.id, C007)


@bot.message_handler(commands=["C008"])
def send_welcome(message):


    bot.send_message(message.chat.id, C008)




@bot.message_handler(commands=["D"])
def send_welcome(message):


    bot.send_message(message.chat.id, D)


@bot.message_handler(commands=["DA"])
def send_welcome(message):


    bot.send_message(message.chat.id, DA)


@bot.message_handler(commands=["DA001"])
def send_welcome(message):


    bot.send_message(message.chat.id, DA001)


@bot.message_handler(commands=["DA002"])
def send_welcome(message):


    bot.send_message(message.chat.id, DA002)


@bot.message_handler(commands=["DA003"])
def send_welcome(message):


    bot.send_message(message.chat.id, DA003)

@bot.message_handler(commands=["DB"])
def send_welcome(message):


    bot.send_message(message.chat.id, DB)


@bot.message_handler(commands=["DB001"])
def send_welcome(message):


    bot.send_message(message.chat.id, DB001)


@bot.message_handler(commands=["DB002"])
def send_welcome(message):


    bot.send_message(message.chat.id, DB002)


@bot.message_handler(commands=["DB003"])
def send_welcome(message):


    bot.send_message(message.chat.id, DB003)



@bot.message_handler(commands=["E"])
def send_welcome(message):


    bot.send_message(message.chat.id, E)



@bot.message_handler(commands=["EA"])
def send_welcome(message):


    bot.send_message(message.chat.id, EA)


@bot.message_handler(commands=["EA001"])
def send_welcome(message):


    bot.send_message(message.chat.id, EA001)



@bot.message_handler(commands=["EB"])
def send_welcome(message):


    bot.send_message(message.chat.id, EB)


@bot.message_handler(commands=["EB001"])
def send_welcome(message):


    bot.send_message(message.chat.id, EB001)



@bot.message_handler(commands=["EC"])
def send_welcome(message):


    bot.send_message(message.chat.id, EC)


@bot.message_handler(commands=["EC001"])
def send_welcome(message):


    bot.send_message(message.chat.id, EC001)


@bot.message_handler(commands=["ED"])
def send_welcome(message):


    bot.send_message(message.chat.id, ED)


@bot.message_handler(commands=["ED001"])
def send_welcome(message):


    bot.send_message(message.chat.id, ED001)



@bot.message_handler(commands=["EE"])
def send_welcome(message):


    bot.send_message(message.chat.id, EE)


@bot.message_handler(commands=["EE001"])
def send_welcome(message):


    bot.send_message(message.chat.id, EE001)


@bot.message_handler(commands=["EE002"])
def send_welcome(message):


    bot.send_message(message.chat.id, EE002)


@bot.message_handler(commands=["EE003"])
def send_welcome(message):


    bot.send_message(message.chat.id, EE003)


@bot.message_handler(commands=["EE004"])
def send_welcome(message):


    bot.send_message(message.chat.id, EE004)


@bot.message_handler(commands=["EE005"])
def send_welcome(message):


    bot.send_message(message.chat.id, EE005)


@bot.message_handler(commands=["EE006"])
def send_welcome(message):


    bot.send_message(message.chat.id, EE006)


@bot.message_handler(commands=["EE007"])
def send_welcome(message):


    bot.send_message(message.chat.id, EE007)




@bot.message_handler(commands=["F"])
def send_welcome(message):


    bot.send_message(message.chat.id, F)




@bot.message_handler(commands=["FA"])
def send_welcome(message):


    bot.send_message(message.chat.id, FA)


@bot.message_handler(commands=["FA001"])
def send_welcome(message):


    bot.send_message(message.chat.id, FA001)


@bot.message_handler(commands=["FA002"])
def send_welcome(message):


    bot.send_message(message.chat.id, FA002)


@bot.message_handler(commands=["FA003"])
def send_welcome(message):


    bot.send_message(message.chat.id, FA003)


@bot.message_handler(commands=["FA004"])
def send_welcome(message):


    bot.send_message(message.chat.id, FA004)



@bot.message_handler(commands=["FB"])
def send_welcome(message):


    bot.send_message(message.chat.id, FB)


@bot.message_handler(commands=["FB001"])
def send_welcome(message):


    bot.send_message(message.chat.id, FB001)




@bot.message_handler(commands=["FC"])
def send_welcome(message):


    bot.send_message(message.chat.id, FC)


@bot.message_handler(commands=["FC001"])
def send_welcome(message):


    bot.send_message(message.chat.id, FC001)


@bot.message_handler(commands=["FC002"])
def send_welcome(message):


    bot.send_message(message.chat.id, FC002)


@bot.message_handler(commands=["G"])
def send_welcome(message):


    bot.send_message(message.chat.id, G)




@bot.message_handler(commands=["GA"])
def send_welcome(message):


    bot.send_message(message.chat.id, GA)




@bot.message_handler(commands=["GB"])
def send_welcome(message):


    bot.send_message(message.chat.id, GB)



@bot.message_handler(commands=["GC"])
def send_welcome(message):


    bot.send_message(message.chat.id, GC)




@bot.message_handler(commands=["GD"])
def send_welcome(message):


    bot.send_message(message.chat.id, GD)



@bot.message_handler(commands=["GE"])
def send_welcome(message):


    bot.send_message(message.chat.id, GE)


@bot.message_handler(commands=["GE001"])
def send_welcome(message):


    bot.send_message(message.chat.id, GE001)


@bot.message_handler(commands=["GE002"])
def send_welcome(message):


    bot.send_message(message.chat.id, GE002)


@bot.message_handler(commands=["GE003"])
def send_welcome(message):


    bot.send_message(message.chat.id, GE003)


@bot.message_handler(commands=["GE004"])
def send_welcome(message):


    bot.send_message(message.chat.id, GE004)


@bot.message_handler(commands=["GE005"])
def send_welcome(message):


    bot.send_message(message.chat.id, GE005)




@bot.message_handler(content_types=['text'])
def echo_messages(message):
    text = message.text
    if text == 'If'  :
         bot.reply_to(message, response)
    elif text == 'Elif' :
         bot.reply_to(message, response)
    else:
         bot.reply_to(message, response)


while True:
    try:
        bot.polling()
    except:
        time.sleep(5)
