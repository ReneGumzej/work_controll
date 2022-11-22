# Workstatus-Controll-Applikation zur Statusabfrage von Arbeitszuständen

## Beschreibung

Dieses Projet wurde aufgund einer räumlichen Trennung der Büros ins Leben gerufen und der damit verbundenen Problematik nicht zu wissen ob ein Mitglied des Teams sich gerade im Kundenservice/Problembehebung befindet.
Es soll eine Appliaktion erstellt werden in der Mitarbeiter den Arbeitsstatus andere Mitarbeiter der gleichen Abteilung einsehen können. Dafür soll eine Webapllikation erstellt werden die über das Intranet zugänglich ist.


## Funktionen

- Registrierung neuer Mitarbeiter (Email, Vorname, Nachnam, Passwort) durch den Admin
- Login für Admin und Mitarbeiter (Email, Passwort)
- Erstellung von Gruppen/Teams für die Statusüberwachung untereinander durch den Admin
- Teamname wird Angezeigt in der sich die Gruppe befindet
- Haupteite enthält Signalleuchten "Rot" und "Grün" und den Namen für jeden Mitarbeiter im Team
- Jeder Mitarbeiter kann nur seinen eigenen Status steuern 
- Es soll für jeden Mitarbeiter ein Textfeld zur Verfügung stehen, in der er seine Notizen zum Gespräch einfügen kann. Jede Notiz soll mit einem Zeitstempel versehen werden. 

Bibliotheken Installation: pip install --proxy=http://sophos.espera.de:8080 [Bib-Name]

Datenbank einrichten: 
- sqlalchemy importieren in vs code
- in dem Ordner der App(work_controll) im Terminal/CMD python aufrufen mit C:\Users\gumzej\AppData\Local\Programs\Python\Python310 
- Datenbank importieren mit "from [App Ordner] import db (db ist eine Instanz der SQLAlchemy Datenbank)
- mit db.create_all() alle in vs code erstellten Datenbanken erstellen
- mit "from work_controll.models import [Tabelle1], [Tabelle2], .." Tabellen in Datenbank importieren
- bsp.: department1 = Department(department='admin')
