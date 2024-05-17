# Echte Geodaten in echten Games

Dies ist die praktische Arbeit der Seminararbeit "Echte Geodaten in echten Games" von Vincent Mielke im Sommersemester 2024.
Dieses Projekt kann zum Schneiden und Skalieren von geografischen Daten verwendet werden.
Dafür verwendet es die Python Bibliotheken geopandas und shapely.

## Funktionsweise

Die Geodaten werden geladen, falls gewünscht geschnitten, skaliert und die skalierten Daten ins out-Verzeichnis geschrieben.
Zur Anpassung werden einige Argumente verwendet die über die Kommandozeile übergeben werden können.

### Kommandozeilen Argumente

| Argument | Beschreibung                                                                                                                                                                                                                          | Beispiele                                             |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| -i       | Eingabedateien mit geografischen Daten die skaliert werden sollen. Kann eine Liste von Dateien sein. Wenn Liste dann muss sie die selbe Größe wie die Liste der Ausgabedateien sein!                                                  | -i ./roads.shp oder -i ./roads.shp,./buildings.shp    |
| -o       | Namen der Dateien in welche die skalierten Daten gespeichert werden sollen. Kann eine Liste von Namen sein. Wenn Liste dann muss sie die selbe Größe wie die Liste der Ausgabedateien sein!                                           | -o roads_scaled oder -o roads_scaled,buidlings_scaled |
| -x | Faktor mit dem die x-Achse skaliert werden soll                                                                                                                                                                                       | -x 0.5                                                |
| -y (optional) | Faktor mit dem die y-Achse skaliert werden soll. Falls nicht angegeben wird Faktor für x-Achse verwendet                                                                                                                              | -y 2                                                  |
| -c (optional) | Zentrum in der Form x,y um das die Daten skaliert werden sollen. Wenn mehrere Dateien skaliert werden sollen muss dieser oder -sc gesetzt sein!                                                | -c 8.393687,48.997433                                 |
| -b (optional) | Bereich der aus den Daten ausgeschnitten und skaliert werden soll. In der Form minx, miny, maxx, maxy                                                                                                                                 | -b 8.388870,49.010217,8.417152,49.017461              |
| -sc (optional) | Skalierungszentrum um welches mehrere geografische Dateien skaliert werden sollen. Gibt den Index der Datei an um welches Zentrum skaliert werden soll. Wenn mehrere Dateien skaliert werden sollen muss dieser oder -c gesetzt sein! | -sc 0                                                 |

## Beispielaufrufe

```shell
-i ./roads.shp -o roads_scaled -x 2
```

```shell
-i ./roads.shp -o roads_scaled -x 2 -y 0.5
```

```shell
-i ./roads.shp,./buildings.shp -o roads_centered,buidlings_centered -x 0.5 -b 8.3,49.0,8.4,49.1 -sc 0
```

```shell
-i ./roads.shp,./buildings.shp -o roads_centered,buidlings_centered -x 0.5 -b 8.3,49.0,8.4,49.1 -c 8.34,49.08
```