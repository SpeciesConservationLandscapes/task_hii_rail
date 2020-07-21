import argparse
import ee
from datetime import datetime, timezone
from task_base import EETask


class HIIInfrastructure(EETask):
    ee_rootdir = "projects/HII/v1/sumatra_poc"
    ee_driverdir = "driver/infrastructure"
    ee_hiistatic_osm = "projects/HII/v1/source/osm_earth/"
    ee_hiistatic_infra = "projects/HII/v1/source/infra/"
    ee_hiistatic_physical = "projects/HII/v1/source/phys/"
    scale = 300
    DECAY_CONSTANT = -0.0002
    INDIRECT_INFLUENCE = 4


    aeroway_aerodrome_weighting = 10
    aeroway_apron_weighting = 10
    aeroway_hangar_weighting = 10
    aeroway_helipad_weighting = 10
    aeroway_heliport_weighting = 10
    aeroway_runway_weighting = 10
    aeroway_spaceport_weighting = 10
    aeroway_taxiway_weighting = 10
    aeroway_terminal_weighting = 10

    amenity_aerialway_weighting = 5
    amenity_alpinecampwild_weighting = 4
    amenity_fuel_weighting = 10
    amenity_sanitary_dump_station_weighting = 10

    barrier_city_wall_weighting = 8
    barrier_ditch_weighting = 8
    barrier_hedge_weighting = 2
    barrier_retaining_wall_weighting = 8
    barrier_wall_weighting = 8

    highway_bridleway_weighting = 10
    highway_bus_guideway_weighting = 10
    highway_cycleway_weighting = 10
    highway_elevator_weighting = 10
    highway_escape_weighting = 4
    highway_footway_weighting = 4
    highway_living_street_weighting = 10
    highway_mini_roundabout_weighting = 10
    highway_motorway_weighting = 10
    highway_motorway_link_weighting = 10
    highway_path_weighting = 4
    highway_pedestrian_weighting = 4
    highway_primary_weighting = 10
    highway_primary_link_weighting = 10
    highway_raceway_weighting = 10
    highway_rest_area_weighting = 10
    highway_road_weighting = 10
    highway_secondary_weighting = 10
    highway_secondary_link_weighting = 10
    highway_service_weighting = 10
    highway_steps_weighting = 4
    highway_tertiary_weighting = 10
    highway_tertiary_link_weighting = 10
    highway_track_weighting = 4
    highway_trunk_weighting = 10
    highway_trunk_link_weighting = 10
    highway_turning_circle_weighting = 10
    highway_unclassified_weighting = 10

    highway_groads_weighting = 10

    landuse_basin_weighting = 10
    landuse_cemetery_weighting = 4
    landuse_industrial_weighting = 10
    landuse_landfill_weighting = 10
    landuse_quarry_weighting = 10
    landuse_salt_pond_weighting = 4
    landuse_village_green_weighting = 4

    leisure_beach_resort_weighting = 4
    leisure_golf_course_weighting = 4
    leisure_marina_weighting = 4
    leisure_pitch_weighting = 4

    man_made_adit_weighting = 10
    man_made_beacon_weighting = 10
    man_made_breakwater_weighting = 10
    man_made_chimney_weighting = 10
    man_made_communications_tower_weighting = 10
    man_made_dyke_weighting = 10
    man_made_embankment_weighting = 10
    man_made_gasometer_weighting = 10
    man_made_groyne_weighting = 10
    man_made_lighthouse_weighting = 10
    man_made_mast_weighting = 10
    man_made_mineshaft_weighting = 10
    man_made_observatorytelescope_weighting = 10
    man_made_petroleum_well_weighting = 10
    man_made_pier_weighting = 10
    man_made_pipeline_weighting = 10
    man_made_pumping_station_weighting = 10
    man_made_reservoir_covered_weighting = 10
    man_made_silo_weighting = 10
    man_made_snow_fence_weighting = 4
    man_made_storage_tank_weighting = 10
    man_made_tower_weighting = 10
    man_made_wastewater_plant_weighting = 10
    man_made_water_tower_weighting = 10
    man_made_water_well_weighting = 10
    man_made_water_works_weighting = 10
    man_made_watermill_weighting = 10
    man_made_windmill_weighting = 10
    man_made_works_weighting = 10

    military_airfield_weighting = 10
    military_ammunition_weighting = 10
    military_barracks_weighting = 10
    military_bunker_weighting = 10
    military_checkpoint_weighting = 10
    military_danger_area_weighting = 8
    military_naval_base_weighting = 10
    military_nuclear_explosion_site_weighting = 10
    military_range_weighting = 8
    military_trench_weighting = 8

    power_cable_weighting = 8
    power_heliostat_weighting = 10
    power_line_weighting = 8
    power_substation_weighting = 10
    power_xbio_weighting = 10
    power_xcoal_weighting = 10
    power_xhydro_weighting = 10
    power_xnuclear_weighting = 10
    power_xoil_weighting = 10
    power_xother_weighting = 10
    power_xsolar_weighting = 10
    power_xwaste_weighting = 10
    power_xwind_weighting = 10

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

    waterway_canal_weighting = 10
    waterway_dam_weighting = 10
    waterway_ditch_weighting = 4
    waterway_drain_weighting = 4
    waterway_lock_gate_weighting = 10
    waterway_weir_weighting = 4


    inputs = {
        "aeroway_aerodrome": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}aeroway/aerodrome",
        },
        "aeroway_apron": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}aeroway/apron",
        },
        "aeroway_hangar": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}aeroway/hangar",
        },
        "aeroway_helipad": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}aeroway/helipad",
        },
        "aeroway_heliport": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}aeroway/heliport",
        },
        "aeroway_runway": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}aeroway/runway",
        },
        "aeroway_spaceport": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}aeroway/spaceport",
        },
        "aeroway_taxiway": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}aeroway/taxiway",
        },
        "aeroway_terminal": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}aeroway/terminal",
        },
        "amenity_aerialway": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}amenity/aerialway",
        },
        "amenity_alpinecampwild": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}amenity/alpinecampwild",
        },
        "leisure_beach_resort": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}leisure/beach_resort",
        },
        "amenity_fuel": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}amenity/fuel",
        },
        "leisure_golf_course": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}leisure/golf_course",
        },
        "leisure_marina": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}leisure/marina",
        },
        "leisure_pitch": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}leisure/pitch",
        },
        "amenity_sanitary_dump_station": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}amenity/sanitary_dump_station",
        },
        "barrier_city_wall": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}barrier/city_wall",
        },
        "barrier_ditch": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}barrier/ditch",
        },
        "barrier_hedge": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}barrier/hedge",
        },
        "barrier_retaining_wall": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}barrier/retaining_wall",
        },
        "barrier_wall": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}barrier/wall",
        },
        "highway_bridleway": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}highway/bridleway",
        },
        "highway_bus_guideway": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}highway/bus_guideway",
        },
        "highway_cycleway": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}highway/cycleway",
        },
        "highway_elevator": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}highway/elevator",
        },
        "highway_escape": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}highway/escape",
        },
        "highway_footway": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}highway/footway",
        },
        "highway_living_street": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}highway/living_street",
        },
        "highway_mini_roundabout": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}highway/mini_roundabout",
        },
        "highway_motorway": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}highway/motorway",
        },
        "highway_motorway_link": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}highway/motorway_link",
        },
        "highway_path": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}highway/path",
        },
        "highway_pedestrian": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}highway/pedestrian",
        },
        "highway_primary": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}highway/primary",
        },
        "highway_primary_link": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}highway/primary_link",
        },
        "highway_raceway": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}highway/raceway",
        },
        "highway_rest_area": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}highway/rest_area",
        },
        "highway_road": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}highway/road",
        },
        "highway_secondary": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}highway/secondary",
        },
        "highway_secondary_link": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}highway/secondary_link",
        },
        "highway_service": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}highway/service",
        },
        "highway_steps": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}highway/steps",
        },
        "highway_tertiary": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}highway/tertiary",
        },
        "highway_tertiary_link": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}highway/tertiary_link",
        },
        "highway_track": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}highway/track",
        },
        "highway_trunk": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}highway/trunk",
        },
        "highway_trunk_link": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}highway/trunk_link",
        },
        "highway_turning_circle": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}highway/turning_circle",
        },
        "highway_unclassified": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}highway/unclassified",
        },
        "groads_additions": {
            "ee_type": EETask.IMAGE,
            "ee_path": f"{ee_hiistatic_infra}groads_additions",
        },
        "landuse_basin": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}landuse/basin",
        },
        "landuse_cemetery": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}landuse/cemetery",
        },
        "landuse_industrial": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}landuse/industrial",
        },
        "landuse_landfill": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}landuse/landfill",
        },
        "landuse_quarry": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}landuse/quarry",
        },
        "landuse_salt_pond": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}landuse/salt_pond",
        },
        "landuse_village_green": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}landuse/village_green",
        },
        "man_made_adit": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/adit",
        },
        "man_made_beacon": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/beacon",
        },
        "man_made_breakwater": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/breakwater",
        },
        "man_made_chimney": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/chimney",
        },
        "man_made_communications_tower": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/communications_tower",
        },
        "man_made_dyke": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/dyke",
        },
        "man_made_embankment": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/embankment",
        },
        "man_made_gasometer": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/gasometer",
        },
        "man_made_groyne": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/groyne",
        },
        "man_made_lighthouse": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/lighthouse",
        },
        "man_made_mast": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/mast",
        },
        "man_made_mineshaft": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/mineshaft",
        },
        "man_made_observatorytelescope": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/observatorytelescope",
        },
        "man_made_petroleum_well": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/petroleum_well",
        },
        "man_made_pier": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/pier",
        },
        "man_made_pipeline": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/pipeline",
        },
        "man_made_pumping_station": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/pumping_station",
        },
        "man_made_reservoir_covered": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/reservoir_covered",
        },
        "man_made_silo": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/silo",
        },
        "man_made_snow_fence": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/snow_fence",
        },
        "man_made_storage_tank": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/storage_tank",
        },
        "man_made_tower": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/tower",
        },
        "man_made_wastewater_plant": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/wastewater_plant",
        },
        "man_made_watermill": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/watermill",
        },
        "man_made_water_tower": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/water_tower",
        },
        "man_made_water_well": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/water_well",
        },
        "man_made_water_works": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/water_works",
        },
        "man_made_windmill": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/windmill",
        },
        "man_made_works": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/works",
        },
        "military_airfield": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}military/airfield",
        },
        "military_ammunition": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}military/ammunition",
        },
        "military_barracks": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}military/barracks",
        },
        "military_bunker": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}military/bunker",
        },
        "military_checkpoint": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}military/checkpoint",
        },
        "military_danger_area": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}military/danger_area",
        },
        "military_naval_base": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}military/naval_base",
        },
        "military_nuclear_explosion_site": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}military/nuclear_explosion_site",
        },
        "military_range": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}military/range",
        },
        "military_trench": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}military/trench",
        },
        "power_cable": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}power/cable",
        },
        "power_heliostat": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}power/heliostat",
        },
        "power_line": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}power/line",
        },
        "power_substation": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}power/substation",
        },
        "power_xbio": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}power/xbio",
        },
        "power_xcoal": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}power/xcoal",
        },
        "power_xhydro": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}power/xhydro",
        },
        "power_xnuclear": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}power/xnuclear",
        },
        "power_xoil": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}power/xoil",
        },
        "power_xother": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}power/xother",
        },
        "power_xsolar": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}power/xsolar",
        },
        "power_xwaste": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}power/xwaste",
        },
        "power_xwind": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}power/xwind",
        },
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
        "waterway_canal": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}waterway/canal",
        },
        "waterway_dam": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}waterway/dam",
        },
        "waterway_ditch": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}waterway/ditch",
        },
        "waterway_drain": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}waterway/drain",
        },
        "waterway_lock_gate": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}waterway/lock_gate",
        },
        "waterway_weir": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}waterway/weir",
        },
        "watermask": {
            "ee_type": EETask.IMAGE,
            "ee_path": f"{ee_hiistatic_physical}watermask_jrc70_cciocean",
            "maxage": 30,
        },
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_aoi_from_ee("{}/sumatra_poc_aoi".format(self.ee_rootdir))

    def calc(self):
        watermask = ee.Image(self.inputs["watermask"]["ee_path"])

        aeroway_aerodrome, aeroway_aerodrome_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["aeroway_aerodrome"]["ee_path"])
        )
        
        aeroway_apron, aeroway_apron_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["aeroway_apron"]["ee_path"])
        )
        
        aeroway_hangar, aeroway_hangar_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["aeroway_hangar"]["ee_path"])
        )
        
        aeroway_helipad, aeroway_helipad_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["aeroway_helipad"]["ee_path"])
        )
        
        aeroway_heliport, aeroway_heliport_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["aeroway_heliport"]["ee_path"])
        )
        
        aeroway_runway, aeroway_runway_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["aeroway_runway"]["ee_path"])
        )
        
        aeroway_spaceport, aeroway_spaceport_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["aeroway_spaceport"]["ee_path"])
        )
        
        aeroway_taxiway, aeroway_taxiway_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["aeroway_taxiway"]["ee_path"])
        )

        aeroway_terminal, aeroway_terminal_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["aeroway_terminal"]["ee_path"])
        )


        amenity_aerialway, amenity_aerialway_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["amenity_aerialway"]["ee_path"])
        )
        
        amenity_alpinecampwild, amenity_alpinecampwild_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["amenity_alpinecampwild"]["ee_path"])
        )
        
        amenity_fuel, amenity_fuel_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["amenity_fuel"]["ee_path"])
        )
        
        amenity_sanitary_dump_station, amenity_sanitary_dump_station_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["amenity_sanitary_dump_station"]["ee_path"])
        )
        

        barrier_city_wall, barrier_city_wall_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["barrier_city_wall"]["ee_path"])
        )
        
        barrier_ditch, barrier_ditch_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["barrier_ditch"]["ee_path"])
        )
        
        barrier_hedge, barrier_hedge_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["barrier_hedge"]["ee_path"])
        )
        
        barrier_retaining_wall, barrier_retaining_wall_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["barrier_retaining_wall"]["ee_path"])
        )
        
        barrier_wall, barrier_wall_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["barrier_wall"]["ee_path"])
        )
        

        highway_bridleway, highway_bridleway_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["highway_bridleway"]["ee_path"])
        )
        
        highway_bus_guideway, highway_bus_guideway_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["highway_bus_guideway"]["ee_path"])
        )
        
        highway_cycleway, highway_cycleway_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["highway_cycleway"]["ee_path"])
        )
        
        highway_elevator, highway_elevator_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["highway_elevator"]["ee_path"])
        )
        
        highway_escape, highway_escape_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["highway_escape"]["ee_path"])
        )
        
        highway_footway, highway_footway_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["highway_footway"]["ee_path"])
        )
        
        highway_living_street, highway_living_street_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["highway_living_street"]["ee_path"])
        )
        
        highway_mini_roundabout, highway_mini_roundabout_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["highway_mini_roundabout"]["ee_path"])
        )

        highway_motorway, highway_motorway_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["highway_motorway"]["ee_path"])
        )

        highway_motorway_link, highway_motorway_link_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["highway_motorway_link"]["ee_path"])
        )
        
        highway_path, highway_path_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["highway_path"]["ee_path"])
        )
        
        highway_pedestrian, highway_pedestrian_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["highway_pedestrian"]["ee_path"])
        )
        
        highway_primary, highway_primary_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["highway_primary"]["ee_path"])
        )
        
        highway_primary_link, highway_primary_link_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["highway_primary_link"]["ee_path"])
        )
        
        highway_raceway, highway_raceway_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["highway_raceway"]["ee_path"])
        )
        
        highway_rest_area, highway_rest_area_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["highway_rest_area"]["ee_path"])
        )
        
        highway_road, highway_road_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["highway_road"]["ee_path"])
        )

        highway_secondary, highway_secondary_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["highway_secondary"]["ee_path"])
        )

        highway_secondary_link, highway_secondary_link_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["highway_secondary_link"]["ee_path"])
        )
        
        highway_service, highway_service_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["highway_service"]["ee_path"])
        )
        
        highway_steps, highway_steps_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["highway_steps"]["ee_path"])
        )
        
        highway_tertiary, highway_tertiary_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["highway_tertiary"]["ee_path"])
        )
        
        highway_tertiary_link, highway_tertiary_link_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["highway_tertiary_link"]["ee_path"])
        )
        
        highway_track, highway_track_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["highway_track"]["ee_path"])
        )
        
        highway_trunk, highway_trunk_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["highway_trunk"]["ee_path"])
        )
        
        highway_trunk_link, highway_trunk_link_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["highway_trunk_link"]["ee_path"])
        )

        highway_turning_circle, highway_turning_circle_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["highway_turning_circle"]["ee_path"])
        )

        highway_unclassified, highway_unclassified_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["highway_unclassified"]["ee_path"])
        )


        landuse_basin, landuse_basin_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["landuse_basin"]["ee_path"])
        )
        
        landuse_cemetery, landuse_cemetery_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["landuse_cemetery"]["ee_path"])
        )
        
        landuse_industrial, landuse_industrial_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["landuse_industrial"]["ee_path"])
        )
        
        landuse_landfill, landuse_landfill_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["landuse_landfill"]["ee_path"])
        )
        
        landuse_quarry, landuse_quarry_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["landuse_quarry"]["ee_path"])
        )
        
        landuse_salt_pond, landuse_salt_pond_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["landuse_salt_pond"]["ee_path"])
        )
        
        landuse_village_green, landuse_village_green_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["landuse_village_green"]["ee_path"])
        )
        

        leisure_beach_resort, leisure_beach_resort_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["leisure_beach_resort"]["ee_path"])
        )
        
        leisure_golf_course, leisure_golf_course_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["leisure_golf_course"]["ee_path"])
        )
        
        leisure_marina, leisure_marina_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["leisure_marina"]["ee_path"])
        )
        
        leisure_pitch, leisure_pitch_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["leisure_pitch"]["ee_path"])
        )
        

        man_made_adit, man_made_adit_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_adit"]["ee_path"])
        )
        
        man_made_beacon, man_made_beacon_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_beacon"]["ee_path"])
        )
        
        man_made_breakwater, man_made_breakwater_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_breakwater"]["ee_path"])
        )
        
        man_made_chimney, man_made_chimney_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_chimney"]["ee_path"])
        )
        
        man_made_communications_tower, man_made_communications_tower_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_communications_tower"]["ee_path"])
        )
        
        man_made_dyke, man_made_dyke_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_dyke"]["ee_path"])
        )
        
        man_made_embankment, man_made_embankment_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_embankment"]["ee_path"])
        )
        
        man_made_gasometer, man_made_gasometer_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_gasometer"]["ee_path"])
        )

        man_made_groyne, man_made_groyne_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_groyne"]["ee_path"])
        )

        man_made_lighthouse, man_made_lighthouse_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_lighthouse"]["ee_path"])
        )
        
        man_made_mast, man_made_mast_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_mast"]["ee_path"])
        )
        
        man_made_mineshaft, man_made_mineshaft_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_mineshaft"]["ee_path"])
        )
        
        man_made_observatorytelescope, man_made_observatorytelescope_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_observatorytelescope"]["ee_path"])
        )
        
        man_made_petroleum_well, man_made_petroleum_well_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_petroleum_well"]["ee_path"])
        )
        
        man_made_pier, man_made_pier_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_pier"]["ee_path"])
        )
        
        man_made_pipeline, man_made_pipeline_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_pipeline"]["ee_path"])
        )
        
        man_made_pumping_station, man_made_pumping_station_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_pumping_station"]["ee_path"])
        )

        man_made_reservoir_covered, man_made_reservoir_covered_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_reservoir_covered"]["ee_path"])
        )

        man_made_silo, man_made_silo_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_silo"]["ee_path"])
        )
        
        man_made_snow_fence, man_made_snow_fence_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_snow_fence"]["ee_path"])
        )
        
        man_made_storage_tank, man_made_storage_tank_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_storage_tank"]["ee_path"])
        )
        
        man_made_tower, man_made_tower_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_tower"]["ee_path"])
        )
        
        man_made_wastewater_plant, man_made_wastewater_plant_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_wastewater_plant"]["ee_path"])
        )
        
        man_made_water_tower, man_made_water_tower_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_water_tower"]["ee_path"])
        )
        
        man_made_water_well, man_made_water_well_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_water_well"]["ee_path"])
        )
        
        man_made_water_works, man_made_water_works_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_water_works"]["ee_path"])
        )

        man_made_watermill, man_made_watermill_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_watermill"]["ee_path"])
        )

        man_made_windmill, man_made_windmill_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_windmill"]["ee_path"])
        )

        man_made_works, man_made_works_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_works"]["ee_path"])
        )


        military_airfield, military_airfield_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["military_airfield"]["ee_path"])
        )
        
        military_ammunition, military_ammunition_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["military_ammunition"]["ee_path"])
        )
        
        military_barracks, military_barracks_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["military_barracks"]["ee_path"])
        )
        
        military_bunker, military_bunker_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["military_bunker"]["ee_path"])
        )
        
        military_checkpoint, military_checkpoint_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["military_checkpoint"]["ee_path"])
        )
        
        military_danger_area, military_danger_area_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["military_danger_area"]["ee_path"])
        )
        
        military_naval_base, military_naval_base_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["military_naval_base"]["ee_path"])
        )
        
        military_nuclear_explosion_site, military_nuclear_explosion_site_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["military_nuclear_explosion_site"]["ee_path"])
        )

        military_range, military_range_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["military_range"]["ee_path"])
        )

        military_trench, military_trench_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["military_trench"]["ee_path"])
        )


        power_cable, power_cable_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_cable"]["ee_path"])
        )
        
        power_heliostat, power_heliostat_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_heliostat"]["ee_path"])
        )
        
        power_line, power_line_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_line"]["ee_path"])
        )
        
        power_substation, power_substation_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_substation"]["ee_path"])
        )
        
        power_xbio, power_xbio_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_xbio"]["ee_path"])
        )
        
        power_xcoal, power_xcoal_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_xcoal"]["ee_path"])
        )
        
        power_xhydro, power_xhydro_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_xhydro"]["ee_path"])
        )
        
        power_xnuclear, power_xnuclear_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_xnuclear"]["ee_path"])
        )

        power_xoil, power_xoil_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_xoil"]["ee_path"])
        )

        power_xother, power_xother_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_xother"]["ee_path"])
        )
        
        power_xsolar, power_xsolar_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_xsolar"]["ee_path"])
        )
        
        power_xwaste, power_xwaste_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_xwaste"]["ee_path"])
        )
        
        power_xwind, power_xwind_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_xwind"]["ee_path"])
        )


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
        

        waterway_canal, waterway_canal_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["waterway_canal"]["ee_path"])
        )
        
        waterway_dam, waterway_dam_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["waterway_dam"]["ee_path"])
        )
        
        waterway_ditch, waterway_ditch_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["waterway_ditch"]["ee_path"])
        )
        
        waterway_drain, waterway_drain_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["waterway_drain"]["ee_path"])
        )
        
        waterway_lock_gate, waterway_lock_gate_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["waterway_lock_gate"]["ee_path"])
        )
        
        waterway_weir, waterway_weir_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["waterway_weir"]["ee_path"])
        )
        

        aeroway_total = (aeroway_aerodrome.multiply(self.aeroway_aerodrome_weighting)
            .add(aeroway_apron.multiply(self.aeroway_apron_weighting))
            .add(aeroway_hangar.multiply(self.aeroway_hangar_weighting))
            .add(aeroway_helipad.multiply(self.aeroway_helipad_weighting))
            .add(aeroway_heliport.multiply(self.aeroway_heliport_weighting))
            .add(aeroway_runway.multiply(self.aeroway_runway_weighting))
            .add(aeroway_spaceport.multiply(self.aeroway_spaceport_weighting))
            .add(aeroway_taxiway.multiply(self.aeroway_taxiway_weighting))
            .add(aeroway_terminal.multiply(self.aeroway_terminal_weighting))
        )

        amenity_total = (amenity_aerialway.multiply(self.amenity_aerialway_weighting)
            .add(amenity_alpinecampwild.multiply(self.amenity_alpinecampwild_weighting))
            .add(amenity_fuel.multiply(self.amenity_fuel_weighting))
            .add(amenity_sanitary_dump_station.multiply(self.amenity_sanitary_dump_station_weighting))
        )


        barrier_total = (barrier_city_wall.multiply(self.barrier_city_wall_weighting)
            .add(barrier_ditch.multiply(self.barrier_ditch_weighting))
            .add(barrier_hedge.multiply(self.barrier_hedge_weighting))
            .add(barrier_retaining_wall.multiply(self.barrier_retaining_wall_weighting))
            .add(barrier_wall.multiply(self.barrier_wall_weighting))
        )

        highway_total = (highway_bridleway.multiply(self.highway_bridleway_weighting)
            .add(highway_bus_guideway.multiply(self.highway_bus_guideway_weighting))
            .add(highway_cycleway.multiply(self.highway_cycleway_weighting))
            .add(highway_elevator.multiply(self.highway_elevator_weighting))
            .add(highway_escape.multiply(self.highway_escape_weighting))
            .add(highway_footway.multiply(self.highway_footway_weighting))
            .add(highway_living_street.multiply(self.highway_living_street_weighting))
            .add(highway_mini_roundabout.multiply(self.highway_mini_roundabout_weighting))
            .add(highway_motorway.multiply(self.highway_motorway_weighting))
            .add(highway_motorway_link.multiply(self.highway_motorway_link_weighting))
            .add(highway_path.multiply(self.highway_path_weighting))
            .add(highway_pedestrian.multiply(self.highway_pedestrian_weighting))
            .add(highway_primary.multiply(self.highway_primary_weighting))
            .add(highway_primary_link.multiply(self.highway_primary_link_weighting))
            .add(highway_raceway.multiply(self.highway_raceway_weighting))
            .add(highway_rest_area.multiply(self.highway_rest_area_weighting))
            .add(highway_road.multiply(self.highway_road_weighting))
            .add(highway_secondary.multiply(self.highway_secondary_weighting))
            .add(highway_secondary_link.multiply(self.highway_secondary_link_weighting))
            .add(highway_service.multiply(self.highway_service_weighting))
            .add(highway_steps.multiply(self.highway_steps_weighting))
            .add(highway_tertiary.multiply(self.highway_tertiary_weighting))
            .add(highway_tertiary_link.multiply(self.highway_tertiary_link_weighting))
            .add(highway_track.multiply(self.highway_track_weighting))
            .add(highway_trunk.multiply(self.highway_trunk_weighting))
            .add(highway_trunk_link.multiply(self.highway_trunk_link_weighting))
            .add(highway_turning_circle.multiply(self.highway_turning_circle_weighting))
            .add(highway_unclassified.multiply(self.highway_unclassified_weighting))
            .add(ee.Image(self.inputs["groads_additions"]["ee_path"]).multiply(self.highway_groads_weighting))
        )

        landuse_total = (landuse_basin.multiply(self.landuse_basin_weighting)
            .add(landuse_cemetery.multiply(self.landuse_cemetery_weighting))
            .add(landuse_industrial.multiply(self.landuse_industrial_weighting))
            .add(landuse_landfill.multiply(self.landuse_landfill_weighting))
            .add(landuse_quarry.multiply(self.landuse_quarry_weighting))
            .add(landuse_salt_pond.multiply(self.landuse_salt_pond_weighting))
            .add(landuse_village_green.multiply(self.landuse_village_green_weighting))
        )

        leisure_total = (leisure_beach_resort.multiply(self.leisure_beach_resort_weighting)
            .add(leisure_golf_course.multiply(self.leisure_golf_course_weighting))
            .add(leisure_marina.multiply(self.leisure_marina_weighting))
            .add(leisure_pitch.multiply(self.leisure_pitch_weighting))
        )

        man_made_total = (man_made_adit.multiply(self.man_made_adit_weighting)
            .add(man_made_beacon.multiply(self.man_made_beacon_weighting))
            .add(man_made_breakwater.multiply(self.man_made_breakwater_weighting))
            .add(man_made_chimney.multiply(self.man_made_chimney_weighting))
            .add(man_made_communications_tower.multiply(self.man_made_communications_tower_weighting))
            .add(man_made_dyke.multiply(self.man_made_dyke_weighting))
            .add(man_made_embankment.multiply(self.man_made_embankment_weighting))
            .add(man_made_gasometer.multiply(self.man_made_gasometer_weighting))
            .add(man_made_groyne.multiply(self.man_made_groyne_weighting))
            .add(man_made_lighthouse.multiply(self.man_made_lighthouse_weighting))
            .add(man_made_mast.multiply(self.man_made_mast_weighting))
            .add(man_made_mineshaft.multiply(self.man_made_mineshaft_weighting))
            .add(man_made_observatorytelescope.multiply(self.man_made_observatorytelescope_weighting))
            .add(man_made_petroleum_well.multiply(self.man_made_petroleum_well_weighting))
            .add(man_made_pier.multiply(self.man_made_pier_weighting))
            .add(man_made_pipeline.multiply(self.man_made_pipeline_weighting))
            .add(man_made_pumping_station.multiply(self.man_made_pumping_station_weighting))
            .add(man_made_reservoir_covered.multiply(self.man_made_reservoir_covered_weighting))
            .add(man_made_silo.multiply(self.man_made_silo_weighting))
            .add(man_made_snow_fence.multiply(self.man_made_snow_fence_weighting))
            .add(man_made_storage_tank.multiply(self.man_made_storage_tank_weighting))
            .add(man_made_tower.multiply(self.man_made_tower_weighting))
            .add(man_made_wastewater_plant.multiply(self.man_made_wastewater_plant_weighting))
            .add(man_made_watermill.multiply(self.man_made_watermill_weighting))
            .add(man_made_water_tower.multiply(self.man_made_water_tower_weighting))
            .add(man_made_water_well.multiply(self.man_made_water_well_weighting))
            .add(man_made_water_works.multiply(self.man_made_water_works_weighting))
            .add(man_made_windmill.multiply(self.man_made_windmill_weighting))
            .add(man_made_works.multiply(self.man_made_works_weighting))
        )

        military_total = (military_airfield.multiply(self.military_airfield_weighting)
            .add(military_ammunition.multiply(self.military_ammunition_weighting))
            .add(military_barracks.multiply(self.military_barracks_weighting))
            .add(military_bunker.multiply(self.military_bunker_weighting))
            .add(military_checkpoint.multiply(self.military_checkpoint_weighting))
            .add(military_danger_area.multiply(self.military_danger_area_weighting))
            .add(military_naval_base.multiply(self.military_naval_base_weighting))
            .add(military_nuclear_explosion_site.multiply(self.military_nuclear_explosion_site_weighting))
            .add(military_range.multiply(self.military_range_weighting))
            .add(military_trench.multiply(self.military_trench_weighting))
        )

        power_total = (power_cable.multiply(self.power_cable_weighting)
            .add(power_heliostat.multiply(self.power_heliostat_weighting))
            .add(power_line.multiply(self.power_line_weighting))
            .add(power_substation.multiply(self.power_substation_weighting))
            .add(power_xbio.multiply(self.power_xbio_weighting))
            .add(power_xcoal.multiply(self.power_xcoal_weighting))
            .add(power_xhydro.multiply(self.power_xhydro_weighting))
            .add(power_xnuclear.multiply(self.power_xnuclear_weighting))
            .add(power_xoil.multiply(self.power_xoil_weighting))
            .add(power_xother.multiply(self.power_xother_weighting))
            .add(power_xsolar.multiply(self.power_xsolar_weighting))
            .add(power_xwaste.multiply(self.power_xwaste_weighting))
            .add(power_xwind.multiply(self.power_xwind_weighting))
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
        )

        waterway_total = (waterway_canal.multiply(self.waterway_canal_weighting)
            .add(waterway_dam.multiply(self.waterway_dam_weighting))
            .add(waterway_ditch.multiply(self.waterway_ditch_weighting))
            .add(waterway_drain.multiply(self.waterway_drain_weighting))
            .add(waterway_lock_gate.multiply(self.waterway_lock_gate_weighting))
            .add(waterway_weir.multiply(self.waterway_weir_weighting))
        )

        osm = aeroway_total\
            .add(amenity_total)\
            .add(barrier_total)\
            .add(landuse_total)\
            .add(leisure_total)\
            .add(man_made_total)\
            .add(military_total)\
            .add(power_total)\
            .add(waterway_total)\
            .multiply(2)


        # TODO: incorporate weightings and eliminate 500m buffer
        roads_bool = highway_total.gt(0).multiply(2)
        roads_500m = roads_bool.reduceNeighborhood(
            reducer=ee.Reducer.max(), kernel=ee.Kernel.square(1, "pixels")
        ).reproject(crs=self.crs, scale=self.scale)

        roads_indirect = roads_bool.eq(0)\
            .cumulativeCost(roads_bool, 15000)\
            .reproject(crs=self.crs, scale=self.scale)\
            .multiply(self.DECAY_CONSTANT)\
            .exp()\
            .multiply(self.INDIRECT_INFLUENCE)\
            .unmask(0)

        roads_total = roads_500m.add(roads_indirect)
        roads_total = roads_total.where(roads_total.gt(8), 8)

        rail_bool = railway_total.gt(0).multiply(2)
        rail_500m = rail_bool.reduceNeighborhood(
            reducer=ee.Reducer.max(), kernel=ee.Kernel.square(1, "pixels")
        ).reproject(crs=self.crs, scale=self.scale)

        current_infra = roads_total.add(rail_500m).add(osm).updateMask(watermask)

        self.export_image_ee(
            current_infra,
            "{}/{}".format(self.ee_driverdir, "hii_infrastructure_driver"),
        )

    def check_inputs(self):
        super().check_inputs()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--taskdate", default=datetime.now(timezone.utc).date())
    options = parser.parse_args()
    infrastructure_task = HIIInfrastructure(**vars(options))
    infrastructure_task.run()
