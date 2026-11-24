from build import AFF_NOTE

JS = r"""
(function(){
function $(s){return document.querySelector(s)}
function f(x){return Math.round(x).toLocaleString('ro-RO')}
var c=$('#calc');if(!c)return;
function run(){
 var a=+$('#arie').value||0,p=+$('#panta').value||0,z=$('#zone').value,o=$('#obst').value,b=+$('#buget').value||0,h=+$('#ore').value||0,ore=+$('#tarif').value||0;
 var tech,why;
 if(z==='multe'||o==='multe'){tech='Fără fir, cu RTK + cameră (Vision AI) sau LiDAR';why='Ai mai multe zone sau multe obstacole: delimitarea virtuală din aplicație și ocolirea obstacolelor cu cameră îți scutesc zeci de metri de fir.'}
 else if(o==='copaci'){tech='Fără fir cu cameră/LiDAR sau RTK + cameră';why='Sub coroanele copacilor semnalul GPS-RTK slăbește; modelele care combină RTK cu cameră sau LiDAR se descurcă mai bine.'}
 else if(b<3000){tech='Cu fir de delimitare (perimetru)';why='La buget mic, modelele cu fir sunt cele mai accesibile și foarte fiabile, dar instalarea firului cere o zi de muncă.'}
 else{tech='Fără fir, cu GPS-RTK';why='Pentru o curte deschisă, RTK-ul oferă trasee drepte și zero fir de îngropat.'}
 var marja=a*1.25,cls=marja<=600?'până la 600 m²':marja<=1000?'până la 1.000 m²':marja<=1500?'până la 1.500 m²':marja<=3000?'până la 3.000 m²':'5.000 m² sau mai mult';
 var tract=p>25?' Alege un model cu tracțiune integrală (AWD) – panta ta depășește 25%.':'';
 $('#rTech').textContent=tech;$('#rCls').textContent=cls;$('#rWhy').textContent=why+tract;
 var oreAn=h*30,econ=oreAn*ore;
 $('#rOre').textContent=f(oreAn)+' ore/an';$('#rEcon').textContent=f(econ)+' lei/an';
 $('#rPay').textContent=econ>0?(b/econ).toFixed(1).replace('.',',')+' ani':'—';
}
c.addEventListener('input',run);c.addEventListener('change',run);run();
})();
"""

TOOL = """<div class="tool"><form id="calc" onsubmit="return false"><h2>Ce robot de tuns iarba ți se potrivește?</h2>
<div class="grid3">
<div><label class="f" for="arie">Suprafața gazonului (m²)</label><input id="arie" type="number" min="0" value="600"></div>
<div><label class="f" for="panta">Panta maximă (%)</label><input id="panta" type="number" min="0" max="100" value="15"></div>
<div><label class="f" for="buget">Buget (lei)</label><input id="buget" type="number" min="0" step="100" value="5000"></div>
<div><label class="f" for="zone">Zone separate de gazon</label><select id="zone"><option value="una">Una singură</option><option value="doua">Două</option><option value="multe">Trei sau mai multe</option></select></div>
<div><label class="f" for="obst">Obstacole</label><select id="obst"><option value="putine">Puține (gazon deschis)</option><option value="copaci">Copaci mari, umbră</option><option value="multe">Multe: straturi, jucării, mobilier</option></select></div>
<div><label class="f" for="ore">Ore pe săptămână cu tunsul acum</label><input id="ore" type="number" min="0" step="0.5" value="1.5"></div>
<div><label class="f" for="tarif">Cât valorează o oră din timpul tău <small>(lei)</small></label><input id="tarif" type="number" min="0" value="40"></div>
</div>
<div class="res"><div class="big"><div class="kpi main"><span>Tehnologie recomandată</span><b id="rTech" style="font-size:19px">–</b></div><div class="kpi"><span>Alege un model pentru</span><b id="rCls">–</b></div></div>
<p id="rWhy" style="margin:12px 0"></p>
<div class="big"><div class="kpi"><span>Timp economisit (sezon ~30 săpt.)</span><b id="rOre">–</b></div><div class="kpi"><span>Valoarea timpului</span><b id="rEcon">–</b></div><div class="kpi"><span>Se „plătește” în</span><b id="rPay">–</b></div></div>
<p class="note">Regula noastră: alege un robot cu capacitate declarată cu cel puțin 25% peste suprafața reală. Producătorii indică suprafețe pentru condiții ideale.</p></div></form></div>"""

