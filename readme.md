# DÜSK - Düsseldorfer Schülerinventar (Desktop-Version)



Eine Desktop-Anwendung für das **Düsseldorfer Schülerinventar (DÜSK)** - ein Instrument zur Erfassung von Schülerkompetenzen durch Selbst- und Fremdeinschätzung.

## 📋 Inhaltsverzeichnis

- [Über das Projekt](#-über-das-projekt)
- [Features](#-features)
- [Technische Voraussetzungen](#-technische-voraussetzungen)
- [Starten der Anwendung](#-starten-der-anwendung)
- [Bedienungsanleitung](#-bedienungsanleitung)
- [API-Endpunkte](#-api-endpunkte)
- [Datenbankstruktur](#-datenbankstruktur)
- [Normtabellen](#-normtabellen)
- [Fehlerbehandlung](#-fehlerbehandlung)


## 🎯 Über das Projekt

Das Düsseldorfer Schülerinventar (DÜSK) ist ein diagnostisches Instrument zur Erfassung von Schülerkompetenzen in sechs Bereichen:

1. **Arbeitsverhalten** - Zuverlässigkeit, Arbeitstempo, Arbeitsplanung, Organisation
2. **Lernverhalten** - Selbstständigkeit, Belastbarkeit, Konzentration
3. **Sozialverhalten** - Teamfähigkeit, Hilfsbereitschaft, Kommunikation
4. **Fachkompetenz** - Schreiben, Lesen, Mathematik, Naturwissenschaften
5. **Personale Kompetenz** - Eigeninitiative, Leistungsbereitschaft, Reflexion
6. **Methodenkompetenz** - Problemlösung, Abstraktion, Präsentation

Die Anwendung ermöglicht die Erfassung von **Selbsteinschätzung (SE)** und **Fremdeinschätzung (FE)** über 36 Items und berechnet daraus Profilwerte im Vergleich zu Normtabellen (Hauptschule/Förderschule).

## ✨ Features

| Funktion | Beschreibung |
|----------|--------------|
| 🔐 **Login** | Authentifizierung mit Benutzername/Passwort (Gastzugang: gast/gast) |
| 📋 **Profilübersicht** | Tabellarische Liste aller Profile mit Name, Gruppe und ID |
| ➕ **Neues Profil** | Vollständige Erfassung aller 36 Items für SE und FE |
| ✏️ **Profil bearbeiten** | Nachträgliche Änderung vorhandener Profile |
| 👁️ **Profil anzeigen** | Detaillierte Ansicht mit SE/FE-Tabellen, Statistik und Items |
| 📊 **Korrelation** | Berechnung der Übereinstimmung zwischen SE und FE |
| 📈 **Zeitreihe** | Verlaufsdarstellung aller Profile einer Gruppe |
| 👥 **Gruppenverwaltung** | Gruppen hinzufügen, löschen und zuordnen |
| 🖥️ **Reine Textdarstellung** | Keine Grafiken, nur klare Tabellen und Texte |

## 💻 Technische Voraussetzungen

- **Python 3.8 oder höher**
- **Internetverbindung** (für API-Zugriff auf `https://paul-koop.org/api/`)
- **Betriebssystem**: Windows, macOS, Linux

### Benötigte Python-Pakete (werden automatisch installiert)

```
requests >= 2.25.0
```

Die GUI verwendet **tkinter** - dies ist in der Standard-Python-Installation enthalten.

Die Anwendung öffnet sich mit einem Login-Fenster.

## 📖 Bedienungsanleitung

### Login

| Feld | Standardwert | Beschreibung |
|------|--------------|--------------|
| Benutzername | `gast` | Ihr persönlicher Benutzername |
| Passwort | `gast` | Ihr persönliches Passwort |

> **Hinweis:** Bei der ersten Anmeldung mit neuen Zugangsdaten wird automatisch ein Benutzerkonto erstellt.

### Hauptfenster

Nach erfolgreichem Login sehen Sie eine Tabelle mit allen Ihren Profilen.

**Toolbar-Buttons:**
- **Neues Profil** - Erstellt ein neues Profil
- **Aktualisieren** - Lädt die Profilliste neu
- **Gruppen verwalten** - Öffnet den Gruppenmanager
- **Abmelden** - Beendet die Sitzung

**Aktionen pro Profil (Buttons unter der Tabelle):**
- **Anzeigen** - Zeigt das komplette Profil mit allen Details
- **Bearbeiten** - Ändert die Item-Werte des Profils
- **Löschen** - Entfernt das Profil (mit Bestätigung)
- **Zeitreihe** - Zeigt alle Profile der gleichen Gruppe

### Neues Profil / Profil bearbeiten

1. **Profil-Informationen**
   - Name des Schülers/der Schülerin
   - Auswahl einer vorhandenen Gruppe oder Erstellung einer neuen Gruppe

2. **Selbsteinschätzung (36 Items)**
   - Bewertungsskala: 4 = trifft voll zu, 3 = trifft zu, 2 = trifft teilweise zu, 1 = trifft nicht zu
   - Standardwert ist 2 (trifft teilweise zu)

3. **Fremdeinschätzung (36 Items)**
   - Gleiche Bewertungsskala wie bei Selbsteinschätzung

### Profil anzeigen

Die Profilansicht ist in vier Reiter unterteilt:

#### 1. Selbsteinschätzung (SE)
- Tabelle mit X-Markierungen für die 6 Kompetenzen (Werte 1-5)
- Textuelle Zusammenfassung der Werte

#### 2. Fremdeinschätzung (FE)
- Gleiche Darstellung wie bei SE

#### 3. Statistik
- **Korrelation** - Statistischer Zusammenhang zwischen SE und FE (Werte zwischen -1 und 1)
- **Übereinstimmung** - Prozentuale Übereinstimmung der 36 Items
- **Interpretation** - Verständliche Erklärung der Ergebnisse
- **Auswertung** - Detaillierte Bewertung jeder Kompetenz

#### 4. Alle Items
- Vollständige Liste aller 36 Items mit SE- und FE-Werten

**Normauswahl:** Oben rechts können Sie zwischen **Hauptschule (HS)** und **Förderschule (FS)** wechseln - die Profilwerte werden neu berechnet.

### Zeitreihe

Zeigt alle Profile einer Gruppe mit ihren Kompetenzwerten:
- Profil-ID
- Name
- Werte für alle 6 Kompetenzen (1-5)

Ideal zur Verlaufsbeobachtung einer Person über mehrere Messzeitpunkte.

### Gruppenverwaltung

- **Hinzufügen** - Neue Gruppe mit Namen erstellen
- **Löschen** - Vorhandene Gruppe entfernen (nur möglich, wenn keine Profile mehr enthalten sind)

## 🔌 API-Endpunkte

Die Anwendung kommuniziert mit folgenden API-Endpunkten:

| Endpunkt | Methode | Beschreibung |
|----------|---------|--------------|
| `api_login.php` | POST | Authentifizierung und Session-Erstellung |
| `api_profiles.php` | GET | Liste aller Profile oder Einzelprofil |
| `api_profiles.php` | POST | Neues Profil erstellen |
| `api_profiles.php` | PUT | Profil aktualisieren |
| `api_profiles.php` | DELETE | Profil löschen |
| `api_groups.php` | GET | Gruppenliste abrufen |
| `api_groups.php` | POST | Neue Gruppe erstellen |
| `api_groups.php` | DELETE | Gruppe löschen |
| `api_logout.php` | POST | Session beenden |

## 🗄️ Datenbankstruktur

Die Anwendung nutzt folgende MySQL-Tabellen:

### `user`
| Feld | Typ | Beschreibung |
|------|-----|--------------|
| ID | INT | Primärschlüssel |
| user | VARCHAR(50) | Benutzername |
| pass | VARCHAR(50) | Passwort |

### `anmeldung`
| Feld | Typ | Beschreibung |
|------|-----|--------------|
| sessionID | INT | Primärschlüssel |
| userID | INT | Fremdschlüssel zu user.ID |
| session | VARCHAR(50) | Session-Token |

### `gruppe`
| Feld | Typ | Beschreibung |
|------|-----|--------------|
| gruppeID | INT | Primärschlüssel |
| userID | INT | Fremdschlüssel zu user.ID |
| name | VARCHAR(50) | Gruppenname |

### `profil`
| Feld | Typ | Beschreibung |
|------|-----|--------------|
| profilID | INT | Primärschlüssel |
| userID | INT | Fremdschlüssel zu user.ID |
| gruppeID | INT | Fremdschlüssel zu gruppe.gruppeID |
| name | VARCHAR(50) | Profilname |
| item1..item36 | INT | Selbsteinschätzung (1-4) |
| feitem1..feitem36 | INT | Fremdeinschätzung (1-4) |
| kompetenz1..kompetenz6 | INT | Berechnete Kompetenzwerte (1-5) |

### Normtabellen
- `normSEhs`, `normFEhs` - Hauptschule-Normen
- `normSEfs`, `normFEfs` - Förderschule-Normen

## 📊 Normtabellen

### Hauptschule (HS)

| Kompetenz | p1 | p2 | p3 | p4 | p5 |
|-----------|----|----|----|----|----|
| Arbeitsverhalten | 21.33 | 25.33 | 29.33 | 33.32 | 37.32 |
| Lernverhalten | 20.87 | 24.95 | 29.03 | 33.13 | 37.18 |
| Sozialverhalten | 17.93 | 21.37 | 24.80 | 28.23 | 31.67 |
| Fachkompetenz | 13.98 | 17.71 | 21.44 | 25.17 | 28.90 |
| Personale Kompetenz | 24.60 | 28.55 | 33.04 | 37.53 | 42.01 |
| Methodenkompetenz | 15.53 | 18.97 | 22.40 | 25.83 | 29.27 |

### Förderschule (FS)

| Kompetenz | p1 | p2 | p3 | p4 | p5 |
|-----------|----|----|----|----|----|
| Arbeitsverhalten | 17.54 | 24.03 | 30.53 | 37.02 | 43.51 |
| Lernverhalten | 17.80 | 24.26 | 30.73 | 37.19 | 43.65 |
| Sozialverhalten | 18.03 | 22.41 | 26.79 | 31.17 | 35.55 |
| Fachkompetenz | 14.28 | 15.55 | 16.83 | 18.10 | 19.37 |
| Personale Kompetenz | 20.69 | 27.49 | 34.29 | 41.09 | 47.89 |
| Methodenkompetenz | 12.44 | 18.06 | 23.68 | 29.29 | 34.91 |

## ⚠️ Fehlerbehandlung

Die Anwendung behandelt folgende Fehlersituationen:

| Fehler | Anzeige | Lösung |
|--------|---------|--------|
| Keine Internetverbindung | "Verbindungsfehler" | Internetverbindung prüfen |
| Falsche Login-Daten | "Anmeldung fehlgeschlagen" | Benutzername/Passwort prüfen |
| API nicht erreichbar | "HTTP Fehler" | Server-Status prüfen |
| Kein Profil ausgewählt | "Bitte wählen Sie ein Profil aus" | Profil in Tabelle markieren |

