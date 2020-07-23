import argparse
import ee
from datetime import datetime, timezone
from task_base import EETask


class HIIRail(EETask):
    ee_rootdir = "projects/HII/v1/sumatra_poc"
    ee_driverdir = "driver/rail"
    ee_hiistatic_osm = "projects/HII/v1/source/osm_earth/"
    ee_hiistatic_infra = "projects/HII/v1/source/infra/"
    ee_hiistatic_physical = "projects/HII/v1/source/phys/"
    scale = 300
    DECAY_CONSTANT = -0.0002
    INDIRECT_INFLUENCE = 4


    railway_abandoned_weighting = 4
    railway_disused_weighting = 4
    railway_funicular_weighting = 10
    railway_halt_weighting = 10
    railway_light_rail_weighting = 10
    railway_miniature_weighting = 10
    railway_monorail_weighting = 10
    railway_narrow_gauge_weighting = 10
    railway_platform_weighting = 10
    railway_preserved_weighting = 10
    railway_rail_weighting = 10
    railway_station_weighting = 10
    railway_subway_weighting = 10
    railway_tram_weighting = 10


    inputs = {
        "railway_abandoned": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}railway/abandoned",
        },
        "railway_disused": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}railway/disused",
        },
        "railway_funicular": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}railway/funicular",
        },
        "railway_halt": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}railway/halt",
        },
        "railway_light_rail": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}railway/light_rail",
        },
        "railway_miniature": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}railway/miniature",
        },
        "railway_monorail": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}railway/monorail",
        },
        "railway_narrow_gauge": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}railway/narrow_gauge",
        },
        "railway_platform": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}railway/platform",
        },
        "railway_preserved": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}railway/preserved",
        },
        "railway_rail": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}railway/rail",
        },
        "railway_station": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}railway/station",
        },
        "railway_subway": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}railway/subway",
        },
        "railway_tram": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}railway/tram",
        },
        "watermask": {
            "ee_type": EETask.IMAGE,
            "ee_path": f"{ee_hiistatic_physical}watermask_jrc70_cciocean",
            "static": True,
        },
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_aoi_from_ee("{}/sumatra_poc_aoi".format(self.ee_rootdir))

    def calc(self):
        watermask = ee.Image(self.inputs["watermask"]["ee_path"])

        railway_abandoned, railway_abandoned_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["railway_abandoned"]["ee_path"])
        )
        
        railway_disused, railway_disused_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["railway_disused"]["ee_path"])
        )
        
        railway_funicular, railway_funicular_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["railway_funicular"]["ee_path"])
        )
        
        railway_halt, railway_halt_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["railway_halt"]["ee_path"])
        )
        
        railway_light_rail, railway_light_rail_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["railway_light_rail"]["ee_path"])
        )
        
        railway_miniature, railway_miniature_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["railway_miniature"]["ee_path"])
        )
        
        railway_monorail, railway_monorail_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["railway_monorail"]["ee_path"])
        )
        
        railway_narrow_gauge, railway_narrow_gauge_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["railway_narrow_gauge"]["ee_path"])
        )

        railway_platform, railway_platform_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["railway_platform"]["ee_path"])
        )

        railway_preserved, railway_preserved_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["railway_preserved"]["ee_path"])
        )
        
        railway_rail, railway_rail_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["railway_rail"]["ee_path"])
        )
        
        railway_station, railway_station_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["railway_station"]["ee_path"])
        )
        
        railway_subway, railway_subway_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["railway_subway"]["ee_path"])
        )
        
        railway_tram, railway_tram_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["railway_tram"]["ee_path"])
        )

        railway_total = (railway_abandoned.multiply(self.railway_abandoned_weighting)
            .add(railway_disused.multiply(self.railway_disused_weighting))
            .add(railway_funicular.multiply(self.railway_funicular_weighting))
            .add(railway_halt.multiply(self.railway_halt_weighting))
            .add(railway_light_rail.multiply(self.railway_light_rail_weighting))
            .add(railway_miniature.multiply(self.railway_miniature_weighting))
            .add(railway_monorail.multiply(self.railway_monorail_weighting))
            .add(railway_narrow_gauge.multiply(self.railway_narrow_gauge_weighting))
            .add(railway_platform.multiply(self.railway_platform_weighting))
            .add(railway_preserved.multiply(self.railway_preserved_weighting))
            .add(railway_rail.multiply(self.railway_rail_weighting))
            .add(railway_station.multiply(self.railway_station_weighting))
            .add(railway_subway.multiply(self.railway_subway_weighting))
            .add(railway_tram.multiply(self.railway_tram_weighting))
        ).multiply(2)

        # What should be the maximum?
        railway_total = railway_total.where(railway_total.gt(10), 10)

        rail_bool = railway_total.gt(0)

        rail_indirect = rail_bool.eq(0)\
            .cumulativeCost(rail_bool, 15000)\
            .reproject(crs=self.crs, scale=self.scale)\
            .multiply(self.DECAY_CONSTANT)\
            .exp()\
            .multiply(self.INDIRECT_INFLUENCE)\
            .unmask(0)

        rail_total = railway_total.add(rail_indirect).updateMask(watermask)

        self.export_image_ee(
            rail_total,
            "{}/{}".format(self.ee_driverdir, "hii_rail_driver"),
        )

    def check_inputs(self):
        super().check_inputs()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--taskdate", default=datetime.now(timezone.utc).date())
    options = parser.parse_args()
    rail_task = HIIRail(**vars(options))
    rail_task.run()