MODELS = """<div class="tw"><table class="t"><tr><th>Model (exemplu)</th><th>Suprafață</th><th>Navigație</th><th class="n">Preț văzut</th></tr>
<tr><td>Ecovacs GOAT O600 RTK</td><td>~600 m²</td><td>RTK, fără fir</td><td class="n">3.690 lei</td></tr>
<tr><td>Segway Navimow i105E</td><td>500 m²</td><td>GPS-RTK + cartografiere AI</td><td class="n">4.290 lei</td></tr>
<tr><td>Segway Navimow i206 AWD</td><td>600 m²</td><td>GPS-RTK + Vision AI, tracțiune integrală</td><td class="n">4.790 lei</td></tr>
<tr><td>Segway Navimow i210 LiDAR</td><td>1.000 m²</td><td>LiDAR + cameră</td><td class="n">–</td></tr>
<tr><td>Husqvarna Automower 430X NERA</td><td>3.200 m²</td><td>Fir sau fără fir (cu modul EPOS)</td><td class="n">–</td></tr>
<tr><td>Segway Navimow X450E</td><td>până la 5.000 m²</td><td>RTK, 43 cm lățime de tăiere</td><td class="n">16.490 lei</td></tr></table></div>
<p class="note">Prețuri observate la un mare magazin de bricolaj din România în 2026. Prețurile se schimbă des, mai ales primăvara.</p>"""

INDEX_BODY = TOOL + """
<section class="sec"><h2>Cum alegi un robot de tuns iarba în 2026</h2>
<p>Cea mai mare schimbare din ultimii doi ani: <strong>roboții fără fir</strong> au coborât sub 5.000 de lei. Până de curând, aproape toți roboții cereau un fir de perimetru îngropat în jurul gazonului. Acum, modelele cu GPS-RTK, cameră AI sau LiDAR își „desenează” singure harta în aplicație.</p>
<h3>Cele trei întrebări care decid</h3><ol><li><strong>Cât de mare este gazonul?</strong> Ia o capacitate cu 25% peste suprafața reală.</li><li><strong>Ai pante?</strong> Peste ~25%, caută tracțiune integrală (AWD).</li><li><strong>Ai copaci și colțuri?</strong> RTK-ul simplu pierde precizia sub coroane; combinația RTK + cameră sau LiDAR rezolvă problema.</li></ol>
<h2>Exemple de modele și prețuri</h2>""" + MODELS + AFF_NOTE + """</section>
<div class="box"><b>Acum e iarnă: cum păstrezi robotul.</b> Bateria nu iubește frigul. Curăță robotul, încarcă bateria la nivel mediu și ține-l în interior, la temperatură pozitivă. <a href="/robot-tuns-iarba-iarna.html">Ghidul complet →</a></div>
<section class="sec"><h2>Ghiduri</h2><div class="cards">
<a class="c" href="/robot-cu-fir-sau-fara-fir.html"><span class="tag">Comparație</span><b>Cu fir sau fără fir?</b><span>RTK, cameră, LiDAR: avantaje și capcane.</span></a>
<a class="c" href="/cat-costa-robot-tuns-iarba.html"><span class="tag">Prețuri</span><b>Cât costă un robot de tuns iarba</b><span>Pe trepte de suprafață, cu exemple reale.</span></a>
<a class="c" href="/robot-tuns-iarba-iarna.html"><span class="tag">Întreținere</span><b>Robotul iarna</b><span>Depozitare, baterie, cuțite.</span></a></div></section>"""

FAQ = [
    ('Merită un robot de tuns iarba pentru 300 m²?', 'Da, dacă vrei gazonul tuns des fără efort. La suprafețe mici există modele fără fir sub 4.000 de lei și modele cu fir și mai ieftine. Tunsul frecvent, cu fire scurte lăsate pe gazon (mulcire), îmbunătățește și aspectul ierbii.'),
    ('Robotul fără fir merge sub copaci?', 'Modelele doar cu RTK pot pierde precizia sub coroanele dese. Alege un model care combină RTK cu cameră (Vision AI) sau LiDAR dacă ai mulți copaci.'),
    ('Pot lăsa robotul afară iarna?', 'Nu e recomandat. Producătorii sfătuiesc depozitarea în interior, curat și cu bateria încărcată parțial, la temperaturi pozitive.'),
]

