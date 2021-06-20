import sys,time,os
def remove():
    if os.name == ('posix'):
        _ = os.system('clear')
    else:
        os.system('cls')
remove()
	
print('Welcome to Engine Math')
print('Copyright \N{COPYRIGHT SIGN} 2021 All right reserved. by: Saif Al-Anwar')
print('Program ini selesai dibuat pada hari jum\'at tanggal 02 maret 2021')
print('\nTunggu sebentar, data sedang diinput..')

animasi = ["Loading[□□□□□□□□□□]","Loading[■□□□□□□□□□]","Loading[■■□□□□□□□□]", "Loading[■■■□□□□□□□]", "Loading[■■■■□□□□□□]", "Loading[■■■■■□□□□□]", "Loading[■■■■■■□□□□]", "Loading[■■■■■■■□□□]", "Loading[■■■■■■■■□□]", "Loading[■■■■■■■■■□]", "Loading[■■■■■■■■■■]"]

for i in range(len(animasi)):
    time.sleep(0.3)
    sys.stdout.write("\r" + animasi[i % len(animasi)])
    sys.stdout.flush()

print('\n------------------------------------------------------------------')
# interface
print('\n0. Motor','1. Mobil')
jenis = ["motor", "mobil"]
m_int = int(input('\nPilih jenis kendaraan: '))

z = (' yang belum terdaftar diaplikasi ini, segera hubungi developer')

if jenis[m_int] == ('motor'):
    from motor import motor
    motor.merk
    motor.x_int
elif jenis[m_int] == ('mobil'):
    from mobil import mobil
    mobil.merk
    mobil.x_int

j_int = int(input('\nJarak tempuh (dalam KM): '))

from bbm import bbm

h_int = int(input('\nHarga perliter: '))
km = int

print('\nData sedang diproses...')
proses = ["[□□□□□□□□□□]","[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(proses)):
    time.sleep(0.5)
    sys.stdout.write("\r" + proses[i % len(proses)])
    sys.stdout.flush()

def hapus_log():
    if os.name == ('posix'):
        _ = os.system('clear')
    else:
        os.system('cls')
hapus_log()

#hasil
print('\nResult: ')

print('Jenis kendaraan anda adalah', jenis[m_int], end='')

if jenis[m_int] == ('motor'):
    print(' dengan merk' ,motor.merk[motor.x_int])
elif jenis[m_int] == ('mobil'):
    print(' dengan merk' ,mobil.merk[mobil.x_int])

print('Untuk menempuh jarak', j_int, end='')
print(' kilometer')

if jenis[m_int] == ('motor'):
    print('Anda membutuhkan', round(j_int / motor.km, 1),end='')
elif jenis[m_int] == ('mobil'):
    print('Anda membutuhkan', round(j_int / mobil.km, 1),end='')

print(' liter',bbm.bbm[bbm.b])

if jenis[m_int] == ('motor'):
    print('Dengan harga:', round((j_int / motor.km) * h_int, 1), end='')
    print(' rupiah')
elif jenis[m_int] == ('mobil'):
    print('Dengan harga:', round((j_int / mobil.km) * h_int, 1), end='')
    print(' rupiah')

print('---------- Result from Google.inc ----------')
print('\nThank\'s for use this program')
waktu = time.strftime ('%A, %d %B %Y %H:%M:%S', time.localtime(time.time()))
print("\nThis Time is", waktu)
print('Copyright \N{COPYRIGHT SIGN} 2021 All right reserved. \nProgram by: Saif Al-Anwar')

lagi = input("\nApakah Anda Ingin Mencoba Lagi? (y/n)")
while (lagi == 'y'):
	import EngineMath
	if lagi == ('n'):
		continue
print('Terimakasih telah menggunakan aplikasi ini....')

keluar = ['Preparing to exit.','Preparing to exit..','Preparing to exit...','Preparing to exit....','Preparing to exit.....','Preparing to exit......','Preparing to exit.......','Preparing to exit........','Preparing to exit..........','Preparing to exit...........',]
for i in range(len(keluar)):
    time.sleep(0.3)
    sys.stdout.write("\r" + keluar[i % len(keluar)])
    sys.stdout.flush()
print('\nExited...')