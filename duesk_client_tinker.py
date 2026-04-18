#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Düsseldorfer Schülerinventar (DÜSK) - Tkinter Vollversion
Alle Funktionen: Login, Profile anzeigen/bearbeiten/löschen, 
Profilansicht mit Tabellen, Zeitreihe, Gruppenverwaltung
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import requests
import math

API_BASE_URL = "https://paul-koop.org/api/"

# Normwerte
NORM_SE_HS = {1: [21.33, 25.33, 29.33, 33.32, 37.32], 2: [20.87, 24.95, 29.03, 33.13, 37.18],
              3: [17.93, 21.37, 24.80, 28.23, 31.67], 4: [13.98, 17.71, 21.44, 25.17, 28.90],
              5: [24.60, 28.55, 33.04, 37.53, 42.01], 6: [15.53, 18.97, 22.40, 25.83, 29.27]}

NORM_FE_HS = {1: [12.66, 18.16, 23.66, 29.16, 34.66], 2: [13.33, 18.42, 23.51, 28.60, 33.69],
              3: [10.75, 15.41, 20.07, 24.73, 29.39], 4: [14.22, 15.30, 16.38, 17.46, 18.54],
              5: [14.12, 20.21, 26.30, 32.39, 38.48], 6: [10.53, 14.51, 18.49, 22.47, 26.45]}

NORM_SE_FS = {1: [17.54, 24.03, 30.53, 37.02, 43.51], 2: [17.80, 24.26, 30.73, 37.19, 43.65],
              3: [18.03, 22.41, 26.79, 31.17, 35.55], 4: [14.28, 15.55, 16.83, 18.10, 19.37],
              5: [20.69, 27.49, 34.29, 41.09, 47.89], 6: [12.44, 18.06, 23.68, 29.29, 34.91]}

NORM_FE_FS = {1: [15.30, 19.79, 24.28, 28.77, 33.26], 2: [14.63, 18.94, 23.25, 27.56, 31.87],
              3: [14.62, 17.81, 21.00, 24.19, 27.38], 4: [15.00, 15.55, 16.10, 16.65, 17.20],
              5: [18.44, 22.61, 26.78, 30.95, 35.12], 6: [9.79, 13.97, 18.15, 22.33, 26.51]}

KOMPETENZEN = ["Arbeitsverhalten", "Lernverhalten", "Sozialverhalten", 
               "Fachkompetenz", "Personale Kompetenz", "Methodenkompetenz"]

ITEMS = [
    "Zuverlässigkeit", "Arbeitstempo", "Arbeitsplanung", "Organisationsfähigkeit",
    "Geschicklichkeit", "Ordnung", "Sorgfalt", "Kreativität", "Problemlösungsfähigkeit",
    "Abstraktionsvermögen", "Selbstständigkeit", "Belastbarkeit", "Konzentrationsfähigkeit",
    "Verantwortungsbewusstsein", "Eigeninitiative", "Leistungsbereitschaft", "Auffassungsgabe",
    "Merkfähigkeit", "Motivationsfähigkeit", "Reflektionsfähigkeit", "Teamfähigkeit",
    "Hilfsbereitschaft", "Kontaktfähigkeit", "Respektvoller Umgang", "Kommunikationsfähigkeit",
    "Einfühlungsvermögen", "Konfliktfähigkeit", "Kritikfähigkeit", "Schreiben", "Lesen",
    "Mathematik", "Naturwissenschaft", "Fremdsprachen", "Präsentationsfähigkeit",
    "PC Kenntnisse", "Fächerübergreifendes Denken"
]


class DueskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DÜSK - Düsseldorfer Schülerinventar")
        self.root.geometry("1100x700")
        
        self.user_id = None
        self.session = None
        self.profiles = []
        self.groups = []
        
        self.setup_login_ui()
        
    def setup_login_ui(self):
        self.login_frame = ttk.Frame(self.root)
        self.login_frame.pack(fill="both", expand=True)
        
        ttk.Label(self.login_frame, text="DÜSK - Düsseldorfer Schülerinventar", 
                  font=("Arial", 20, "bold")).pack(pady=30)
        
        form = ttk.Frame(self.login_frame)
        form.pack(pady=20)
        
        ttk.Label(form, text="Benutzername:").grid(row=0, column=0, padx=5, pady=5)
        self.username_entry = ttk.Entry(form, width=20)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)
        self.username_entry.insert(0, "gast")
        
        ttk.Label(form, text="Passwort:").grid(row=1, column=0, padx=5, pady=5)
        self.password_entry = ttk.Entry(form, width=20, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)
        self.password_entry.insert(0, "gast")
        
        ttk.Button(self.login_frame, text="Anmelden", command=self.do_login).pack(pady=20)
        ttk.Label(self.login_frame, text="Server: paul-koop.org\nBenutzung mit gast/gast möglich",
                  font=("Arial", 9), foreground="gray").pack()
        
    def setup_main_ui(self):
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)
        
        # Toolbar
        toolbar = ttk.Frame(self.main_frame)
        toolbar.pack(fill="x", padx=5, pady=5)
        
        ttk.Button(toolbar, text="Neues Profil", command=self.new_profile).pack(side="left", padx=5)
        ttk.Button(toolbar, text="Aktualisieren", command=self.load_profiles).pack(side="left", padx=5)
        ttk.Button(toolbar, text="Gruppen verwalten", command=self.manage_groups).pack(side="left", padx=5)
        ttk.Button(toolbar, text="Abmelden", command=self.logout).pack(side="right", padx=5)
        
        # Tabelle
        columns = ("Name", "Gruppe", "ProfilID")
        self.tree = ttk.Treeview(self.main_frame, columns=columns, show="headings", height=15)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=200 if col == "Name" else 150)
        self.tree.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Buttons unter der Tabelle
        btn_frame = ttk.Frame(self.main_frame)
        btn_frame.pack(fill="x", padx=5, pady=5)
        ttk.Button(btn_frame, text="Anzeigen", command=self.view_profile).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Bearbeiten", command=self.edit_profile).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Löschen", command=self.delete_profile).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Zeitreihe (Gruppe)", command=self.show_time_series).pack(side="left", padx=5)
        
        # Statusbar
        self.status_var = tk.StringVar()
        self.status_var.set("Bereit")
        statusbar = ttk.Label(self.main_frame, textvariable=self.status_var, relief="sunken")
        statusbar.pack(fill="x", padx=5, pady=5)
        
        self.load_profiles()
        self.load_groups()
        
    def get_selected_profile(self):
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Keine Auswahl", "Bitte wählen Sie ein Profil aus.")
            return None
        item = self.tree.item(selection[0])
        profile_id = item['values'][2]
        for p in self.profiles:
            if str(p.get('profilID')) == str(profile_id):
                return p
        return None
        
    def do_login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        try:
            resp = requests.post(API_BASE_URL + "api_login.php", 
                                json={"username": username, "password": password}, timeout=30)
            data = resp.json()
            
            if data.get('success') or data.get('userID'):
                self.user_id = data['userID']
                self.session = data['session']
                self.login_frame.pack_forget()
                self.setup_main_ui()
            else:
                messagebox.showerror("Fehler", "Anmeldung fehlgeschlagen")
        except Exception as e:
            messagebox.showerror("Fehler", f"Verbindungsfehler: {e}")
            
    def load_profiles(self):
        self.status_var.set("Lade Profile...")
        self.root.update()
        
        try:
            headers = {'X-User-ID': str(self.user_id), 'X-Session': self.session}
            resp = requests.get(API_BASE_URL + "api_profiles.php", headers=headers, timeout=30)
            profiles = resp.json()
            
            if isinstance(profiles, list):
                self.profiles = profiles
                for item in self.tree.get_children():
                    self.tree.delete(item)
                for p in profiles:
                    self.tree.insert("", "end", values=(
                        p.get('name', ''), 
                        p.get('gruppename', ''), 
                        p.get('profilID', '')
                    ))
                self.status_var.set(f"{len(profiles)} Profile geladen")
            else:
                self.status_var.set("Keine Profile gefunden")
        except Exception as e:
            self.status_var.set(f"Fehler: {e}")
            
    def load_groups(self):
        try:
            headers = {'X-User-ID': str(self.user_id), 'X-Session': self.session}
            resp = requests.get(API_BASE_URL + "api_groups.php", headers=headers, timeout=30)
            if resp.status_code == 200:
                self.groups = resp.json() if isinstance(resp.json(), list) else []
        except:
            self.groups = []
            
    def new_profile(self):
        dialog = ProfileEditDialog(self.root, self.user_id, self.session, self.groups)
        if dialog.result:
            self.load_profiles()
            
    def edit_profile(self):
        profile = self.get_selected_profile()
        if profile:
            # Vollständiges Profil laden
            headers = {'X-User-ID': str(self.user_id), 'X-Session': self.session}
            resp = requests.get(API_BASE_URL + "api_profiles.php", 
                               params={"id": profile.get('profilID')}, headers=headers, timeout=30)
            full_profile = resp.json()
            if isinstance(full_profile, dict):
                dialog = ProfileEditDialog(self.root, self.user_id, self.session, self.groups, full_profile)
                if dialog.result:
                    self.load_profiles()
                
    def view_profile(self):
        profile = self.get_selected_profile()
        if profile:
            headers = {'X-User-ID': str(self.user_id), 'X-Session': self.session}
            resp = requests.get(API_BASE_URL + "api_profiles.php", 
                               params={"id": profile.get('profilID')}, headers=headers, timeout=30)
            full_profile = resp.json()
            if isinstance(full_profile, dict):
                ProfileViewDialog(self.root, full_profile)
                
    def delete_profile(self):
        profile = self.get_selected_profile()
        if profile:
            if messagebox.askyesno("Löschen", f"Profil '{profile.get('name')}' wirklich löschen?"):
                headers = {'X-User-ID': str(self.user_id), 'X-Session': self.session}
                requests.delete(API_BASE_URL + "api_profiles.php", 
                               params={"id": profile.get('profilID')}, headers=headers, timeout=30)
                self.load_profiles()
                
    def show_time_series(self):
        profile = self.get_selected_profile()
        if not profile:
            return
        group_id = profile.get('gruppeID')
        group_name = profile.get('gruppename', 'Unbekannt')
        
        # Alle Profile der gleichen Gruppe mit vollständigen Daten laden
        group_profiles = []
        for p in self.profiles:
            if p.get('gruppeID') == group_id:
                headers = {'X-User-ID': str(self.user_id), 'X-Session': self.session}
                resp = requests.get(API_BASE_URL + "api_profiles.php", 
                                   params={"id": p.get('profilID')}, headers=headers, timeout=30)
                full = resp.json()
                if isinstance(full, dict):
                    group_profiles.append(full)
                    
        if group_profiles:
            TimeSeriesDialog(self.root, group_name, group_profiles)
        else:
            messagebox.showinfo("Info", "Keine weiteren Profile in dieser Gruppe.")
            
    def manage_groups(self):
        dialog = GroupManagerDialog(self.root, self.user_id, self.session, self.groups, self.load_groups)
        if dialog.result:
            self.load_groups()
            self.load_profiles()
            
    def logout(self):
        try:
            headers = {'X-User-ID': str(self.user_id), 'X-Session': self.session}
            requests.post(API_BASE_URL + "api_logout.php", headers=headers, timeout=30)
        except:
            pass
        self.main_frame.pack_forget()
        self.setup_login_ui()


