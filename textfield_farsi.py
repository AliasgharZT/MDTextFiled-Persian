from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from arabic_reshaper import reshape
from bidi.algorithm import get_display
from kivy.core.window import Window
import translate


class MainApp2(MDApp):
    l = []
    ll = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_key_down=self.ghap)

    def farsi(self, text):
        t = get_display(reshape(text))
        return t

    def ghap(self, *args):
        q = self.l
        print(args)
        print(args[len(args) - 2])
        if args[len(args) - 2] == ' ':
            t = self.e.text
            self.e.text = ''
            t.split()
            tt = t.split()
            print(tt)
            print(tt[-1])
            q.append(tt[-1])
            print(q)
            for w in q[-1::-1]:
                self.e.text += self.farsi(w)
        if args[len(args) - 2] == 'Ĳ':
            r = self.ll
            for qq in q:
                # qqq=self.farsi(qq)
                r.append(self.translator(qq))
            print(r)
            self.e.text = ''
            self.e.font_name = ''
            for p in r:
                self.e.text += p

    def translator(self, text):
        try:
            option = translate.translate.Translator(from_lang='fa', to_lang='en')
            text_out = option.translate(text)
            if text_out.find(','):
                t=text_out.split(',')
                return t[0]
            else:
                return text_out
        except:
            return text 

    def build(self):
        self.e = MDTextField()
        self.e.mode = 'round'
        self.e.pos_hint = {'y': 0.5}
        self.e.font_name = 'Persian'
        # self.e.text='  '*101
        self.e.focus = True

        return self.e

MainApp2().run()
