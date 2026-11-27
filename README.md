# RobotGazon

Site: https://robotgazon.online — conținut în `site_robotgazon.py` (ghiduri, selector) și `site_robotgazon_p.py` (produse, comparator, portada), generat automat de GitHub Actions (build.py din Manux1926/dronaagricola).

`og-image.jpg` și `logo.png` se copiază automat în site. Fotografiile oficiale de presă ale produselor (dicționarul `PRESS` din build.py) se descarcă și se micșorează la fiecare build.

Verificare Profitshare: etichetele `PS_META` în `<head>` și fișierele `<cod>.html` (`PS_CODES` din build.py) în rădăcina site-ului.

Opțional, `site_<sid>_a.py` adaugă articole noi (`PAGES`), corecturi de produse (`PATCH`) și actualizări ale ghidurilor (câmpul `modified` pentru data actualizării).
