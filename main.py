import stegano.lsb as lsb
import os
import time

class Hide:
    def hide_img(self, In, Out):
        msg1 = 'Ukryta wiadomosc'
        msg2 = 'Ukryta wiadomosc, Ukryta wiadomosc ,Ukryta wiadomosc, Ukryta wiadomosc'
        msg3 = 'Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc, Ukryta wiadomosc'

        m1 = self.get_time_and_size(In, Out, msg1)
        m2 = self.get_time_and_size(In, Out, msg2)
        m3 = self.get_time_and_size(In, Out, msg3)

        return m1,m2,m3

    def get_time_and_size(self, In, Out, msg):
        x = time.time()
        lsb.hide(In, message=msg).save(Out)
        y = time.time()
        return f'{y-x} | Rozmiar: {self.get_size(Out)} B'

    def get_size(self,file):
        return os.stat(file).st_size

    def reveal_img_time(self,Out):
        x = time.time()
        lsb.reveal(Out)
        y = time.time()
        return y-x


In100KB = '100KB.png'
Out100KB = '100KBout.png'

In1MB = '1MB.png'
Out1MB = '1MBout.png'

In10MB = '10MB.png'
Out10MB = '10MBout.png'

if __name__ == "__main__":
    hide = Hide()

    x, xx, xxx = hide.hide_img(In100KB, Out100KB)
    y, yy, yyy = hide.hide_img(In1MB, Out1MB)
    z, zz, zzz = hide.hide_img(In10MB, Out10MB)



    print(f'Czas szyfrowania dla {In100KB} oraz rozmiar (rozmiar oryginalny: {hide.get_size(In100KB)} B): \n '
          f'- Krotkie: {x}\n '
          f'- Srednie: {xx}\n'
          f'- Dlugie: {xxx}\n'
          f'Czas szyfrowania dla {In1MB} oraz rozmiar (rozmiar oryginalny: {hide.get_size(In1MB)} B): \n '
          f'- Krotkie: {y}\n'
          f'- Srednie: {yy}\n'
          f'- Dlugie: {yyy}\n'
          f'Czas szyfrowania dla {In10MB} oraz rozmiar (rozmiar oryginalny: {hide.get_size(In10MB)} B): \n '
          f'- Krotkie: {z}\n'
          f'- Srednie: {zz}\n'
          f'- Dlugie: {zzz}\n\n')

    print(f'Czas odszyfrowania dla {Out100KB}: \n '
          f'- {hide.reveal_img_time(Out100KB)}\n '
          f'Czas odszyfrowania dla {Out1MB}: \n '
          f'- {hide.reveal_img_time(Out1MB)}\n'
          f'Czas odszyfrowania dla {Out10MB}: \n '
          f'- {hide.reveal_img_time(Out10MB)}\n')

