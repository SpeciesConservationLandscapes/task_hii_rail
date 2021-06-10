import argparse
import ee
from datetime import datetime, timezone
from task_base import HIITask


class HIIRail(HIITask):
    scale = 300
    OSM_START = datetime(2012, 9, 12).date()
    NOMINAL_RAIL_WIDTH = 300  # width of roads in inputs
    DIRECT_INFLUENCE_WIDTH = 1000  # total width of direct influence (meters)
    INDIRECT_INFLUENCE_RADIUS = (
        15000  # distance from road indirect influence limit (meters)
    )
    DECAY_CONSTANT = -0.0002
    DIRECT_INDIRECT_INFLUENCE_RATIO = 0.5

    inputs = {
        "osm": {
            "ee_type": HIITask.IMAGECOLLECTION,
            "ee_path": "projects/HII/v1/osm/osm_image",
            "maxage": 1,
        },
        # TODO: refactor source dir structure
        "vmap": {
            "ee_type": HIITask.IMAGE,
            "ee_path": "projects/HII/v1/source/infra/vMap-rails-v3-global",
            "static": True,
        },
        "water": {
            "ee_type": HIITask.IMAGE,
            "ee_path": "projects/HII/v1/source/phys/watermask_jrc70_cciocean",
            "static": True,
        },
    }

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.osm, _ = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["osm"]["ee_path"])
        )
        self.vmap = ee.Image(self.inputs["vmap"]["ee_path"])
        self.water = ee.Image(self.inputs["water"]["ee_path"])
        self.rail_direct_cost = None
        self.rail_indirect_cost = None
        self.kernel = {
            "DIRECT": ee.Kernel.euclidean(
                radius=self.DIRECT_INFLUENCE_WIDTH / 2, units="meters"
            ),
            "INDIRECT": ee.Kernel.euclidean(
                radius=self.INDIRECT_INFLUENCE_RADIUS, units="meters"
            ),
        }

    def osm_vmap_combined_influence(self):
        osm_band_names = self.osm.bandNames()
        vmap_band_names = self.vmap.bandNames()
        osm_weights = ee.Dictionary(self.railway_weights["osm"])
        vmap_weights = ee.Dictionary(self.railway_weights["vmap"])
        rail_weights = osm_weights.combine(vmap_weights)
        band_names = ee.Dictionary(
            {
                "all": rail_weights.keys(),
                "osm": osm_band_names.filter(
                    ee.Filter.inList("item", rail_weights.keys())
                ),
                "vmap": vmap_band_names.filter(
                    ee.Filter.inList("item", rail_weights.keys())
                ),
            }
        )
        direct_weights = rail_weights.toImage()
        indirect_weights = direct_weights.multiply(self.DIRECT_INDIRECT_INFLUENCE_RATIO)

        osm_rails = self.osm.select(band_names.get("osm"))
        osm_direct = (
            osm_rails.distance(kernel=self.kernel["DIRECT"], skipMasked=False)
            .lte((self.DIRECT_INFLUENCE_WIDTH - self.NOMINAL_RAIL_WIDTH) / 2)
            .multiply(direct_weights.select(band_names.get("osm")))
        )

        vmap_rails = self.vmap.select(band_names.get("vmap"))

        vmap_direct = (
            vmap_rails.distance(kernel=self.kernel["DIRECT"], skipMasked=False)
            .lte((self.DIRECT_INFLUENCE_WIDTH - self.NOMINAL_RAIL_WIDTH) / 2)
            .multiply(direct_weights.select(band_names.get("vmap")))
        )

        non_osm = osm_direct.reduce(ee.Reducer.max()).unmask(0).eq(0).selfMask()

        vmap_fill = vmap_direct.updateMask(non_osm)

        rail_direct_bands = osm_direct.addBands(vmap_fill)

        self.rail_direct_cost = rail_direct_bands.reduce(ee.Reducer.max()).rename(
            "rail_direct"
        )
        rail_indirect_cost_distance = rail_direct_bands.distance(
            kernel=self.kernel["INDIRECT"], skipMasked=False
        )

        rail_indirect_cost = rail_indirect_cost_distance.select(band_names.get("all"))

        self.rail_indirect_cost = (
            rail_indirect_cost.multiply(self.DECAY_CONSTANT)
            .exp()
            .multiply(indirect_weights.select(band_names.get("all")))
            .updateMask(
                rail_indirect_cost.lte(
                    self.INDIRECT_INFLUENCE_RADIUS - (self.DIRECT_INFLUENCE_WIDTH / 2)
                )
            )
            .reduce(ee.Reducer.max())
            .rename("rail_indirect")
        )

    def vmap_influence(self):
        vmap_band_names = self.vmap.bandNames()
        vmap_weights = ee.Dictionary(self.railway_weights["vmap"])

        band_names = ee.Dictionary(
            {
                "vmap": vmap_band_names.filter(
                    ee.Filter.inList("item", vmap_weights.keys())
                ),
            }
        )

        vmap_direct_weights = vmap_weights.toImage().select(band_names.get("vmap"))

        vmap_indirect_weights = vmap_direct_weights.multiply(
            self.DIRECT_INDIRECT_INFLUENCE_RATIO
        ).select(band_names.get("vmap"))

        rail_direct_cost = (
            self.vmap.select(band_names.get("vmap"))
            .distance(kernel=self.kernel["DIRECT"], skipMasked=False)
            .lte((self.DIRECT_INFLUENCE_WIDTH - self.NOMINAL_RAIL_WIDTH) / 2)
            .multiply(vmap_direct_weights)
            # .reduce(ee.Reducer.max())
            # .rename("rail_direct")
        )

        vmap_indirect_cost_distance = rail_direct_cost.distance(
            kernel=self.kernel["INDIRECT"], skipMasked=False
        )
        self.rail_direct_cost = rail_direct_cost.reduce(ee.Reducer.max()).rename(
            "rail_direct"
        )

        self.rail_indirect_cost = (
            vmap_indirect_cost_distance.multiply(self.DECAY_CONSTANT)
            .exp()
            .multiply(vmap_indirect_weights)
            .updateMask(
                vmap_indirect_cost_distance.lte(
                    self.INDIRECT_INFLUENCE_RADIUS - (self.DIRECT_INFLUENCE_WIDTH / 2)
                )
            )
            .reduce(ee.Reducer.max())
            .rename("rail_indirect")
        )

    def calc(self):
        if self.osm:
            self.osm_vmap_combined_influence()
        else:
            self.vmap_influence()

        rail_driver = (
            self.rail_direct_cost.addBands(self.rail_indirect_cost)
            .reduce(ee.Reducer.max())
            .unmask(0)
            .updateMask(self.water)
            .multiply(100)
            .int()
            .rename("hii_railway_driver")
        )

        self.export_image_ee(
            rail_driver,
            f"driver/railways",
        )

    def check_inputs(self):
        if self.taskdate >= self.OSM_START:
            super().check_inputs()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--taskdate")
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="overwrite existing outputs instead of incrementing",
    )
    options = parser.parse_args()
    rail_task = HIIRail(**vars(options))
    rail_task.run()
