from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
# Not: iOS bildirimleri için plyer kütüphanesi gerekebilir
from plyer import notification 

class WaterApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        self.label = Label(text="Su Hatırlatıcı Kapalı", font_size='20sp')
        
        self.btn = Button(
            text="Başlat (30 Dakika)", 
            size_hint=(1, 0.2),
            background_color=(0, 0.5, 1, 1)
        )
        self.btn.bind(on_press=self.toggle_reminder)
        
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.btn)
        self.active = False
        return self.layout

    def toggle_reminder(self, instance):
        if not self.active:
            self.active = True
            self.btn.text = "Durdur"
            self.label.text = "Hatırlatıcı Aktif: Her 30 dk"
            # 1800 saniye = 30 dakika
            Clock.schedule_interval(self.send_water_notification, 1800)
        else:
            self.active = False
            self.btn.text = "Başlat"
            self.label.text = "Hatırlatıcı Kapalı"
            Clock.unschedule(self.send_water_notification)

    def send_water_notification(self, dt):
        notification.notify(
            title="Su Vakti! 💧",
            message="Yarım saat doldu, bir bardak su içmelisin.",
            app_name="Su Hatırlatıcı"
        )

if __name__ == '__main__':
    WaterApp().run()
