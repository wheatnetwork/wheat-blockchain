from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "wheat_harvester wheat_timelord_launcher wheat_timelord wheat_farmer wheat_full_node wheat_wallet".split(),
    "node": "wheat_full_node".split(),
    "harvester": "wheat_harvester".split(),
    "farmer": "wheat_harvester wheat_farmer wheat_full_node wheat_wallet".split(),
    "farmer-no-wallet": "wheat_harvester wheat_farmer wheat_full_node".split(),
    "farmer-only": "wheat_farmer".split(),
    "timelord": "wheat_timelord_launcher wheat_timelord wheat_full_node".split(),
    "timelord-only": "wheat_timelord".split(),
    "timelord-launcher-only": "wheat_timelord_launcher".split(),
    "wallet": "wheat_wallet".split(),
    "introducer": "wheat_introducer".split(),
    "simulator": "wheat_full_node_simulator".split(),
    "crawler": "wheat_crawler".split(),
    "seeder": "wheat_crawler wheat_seeder".split(),
    "seeder-only": "wheat_seeder".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
