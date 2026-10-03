"""Keep existing topic identities while organizing a revised course map."""
from copy import deepcopy


def reorganize(legacy_units, definitions, unit_mapping, topic_overrides, additions):
    units = [dict(name=name, description=description, ap_weight_min=minimum,
                  ap_weight_max=maximum, display_order=index + 1, topics=[])
             for index, (name, description, minimum, maximum) in enumerate(definitions)]
    by_name = {unit['name']: unit for unit in units}
    for old_unit in legacy_units:
        for topic in old_unit['topics']:
            target = topic_overrides.get(topic['name'], unit_mapping.get(old_unit['name']))
            if target is not None:
                by_name[target]['topics'].append(deepcopy(topic))
    for target, name, description, tags in additions:
        by_name[target]['topics'].append(dict(name=name, description=description, skill_tags=tags))
    for unit in units:
        for index, topic in enumerate(unit['topics']):
            topic['display_order'] = index + 1
    return units
