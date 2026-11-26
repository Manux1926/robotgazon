# Artículos y correcciones añadidos el 26 nov 2026 (build.py los carga si existe este archivo).
NOTE = ('<p class="note">Unele linkuri către magazine pot fi linkuri de afiliere. Prețurile sunt orientative, '
        'verificate la data actualizării; verifică prețul final în magazin.</p>')

# Corrección: el X450E es de la serie X4, con tracción integral (Xero-Turn AWD) y pendientes de hasta 84 %.
PATCH = {
    'segway-navimow-x450e': {
        'meta': 'Segway Navimow X450E pentru gazon mare: până la 5.000 m², lățime de tăiere 43 cm, tracțiune integrală și pante de până la 84%, ~16.490 lei.',
        'keys': [['Suprafață', '5.000 m²'], ['Lățime tăiere', '43 cm'], ['Tracțiune', 'integrală (AWD)'], ['Pantă', 'până la 84%']],
        'desc': ('<p>Seria X4 de la Segway este gândită pentru suprafețe mari. X450E are o lățime de tăiere de 43 cm (de peste '
                 'două ori mai mare decât modelele i), tracțiune integrală Xero-Turn AWD, urcă pante de până la 84% (40°) și poate '
                 'întreține până la 5.000 m². Se orientează cu Network RTK și camere de 360°, fără fir de perimetru.</p>\n'
                 '<p>Într-un test comparativ din 2026 al unei publicații norvegiene, fratele său X420E a ieșit „cel mai bun din test” '
                 'între roboții cu tracțiune integrală, iar în SUA modelul X430 a fost desemnat cel mai bun robot de tuns în general '
                 'de echipa Bob Vila. Seria X are deci o reputație solidă.</p>\n<h2>Merită pentru tine?</h2><p>Doar dacă ai cu '
                 'adevărat o suprafață mare. Sub 1.000 m² un i206 sau i210 face aceeași treabă pentru o treime din preț.</p>'),
        'pros': ['Lățime de tăiere de 43 cm', 'Până la 5.000 m²', 'Tracțiune integrală, pante de până la 84%',
                 'Seria X: rezultate foarte bune în testele independente'],
        'specs': [['Suprafață recomandată', 'până la 5.000 m²'], ['Lățime de tăiere', '43 cm'],
                  ['Tracțiune', 'integrală (Xero-Turn AWD)'], ['Pantă maximă', '84% (40°)'],
                  ['Navigare', 'Network RTK + camere 360°, fără fir']],
        'src': 'Surse: Hornbach România; fișa producătorului și MediaMarkt (seria X4); teste tek.no și Bob Vila (2026).',
        'spec': {'area': [5000, '5.000 m²'], 'cut': [43, '43 cm'], 'nav': 'Network RTK + Vision', 'awd': 'Da (84%)',
                 'price': [16490, '~16.490 lei'], 'ideal': 'Curți mari, pensiuni'},
    },
}