ART_FIR = """<p>Alegerea dintre un robot cu fir de perimetru și unul fără fir este prima decizie. Iată diferențele, fără marketing.</p>
<h2>Roboții cu fir de delimitare</h2><p>Un fir subțire, îngropat sau prins cu cuie la marginea gazonului, îi arată robotului unde să se oprească. <strong>Plus:</strong> fiabili, ieftini, funcționează oriunde, inclusiv sub copaci. <strong>Minus:</strong> instalarea durează, firul se poate rupe la săpături și schimbarea formei grădinii înseamnă reinstalare.</p>
<h2>Roboții fără fir: trei tehnologii</h2>
<h3>GPS-RTK</h3><p>Robotul folosește sateliți și o stație de referință (sau o rețea RTK) pentru o precizie de câțiva centimetri. Trasează benzi drepte și desenezi zonele în aplicație. Punct slab: zonele umbrite de copaci înalți sau de clădiri.</p>
<h3>Cameră cu inteligență artificială (Vision AI)</h3><p>Robotul vede marginea gazonului și obstacolele. Multe modele noi combină RTK cu cameră pentru a acoperi punctele moarte.</p>
<h3>LiDAR</h3><p>Un senzor laser scanează împrejurimile și construiește harta, fără să depindă de sateliți. Bun pentru grădini cu mulți copaci.</p>
<h2>Ce alegi</h2><div class="tw"><table class="t"><tr><th>Grădina ta</th><th>Recomandare</th></tr><tr><td>Deschisă, fără copaci mari</td><td>RTK</td></tr><tr><td>Mulți copaci, umbră</td><td>RTK + cameră sau LiDAR</td></tr><tr><td>Buget foarte mic</td><td>Cu fir</td></tr><tr><td>Mai multe zone separate</td><td>Fără fir (zonele se definesc în aplicație)</td></tr></table></div>
<div class="box info">Răspunde la 6 întrebări în <a href="/">selectorul de robot</a> și vezi recomandarea pentru curtea ta.</div>"""

ART_PRET = """<p>Prețul unui robot de tuns iarba depinde de trei lucruri: suprafața, tehnologia de navigație și tracțiunea. Iată pragurile de preț pe care le vezi în magazinele din România în 2026.</p>
<h2>Pe trepte de suprafață</h2><ul><li><strong>Până la 600 m²:</strong> modelele fără fir cu RTK pornesc de la circa 3.700 de lei (ex. Ecovacs GOAT O600 RTK, 3.690 lei), iar Segway Navimow i105E costă în jur de 4.290 de lei.</li><li><strong>600–1.000 m²:</strong> modele cu tracțiune integrală sau LiDAR, de la circa 4.800 de lei (Navimow i206 AWD, 4.790 lei).</li><li><strong>Peste 3.000 m²:</strong> modelele profesionale ajung la peste 16.000 de lei (Navimow X450E, 16.490 lei, pentru până la 5.000 m²).</li></ul>
<h2>Tabel cu exemple</h2>""" + MODELS + AFF_NOTE + """
<h2>Costuri suplimentare</h2><ul><li>Instalare (dacă nu o faci singur), mai ales la modelele cu fir.</li><li>Garaj sau acoperiș pentru stație.</li><li>Cuțite de schimb: se schimbă de mai multe ori pe sezon.</li><li>La unele modele fără fir: modul 4G sau stație RTK separată.</li></ul>
<h2>Când e cel mai bun moment să cumperi</h2><p>Modelele noi apar de obicei primăvara, iar reducerile la modelele din anul anterior apar toamna și iarna. Dacă poți aștepta, compară prețurile din decembrie–februarie cu cele din aprilie.</p>"""

ART_IARNA = """<p>Sezonul de tuns s-a încheiat. Cum îți pregătești robotul pentru iarnă determină cât rezistă bateria și cât de repede pornește în aprilie.</p>
<h2>Pașii de depozitare</h2><ol><li><strong>Curăță complet</strong> robotul: dedesubt, roțile și cuțitele, cu o perie și o lavetă umedă. Fără furtun de apă.</li><li><strong>Verifică cuțitele</strong>: dacă sunt tocite, notează-ți să le schimbi primăvara.</li><li><strong>Bateria</strong>: încarcă-o la un nivel mediu și ține robotul în interior, la temperatură pozitivă. Frigul și descărcarea completă scurtează viața bateriilor litiu-ion.</li><li><strong>Stația de încărcare</strong>: deconectează sursa de alimentare. Mulți producători recomandă ca și stația să fie depozitată în interior.</li><li><strong>Firul de perimetru</strong> (dacă există) rămâne în pământ fără probleme.</li><li><strong>Actualizarea software</strong>: fă-o primăvara, înainte de prima tundere.</li></ol>
<h2>Service de iarnă</h2><p>Unii dealeri oferă revizie de iarnă: verifică motoarele, bateria și senzorii. Merită la modelele scumpe sau dacă ai observat probleme în sezon.</p>
<h2>Primăvara</h2><p>Prima tundere o faci cu o mașină clasică dacă iarba este foarte înaltă, apoi lași robotul să preia. Setează inițial o înălțime de tăiere mai mare și coboar-o treptat.</p>
<div class="box info">Te gândești să cumperi pentru primăvară? Iarna e perioada cu reduceri la modelele anului trecut. Vezi <a href="/cat-costa-robot-tuns-iarba.html">prețurile orientative</a>.</div>"""

