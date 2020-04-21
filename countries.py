import random
dictionary={"Islandia":"Rejkiawik","Irlandia":"Dublin","Portugalia":"Lisbona",
"Hiszpania":"Madryt", "Wielka Brytania":"Londyn", "Francja":"Paryż","Holandia":"Amsterdam",
"Belgia":"Bruksela","Szwajcaria":"Berno","Liechtenstein":"Vaduz","Malta":"Valletta",
"Azerbejdżan":"Baku","Armenia":"Erywan","Liban":"Bejrut","Izrael":"Tel Awiw","Syria":"Damaszek",
"Jordania":"Amman","Oman":"Maskat","ZEA":"Abu-Zabi","Bahrajn":"Al-Manama","Katar":"Al.-Dauha",
"Iran":"Teheran","Kazachstan":"Ałma-Ata(Astana)","Uzbekistan":"Taszkent","Kirgistan":"Biszkek",
"Turkmenistan":"Aszchabad","Tadżykistan":"Duszanbe","Tajwan":"Tajpej","Indonezja":"Dzakarta",
"Sri Lanka":"Kolombo","Nepal":"Katmandu","Bhutan":"Thimphu","Chiny":"Pekin","Mongolia":"Ułan-Bator",
"Maroko":"Rabat","Algieria":"Algier","Tunezja":"Tunis","Mali":"Bamako","Niger":"Niamej",
"Czad":"Ndżamena","Sudan":"Chartum","Erytrea":"Asmara","Senegal":"Dakar","Gambia":"Bandżul","Burkina Faso":"Wagadugu",
"Ghana":"Akra","Togo":"Lome","Benin":"Porto Novo","Nigeria":"Abudża","Kamerun":"Jaunde","Rep.Środ.-Afr.":"Bangi",
"Etiopia":"Addis Abeba","Kenia":"Nairobi","Tanzania":"Dodoma","Angola":"Luanada","Zambia":"Lusaka",
"Malawi":"Lilongwe","Namibia":"Windhuk","Bostwana":"Gaborone","Zimbabwe":"Harare","Mozambik":"Maputo",
"Madagaskar":"Antanarywa","RPA":"Pretoria","Suazi":"Mbabane","Lesoto":"Maseru","Kanada":"Ottawa","USA":"Waszyngton",
"Polska":"Warszawa","Indie":"Delhi","Meksyk":"Meksyk","Kolumbia":"Bogota","Wenezuela":"Caracas","Gujana":"Georgetown",
"Surinam":"Paramaribo","Gujana Francuska":"Kajenna","Ekwador":"Quito","Peru":"Lima","Brazylia":"Brasilia",
"Boliwia":"La Paz","Chile":"Santiago","Argentyna":"Buenos Aires","Paragwaj":"Asuncion","Urugwaj":"Montevideo",
"Australia":"Canberra","Nowa Gwinea":"Port Moresby","Nowa Zelandia":"Wellington"}

panstwa=list(dictionary.keys())
random.shuffle(panstwa)
print()
imie=input("podaj imie\n")
print()
print(imie,"WITAJ W QUIZIE PANSTWA MIASTA!!")
suma_dobrych_odp=[]
# suma_zlych_odp=[]

for question in range(10):
	print()
	print("Jaka jest stolica: ",panstwa[question],"?\n")
	correctAnswer=dictionary[panstwa[question]]
	# print(correctAnswer)
	wrongAnswers=list(dictionary.values())
	del wrongAnswers[wrongAnswers.index(correctAnswer)]
	wrongAnswers=random.sample(wrongAnswers,4)
	allAnswer=wrongAnswers+[correctAnswer]
	
	random.shuffle(allAnswer)
	# print(allAnswer)
	
	ABC=["A","B","C","D","E"]
	
	for i in range(5):
		print(ABC[i],". ",allAnswer[i])
		
	while True:
		odpowiedz=input("\n")
		odpowiedz=odpowiedz.upper()
		if odpowiedz not in ABC:
			print("podaj A,B,C,D lub E")
			continue
		else:
			break
	
	index=allAnswer.index(correctAnswer)
	odp_poprawna=ABC[index]
	dobra_lista=["Swietnie!","Brawo","Dobrze","Nieżle"]
	zla_lista=["Zlee!!","OMG nie","chyba żartujesz?","no co ty"]
	
	if odpowiedz==odp_poprawna:
		print(random.choice(dobra_lista),"\n")
		suma_dobrych_odp.append(odpowiedz)
	else:
		print(random.choice(zla_lista),"\npoprawna odpowiedz to: ",odp_poprawna,"\n")
		# suma_zlych_odp.append(odpowiedz)
	
dobre=len(suma_dobrych_odp)
koniec=["Ale z Ciebie Nieuk","Mogłoby byc lepiej","Nieżle", "Brawo, Jestes mistrzem"]
print("TWOJ WYNIK TO: ", dobre,"/",10)
if dobre==10:
	print(koniec[3],imie)
elif dobre<9 and dobre>6:
	print(koniec[2],imie)
elif dobre>3 and dobre<7:
	print(koniec[1],imie)
else:
	print(koniec[0],imie)