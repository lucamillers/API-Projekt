<h1># RestAPI</h1>
Schulprojekt der IFA01, LF9 (Herr Wichmann) zur Erstellung einer Rest-API

<h2>Entwurf und Implementierung einer REST-Schnittstelle</h2>

Es soll eine REST-Schnittstelle (Application Programming Interface, API) für
eine Todo-Listen-Verwaltung entworfen und implementiert werden. Der Ent-
wurf soll gemäß der OpenAPI-Specification umgesetzt werden. Dieser Standard
dient der Beschreibung REST-konformer Programmierschnittstellen. Damit
kann eine API hersteller- und plattformunabhängig dokumentiert werden.
Die Implementierung erfolgt in der Programmiersprache Python mit der Biblio-
thek Flask.

<h3>① Git-Repository einrichten</h3>
Die zu erstellenden Spezifikation und der Quellcode für den Server in Python sollen in einem Git-Repository
gespeichert und versioniert werden. Das Repository muss öffentlich erreichbar und lesbar sein, am einfachsten
umzusetzen ist die Nutzung von Github. Die Abgabe des Projektergebnisses erfolgt über das Zusenden der
URL des Repository.

<h3>② API entwerfen</h3>
<b>Folgende Beschreibung der Schnittstelle ist gegeben:</b>

<li>Es soll eine Server-Anwendung erstellt werden, mit deren Hilfe Todo-Listen mit entsprechenden Einträgen erstellt und bearbeitet werden können. </li>
<li>Jede Liste besteht aus einer beliebigen Anzahl an Einträgen und ist einem Benutzer zugewiesen.</li>
<li>Jeder Eintrag einer Todo-Liste besteht aus einer ID, einem Namen, einer optionalen Beschreibung und der Zuordnung zu einer Todo-Liste und einem Benutzer. </li>
<li>Jede To-do-Liste und jeder Benutzer besitzt neben der ID einen Namen.</li>
<li>Die Schnittstelle muss es ermöglichen, Listen neu anzulegen und bestehende Listen zu löschen. </li>
<li>Über einen Endpunkt können alle Einträge der Liste geladen werden. </li>
<li>Außerdem müssen Einträge in Listen hinzugefügt und gelöscht werden können.</li>
<li>Für die Festlegung der Listenbesitzer müssen neue Benutzer hinzugefügt und gelöscht und es muss eine Liste aller vorhandenen Benutzer abgefragt werden können.</li>
<li>Eine Authentifizierung ist zunächst nicht zu planen bzw. implementieren. </li>
<li>Aus Sicherheitsgründen sollen jedoch für alle verwendeten IDs keine fortlaufenden Nummern verwendet werden. Stattdessen werden zufällige GUID genutzt.</li>
  
Um die Schnittstelle zu spezifizieren, müssen zunächst alle Endpunkten festgelegt werden:

### Entwurf und Implementierung einer REST-Schnittstelle ###

![grafik](https://user-images.githubusercontent.com/79851320/152154251-db2d42ef-4941-4654-9d19-79516b55f039.png)

Für das Erstellen der Spezifikation reicht ein einfacher Text-Editor. Für ein besseres Syntax-Highlighting und
automatisches Einrücken wird Visual Studio Code mit entsprechenden Plugins empfohlen. Als Vorlage und Aus-
gangspunkt kann eine Beispieldatei des Swagger-Projektes genutzt werden: Petstore API1.

<h3>③ Implementierung mit Python+Flask</h3>
Nach der Spezifikation der Schnittstelle kann die Implementierung in Python umgesetzt werden. Dazu ist die
Bibliothek Flask zu nutzen. Das Programm muss Daten nicht dauerhaft speichern. Eine Speicherung während
der Laufzeit des Programm reicht aus. Zur Speicherung von JSON-Objekten bietet sich in Python die Daten-
struktur Dictionary2 an. Diese Objekte lassen sich auch in Listen zusammenfassen:<br>

![grafik](https://user-images.githubusercontent.com/79851320/152155341-10250436-4450-4f09-b008-b3126122d7f7.png)

<h3>④ Implementierung eines Clients in einer beliebigen Programmiersprache [Bonusaufgabe]</h3>
