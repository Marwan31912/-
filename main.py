from flet import *
def marwan(page:Page):
    page.title = "أذكار" # اسم التطبيق
    page.window.width= 390
    page.window.height= 700
    page.window.top =10
    page.window.left = 950
    
    page.vertical_alignment="center" # توسيط العناصر من الاعلى و الاسفل
    page.horizontal_alignment="center" # توسيط العناصر من اليسار و اليمين
    lib = Image(src=f"image/pips.png")
    page.bgcolor= '#ecdab6'

    page.add(
        lib
    )
    
        ########### الجزء العلوي من التطبيق##########
    page.appbar = AppBar(
        bgcolor= '#763705',
        title= Text("القائمة الرئيسية",color="#ecdab6"),
        center_title= True,
        leading=Icon(icons.HOME,color="#ecdab6"),
        actions=[
            PopupMenuButton(
                items=[
                    PopupMenuItem(text="الاعدادات")   
                ]
            ) 
        ]
    )
    ########### نهاية الجزء العلوي     ##########
    

    page.update()

    
app(marwan)
