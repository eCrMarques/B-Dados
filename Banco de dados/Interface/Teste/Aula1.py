import customtkinter
from PIL import ImageTk, Image
janela = customtkinter.CTk()
customtkinter.set_appearance_mode("light")
janela
image=Image.open("Teste/Calendario.jpg")
photo=ImageTk.PhotoImage(image)
janela.bbox()

btn = customtkinter.CTkButton(janela,text="Ola",image=photo)
btn.pack()
print(btn._clicked())
janela.mainloop()