SITE = {
    'name': 'RobotGazon', 'domain': 'robotgazon.online',
    'c1': '#1b7a43', 'c2': '#2fb36b', 'accent': '#ffcc33',
    'mark': '<rect x="12" y="24" width="40" height="20" rx="10" fill="#fff"/><circle cx="20" cy="46" r="5" fill="#ffcc33"/><circle cx="44" cy="46" r="5" fill="#ffcc33"/><path d="M28 24l4-8 4 8" fill="#fff"/>',
    'tagline': 'Ghiduri independente pentru roboții de tuns iarba: ce model alegi, cât costă și cum îl întreții.',
    'badges': ['Prețuri 2026', 'Cu fir vs fără fir', 'Selector gratuit'],
    'nav': [('/', 'Selector'), ('/robot-cu-fir-sau-fara-fir.html', 'Fir vs fără fir'), ('/cat-costa-robot-tuns-iarba.html', 'Prețuri'), ('/ghiduri.html', 'Ghiduri')],
    'main_tool': 'Selector robot de tuns iarba',
    'side_title': 'Ce robot ți se potrivește?', 'side_text': 'Suprafață, pantă, obstacole: recomandarea în 6 întrebări.',
    'about': '<p>RobotGazon este un site independent care compară roboții de tuns iarba disponibili în România. Folosim fișele tehnice ale producătorilor și prețurile publice din magazine.</p><p>Nu primim produse gratuite pentru recenzii. Unele linkuri pot fi de afiliere și sunt marcate.</p>',
    'js': JS,
    'pages': [
        {'slug': 'index', 'title': 'Robot de tuns iarba: ce model alegi în 2026 | RobotGazon', 'kind': 'tool', 'short': 'Selector robot', 'appcat': 'LifestyleApplication',
         'desc': 'Află ce robot de tuns iarba ți se potrivește: cu fir sau fără fir (RTK, cameră, LiDAR), ce capacitate și ce buget. Exemple de modele și prețuri din România.',
         'h1': 'Robot de tuns iarba: ce model ți se potrivește?', 'toolname': 'Selector robot de tuns iarba',
         'lead': 'Răspunde la câteva întrebări despre curtea ta și afli tehnologia potrivită, capacitatea necesară și în cât timp își „plătește” robotul timpul economisit.', 'body': INDEX_BODY, 'faq': FAQ},
        {'slug': 'robot-cu-fir-sau-fara-fir', 'title': 'Robot de tuns iarba cu fir sau fără fir? RTK, cameră, LiDAR', 'kind': 'article', 'short': 'Cu fir sau fără fir?',
         'desc': 'Diferențele dintre roboții de tuns iarba cu fir de perimetru și cei fără fir (GPS-RTK, Vision AI, LiDAR) și ce alegi pentru grădina ta.',
         'h1': 'Robot cu fir sau fără fir: ce alegi', 'lead': 'Cum funcționează fiecare tehnologie și unde dă greș.', 'body': ART_FIR},
        {'slug': 'cat-costa-robot-tuns-iarba', 'title': 'Cât costă un robot de tuns iarba în 2026', 'kind': 'article', 'short': 'Cât costă un robot',
         'desc': 'Prețuri reale pentru roboți de tuns iarba în România în 2026: de la ~3.700 lei (fără fir, 600 m²) la peste 16.000 lei pentru 5.000 m². Costuri suplimentare.',
         'h1': 'Cât costă un robot de tuns iarba în 2026', 'lead': 'Praguri de preț pe suprafață, exemple de modele și costurile la care nu te gândești.', 'body': ART_PRET},
        {'slug': 'robot-tuns-iarba-iarna', 'title': 'Robotul de tuns iarba iarna: depozitare și baterie', 'kind': 'article', 'short': 'Robotul iarna',
         'desc': 'Cum pregătești robotul de tuns iarba pentru iarnă: curățare, baterie, stație de încărcare, fir de perimetru și repornirea de primăvară.',
         'h1': 'Cum pregătești robotul de tuns iarba pentru iarnă', 'lead': 'Șase pași care prelungesc viața bateriei și a robotului.', 'body': ART_IARNA},
    ]
}
