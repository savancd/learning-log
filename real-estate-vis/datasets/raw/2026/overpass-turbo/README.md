# overpass-turbo

The following file is to track all the downloaded data and sources.   


## Main Roads

> [!24.06.2026]   

![Screenshot](img/highway_motorway_link.geojson)

- File: highway_motorway_link.geojson   

### main roads script

```bash
[out:json][timeout:300];

way
["highway"~
"motorway|motorway_link|trunk|trunk_link|primary|primary_link|secondary|secondary_link"]
({{bbox}});

out geom;
```
