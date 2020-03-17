import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter.font as font


def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))


def on_configure1(event):
    canvas1.configure(scrollregion=canvas1.bbox('all'))


def on_configure2(event):
    canvas2.configure(scrollregion=canvas2.bbox('all'))


root = tk.Tk()
root.geometry('900x400+200+100')
root.resizable(0, 0)
root.title("TF2CFG Generator")
root.iconbitmap('icon.ico')
note = ttk.Notebook(root)

tab1 = Canvas(note, highlightthickness=0)
tab2 = Canvas(note, highlightthickness=0)
tab3 = Canvas(note, highlightthickness=0, height=10000)

canvas = tk.Canvas(tab1, width=600, height=900, highlightthickness=0)
canvas.pack(side=tk.LEFT)
scrollbar = tk.Scrollbar(tab1, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill='y')
canvas.configure(yscrollcommand = scrollbar.set)
canvas.bind('<Configure>', on_configure)
frame = tk.Frame(canvas, width=700)
canvas.create_window((0,0), window=frame, anchor='nw')

canvas1 = tk.Canvas(tab2, width=600, height=900, highlightthickness=0)
canvas1.pack(side=tk.LEFT)
scrollbar1 = tk.Scrollbar(tab2, command=canvas1.yview)
scrollbar1.pack(side=tk.RIGHT, fill='y')
canvas1.configure(yscrollcommand = scrollbar1.set)
canvas1.bind('<Configure>', on_configure1)
frame1 = tk.Frame(canvas1, width=700)
canvas1.create_window((0,0), window=frame1, width=700, anchor='nw')

canvas2 = tk.Canvas(tab3, width=600, height=900, highlightthickness=0)
canvas2.pack(side=tk.LEFT, fill='y')
scrollbar2 = tk.Scrollbar(tab3, command=canvas2.yview)
scrollbar2.pack(side=tk.RIGHT, fill='y')
canvas2.configure(yscrollcommand = scrollbar2.set)
canvas2.bind('<Configure>', on_configure2)
frame2 = tk.Frame(canvas2, width=700)
canvas2.create_window((0,0), window=frame2, width=700, anchor='nw')


title_text = font.Font(family='TF2 Build', size=15)
myFont = font.Font(family='TF2 Build')
note.add(tab1, text="Графика")
note.add(tab2, text="Интерфейс")
note.add(tab3, text="Геймплей")
note.config(width=650)
note.pack(side=LEFT, fill=BOTH, pady=5, padx=5,)


