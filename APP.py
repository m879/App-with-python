from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivy.lang import Builder

from kivymd.uix.list import OneLineIconListItem, MDList

import time
from kivy.uix.video import Video
from kivymd.uix.picker import MDThemePicker


KV="""
<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "image1.png"
    MDLabel:
        text: "MERAJ AHMED "
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: "merajahmed2112@gmail.com"
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]


    ScrollView:
        MDList:
            OneLineIconListItem:
                text:'All Files'
                on_press:
                    root.nav_drawer.set_state('close')
                    root.screen_manager.current='screen 1'
                IconLeftWidget:
                    icon:'folder'
                    theme_text_color: "Custom"
    
            OneLineIconListItem:
                text:'Camera'
                on_press:
                    root.nav_drawer.set_state('close')
                    root.screen_manager.current='screen 2'
                IconLeftWidget:
                    icon:'camera'
                    theme_text_color: "Custom"

            OneLineIconListItem:
                text:'Music'
                on_press:
                    root.nav_drawer.set_state('close')
                    root.screen_manager.current='screen 3'
                IconLeftWidget:
                    icon:'music'
                    theme_text_color: "Custom"



            OneLineIconListItem:
                text:'Video Player'
                on_press:
                    root.nav_drawer.set_state('close')
                    root.screen_manager.current='screen 4'
                IconLeftWidget:
                    icon:'video'
                    theme_text_color: "Custom"
            
            OneLineIconListItem:
                text:'Text Editor'
                on_press:
                    root.nav_drawer.set_state('close')
                    root.screen_manager.current='screen 5'
                IconLeftWidget:
                    icon:'file-document-edit'
                    theme_text_color: "Custom"
            
            OneLineIconListItem:
                text:'Books'
                on_press:
                    root.nav_drawer.set_state('close')
                    root.screen_manager.current='screen 6'
                IconLeftWidget:
                    icon:'library-books'
                    theme_text_color: "Custom"


            OneLineIconListItem:
                text:'Calculator'
                on_press:
                    root.nav_drawer.set_state('close')
                    root.screen_manager.current='screen 7'
                IconLeftWidget:
                    icon:'calculator'
                    theme_text_color: "Custom"

            OneLineIconListItem:
                text:'Downloads'
                on_press:
                    root.nav_drawer.set_state('close')
                    root.screen_manager.current='screen 8'
                IconLeftWidget:
                    icon:'download'
                    theme_text_color: "Custom"

            OneLineIconListItem:
                text:'Settings'
                on_press:
                    root.nav_drawer.set_state('close')
                    root.screen_manager.current='screen 9'
                IconLeftWidget:
                    icon:'settings-outline'
                    theme_text_color: "Custom"



Screen:
    MDToolbar:
        id:toolbar
        pos_hint:{'top':1}
        elevation:10
        title:"Meraj App"
        left_action_items:[['menu',lambda x:nav_drawer.set_state('open')]]
    



    NavigationLayout:
        x:toolbar.height
        
        ScreenManager:
            id:screen_manager

            Screen:
                name: "screen 1"
                MDLabel:
                    font_style:'H3'
                    text: "All Files"
                    halign: "center"

                MDGridLayout:
                    cols:3  

                    MDLabel:
                        text: 'Welcome to web development'
                        bold: True
                        font_style: "H5"
                        pos_hint: {"center_x": .5, "center_y": .9}

                    # MDLabel:
                        # text: 'Welcome to Meraj Ahmed'
                        # bold: True
                        # font_style: "H5"
                        # pos_hint: {"center_x": .4, "center_y": .8}
                    # MDLabel:
                        # text: 'Welcome to computer coding'
                        # bold: True
                        # font_style: "H5"
                        # pos_hint: {"center_x": .3, "center_y": .7}

                    MDRectangleFlatIconButton:
                        text: "MDRectangleFlatIconButton"
                        icon: "language-python"
                        width: dp(230)
                        pos_hint: {"center_x": .2,'center_y':0.2}
    
 



            Screen:
                name: "screen 2"
                MDLabel:
                    text: "Camera"
                    halign: "center"

            Screen:
                name: "screen 3"
                MDLabel:
                    text: "Music"
                    halign: "center"
                # Video:    
                    # source:"music.mp3"
                    # play:True
    


            Screen:
                name: "screen 4"
                # MDLabel:
                    # text: "Video Player"
                    # halign: "center"
                MDRectangleFlatIconButton:
                    text: "Play Video"
                    icon: "video"
                    pos_hint: {"center_x": .2,'center_y':0.2}
                    # on_release:app.play_video()
                    
                # Video:    
                    # source:"video1.mp4"
                    # play:True

            Screen:
                name: "screen 5"
                MDLabel:
                    text: "Text Editor"
                    halign: "center"
                MDTextField:
                    hint_text: 'Field with left and right icons' 
                    width: dp(20)   
            
            Screen:
                name: "screen 6"
                md_bg_color: app.theme_cls.primary_color
                MDLabel:
                    text: "Books"
                    halign: "center"
            
            Screen:
                name: "screen 7"
                MDLabel:
                    text: "Calculator"
                    halign: "center"
            Screen:
                name: "screen 8"
                MDLabel:
                    text: "Downloads"
                    halign: "center"
            
            Screen:
                name: "screen 9"
                # MDGridLayout:
                MDRectangleFlatIconButton:
                    text: "Open Settings"
                    icon: "settings"
                    pos_hint: {"center_x": .5,'center_y':0.5}
                    on_release: app.open_settings()
                MDRectangleFlatIconButton:
                    text: "Themes"
                    icon: "settings"
                    pos_hint: {"center_x": .2,'center_y':0.2}
                    on_release: app.show_theme_picker()
             
        MDNavigationDrawer:
            id:nav_drawer
            ContentNavigationDrawer: 
                screen_manager: screen_manager
                nav_drawer: nav_drawer

"""

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class MerajApp(MDApp):
    def build(self):
        # self.theme_cls.theme_style = "Dark"  # "Light"
        # self.theme_cls.primary_palette = "Red"
        return Builder.load_string(KV)
    
    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()
    # def play_video(self):
        # s = Video(source="video1.mp4", play=True)
        # return s

MerajApp().run()