class ProfileEditDialog:
    def __init__(self, parent, user_id, session, groups, profile=None):
        self.parent = parent
        self.user_id = user_id
        self.session = session
        self.groups = groups
        self.profile = profile
        self.result = False
        self.se_vars = {}
        self.fe_vars = {}
        
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Profil bearbeiten" if profile else "Neues Profil")
        self.dialog.geometry("900x700")
        
        self.setup_ui()
        if profile:
            self.load_values()
            
        self.dialog.transient(parent)
        self.dialog.grab_set()
        parent.wait_window(self.dialog)
        
    def setup_ui(self):
        # Basis
        info_frame = ttk.LabelFrame(self.dialog, text="Profil-Informationen")
        info_frame.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(info_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(info_frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        if self.profile:
            self.name_entry.insert(0, self.profile.get('name', ''))
            
        ttk.Label(info_frame, text="Gruppe:").grid(row=1, column=0, padx=5, pady=5)
        self.group_combo = ttk.Combobox(info_frame, width=27)
        group_names = [g.get('name', '') for g in self.groups]
        self.group_combo['values'] = group_names
        if self.groups:
            self.group_combo.current(0)
        if self.profile and self.profile.get('gruppename'):
            for i, g in enumerate(self.groups):
                if g.get('name') == self.profile.get('gruppename'):
                    self.group_combo.current(i)
                    break
        self.group_combo.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(info_frame, text="Neue Gruppe:").grid(row=2, column=0, padx=5, pady=5)
        self.new_group_entry = ttk.Entry(info_frame, width=30)
        self.new_group_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Notebook
        notebook = ttk.Notebook(self.dialog)
        notebook.pack(fill="both", expand=True, padx=10, pady=5)
        
        se_frame = ttk.Frame(notebook)
        notebook.add(se_frame, text="Selbsteinschätzung")
        self.create_item_grid(se_frame, self.se_vars, "se")
        
        fe_frame = ttk.Frame(notebook)
        notebook.add(fe_frame, text="Fremdeinschätzung")
        self.create_item_grid(fe_frame, self.fe_vars, "fe")
        
        # Buttons
        btn_frame = ttk.Frame(self.dialog)
        btn_frame.pack(fill="x", padx=10, pady=10)
        ttk.Button(btn_frame, text="Speichern", command=self.save).pack(side="right", padx=5)
        ttk.Button(btn_frame, text="Abbrechen", command=self.dialog.destroy).pack(side="right", padx=5)
        
    def create_item_grid(self, parent, vars_dict, prefix):
        canvas = tk.Canvas(parent)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        for i, item_name in enumerate(ITEMS, 1):
            frame = ttk.LabelFrame(scrollable_frame, text=f"{i:2d}. {item_name}")
            frame.pack(fill="x", padx=5, pady=2)
            
            var = tk.IntVar(value=2)
            vars_dict[i] = var
            
            for val, label in [(4, "trifft voll zu (4)"), (3, "trifft zu (3)"), 
                              (2, "trifft teilweise zu (2)"), (1, "trifft nicht zu (1)")]:
                rb = ttk.Radiobutton(frame, text=label, variable=var, value=val)
                rb.pack(side="left", padx=5)
                
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
    def load_values(self):
        for i in range(1, 37):
            se_val = self.profile.get(f'item{i}', 2)
            if se_val and i in self.se_vars:
                self.se_vars[i].set(se_val)
            fe_val = self.profile.get(f'feitem{i}', 2)
            if fe_val and i in self.fe_vars:
                self.fe_vars[i].set(fe_val)
                
    def save(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showerror("Fehler", "Bitte Name eingeben")
            return
            
        group_name = self.group_combo.get()
        new_group = self.new_group_entry.get().strip()
        
        data = {'name': name}
        
        if new_group:
            data['namegruppe'] = new_group
        elif group_name:
            for g in self.groups:
                if g.get('name') == group_name:
                    data['gruppeID'] = g.get('gruppeID')
                    break
                    
        for i in range(1, 37):
            data[f'item{i}'] = self.se_vars[i].get()
            data[f'feitem{i}'] = self.fe_vars[i].get()
            
        if self.profile:
            data['profilID'] = self.profile.get('profilID')
            method = requests.put
        else:
            method = requests.post
            
        try:
            headers = {'Content-Type': 'application/json', 'X-User-ID': str(self.user_id), 'X-Session': self.session}
            resp = method(API_BASE_URL + "api_profiles.php", json=data, headers=headers, timeout=30)
            result = resp.json()
            if result.get('success'):
                self.result = True
                self.dialog.destroy()
            else:
                messagebox.showerror("Fehler", result.get('error', 'Unbekannter Fehler'))
        except Exception as e:
            messagebox.showerror("Fehler", str(e))


class ProfileViewDialog:
    def __init__(self, parent, profile):
        self.parent = parent
        self.profile = profile
        self.current_norm = "HS"
        
        self.dialog = tk.Toplevel(parent)
        self.dialog.title(f"Profil: {profile.get('name', 'Unbekannt')}")
        self.dialog.geometry("1000x800")
        
        self.setup_ui()
        self.calculate()
        
    def setup_ui(self):
        # Header
        header = ttk.Frame(self.dialog)
        header.pack(fill="x", padx=10, pady=5)
        ttk.Label(header, text=f"Name: {self.profile.get('name', 'Unbekannt')}", 
                  font=("Arial", 14, "bold")).pack(side="left")
        ttk.Label(header, text=f"Profil-ID: {self.profile.get('profilID', '?')}").pack(side="right")
        
        # Normauswahl
        norm_frame = ttk.Frame(self.dialog)
        norm_frame.pack(fill="x", padx=10, pady=5)
        ttk.Label(norm_frame, text="Normtabelle:").pack(side="left")
        self.norm_var = tk.StringVar(value="HS")
        hs_radio = ttk.Radiobutton(norm_frame, text="Hauptschule (HS)", variable=self.norm_var, value="HS", command=self.calculate)
        fs_radio = ttk.Radiobutton(norm_frame, text="Förderschule (FS)", variable=self.norm_var, value="FS", command=self.calculate)
        hs_radio.pack(side="left", padx=5)
        fs_radio.pack(side="left", padx=5)
        
        # Notebook
        notebook = ttk.Notebook(self.dialog)
        notebook.pack(fill="both", expand=True, padx=10, pady=5)
        
        self.se_frame = ttk.Frame(notebook)
        notebook.add(self.se_frame, text="Selbsteinschätzung (SE)")
        
        self.fe_frame = ttk.Frame(notebook)
        notebook.add(self.fe_frame, text="Fremdeinschätzung (FE)")
        
        self.stats_frame = ttk.Frame(notebook)
        notebook.add(self.stats_frame, text="Statistik")
        
        self.items_frame = ttk.Frame(notebook)
        notebook.add(self.items_frame, text="Alle Items (36)")
        
    def calculate_sums(self, items):
        sums = [0] * 7
        sums[1] = sum(items[0:10])
        sums[2] = sum(items[10:20])
        sums[3] = sum(items[20:28]) + items[8] + items[9]
        sums[4] = sum(items[28:36])
        sums[5] = items[0] + items[1] + items[5] + items[6] + items[7] + items[8] + items[9] + items[11] + items[12] + items[13] + items[14]
        sums[6] = items[2] + items[3] + items[4] + items[8] + items[9] + items[10] + items[16] + items[17]
        return sums
        
    def get_profile_values(self, sums, norm):
        values = [0] * 6
        for k in range(1, 7):
            placed = False
            for p in range(5):
                if sums[k] < norm[k][p]:
                    values[k-1] = p
                    placed = True
                    break
            if not placed:
                values[k-1] = 4
        return values
        
    def create_competence_table(self, parent, title, items, norm):
        for widget in parent.winfo_children():
            widget.destroy()
            
        ttk.Label(parent, text=title, font=("Arial", 12, "bold")).pack(pady=5)
        
        tree = ttk.Treeview(parent, columns=("kompetenz", "1", "2", "3", "4", "5"), show="headings", height=6)
        tree.heading("kompetenz", text="Kompetenz")
        for i in range(1, 6):
            tree.heading(str(i), text=str(i))
        tree.column("kompetenz", width=150)
        for i in range(1, 6):
            tree.column(str(i), width=50, anchor="center")
        tree.pack(pady=5)
        
        sums = self.calculate_sums(items)
        values = self.get_profile_values(sums, norm)
        chart_values = [v + 1 for v in values]
        
        for i, (komp, val) in enumerate(zip(KOMPETENZEN, values)):
            row = [komp]
            for j in range(5):
                row.append("X" if j == val else "")
            tree.insert("", "end", values=row)
            
        text = " | ".join([f"{k}: {v}" for k, v in zip(KOMPETENZEN, chart_values)])
        ttk.Label(parent, text=text, font=("Courier", 9)).pack(pady=5)
        
        return chart_values
        
    def calculate(self):
        se_items = [int(self.profile.get(f'item{i}', 2)) for i in range(1, 37)]
        fe_items = [int(self.profile.get(f'feitem{i}', 2)) for i in range(1, 37)]
        
        if self.norm_var.get() == "HS":
            norm_se, norm_fe = NORM_SE_HS, NORM_FE_HS
        else:
            norm_se, norm_fe = NORM_SE_FS, NORM_FE_FS
            
        se_chart = self.create_competence_table(self.se_frame, "Selbsteinschätzung", se_items, norm_se)
        fe_chart = self.create_competence_table(self.fe_frame, "Fremdeinschätzung", fe_items, norm_fe)
        
        self.create_stats_view(se_chart, fe_chart, se_items, fe_items)
        self.create_items_view(se_items, fe_items)
        
    def create_stats_view(self, se_chart, fe_chart, se_items, fe_items):
        for widget in self.stats_frame.winfo_children():
            widget.destroy()
            
        def calc_corr(a, b):
            ma, mb = sum(a)/6, sum(b)/6
            num = sum((a[i]-ma)*(b[i]-mb) for i in range(6))
            den = math.sqrt(sum((a[i]-ma)**2 for i in range(6)) * sum((b[i]-mb)**2 for i in range(6)))
            return num/den if den != 0 else 0
            
        corr = calc_corr(se_chart, fe_chart)
        agree = sum(1 for s, f in zip(se_items, fe_items) if s == f) * 100 / 36
        
        ttk.Label(self.stats_frame, text=f"Korrelation: {corr:.2f}", font=("Arial", 12)).pack(pady=5)
        ttk.Label(self.stats_frame, text=f"Übereinstimmung: {agree:.1f}%", font=("Arial", 12)).pack(pady=5)
        
        text = tk.Text(self.stats_frame, wrap="word", height=12, width=80)
        text.pack(pady=10, padx=10, fill="both", expand=True)
        
        interpretation = f"Die Korrelation von {corr:.2f} bedeutet: "
        if corr >= 0.8:
            interpretation += "Sehr gute Übereinstimmung zwischen Selbst- und Fremdeinschätzung.\n\n"
        elif corr >= 0.5:
            interpretation += "Mäßige Übereinstimmung zwischen Selbst- und Fremdeinschätzung.\n\n"
        elif corr >= 0.3:
            interpretation += "Schwache Übereinstimmung zwischen Selbst- und Fremdeinschätzung.\n\n"
        else:
            interpretation += "Keine signifikante Übereinstimmung zwischen Selbst- und Fremdeinschätzung.\n\n"
            
        ratings = ["weit unterdurchschnittlich", "unterdurchschnittlich", "durchschnittlich", 
                   "überdurchschnittlich", "weit überdurchschnittlich"]
        
        interpretation += "Auswertung der Kompetenzen:\n"
        interpretation += "-" * 50 + "\n"
        interpretation += "Selbsteinschätzung:\n"
        for i, v in enumerate(se_chart):
            interpretation += f"  • {KOMPETENZEN[i]}: {ratings[v-1]}\n"
        interpretation += "\nFremdeinschätzung:\n"
        for i, v in enumerate(fe_chart):
            interpretation += f"  • {KOMPETENZEN[i]}: {ratings[v-1]}\n"
            
        text.insert("1.0", interpretation)
        text.config(state="disabled")
        
    def create_items_view(self, se_items, fe_items):
        for widget in self.items_frame.winfo_children():
            widget.destroy()
            
        container = ttk.Frame(self.items_frame)
        container.pack(fill="both", expand=True)
        
        scroll_y = ttk.Scrollbar(container, orient="vertical")
        scroll_x = ttk.Scrollbar(container, orient="horizontal")
        
        tree = ttk.Treeview(container, columns=("item", "se", "fe"), show="headings",
                           yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        tree.heading("item", text="Item")
        tree.heading("se", text="Selbst")
        tree.heading("fe", text="Fremd")
        tree.column("item", width=280)
        tree.column("se", width=50, anchor="center")
        tree.column("fe", width=50, anchor="center")
        
        scroll_y.config(command=tree.yview)
        scroll_x.config(command=tree.xview)
        scroll_y.pack(side="right", fill="y")
        scroll_x.pack(side="bottom", fill="x")
        tree.pack(fill="both", expand=True)
        
        for i, name in enumerate(ITEMS, 1):
            tree.insert("", "end", values=(f"{i:2d}. {name}", se_items[i-1], fe_items[i-1]))


class TimeSeriesDialog:
    def __init__(self, parent, group_name, profiles):
        self.dialog = tk.Toplevel(parent)
        self.dialog.title(f"Zeitreihe - {group_name}")
        self.dialog.geometry("900x500")
        
        ttk.Label(self.dialog, text=f"Gruppe: {group_name}", font=("Arial", 14, "bold")).pack(pady=10)
        ttk.Label(self.dialog, text=f"Anzahl Profile: {len(profiles)}").pack()
        
        columns = ("ProfilID", "Name", "Arbeitsverhalten", "Lernverhalten", "Sozialverhalten",
                   "Fachkompetenz", "Personale Kompetenz", "Methodenkompetenz")
        tree = ttk.Treeview(self.dialog, columns=columns, show="headings", height=20)
        for col in columns:
            tree.heading(col, text=col)
            width = 80 if col != "Name" else 120
            tree.column(col, width=width, anchor="center" if col != "Name" else "w")
        tree.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Berechne Kompetenzwerte für jedes Profil, falls nicht vorhanden
        for p in sorted(profiles, key=lambda x: int(x.get('profilID', 0))):
            # Berechne Kompetenzwerte aus Items, falls nicht gespeichert
            kompetenz = []
            for prefix in ['', 'fe']:
                items = [int(p.get(f'{prefix}item{i}', 2)) for i in range(1, 37)]
                sums = [0] * 7
                sums[1] = sum(items[0:10])
                sums[2] = sum(items[10:20])
                sums[3] = sum(items[20:28]) + items[8] + items[9]
                sums[4] = sum(items[28:36])
                sums[5] = items[0] + items[1] + items[5] + items[6] + items[7] + items[8] + items[9] + items[11] + items[12] + items[13] + items[14]
                sums[6] = items[2] + items[3] + items[4] + items[8] + items[9] + items[10] + items[16] + items[17]
                
                values = [0] * 6
                for k in range(1, 7):
                    placed = False
                    for pu in range(5):
                        if sums[k] < NORM_SE_HS[k][pu]:
                            values[k-1] = pu
                            placed = True
                            break
                    if not placed:
                        values[k-1] = 4
                kompetenz.extend([v+1 for v in values])
            
            tree.insert("", "end", values=(
                p.get('profilID', ''),
                p.get('name', ''),
                kompetenz[0], kompetenz[1], kompetenz[2], kompetenz[3], kompetenz[4], kompetenz[5]
            ))
            
        ttk.Button(self.dialog, text="Schließen", command=self.dialog.destroy).pack(pady=10)


class GroupManagerDialog:
    def __init__(self, parent, user_id, session, groups, refresh_callback):
        self.parent = parent
        self.user_id = user_id
        self.session = session
        self.groups = groups
        self.refresh_callback = refresh_callback
        self.result = False
        
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Gruppenverwaltung")
        self.dialog.geometry("400x400")
        
        self.tree = ttk.Treeview(self.dialog, columns=("name",), show="headings", height=10)
        self.tree.heading("name", text="Gruppenname")
        self.tree.column("name", width=250)
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.refresh_list()
        
        add_frame = ttk.Frame(self.dialog)
        add_frame.pack(fill="x", padx=10, pady=5)
        self.new_name_entry = ttk.Entry(add_frame, width=25)
        self.new_name_entry.pack(side="left", padx=5)
        ttk.Button(add_frame, text="Hinzufügen", command=self.add_group).pack(side="left", padx=5)
        
        btn_frame = ttk.Frame(self.dialog)
        btn_frame.pack(fill="x", padx=10, pady=10)
        ttk.Button(btn_frame, text="Löschen", command=self.delete_group).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Schließen", command=self.dialog.destroy).pack(side="right", padx=5)
        
        self.dialog.transient(parent)
        self.dialog.grab_set()
        parent.wait_window(self.dialog)
        
    def refresh_list(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for g in self.groups:
            self.tree.insert("", "end", values=(g.get('name', ''),), tags=(g.get('gruppeID'),))
            
    def get_selected_group(self):
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            group_name = item['values'][0]
            for g in self.groups:
                if g.get('name') == group_name:
                    return g
        return None
        
    def add_group(self):
        name = self.new_name_entry.get().strip()
        if not name:
            return
        try:
            headers = {'Content-Type': 'application/json', 'X-User-ID': str(self.user_id), 'X-Session': self.session}
            resp = requests.post(API_BASE_URL + "api_groups.php", json={"name": name}, headers=headers, timeout=30)
            if resp.status_code == 200:
                self.new_name_entry.delete(0, tk.END)
                self.result = True
                self.refresh_callback()
                self.load_groups()
        except:
            pass
            
    def delete_group(self):
        group = self.get_selected_group()
        if group and messagebox.askyesno("Löschen", f"Gruppe '{group.get('name')}' wirklich löschen?"):
            try:
                headers = {'X-User-ID': str(self.user_id), 'X-Session': self.session}
                requests.delete(API_BASE_URL + "api_groups.php", params={"id": group.get('gruppeID')}, headers=headers, timeout=30)
                self.result = True
                self.refresh_callback()
                self.load_groups()
            except:
                pass
                
    def load_groups(self):
        try:
            headers = {'X-User-ID': str(self.user_id), 'X-Session': self.session}
            resp = requests.get(API_BASE_URL + "api_groups.php", headers=headers, timeout=30)
            if resp.status_code == 200:
                self.groups = resp.json() if isinstance(resp.json(), list) else []
                self.refresh_list()
        except:
            pass


def main():
    root = tk.Tk()
    app = DueskApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
