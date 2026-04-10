import tkinter as tk
import modbus

status_word = 0
alarmCode = 0
temperature = 0
humidite = 0
pression = 0

port="COM4"
baudrate = 9600
requete = bytes([0x01, 0x03, 0x00, 0x00, 0x00, 0x05, 0x85, 0xC9])
reponse_modbus = ""

def envoyer_requete():
    global port
    global reponse_modbus
    reponse_modbus = modbus.envoyer_trame(port, baudrate, requete)

FF = tk.Tk()
FF.title("")
FF.geometry("680x400")
page = tk.LabelFrame(FF, bg="peachpuff")
page.pack(expand=True, fill=tk.X)

TitreSalle = tk.Label(page, text="Supervision de la salle T/H/P", font=("Arial", 15), bg="peachpuff")
TitreSalle.pack(expand=True)

#*****************************Zone Message**************************************************************
frame_alarme = tk.LabelFrame(page, bg="seashell3")
frame_alarme.pack(fill="both", expand=True)
AlarmSttus = tk.Label(frame_alarme, text="RAS", bg="greenyellow")
AlarmSttus.pack(padx=10, pady=5, side="left")
message_user = tk.Label(frame_alarme, text="Message à l'affiche de l'utilisateur", bg="seashell3")
message_user.pack(padx=50, pady=5, side="left")


#*****************************Zone configuration**************************************************************
frame_configuration = tk.LabelFrame(page, text="Configuration", bg="seashell3")
frame_configuration.pack(fill="both", expand=True)
VitesseBauds = tk.Label(frame_configuration, text="Vitesse de transmission")
VitesseBauds.pack(padx=10, pady=5, side="left")
ChoixVitesse = tk.Entry(frame_configuration, font=("Arial", 15))
ChoixVitesse.pack(padx=10, pady=5, side="left")
#ChoixVitesse.bind("<Return>", )
Port = tk.Label(frame_configuration, text="Port :")
Port.pack(padx=10, pady=5, side="left")
ChoixPort = tk.Entry(frame_configuration, font=("Arial", 15))
ChoixPort.pack(padx=10, pady=5, side="left")
#ChoixPort.bind("<return>", )

#*****************************Zone Requête**************************************************************

frame_requetemdb = tk.LabelFrame(page, text="Requête modbus", bg="seashell3")
frame_requetemdb.pack(fill="both", expand=True)
request_texte = tk.Label(frame_requetemdb, text="Requête :")
request_texte.pack(padx=10, pady=5, side="left")
requete_entry = tk.Entry(frame_requetemdb, font=("Arial", 15))
requete_entry.pack(padx=10, pady=5, side="left")
requete_entry.insert(0, requete.hex())


requete_send = tk.Button(frame_requetemdb, text="Envoyer",command=envoyer_requete)
requete_send.pack(padx=10, pady=5, side="right")

#*****************************Zone Données**************************************************************

frame_donnees = tk.LabelFrame(page, text="Données", bg="seashell3")
frame_donnees.pack(fill="both", expand=True)
sous_frame_reponse = tk.LabelFrame(frame_donnees, bg="seashell3")
sous_frame_reponse.pack(fill="both", expand=True)
Reponse_label = tk.Label(sous_frame_reponse, text="Reponse :")
Reponse_label.pack(padx=10, pady=5)
requete_reponse = tk.Label(sous_frame_reponse, text="")
requete_reponse.pack(padx=10, pady=5)


#**************************************Température****************************************************
sous_frame_temperature = tk.LabelFrame(frame_donnees, bg="seashell3")
sous_frame_temperature.pack(fill="both", expand=True, padx=10, pady=5, side = "left")
temperature_data = tk.Label(sous_frame_temperature, text="")
temperature_data.pack(padx=10, pady=5)

#**************************************Humidité****************************************************
sous_frame_humidite = tk.LabelFrame(frame_donnees, bg="seashell3")
sous_frame_humidite.pack(fill="both", expand=True, padx=10, pady=5, side = "left")
humidite_data = tk.Label(sous_frame_temperature, text="")
humidite_data.pack(padx=10, pady=5)

#**************************************Pression****************************************************
sous_frame_pression = tk.LabelFrame(frame_donnees, bg="seashell3")
sous_frame_pression.pack(fill="both", expand=True, padx=10, pady=5, side = "right")
pression_data = tk.Label(sous_frame_temperature, text="")
pression_data.pack(padx=10, pady=5)

t


FF.mainloop()