preset_configs = {
    "r_waterdrawreflection": "0",
    "r_waterforceexpensive": "0",
    "r_shadowrendertotexture": "0",
    "r_shadows": "0",
    "r_drawflecks": "0",
    "r_dynamic": "0",
    "r_drawmodeldecals": "0",
    "r_renderoverlayfragment": "0",
    "r_3dsky": "0",
    "r_lightaverage": "0",
    "r_flashlightdepthtexture": "0",
    "r_ropetranslucent": "0",
    "r_ForceWaterLeaf": "0",
    "r_ambientboost": "0",
    "r_drawdetailprops": "0",
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


folder_path = str()


def on_click(toggle, key_set):
    if toggle.get() == 1:
        preset_configs[key_set] = "1"
    else:
        preset_configs[key_set] = "0"


def done():
    main_config = open(folder_path+"/autoexec.cfg", 'w')
    for key in preset_configs:
        main_config.write(key + ' ' + preset_configs[key] + '\n')
    main_config.close()


check_var = IntVar()
check = Checkbutton(frame, text='Отражения на воде', onvalue=1, offvalue=0, variable=check_var, font=myFont, command=lambda: on_click(check_var, "r_waterdrawreflection")).pack(anchor=W, padx=2, ipady=5)
check_var1 = IntVar()
check1 = Checkbutton(frame, text='Продвинутые отражения на воде', onvalue=1, offvalue=0, variable=check_var1, font=myFont, command=lambda: on_click(check_var1, "r_waterforceexpensive")).pack(anchor=W, padx=2, ipady=5)
check_var2 = IntVar()
check2 = Checkbutton(frame, text='Динамические тени на объектах', onvalue=1, offvalue=0, variable=check_var2, font=myFont, command=lambda: on_click(check_var2, "r_shadowrendertotexture")).pack(anchor=W, padx=2, ipady=5)
check_var3 = IntVar()
check3 = Checkbutton(frame, text='Динамические тени на местности', onvalue=1, offvalue=0, variable=check_var3, font=myFont, command=lambda: on_click(check_var3, "r_shadows")).pack(anchor=W, padx=2, ipady=5)
check_var4 = IntVar()
check4 = Checkbutton(frame, text='Прорисовка мелких осколков и пыли при попадании пули', onvalue=1, offvalue=0, variable=check_var4, font=myFont, command=lambda: on_click(check_var4, "r_drawflecks")).pack(anchor=W, padx=2, ipady=5)
check_var5 = IntVar()
check5 = Checkbutton(frame, text='Детализация мелких предметов', onvalue=1, offvalue=0, variable=check_var5, font=myFont, command=lambda: on_click(check_var5, "r_drawdetailprops")).pack(anchor=W, padx=2, ipady=5)
check_var24 = IntVar()
check24 = Checkbutton(frame, text='Динамические отсветы от объектов', onvalue=1, offvalue=0, variable=check_var24, font=myFont, command=lambda: on_click(check_var24, "r_dynamic")).pack(anchor=W, padx=2, ipady=5)
check_var25 = IntVar()
check25 = Checkbutton(frame, text='"Деколы" (детали) на моделях игроков', onvalue=1, offvalue=0, variable=check_var25, font=myFont, command=lambda: on_click(check_var25, "r_drawmodeldecals")).pack(anchor=W, padx=2, ipady=5)
check_var26 = IntVar()
check26 = Checkbutton(frame, text='Наложенные на текстуры объекты (плакаты на стенах и т.д.)', onvalue=1, offvalue=0, variable=check_var26, font=myFont, command=lambda: on_click(check_var26, "r_renderoverlayfragment")).pack(anchor=W, padx=2, ipady=5)
check_var27 = IntVar()
check27 = Checkbutton(frame, text='3D фон (например здания)', onvalue=1, offvalue=0, variable=check_var27, font=myFont, command=lambda: on_click(check_var27, "r_3dsky")).pack(anchor=W, padx=2, ipady=5)
check_var28 = IntVar()
check28 = Checkbutton(frame, text='Детализация мелких предметов', onvalue=1, offvalue=0, variable=check_var28, font=myFont, command=lambda: on_click(check_var28, "r_lightaverage")).pack(anchor=W, padx=2, ipady=5)
check_var29 = IntVar()
check29 = Checkbutton(frame, text='Усреднение света', onvalue=1, offvalue=0, variable=check_var29, font=myFont, command=lambda: on_click(check_var29, "r_flashlightdepthtexture")).pack(anchor=W, padx=2, ipady=5)
check_var30 = IntVar()
check30 = Checkbutton(frame, text='Глубина освещения текстур', onvalue=1, offvalue=0, variable=check_var30, font=myFont, command=lambda: on_click(check_var30, "r_ropetranslucent")).pack(anchor=W, padx=2, ipady=5)
check_var31 = IntVar()
check31 = Checkbutton(frame, text='Прозрачность канатов', onvalue=1, offvalue=0, variable=check_var31, font=myFont, command=lambda: on_click(check_var31, "r_ForceWaterLeaf")).pack(anchor=W, padx=2, ipady=5)
check_var32 = IntVar()
check32 = Checkbutton(frame, text=' Качество обзора находясь под водой', onvalue=1, offvalue=0, variable=check_var32, font=myFont, command=lambda: on_click(check_var32, "r_ambientboost")).pack(anchor=W, padx=2, ipady=5)


check_var6 = IntVar()
check6 = Checkbutton(frame1, text='Показывать количество нанесённого урона над врагом', onvalue=1, offvalue=0, variable=check_var6, font=myFont, command=lambda: on_click(check_var6, "hud_combattext")).pack(anchor=W, padx=2, ipady=5)
check_var7 = IntVar()
check7 = Checkbutton(frame1, text='Переключить наложение текста урона друг на друга в\nпределах 0.10 сек. интервала', justify=LEFT, onvalue=1, offvalue=0, variable=check_var7, font=myFont, command=lambda: on_click(check_var7, "hud_combattext_batching")).pack(anchor=W, padx=2, ipady=5)
check_var8 = IntVar()
check8 = Checkbutton(frame1, text='Быстрое переключение оружия (только колёсиком мыши)', onvalue=1, offvalue=0, variable=check_var8, font=myFont, command=lambda: on_click(check_var8, "hud_fastswitch")).pack(anchor=W, padx=2, ipady=5)
check_var9 = IntVar()
check9 = Checkbutton(frame1, text='Переключить текст лечения союзников', onvalue=1, offvalue=0, variable=check_var9, font=myFont, command=lambda: on_click(check_var9, "hud_combattext_healing")).pack(anchor=W, padx=2, ipady=5)
check_var10 = IntVar()
check10 = Checkbutton(frame1, text='Переключить накладывающиеся эффекты частиц,\nиспользуемые для критов и мини-критов', justify=LEFT, onvalue=1, offvalue=0, variable=check_var10, font=myFont, command=lambda: on_click(check_var10, "hud_combattext_doesnt_block_overhead_text")).pack(anchor=W, padx=2, ipady=5)
check_var11 = IntVar()
check11 = Checkbutton(frame1, text='Авто скриншот «tab» в конце карты', onvalue=1, offvalue=0, variable=check_var11, font=myFont, command=lambda: on_click(check_var11, "hud_takesshots")).pack(anchor=W, padx=2, ipady=5)

check_var12 = IntVar()
check12 = Checkbutton(frame2, text='Вопрос о добавлении сервера в чёрный список\nпосле недолгого пребывания на нём', justify=LEFT,  onvalue=1, offvalue=0, variable=check_var12, font=myFont, command=lambda: on_click(check_var12, "cl_ask_blacklist_opt_out")).pack(anchor=W, padx=2, ipady=5)
check_var13 = IntVar()
check13 = Checkbutton(frame2, text='вопрос о добавлении сервера в избранное\nпосле недолгого пребывания на нём', justify=LEFT, onvalue=1, offvalue=0, variable=check_var13, font=myFont, command=lambda: on_click(check_var13, "cl_ask_favorite_opt_out")).pack(anchor=W, padx=2, ipady=5)
check_var14 = IntVar()
check14 = Checkbutton(frame2, text='Автоматическая перезарядка, т.е.,\nодин выстрел активирует перезарядку', justify=LEFT,  onvalue=1, offvalue=0, variable=check_var14, font=myFont, command=lambda: on_click(check_var14, "cl_autoreload")).pack(anchor=W, padx=2, ipady=5)
check_var15 = IntVar()
check15 = Checkbutton(frame2, text='Возвращение в режим прицеливания у снайперской\nвинтовки после выстрела', justify=LEFT,  onvalue=1, offvalue=0, variable=check_var15, font=myFont, command=lambda: on_click(check_var15, "cl_autorezoom")).pack(anchor=W, padx=2, ipady=5)
check_var16 = IntVar()
check16 = Checkbutton(frame2, text='Разрешить частям тела гореть', onvalue=1, offvalue=0, variable=check_var16, font=myFont, command=lambda: on_click(check_var16, "cl_burninggibs")).pack(anchor=W, padx=2, ipady=5)
check_var17 = IntVar()
check17 = Checkbutton(frame2, text='Показать/убрать пользовательский\nинтерфейс (т.е. показ здоровья, патронов и т.п.)', justify=LEFT, onvalue=1, offvalue=0, variable=check_var17, font=myFont, command=lambda: on_click(check_var17, "cl_drawhud")).pack(anchor=W, padx=2, ipady=5)
check_var18 = IntVar()
check18 = Checkbutton(frame2, text='Режим отображения оружия обычный/противоположный\n(в левой руке)', justify=LEFT,  onvalue=1, offvalue=0, variable=check_var18, font=myFont, command=lambda: on_click(check_var18, "cl_flipviewmodels")).pack(anchor=W, padx=2, ipady=5)
check_var19 = IntVar()
check19 = Checkbutton(frame2, text='Новые эффекты повреждения поверхности,\nлучше всего заметно на стёклах', justify=LEFT,  onvalue=1, offvalue=0, variable=check_var19, font=myFont, command=lambda: on_click(check_var19, "cl_new_impact_effects")).pack(anchor=W, padx=2, ipady=5)
check_var20 = IntVar()
check20 = Checkbutton(frame2, text='Коллизии рагдоллов (трупов) (только у игрока)', onvalue=1, offvalue=0, variable=check_var20, font=myFont, command=lambda: on_click(check_var20, "cl_ragdoll_collide")).pack(anchor=W, padx=2, ipady=5)
check_var21 = IntVar()
check21 = Checkbutton(frame2, text='Цветовая подсветка предметов при обмене', onvalue=1, offvalue=0, variable=check_var21, font=myFont, command=lambda: on_click(check_var21, "cl_showbackpackrarities")).pack(anchor=W, padx=2, ipady=5)
check_var22 = IntVar()
check22 = Checkbutton(frame2, text='счётчик кадров в секунду', onvalue=1, offvalue=0, variable=check_var22, font=myFont, command=lambda: on_click(check_var22, "cl_showfps")).pack(anchor=W, padx=2, ipady=5)
check_var23 = IntVar()
check23 = Checkbutton(frame2, text='Показывать текущую позицию,\nугол обзора и скорость передвижения игрока', justify=LEFT, onvalue=1, offvalue=0, variable=check_var23, font=myFont, command=lambda: on_click(check_var23, "cl_showpos")).pack(anchor=W, padx=2, ipady=5)

info = Label(root, text="TF2 Config \n Generator \n -v. 0.0.1", font=title_text).pack(pady=5)
ask_path = Label(root, text="Укажите путь к папке с конфигами TF2 \n (обычно это: \n 'Steam/steamapps/common \n /Team Fortress 2/tf/cfg')").pack(pady=5)
browsebutton = Button(root, text="Обзор...", font=myFont, command=browsefunc).pack()
btn = Button(root, text="Сохранить", font=myFont, command=done).pack(side=LEFT, anchor=S, pady=5, padx=5)
exit1 = Button(root, text="Выйти", font=myFont, command=root.quit).pack(side=LEFT, anchor=S, pady=5)

root.mainloop()