"""
Protección de Vista - atenuador de pantalla con filtro cálido.
Funciona mejor en Windows (los clics atraviesan el filtro).
Uso: python proteccion_vista.py
"""
import json
import os
import sys
import tkinter as tk
from tkinter import ttk

CONFIG = os.path.join(os.path.expanduser("~"), ".proteccion_vista.json")

PRESETS = {
    "Normal":      {"oscuridad": 0,  "calidez": 0},
    "Lectura":     {"oscuridad": 20, "calidez": 35},
    "Noche":       {"oscuridad": 45, "calidez": 65},
    "Muy oscuro":  {"oscuridad": 70, "calidez": 80},
    "Extremo":     {"oscuridad": 88, "calidez": 90},
}

DEFAULTS = {"oscuridad": 30, "calidez": 40, "activo": True, "preset": "Lectura"}


def cargar():
    try:
        with open(CONFIG, "r", encoding="utf-8") as f:
            return {**DEFAULTS, **json.load(f)}
    except Exception:
        return dict(DEFAULTS)


def guardar(cfg):
    try:
        with open(CONFIG, "w", encoding="utf-8") as f:
            json.dump(cfg, f)
    except Exception:
        pass


class App:
    def __init__(self, root):
        self.root = root
        self.cfg = cargar()
        root.title("Protección de Vista")
        root.geometry("360x470")
        root.resizable(False, False)

        self.overlay = None
        self.var_osc = tk.IntVar(value=self.cfg["oscuridad"])
        self.var_cal = tk.IntVar(value=self.cfg["calidez"])
        self.var_on = tk.BooleanVar(value=self.cfg["activo"])

        self._construir_ui()
        self._crear_overlay()
        self.aplicar()
        root.protocol("WM_DELETE_WINDOW", self.cerrar)

    # ---------- Interfaz ----------
    def _construir_ui(self):
        pad = {"padx": 16, "pady": 6}
        ttk.Label(self.root, text="Protección de Vista",
                  font=("Segoe UI", 16, "bold")).pack(pady=(14, 4))

        ttk.Checkbutton(self.root, text="Filtro activado",
                        variable=self.var_on,
                        command=self.aplicar).pack(**pad)

        # Oscuridad
        f1 = ttk.LabelFrame(self.root, text="Oscuridad (más bajo que el brillo normal)")
        f1.pack(fill="x", **pad)
        self.lbl_osc = ttk.Label(f1, text="")
        self.lbl_osc.pack()
        ttk.Scale(f1, from_=0, to=92, variable=self.var_osc,
                  command=lambda _: self.aplicar()).pack(fill="x", padx=10, pady=6)

        # Calidez
        f2 = ttk.LabelFrame(self.root, text="Calidez (menos luz azul)")
        f2.pack(fill="x", **pad)
        self.lbl_cal = ttk.Label(f2, text="")
        self.lbl_cal.pack()
        ttk.Scale(f2, from_=0, to=100, variable=self.var_cal,
                  command=lambda _: self.aplicar()).pack(fill="x", padx=10, pady=6)

        # Presets
        f3 = ttk.LabelFrame(self.root, text="Perfiles rápidos")
        f3.pack(fill="x", **pad)
        for nombre in PRESETS:
            ttk.Button(f3, text=nombre,
                       command=lambda n=nombre: self.preset(n)).pack(
                fill="x", padx=10, pady=2)

        ttk.Label(self.root, text="Cerrar esta ventana quita el filtro.",
                  foreground="gray").pack(pady=6)

    # ---------- Overlay ----------
    def _crear_overlay(self):
        ov = tk.Toplevel(self.root)
        ov.overrideredirect(True)
        ov.attributes("-topmost", True)
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        ov.geometry(f"{w}x{h}+0+0")
        ov.configure(bg="black")
        ov.update_idletasks()
        self._click_through(ov)
        self.overlay = ov
        # Mantener la ventana de control por encima del filtro no es posible
        # sin romper el efecto, así que el control queda debajo (atenuado).

    def _click_through(self, win):
        """Hace que los clics atraviesen el filtro (solo Windows)."""
        if sys.platform != "win32":
            return
        try:
            import ctypes
            from ctypes import wintypes
            user32 = ctypes.windll.user32
            user32.GetAncestor.argtypes = [wintypes.HWND, wintypes.UINT]
            user32.GetAncestor.restype = wintypes.HWND
            user32.GetWindowLongW.argtypes = [wintypes.HWND, ctypes.c_int]
            user32.GetWindowLongW.restype = ctypes.c_long
            user32.SetWindowLongW.argtypes = [wintypes.HWND, ctypes.c_int, ctypes.c_long]
            user32.SetWindowLongW.restype = ctypes.c_long

            win.update_idletasks()
            hijo = win.winfo_id()
            raiz = user32.GetAncestor(hijo, 2) or hijo  # GA_ROOT
            GWL_EXSTYLE = -20
            # LAYERED | TRANSPARENT | TOOLWINDOW | NOACTIVATE
            banderas = 0x80000 | 0x20 | 0x80 | 0x08000000
            for h in {raiz, hijo}:
                estilo = user32.GetWindowLongW(h, GWL_EXSTYLE)
                user32.SetWindowLongW(h, GWL_EXSTYLE, estilo | banderas)
        except Exception as e:
            print("No se pudo activar el modo clic-a-través:", e)

    def aplicar(self):
        osc = int(self.var_osc.get())
        cal = int(self.var_cal.get())
        self.lbl_osc.config(text=f"{osc}%")
        self.lbl_cal.config(text=f"{cal}%")

        if not self.var_on.get():
            self.overlay.attributes("-alpha", 0.0)
        else:
            # Color: negro que se vuelve ámbar oscuro con la calidez.
            c = cal / 100
            r, g, b = int(150 * c), int(55 * c), 0
            self.overlay.configure(bg=f"#{r:02x}{g:02x}{b:02x}")
            self.overlay.attributes("-alpha", max(0.0, osc / 100))
            self.overlay.attributes("-topmost", True)

        # La ventana de controles siempre queda por encima del filtro
        self.root.attributes("-topmost", True)
        self.root.lift()
        self._click_through(self.overlay)

        self.cfg.update(oscuridad=osc, calidez=cal, activo=self.var_on.get())
        guardar(self.cfg)

    def preset(self, nombre):
        p = PRESETS[nombre]
        self.var_osc.set(p["oscuridad"])
        self.var_cal.set(p["calidez"])
        self.var_on.set(True)
        self.aplicar()

    def cerrar(self):
        guardar(self.cfg)
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()