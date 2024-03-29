HII RAIL DRIVER
---------------

## What does this task do?

This task calculates the anthropogenic impact of railways on the terrestrial surface as one of the key
drivers for a combined [Human Impact Index](https://github.com/SpeciesConservationLandscapes/task_hii_weightedsum). 
"Impact" is the `direct` impact relative to each cell with at least one railway feature; unlike roads, we do not 
calculate indirect impact of railways. 
The output HII driver calculated by this task is, like all other HII drivers, unitless; it refers to an absolute 0-10
scale but is not normalized to it, so the actual range of values may be smaller than 0-10.

Source railway cells are a combination of:

1. The most recent OSM data relative to `taskdate`, as rasterized by the
   [task_hii_osm_csv](https://github.com/SpeciesConservationLandscapes/task_hii_osm_csv) and
   [task_hii_osm_ingest](https://github.com/SpeciesConservationLandscapes/task_hii_osm_ingest) tasks. This image,
   stored in Earth Engine at `projects/HII/v1/osm/osm_image`, contains up to 14
   bands for OSM features with railway tags. A cell in each band has a
   value of 1 in every 300m pixel if there are any OSM features with that tag in the cell, and NoData otherwise.
   This data is available since 2012-09-12, in steadily increasing quantity and quality; for HII calculations we 
   use OSM data starting in June 2014.
2. Static VMap0 railway data (https://gis-lab.info/qa/vmap0-eng.html) representing
   1980-2010 are used to fill cells not marked by OSM. (Implicitly, we do not capture rails that actually disappear
   over time.) In the future, once VMap0's contribution is marginal enough, we will discontinue its use. Conversely,
   prior to 2014-06-04, it is the only source.

We are able to use the different OSM rail types to weight rail impact by type, a key advance over previous Human
Footprint efforts. These weights are based on the 
[OSM Wiki descriptions](https://wiki.openstreetmap.org/wiki/Key:railway).

```
railway_weights = {
      "osm": {
          "railway_abandoned": 4,
          "railway_disused": 4,
          "railway_miniature": 4,
          "railway_preserved": 4,
          "railway_funicular": 10,
          "railway_halt": 10,
          "railway_light_rail": 10,
          "railway_monorail": 10,
          "railway_narrow_gauge": 10,
          "railway_platform": 10,
          "railway_rail": 10,
          "railway_station": 10,
          "railway_subway": 10,
          "railway_tram": 10,
      },
      "vmap": {
          "Not_Usable": 6,
          "Doubtful": 7,
          "Unexamined_Unsurveyed": 10,
          "Under_Construction": 9,
          "Operational": 10,
      },
  }
```

Direct impact is calculated as the per-rail-type full weight (above) for 0.5 km to either side of a railway. 
For any given output cell, the end result is the maximum (**not** the cumulative addition) of each direct 
impact calculated for each type of railway. Values are multiplied by 100 and converted to integer for efficient
exporting to and storage in the Earth Engine HII Railway Driver image collection (`projects/HII/v1/driver/railways`).

## Variables and Defaults

### Environment variables
```
SERVICE_ACCOUNT_KEY=<GOOGLE SERVICE ACCOUNT KEY>
```

### Class constants

```
OSM_START = datetime(2014, 6, 4).date()
NOMINAL_RAIL_WIDTH=300
DIRECT_INFLUENCE_WIDTH=1000
DECAY_CONSTANT=-0.0002
```

## Usage

*All parameters may be specified in the environment as well as the command line.*

```
/app # python task.py --help
usage: task.py [-h] [-d TASKDATE] [--overwrite]

optional arguments:
  -h, --help            show this help message and exit
  -d TASKDATE, --taskdate TASKDATE
  --overwrite           overwrite existing outputs instead of incrementing

```

### License
Copyright (C) 2022 Wildlife Conservation Society
The files in this repository  are part of the task framework for calculating 
Human Impact Index and Species Conservation Landscapes (https://github.com/SpeciesConservationLandscapes) 
and are released under the GPL license:
https://www.gnu.org/licenses/#GPL
See [LICENSE](./LICENSE) for details.
