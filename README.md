# Jupyter notebook alapu python feladatok keszitese

Motivacio:
- Jo lenne ha egy aktualis feladat verzio managelese egyszeru lenne oktatoi reszrol (eg: git)
- Jo lenne ha lennenek helyben, konnyen futtathato tesztek a feladatokra a tanuloknak (interaktiv kornyezet pl)
- Jo lenne ha nagyon kezdok is tudnak kezelni ezeket (ne kelljen sokat hozzatanulni egy kezdonek csak hogy futtatni tudjon)

Jupyter notebook + `nbgrader` modul-t hasznalunk feladatok megirasahoz, es ezek ellenorzesehez, valamint `jupyter_contrib_nbextensions`-t a teszt kornyezet automata konfiguraciojahoz.

Erdemes atnezni az `nbgrader` es az `init_cell` hasznalatat ha valaki feladatokat akar szerkeszteni.
* https://nbgrader.readthedocs.io/en/stable/
* https://github.com/ipython-contrib/jupyter_contrib_nbextensions
* https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/init_cell/README.html

# Altalanos leiras
Az nbgrader alapelve az, hogy a tanar megcsinalja a notebookot (specialis utasitasokkal lehet teszteket letrehozni, ezeket osztalyozni, stb). Mi itt csak a munkafuzetek automatikus teszteleset akarjuk (tanulo oldalon), az ide/oda kuldozgetest, kezi osztalyozast nem.

# Teacher notebook kornyezet
Az eredeti feladatok, megoldasok, tesztek kontenere. Ebbol kell generalni azokat a notebookokat amiket majd a tanulok kapnak meg. Ajanlott a `docker-compose` hasznalata.

## Docker-compose
```
docker-compose build teacher
docker-compose up -d teacher
```

## Docker build & run
```
docker build -t t360_python/teacher -f teacher_dockerfile .
docker run -p 8888:8888 -v $(pwd):/assignments/ t360_python/teacher
```

## Jupyter belepes
Futtatas utan kapunk egy URL-t, amire kattintsunk ra, vagy navigaljunk ide a bongeszoben, pl:
```
http://127.0.0.1:8888/?token=39a02779b8a0d36b17c1a24ccbef179c560551b93a0ae446
```

Ezutan latni fogjuk a Jupyter feluletet.

## Feladatok kezelese, szerkesztese
A `source` konyvtarban talalhatoak a feladatok.

A kotelezo szerkezet amit tartani kell:
`source/<feladat_neve>/<feladat_neve>.ipynb`

Ha megnyitjuk pl a `source/kezdo_python/kezdo_python.ipynb` notebookot, lathatjuk hogyan kell hozzaadni a feladatokat, tesztelest, stb.

Tesztelesre a `nose` modul van hasznalva a peldakban.

## Automatikus teszt kornyezet futtatas
A `jupyter_contrib_nbextensions` teszi lehetove, hogy a feladatok tesztelesehez kello kodreszleteket a kernel betoltesekor automatikusan futtassuk. Ez most a `jupyter_contrib_nbextensions` > `init_cell` modullal tortenik.

Az adott munkafuzetben a View > Cell toolbar > Initialization Cell -re kattintva lehet elohozni azt a cell headert, amit bekattintva a kernel toltesekor az adott cella automatikusan fut majd. A munkafuzetekben most ez a teszthez kello inicializaciot tolti be automatikusan.

## Tanulo notebookok generalasa
Kattintsunk a menuben a Formgrader tab-ra.

Automatikusan letrejonnek az "assignment"-ek. A generate ikonjara kattintva pedig az adott beadandohoz legeneralodik a tanuloi valtozat a `release` mappaba. Ezek a munkafuzetek bizonyos kodokat nem tartalmaznak, ezekben tudnak a tanulok kodolni es magukat ellenorizni.


# Tanulo notebook kornyezet
Ez a kornyezet szolgal a tanulo feladatmegoldasara. Ajanlott a `docker-compose` hasznalata. A tanar formgraderben generalt fajlokat masoljuk bele a kontenerbe az egyszeruseg kedveert, igy verziozhato maga a kontener a feladatokkal egyutt.

## Docker-compose
```
docker-compose build student
docker-compose up -d student
```

## Docker build & run
```
docker build -t t360_python/student -f student_dockerfile .
docker run -p 8887:8887 t360_python/student
```

## Jupyter belepes
Futtatas utan kapunk egy URL-t, amire kattintsunk ra, vagy navigaljunk ide a bongeszoben, pl:
```
http://127.0.0.1:8887/?token=39a02779b8a0d36b17c1a24ccbef179c560551b93a0ae446
```

Innentol pedig lehet feladatot megoldani
