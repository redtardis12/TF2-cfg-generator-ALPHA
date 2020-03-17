import tkinter as tk
from tkinter import *
from tkinter import filedialog  # uses for directory brows button
from tkinter import ttk  # uses to create tab menu
import tkinter.font as font  # importing fonts


def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))


def on_configure1(event):
    canvas1.configure(scrollregion=canvas.bbox('all'))
# functions allows to scroll windows with any widgets in it


root = tk.Tk()
root.geometry('900x400+200+100')  # size 900x400px
root.resizable(0, 0)  # not allows user to change sizes of window
root.title("TF2CFG Generator")
root.iconbitmap('icon.ico')
note = ttk.Notebook(root)  # create tab menu area in window with notebook widget

tab1 = Canvas(note, highlightthickness=0)
tab2 = Canvas(note, highlightthickness=0)
tab3 = Canvas(note, highlightthickness=0)

canvas = tk.Canvas(tab1, width=600, highlightthickness=0)
canvas.pack(side=tk.LEFT)
scrollbar = tk.Scrollbar(tab1, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill='y')
canvas.configure(yscrollcommand = scrollbar.set)
canvas.bind('<Configure>', on_configure)
frame = tk.Frame(canvas, width=700)
canvas.create_window((0,0), window=frame, anchor='nw')
# create scrollbar placed in tab, using canvas and frame

canvas1 = tk.Canvas(tab2, width=600, highlightthickness=0)
canvas1.pack(side=tk.LEFT)
scrollbar1 = tk.Scrollbar(tab2, command=canvas1.yview)
scrollbar1.pack(side=tk.RIGHT, fill='y')
canvas1.configure(yscrollcommand = scrollbar1.set)
canvas1.bind('<Configure>', on_configure1)
frame1 = tk.Frame(canvas1, width=700)
canvas1.create_window((0,0), window=frame1, width=700, anchor='nw')


title_text = font.Font(family='TF2 Build', size=15)
myFont = font.Font(family='TF2 Build')  # main font in app
note.add(tab1, text="Графика")
note.add(tab2, text="Интерфейс")
note.add(tab3, text="Интернет")
note.config(width=650)
note.pack(side=LEFT, fill=BOTH, pady=5, padx=5,)


preset_configs = {   # dictionary with all content of commands tf2
    "r_waterdrawreflection": "0",
    "r_waterforceexpensive": "0",
    "r_shadowrendertotexture": "0",
    "r_shadows": "0",
    "r_drawflecks": "0",
    "r_drawdetailprops": "0",
    "r_dynamic": "0",
    "r_drawmodeldecals": "0",
    "r_renderoverlayfragment": "0",
    "r_3dsky": "0",
    "r_lightaverage": "0",
    "r_flashlightdepthtexture": "0",
    "r_ropetranslucent": "0",
    "r_ForceWaterLeaf": "0",
    "r_ambientboost": "0",
    "hud_combattext": "0",
    "hud_combattext_batching": "0",
    "hud_fastswitch": "0",
    "hud_combattext_healing": "0",
    "hud_combattext_doesnt_block_overhead_text": "0",
    "hud_takesshots": "0",
    "cl_ask_blacklist_opt_out": "0",
    "cl_ask_favorite_opt_out": "0",
    "cl_autoreload": "0",
    "cl_autorezoom": "0",
    "cl_burninggibs": "0",
    "cl_drawhud": "0",
    "cl_flipviewmodels": "0",
    "cl_new_impact_effects": "0",
    "cl_ragdoll_collide": "0",
    "cl_showbackpackrarities": "0",
    "cl_showfps": "0",
    "cl_showpos": "0",
}


def browsefunc():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path = filename
# opens window with choosing directory and store it in global var


folder_path = str()


def on_click(toggle, key_set):
    if toggle.get() == 1:
        preset_configs[key_set] = "1"
    else:
        preset_configs[key_set] = "0"
# changing values in main dictionary using checkboxes' states


def done():
    main_config = open(folder_path+"/autoexec.cfg", 'w')
    for key in preset_configs:
        main_config.write(key + ' ' + preset_configs[key] + '\n')
    main_config.close()
# create file in chosen directory and loop adds dictionary keys and states in it by pressing save button


