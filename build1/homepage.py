# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\PFE\Tkinter-Designer-master\build1\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def on_enter(event, widget_id):
    canvas.itemconfig(widget_id, fill="#3AB1AC")

def on_leave(event, widget_id):
    canvas.itemconfig(widget_id, fill="#4D4D4D")

window = Tk()
window.geometry("768x576")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=576,
    width=768,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
canvas.create_image(384.0, 288.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
canvas.create_image(41.0, 35.0, image=image_image_2)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
canvas.create_image(687.0, 218.0, image=image_image_3)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
canvas.create_image(687.0, 271.0, image=image_image_4)

image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
canvas.create_image(687.0, 324.0, image=image_image_5)

image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
canvas.create_image(687.0, 165.0, image=image_image_6)

image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
canvas.create_image(687.0, 378.0, image=image_image_7)

image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
canvas.create_image(687.0, 431.0, image=image_image_8)

image_image_9 = PhotoImage(file=relative_to_assets("image_9.png"))
canvas.create_image(738.0, 529.0, image=image_image_9)

image_image_10 = PhotoImage(file=relative_to_assets("image_10.png"))
canvas.create_image(672.0, 529.0, image=image_image_10)

text_items = []

text_items.append(canvas.create_text(
    575.0,
    202.0,
    anchor="nw",
    text="تسيير الطلاب",
    fill="#4D4D4D",
    font=("ArefRuqaa Regular", 19 * -1)
))

text_items.append(canvas.create_text(
    575.0,
    145.0,
    anchor="nw",
    text="تسيير الاساتذة",
    fill="#4D4D4D",
    font=("ArefRuqaa Regular", 19 * -1)
))

text_items.append(canvas.create_text(
    455.0,
    253.0,
    anchor="nw",
    text="ادارت الاقسام و الافواج و الفواتير ",
    fill="#4D4D4D",
    font=("ArefRuqaa Regular", 19 * -1)
))

text_items.append(canvas.create_text(
    526.0,
    307.0,
    anchor="nw",
    text="البرامج  و الاستمارات ",
    fill="#4D4D4D",
    font=("ArefRuqaa Regular", 19 * -1)
))

text_items.append(canvas.create_text(
    605.0,
    362.0,
    anchor="nw",
    text="العلامات",
    fill="#4D4D4D",
    font=("ArefRuqaa Regular", 19 * -1)
))

text_items.append(canvas.create_text(
    551.0,
    415.0,
    anchor="nw",
    text="استخراج  الوثائق",
    fill="#4D4D4D",
    font=("ArefRuqaa Regular", 19 * -1)
))

text_items.append(canvas.create_text(
    706.0,
    550.0,
    anchor="nw",
    text="الاعدادات",
    fill="#4D4D4D",
    font=("ArefRuqaa Regular", 19 * -1)
))

text_items.append(canvas.create_text(
    644.0,
    550.0,
    anchor="nw",
    text="المساعدة",
    fill="#4D4D4D",
    font=("ArefRuqaa Regular", 19 * -1)
))

for item in text_items:
    canvas.tag_bind(item, "<Enter>", lambda event, widget_id=item: on_enter(event, widget_id))
    canvas.tag_bind(item, "<Leave>", lambda event, widget_id=item: on_leave(event, widget_id))



image_image_11 = PhotoImage(file=relative_to_assets("image_11.png"))
canvas.create_image(176.0, 517.0, image=image_image_11)

image_image_12 = PhotoImage(file=relative_to_assets("image_12.png"))
canvas.create_image(621.0, 50.0, image=image_image_12)

window.resizable(False, False)
window.mainloop()