PAGES = [
{
    'slug': 'cel-mai-bun-robot-tuns-iarba-2026',
    'date': '2026-11-26',
    'date_ro': '26 noiembrie 2026',
    'title': 'Cel mai bun robot de tuns iarba 2026: ce model alegi',
    'kind': 'article',
    'short': 'Cel mai bun robot 2026',
    'desc': 'Cel mai bun robot de tuns iarba în 2026, pe categorii: pentru curți mici, cu pantă, cu mulți copaci, pentru buget redus și pentru suprafețe mari. Prețuri din România.',
    'h1': 'Cel mai bun robot de tuns iarba în 2026, pe categorii',
    'lead': 'Nu există un singur „cel mai bun” robot. Există cel mai bun pentru curtea ta. Iată alegerile noastre, cu prețuri din magazinele din România.',
    'body': """<p>Roboții de tuns iarba s-au schimbat complet în ultimii doi ani. Firul de perimetru îngropat în pământ a devenit opțional: modelele noi se orientează prin satelit (RTK), camere și, la cele mai scumpe, senzori LiDAR. Prețurile au coborât, iar în România găsești acum roboți fără fir de la mai puțin de 4.000 de lei, la Hornbach, eMAG sau Altex.</p>
<p>Ca să alegi bine, contează trei lucruri, în ordinea asta: <strong>suprafața</strong> reală de iarbă, <strong>panta</strong> maximă din curte și <strong>câte obstacole</strong> blochează cerul (copaci, case înalte, pergole). Am grupat recomandările după aceste criterii.</p>

<h2>Pe scurt: alegerile noastre</h2>
<div class="tw"><table class="t"><tr><th>Categorie</th><th>Recomandare</th><th>Preț orientativ</th><th>De ce</th></tr>
<tr><td>Buget mic, curte plană</td><td>Ecovacs GOAT O600 RTK</td><td>~3.690 lei</td><td>Fără fir, până la ~600 m², pante de 45%</td></tr>
<tr><td>Curte mică, deschisă</td><td>Segway Navimow i105E</td><td>4.290 lei</td><td>Cel mai simplu de instalat, până la 500 m²</td></tr>
<tr><td>Curte cu pantă, până la 600 m²</td><td>Segway Navimow i206 AWD</td><td>4.790 lei</td><td>Tracțiune integrală, pante de 45%</td></tr>
<tr><td>Mulți copaci, umbră</td><td>Segway Navimow i210 LiDAR E</td><td>5.999 lei</td><td>LiDAR: nu depinde de semnalul satelit</td></tr>
<tr><td>Pante mari, teren dificil</td><td>Mammotion Luba mini 2 AWD 1000</td><td>7.649 lei</td><td>Pante de până la 80%</td></tr>
<tr><td>Suprafețe de 2.000–5.000 m²</td><td>Segway Navimow X450E</td><td>~16.490 lei</td><td>Tăiere de 43 cm, AWD, pante de 84%</td></tr></table></div>

<h2>Cel mai bun pentru buget mic: Ecovacs GOAT O600 RTK</h2>
<p>Dacă ai o curte plană de câteva sute de metri pătrați și vrei să scapi de fir fără să cheltui mult, GOAT O600 RTK este alegerea rațională. Producătorul îl recomandă pentru gazon de până la 600 m², are navigare RTK cu cameră pentru obstacole și urcă pante de până la 45% (24°). Compromisul: aplicația și precizia la margini nu sunt la nivelul modelelor mai scumpe, iar sub copaci deși semnalul RTK poate slăbi.</p>

<h2>Cel mai bun pentru o curte mică și deschisă: Segway Navimow i105E</h2>
<p>i105E este robotul pe care îl recomandăm cel mai des pentru o curte obișnuită de casă, de până la 500 m², fără prea mulți copaci. Instalarea durează puțin, aplicația Navimow este printre cele mai clare, iar rețeaua de service prin magazinele mari este un avantaj în România. Limita lui este panta: urcă doar până la 30% (17°), iar la margini producătorul indică 10%. Dacă ai taluzuri, treci la i206 AWD.</p>

<h2>Cel mai bun pentru pante moderate: Segway Navimow i206 AWD</h2>
<p>Pentru 500 de lei în plus față de i105E primești tracțiune integrală și pante de până la 45% (24°), plus navigare RTK cu cameră AI. Este cel mai bun raport preț/teren dificil pentru curți de până la 600 m². Suprafața recomandată este ceva mai mare decât la i105E, iar roțile cu tracțiune se descurcă mai bine și pe iarbă udă.</p>

<h2>Cel mai bun pentru curți cu mulți copaci: Segway Navimow i210 LiDAR E</h2>
<p>Navigarea prin satelit are o slăbiciune: sub coroane dese sau lângă clădiri înalte, semnalul se pierde, iar robotul se oprește sau „sare” peste zone. i210 folosește un senzor LiDAR care vede în 3D spațiul din jur și nu depinde de cer. Taie pe 22 cm, e recomandat pentru până la 1.000 m² și urcă pante de 45%. Costă mai mult, dar într-o curte cu nuci, tei sau case înalte e diferența dintre un robot care funcționează și unul care te enervează.</p>

<h2>Cel mai bun pentru pante mari: Mammotion Luba mini 2 AWD 1000</h2>
<p>Mammotion a fost printre primii producători care au adus tracțiunea integrală la roboții de tuns, iar Luba mini 2 AWD urcă pante de până la 80%. Se orientează cu trei camere și NetRTK (RTK prin rețea, fără antenă proprie în multe zone) și este recomandat pentru până la 1.000 m². Este alegerea pentru curți în pantă abruptă, taluzuri și teren denivelat, unde modelele de 45% nu ajung.</p>

<h2>Cel mai bun pentru suprafețe mari: Segway Navimow X450E</h2>
<p>Pentru pensiuni, spații verzi de firmă sau proprietăți de 2.000–5.000 m², X450E are tăiere de 43 cm, tracțiune integrală și urcă pante de până la 84% (40°). Prețul este pe măsură. Sub 1.000 m² nu are sens: un i206 sau i210 face aceeași treabă pentru o treime din bani.</p>
{{PRODUCTS}}

<h2>Cum alegi în 3 minute</h2>
<ol><li><strong>Măsoară suprafața de iarbă</strong>, nu tot terenul. Aleile, terasa, casa și straturile de flori nu se pun la socoteală. Poți măsura pe Google Maps sau în aplicația producătorului.</li>
<li><strong>Alege un model cu 20–30% peste suprafața ta.</strong> Roboții lucrează mai bine când nu sunt la limita capacității, iar iarba crește mai repede primăvara.</li>
<li><strong>Verifică panta cea mai abruptă</strong> din curte (vezi <a href="/robot-tuns-iarba-panta.html">ghidul pentru pante</a>) și lasă o marjă, pentru că pe iarbă udă aderența scade.</li>
<li><strong>Uită-te în sus:</strong> dacă jumătate din curte stă sub copaci, ia în calcul LiDAR sau un model cu cameră și RTK prin rețea.</li></ol>
<p>Nu știi încă ce tehnologie ți se potrivește? Răspunde la câteva întrebări în <a href="/selector-robot-tuns-iarba.html">selectorul de robot</a> sau citește <a href="/robot-cu-fir-sau-fara-fir.html">diferența dintre robot cu fir și fără fir</a>.</p>
<p class="note">Surse: fișele producătorilor (Segway Navimow, Mammotion, Ecovacs), ofertele Hornbach România. Prețurile sunt din noiembrie 2026 și se pot schimba.</p>""" + NOTE,
    'faq': [
        ('Care este cel mai bun robot de tuns iarba pentru o curte de 500 m²?',
         'Pentru o curte plană și deschisă, Segway Navimow i105E. Dacă ai pante de peste 30% sau iarbă care rămâne des udă, Navimow i206 AWD, care are tracțiune integrală și urcă 45%.'),
        ('Merită un robot fără fir de perimetru?',
         'Pentru majoritatea curților, da: instalarea durează minute în loc de o zi, iar zonele se modifică din aplicație. Excepția sunt curțile cu mulți copaci deși, unde un model cu LiDAR sau unul clasic cu fir poate fi mai sigur.'),
        ('Cât costă un robot de tuns iarba bun în 2026?',
         'În România, modelele fără fir pentru curți mici pornesc de la aproximativ 3.700–4.300 de lei. Pentru pante și curți cu copaci ai nevoie de 4.800–7.700 de lei, iar pentru suprafețe de peste 2.000 m² de peste 15.000 de lei.'),
    ],
},
{
    'slug': 'robot-tuns-iarba-panta',
    'date': '2026-11-26',
    'date_ro': '26 noiembrie 2026',
    'title': 'Robot de tuns iarba pentru pantă: cât urcă fiecare model',
    'kind': 'article',
    'short': 'Robot pentru pantă',
    'desc': 'Ce robot de tuns iarba urcă pante de 30%, 45% sau 80%: cum măsori panta curții, diferența dintre procente și grade și ce modele cu tracțiune integrală merită.',
    'h1': 'Robot de tuns iarba pentru pantă: cât urcă fiecare model',
    'lead': 'Cum măsori panta din curte, ce înseamnă 45% în grade și ce roboți se descurcă pe taluzuri.',
    'body': """<p>Panta este motivul numărul unu pentru care un robot de tuns iarba ajunge înapoi la magazin. În broșură scrie „urcă pante de 45%”, în curte robotul patinează pe taluz, se blochează sau refuză să intre în zona din spatele casei. De cele mai multe ori nu e vina robotului, ci a unei confuzii între procente și grade, plus faptul că valoarea maximă e măsurată în condiții ideale.</p>

<h2>Procente și grade: nu sunt același lucru</h2>
<p>Producătorii dau panta în procente. 45% <strong>nu</strong> înseamnă 45 de grade. Procentul arată câți centimetri urcă terenul la fiecare metru parcurs pe orizontală: 45% înseamnă 45 cm la 1 metru, adică aproximativ 24°. O pantă de 100% are 45°.</p>
<div class="tw"><table class="t"><tr><th>Pantă în procente</th><th>În grade (aprox.)</th><th>Cum arată</th></tr>
<tr><td>10%</td><td>~6°</td><td>abia se simte, ca o rampă de acces</td></tr>
<tr><td>30%</td><td>~17°</td><td>pantă vizibilă, urci cu efort</td></tr>
<tr><td>45%</td><td>~24°</td><td>taluz serios, greu de tuns cu mașina clasică</td></tr>
<tr><td>80–84%</td><td>~39–40°</td><td>foarte abrupt, aproape de limita pe care o urci în picioare</td></tr></table></div>

<h2>Cum măsori panta din curte</h2>
<ol><li><strong>Cu telefonul:</strong> multe telefoane au o funcție de nivel (pe iPhone, în aplicația Măsurători; pe Android, aplicații gratuite de tip „nivelă”). Așază telefonul pe o scândură dreaptă de 1–2 m pusă pe pantă și citește unghiul în grade.</li>
<li><strong>Cu o riglă și o sfoară:</strong> întinde o sfoară orizontal (cu o nivelă cu bulă) 1 metru de la punctul de sus și măsoară cât coboară terenul până la ea. 30 cm = 30%.</li>
<li><strong>Măsoară în zona cea mai abruptă</strong>, nu în medie. Robotul se blochează în cel mai rău punct.</li></ol>

<h2>Cât urcă modelele pe care le recomandăm</h2>
<div class="tw"><table class="t"><tr><th>Model</th><th>Pantă maximă</th><th>Tracțiune</th><th>Preț orientativ</th></tr>
<tr><td>Segway Navimow i105E</td><td>30% (17°)</td><td>față</td><td>4.290 lei</td></tr>
<tr><td>Ecovacs GOAT O600 RTK</td><td>45% (24°)</td><td>fără AWD</td><td>~3.690 lei</td></tr>
<tr><td>Segway Navimow i206 AWD</td><td>45% (24°)</td><td>integrală</td><td>4.790 lei</td></tr>
<tr><td>Segway Navimow i210 LiDAR E</td><td>45% (24°)</td><td>fără AWD</td><td>5.999 lei</td></tr>
<tr><td>Mammotion Luba mini 2 AWD 1000</td><td>80% (~39°)</td><td>integrală</td><td>7.649 lei</td></tr>
<tr><td>Segway Navimow X450E</td><td>84% (40°)</td><td>integrală</td><td>~16.490 lei</td></tr></table></div>
<p>Atenție la a doua cifră din fișele tehnice: <strong>panta la margine</strong> (la perimetrul zonei) este de obicei mult mai mică decât panta maximă. La i105E, de exemplu, producătorul indică 30% în interiorul zonei și doar 10% la margine. Dacă marginea curții tale este chiar pe taluz, contează a doua valoare, pentru că acolo robotul trebuie să întoarcă.</p>
{{CARDS:segway-navimow-i206-awd,mammotion-luba-mini-2-awd-1000,segway-navimow-x450e}}

<h2>De ce tracțiunea integrală face diferența</h2>
<p>Un robot cu tracțiune doar pe două roți se bazează pe greutatea pusă pe acele roți. Pe pantă, greutatea se mută, roțile patinează și rup gazonul. Modelele <strong>AWD</strong> (tracțiune integrală) împart forța pe toate roțile și, la cele mai bune, o ajustează electronic în timp real, ca la o mașină. Rezultatul: urcă mai mult, nu sapă gazonul la întoarceri și se descurcă mai bine pe iarbă udă.</p>

<h2>Iarbă udă, margine de siguranță</h2>
<p>Valorile maxime sunt măsurate pe iarbă uscată, tunsă, în condiții de laborator. Dimineața cu rouă sau după ploaie, aderența scade simțitor. Regula noastră: alege un robot care urcă cu cel puțin <strong>10 puncte procentuale</strong> mai mult decât panta cea mai abruptă din curte. Pentru un taluz de 35%, un model de 45% e la limită; unul de 80% lucrează relaxat.</p>

<h2>Ce faci dacă ai o zonă prea abruptă</h2>
<ul><li><strong>Exclude-o din hartă</strong> și tunde-o manual de câteva ori pe sezon, cu o motocositoare.</li>
<li><strong>Transform-o în strat de plante tapisante</strong> sau flori: un taluz abrupt rareori arată bine tuns oricum.</li>
<li><strong>Creează un traseu în diagonală:</strong> unii roboți pot fi ghidați să urce pe o potecă în zig-zag, mai puțin abruptă decât panta directă.</li></ul>
<p>Pentru alegerea completă, pe suprafață și obstacole, vezi <a href="/cel-mai-bun-robot-tuns-iarba-2026.html">cel mai bun robot de tuns iarba în 2026</a> sau folosește <a href="/selector-robot-tuns-iarba.html">selectorul</a>.</p>
<p class="note">Surse: fișele tehnice Segway Navimow (seriile i și X4), Mammotion, Ecovacs; ofertele Hornbach România. Pantele sunt valorile maxime declarate de producători.</p>""" + NOTE,
    'faq': [
        ('Ce înseamnă pantă de 45% la un robot de tuns iarba?',
         'Terenul urcă 45 cm la fiecare metru orizontal, adică aproximativ 24°. Nu înseamnă 45 de grade: 45° ar fi o pantă de 100%.'),
        ('Ce robot de tuns iarba urcă cele mai mari pante?',
         'Dintre modelele recomandate de noi, Segway Navimow X450E (84%) și Mammotion Luba mini 2 AWD (80%), ambele cu tracțiune integrală. Pentru pante moderate, de până la 35%, Navimow i206 AWD este varianta mai accesibilă.'),
        ('Merge un robot obișnuit pe o curte în pantă?',
         'Pe pante de până la 15–20%, da, aproape orice model. Peste 30% ai nevoie de un robot care declară explicit 45% sau mai mult și, ideal, de tracțiune integrală.'),
    ],
},
{
    'slug': 'navimow-vs-mammotion',
    'date': '2026-11-26',
    'date_ro': '26 noiembrie 2026',
    'title': 'Segway Navimow vs Mammotion: ce robot alegi în 2026',
    'kind': 'article',
    'short': 'Navimow vs Mammotion',
    'desc': 'Segway Navimow sau Mammotion? Comparăm i206 AWD și i210 LiDAR cu Luba mini 2 AWD: navigare, pante, suprafață, preț în România și pentru ce curte e fiecare.',
    'h1': 'Segway Navimow vs Mammotion: ce robot de tuns iarba alegi',
    'lead': 'Cele două mărci care domină roboții fără fir, comparate pe ce contează: navigare, pante, preț și service.',
    'body': """<p>Dacă cauți un robot de tuns iarba fără fir de perimetru, ajungi aproape sigur la două nume: <strong>Segway Navimow</strong> și <strong>Mammotion</strong>. Ambele sunt mărci chinezești specializate, ambele au renunțat la firul îngropat și ambele se vând în România, inclusiv la Hornbach. Diferențele sunt însă reale și contează în funcție de curtea ta.</p>

<h2>Pe scurt</h2>
<ul><li><strong>Alege Navimow</strong> dacă ai o curte obișnuită, cu pante moderate (până la ~35%), și vrei cel mai bun raport preț/calitate, o aplicație foarte simplă și o gamă largă de modele.</li>
<li><strong>Alege Mammotion</strong> dacă ai pante mari, taluzuri sau teren denivelat, unde tracțiunea integrală puternică face diferența.</li></ul>

<h2>Modelele comparate</h2>
<div class="tw"><table class="t"><tr><th></th><th>Navimow i206 AWD</th><th>Navimow i210 LiDAR E</th><th>Mammotion Luba mini 2 AWD 1000</th></tr>
<tr><td>Suprafață recomandată</td><td>600 m²</td><td>1.000 m²</td><td>1.000 m²</td></tr>
<tr><td>Navigare</td><td>RTK + cameră AI</td><td>LiDAR + cameră</td><td>3 camere + NetRTK</td></tr>
<tr><td>Pantă maximă</td><td>45%</td><td>45%</td><td>80%</td></tr>
<tr><td>Tracțiune</td><td>integrală</td><td>fără AWD</td><td>integrală</td></tr>
<tr><td>Lățime de tăiere</td><td>18 cm</td><td>22 cm</td><td>20 cm</td></tr>
<tr><td>Preț orientativ în România</td><td>4.790 lei</td><td>5.999 lei</td><td>7.649 lei</td></tr></table></div>
{{CARDS:segway-navimow-i206-awd,segway-navimow-i210-lidar,mammotion-luba-mini-2-awd-1000}}

<h2>Navigare: satelit, camere sau LiDAR</h2>
<p>Navimow a construit sistemul EFLS, care combină poziționarea prin satelit RTK cu o cameră AI. Funcționează excelent în curți deschise, dar ca orice sistem bazat pe satelit poate avea probleme sub copaci deși. Pentru asemenea curți, Navimow are seria cu <strong>LiDAR</strong> (i210), care scanează spațiul în 3D și nu depinde de cer.</p>
<p>Mammotion merge pe varianta „vedere + rețea”: Luba mini 2 AWD folosește trei camere și NetRTK, adică primește corecțiile RTK prin internet, de la o rețea de stații de referință, în loc de o antenă pusă în curte. Producătorul spune că sistemul rămâne precis sub copaci și streașini. În practică, ambele abordări funcționează bine în majoritatea curților; diferențele apar la extreme (umbră densă, clădiri foarte înalte).</p>

<h2>Pante: aici Mammotion câștigă clar</h2>
<p>Mammotion a fost printre pionierii tracțiunii integrale la roboții de tuns, iar Luba mini 2 AWD urcă până la 80%. Navimow i206 AWD și i210 se opresc la 45%. Pentru o curte plană sau cu pante blânde, diferența nu contează. Pentru un taluz de 50–60%, Navimow din seria i nu e o opțiune; ar trebui să urci la seria X4 (X450E, 84%), care costă de două ori mai mult.</p>

<h2>Preț și raport calitate/preț</h2>
<p>Navimow este mai ieftin la aceeași suprafață: i206 AWD costă cu aproape 3.000 de lei mai puțin decât Luba mini 2 AWD, iar i210 LiDAR acoperă tot 1.000 m² pentru aproximativ 1.650 de lei mai puțin. Dacă nu ai nevoie de pantele de 80%, Navimow îți lasă bani pentru garaj, montaj sau o rezervă de lame.</p>

<h2>Aplicație, instalare și service</h2>
<p>Ambele mărci au aplicații în care desenezi zonele, setezi programul și vezi robotul în timp real. Navimow are reputația celei mai simple aplicații pentru începători; Mammotion oferă mai multe setări avansate (modele de tuns, zone, viteze), apreciate de cei care vor control. Pentru service și garanție, contează mult de unde cumperi: un magazin mare din România (Hornbach, eMAG, Altex) rezolvă returul și garanția local, ceea ce e mai important decât marca în sine.</p>

<h2>Verdictul nostru</h2>
<ul><li><strong>Curte plană sau cu pante blânde, până la 600 m²:</strong> Navimow i206 AWD.</li>
<li><strong>Curte de până la 1.000 m² cu mulți copaci:</strong> Navimow i210 LiDAR E.</li>
<li><strong>Curte în pantă abruptă, taluzuri, teren denivelat:</strong> Mammotion Luba mini 2 AWD.</li></ul>
<p>Pentru toate categoriile, vezi <a href="/cel-mai-bun-robot-tuns-iarba-2026.html">cel mai bun robot de tuns iarba în 2026</a>; pentru pante, <a href="/robot-tuns-iarba-panta.html">ghidul complet</a>. Poți compara orice trei modele față în față în <a href="/#compara">comparatorul de pe prima pagină</a>.</p>
<p class="note">Surse: fișele producătorilor Segway Navimow și Mammotion, ofertele Hornbach România (noiembrie 2026).</p>""" + NOTE,
    'faq': [
        ('Ce e mai bun, Navimow sau Mammotion?',
         'Depinde de curte. Navimow oferă un raport preț/calitate mai bun și o aplicație foarte simplă pentru curți plane sau cu pante moderate. Mammotion este mai bun pe pante mari, unde Luba mini 2 AWD urcă până la 80%.'),
        ('Au nevoie de antenă RTK în curte?',
         'Navimow i206 combină RTK cu o cameră AI; verifică în fișa modelului dacă vine cu antenă proprie. i210 se bazează pe LiDAR. Mammotion Luba mini 2 AWD folosește NetRTK, adică primește corecțiile prin internet, fără antenă proprie, acolo unde rețeaua este disponibilă.'),
        ('Care e mai silențios?',
         'Ambele mărci produc roboți silențioși, mult sub o mașină de tuns cu motor; pentru seria i2, Navimow declară în jur de 59 dB(A). Valoarea exactă pentru fiecare model este în fișa tehnică a producătorului.'),
    ],
},
]
