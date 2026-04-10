import tkinter as tk
from traceback import format_tb

FF = tk.Tk()
FF.title("")
FF.geometry("800x800")
page = tk.LabelFrame(FF, bg="peachpuff")
page.pack(side="top")

TitreSalle = tk.Label(page, text="Supervision de la salle T/H/P", font=("Arial", 15), bg="peachpuff")
TitreSalle.pack(side="top")



Config = tk.LabelFrame(page,text="Configuration", bg="seashell3")
Config.pack(side="bottom")

AlarmSttus = tk.Label(Config, text="RAS", bg="greenyellow", bd=2)
AlarmSttus.pack(padx=10, pady=5, side="left")
VitesseTexte = tk.Label(Config, text="Vitesse de transmission")
VitesseTexte.pack(padx=10, pady=5, side="left")
ChoixVitesse = tk.Entry(Config, font=("Arial", 15))
ChoixVitesse.pack(padx=10, pady=5)
Port = tk.Label(Config, text="Port")
Port.pack(padx=10, pady=5)
ChoixPort = tk.Entry(Config, font=("Arial", 15))
ChoixPort.pack(padx=10, pady=5, side="right")
ReqModbus = tk.LabelFrame(page, text="Requête modbus", bg="seashell3")
ReqModbus.pack(fill="both", expand="yes")
Ktexte = tk.Label(ReqModbus, text="Requête")
Ktexte.pack(padx=10, pady=5, side="left")
Requete = tk.Entry(ReqModbus, font=("Arial", 15))
requetesend = tk.Button(ReqModbus, text="Envoyer")
requetesend.pack(padx=10, pady=5, side="right")
Requete.pack(padx=20, pady=5, side="left")
Donnees = tk.LabelFrame(page, text="Données", bg="seashell3")
Donnees.pack(fill="both", expand="yes")
Reponse = tk.Label(Donnees, text="Reponse")
Reponse.pack(padx=10, pady=5, side="left")






FF.mainloop()
