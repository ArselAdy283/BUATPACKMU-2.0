import uuid
import tkinter as tk

# ============================
# =========== GUI ============
# ============================

root = tk.Tk()
root.geometry("600x400")
root.title("BUATBACKMU")

menu = tk.Frame(root)
generator_UUID = tk.Frame(root)
template_RP = tk.Frame(root)
mcpack = tk.Frame(root)

def show_frame(frame):
    frame.tkraise()

# ISI MENU
label_menu = tk.Label(menu, text="BUATPACKMU", font=("Arial", 25))
label_menu.pack(padx=180, pady=30)

buttonUUID = tk.Button(menu, text="Generate UUID", width=30, font=("Arial", 15), command=lambda: show_frame(generator_UUID))
buttonUUID.pack(pady=10)
buttonBuatRP = tk.Button(menu, text="Template ResourcePack", width=30, font=("Arial", 15), command=lambda: show_frame(template_RP))
buttonBuatRP.pack(pady=10)
buttonMcPack = tk.Button(menu, text="Buat MCPACK", width=30, font=("Arial", 15), command=lambda: show_frame(mcpack))
buttonMcPack.pack(pady=10)

# ISI GENERATE UUID
label_uuid = tk.Label(generator_UUID, text="Generate UUID", font=("Arial", 25))
label_uuid.pack()

# ISI TEMPLATE RP
label_rp = tk.Label(template_RP, text="Template ResourcePack", font=("Arial", 25))
label_rp.pack()

# ISI MCPACK
label_mcpack = tk.Label(mcpack, text="Buat MCPACK", font=("Arial", 25))
label_mcpack.pack()

for frame in (menu, generator_UUID, template_RP, mcpack):
    frame.grid(row=0, column=0, sticky='nsew')

show_frame(menu)

root.mainloop()