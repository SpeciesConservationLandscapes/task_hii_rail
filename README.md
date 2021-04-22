HII RAIL DRIVER
---------------

## What does this task do?

This task calculates the (unitless) anthropogenic "influence" of railways on the terrestrical surface as one of the key
drivers for a combined [Human Influence Index](https://github.com/SpeciesConservationLandscapes/task_hii_weightedsum)
. "Influence" is a combination of `direct` and `indirect` influence
relative to each cell with at least one railway feature. These source rail cells are a combination of:

1. The most recent OSM data relative to `taskdate`, as rasterized by the
   [task_hii_osm_csv](https://github.com/SpeciesConservationLandscapes/task_hii_osm_csv) and
   [task_hii_osm_ingest](https://github.com/SpeciesConservationLandscapes/task_hii_osm_ingest) tasks. This image,
   stored in Earth Engine at `projects/HII/v1/osm/osm_image`, contains up to 14
   bands for OSM features with railway tags. A cell in each band has a
   value of 1 in every 300m pixel if there are any OSM features with that tag in the cell, and NoData otherwise.
   This data is available since 2012-09-12, in steadily increasing quantity and quality.
2. Static VMap0 railway data (https://gis-lab.info/qa/vmap0-eng.html) representing
   1980-2010 are used to fill cells not marked by OSM. (Implicitly, we do not capture rails that actually disappear
   over time.) In the future, once VMap0's contribution is marginal enough, we will discontinue its use. Conversely,
   prior to 2012-09-12, it is the only source.

We are able to use the different OSM rail types to weight rail influence by type, a key advance over previous Human
Footprint efforts. These weights are based on the OSM Wiki descriptions: https://wiki.openstreetmap.org/wiki/Key:railway


```
railway_weights = {
      "railway_abandoned": 4,
      "railway_disused": 4,
      "railway_funicular": 10,
      "railway_halt": 10,
      "railway_light_rail": 10,
      "railway_miniature": 10,
      "railway_monorail": 10,
      "railway_narrow_gauge": 10,
      "railway_platform": 10,
      "railway_preserved": 10,
      "railway_rail": 10,
      "railway_station": 10,
      "railway_subway": 10,
      "railway_tram": 10,
      "vmap_rails": 10,
  }
```

Direct influence is calculated as the per-rail-type full weight (above) for 0.5 km to either side of a railway.

Indirect influence is calculated using an exponential decay function for 0.5 km to 15 km to either side of a railway:

- The indirect maximum weight (at 0.5 km) is 1/2 of the direct weight for a given rail type. (This is
  directly comparable to the logic followed by  
  [Venter et al. 2016](https://www.nature.com/articles/sdata201667))
- Utilized railways and abandoned railways have distinct decay functions, reflecting the relative degree of access from
  the railways itself by different modes of travel.
- The decay function is defined as:
```
indirect_influence = e^(distance * decay_constant) * indirect_weight
```

For any given output cell, the end result is the maximum (**not** the cumulative addition) of each direct and indirect
influence calculated for each type of railway. Values are multiplied by 100 and converted to integer for efficient
exporting to and storage in the Earth Engine HII Railway Driver image collection (`projects/HII/v1/driver/railways`).

## Variables and Defaults

### Environment variables
```
SERVICE_ACCOUNT_KEY=<GOOGLE SERVICE ACCOUNT KEY>
```

### Class constants

```
SCALE=300
OSM_START=(2012-09-09)
NOMINAL_RAIL_WIDTH=300
DIRECT_INFLUENCE_WIDTH=1000
INDIRECT_INFLUENCE_RADIUS=15000
DECAY_CONSTANT=-0.0002
DIRECT_INDIRECT_INFLUENCE_RATIO=0.5
```

## Usage

```
/app # python hii_rail.py --help
usage: task.py [-h] [-d TASKDATE]

optional arguments:
  -h, --help            show this help message and exit
  -d TASKDATE, --taskdate TASKDATE
```