check_var = IntVar()
check = Checkbutton(frame, text='Отражения на воде', onvalue=1, offvalue=0, variable=check_var, font=myFont, command=lambda: on_click(check_var, "r_waterdrawreflection")).pack(anchor=W, padx=2)
check_var1 = IntVar()
check1 = Checkbutton(frame, text='Продвинутые отражения на воде', onvalue=1, offvalue=0, variable=check_var1, font=myFont, command=lambda: on_click(check_var1, "r_waterforceexpensive")).pack(anchor=W, padx=2)
check_var2 = IntVar()
check2 = Checkbutton(frame, text='Динамические тени на объектах', onvalue=1, offvalue=0, variable=check_var2, font=myFont, command=lambda: on_click(check_var2, "r_shadowrendertotexture")).pack(anchor=W, padx=2)
check_var3 = IntVar()
check3 = Checkbutton(frame, text='Динамические тени на местности', onvalue=1, offvalue=0, variable=check_var3, font=myFont, command=lambda: on_click(check_var3, "r_shadows")).pack(anchor=W, padx=2)
check_var4 = IntVar()
check4 = Checkbutton(frame, text='Прорисовка мелких осколков и пыли при попадании пули', onvalue=1, offvalue=0, variable=check_var4, font=myFont, command=lambda: on_click(check_var4, "r_drawfleckse")).pack(anchor=W, padx=2)
check_var5 = IntVar()
check5 = Checkbutton(frame, text='Детализация мелких предметов', onvalue=1, offvalue=0, variable=check_var5, font=myFont, command=lambda: on_click(check_var5, "r_drawdetailprops")).pack(anchor=W, padx=2)
# options for 1st tab

check_var6 = IntVar()
check6 = Checkbutton(frame1, text='Показывать количество нанесённого урона над врагом', onvalue=1, offvalue=0, variable=check_var6, font=myFont, command=lambda: on_click(check_var6, "hud_combattext")).pack(anchor=W, padx=2)
check_var7 = IntVar()
check7 = Checkbutton(frame1, text='Переключить наложение текста урона друг на друга в\nпределах 0.10 сек. интервала', justify=LEFT, onvalue=1, offvalue=0, variable=check_var7, font=myFont, command=lambda: on_click(check_var7, "hud_combattext_batching")).pack(anchor=W, padx=2)
check_var8 = IntVar()
check8 = Checkbutton(frame1, text='Быстрое переключение оружия (только колёсиком мыши)', onvalue=1, offvalue=0, variable=check_var8, font=myFont, command=lambda: on_click(check_var8, "hud_fastswitch")).pack(anchor=W, padx=2)
check_var9 = IntVar()
check9 = Checkbutton(frame1, text='Переключить текст лечения союзников', onvalue=1, offvalue=0, variable=check_var9, font=myFont, command=lambda: on_click(check_var9, "hud_combattext_healing")).pack(anchor=W, padx=2)
check_var10 = IntVar()
check10 = Checkbutton(frame1, text='Переключить накладывающиеся эффекты частиц,\nиспользуемые для критов и мини-критов', justify=LEFT, onvalue=1, offvalue=0, variable=check_var10, font=myFont, command=lambda: on_click(check_var10, "hud_combattext_doesnt_block_overhead_text")).pack(anchor=W, padx=2)
check_var11 = IntVar()
check11 = Checkbutton(frame1, text='Авто скриншот «tab» в конце карты', onvalue=1, offvalue=0, variable=check_var11, font=myFont, command=lambda: on_click(check_var11, "hud_takesshots")).pack(anchor=W, padx=2)
# options for 2sd tab

info = Label(root, text="TF2 Config \n Generator \n -v. 0.0.1", font=title_text).pack(pady=5)
ask_path = Label(root, text="Укажите путь к папке с конфигами TF2 \n (обычно это: \n 'Steam/steamapps/common \n /Team Fortress 2/tf/cfg')").pack(pady=5)
browsebutton = Button(root, text="Обзор...", font=myFont, command=browsefunc).pack()
btn = Button(root, text="Сохранить", font=myFont, command=done).pack(side=LEFT, anchor=S, pady=5, padx=5)
exit1 = Button(root, text="Выйти", font=myFont, command=root.quit).pack(side=LEFT, anchor=S, pady=5)

root.mainloop()  # main app loop