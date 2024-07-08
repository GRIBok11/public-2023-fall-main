import typing as tp


def get_unique_page_ids(records: list[tp.Mapping[str, tp.Any]]) -> set[int]:
    """
    Get unique web pages visited
    :param records: records of hit-log
    :return: Unique web pages
    """
    unique_page_ids = set()
    for record in records:
        page_ids = record.get('PageID')
        if isinstance(page_ids, int):
            unique_page_ids.add(page_ids)
        elif isinstance(page_ids, (list, tuple)):
            unique_page_ids.update(page_ids)
    return unique_page_ids


def get_unique_page_ids_visited_after_ts(records: list[tp.Mapping[str, tp.Any]], ts: int) -> set[int]:
    """
    Get unique web pages visited after some timestamp (not included)
    :param records: records of hit-log
    :param ts: timestamp
    :return: Unique web pages visited in hit-log after some timestamp
    """
    unique_page_ids = set()
    for record in records:
        if record.get('EventTime', 0) > ts:
            page_ids = record.get('PageID')
            if isinstance(page_ids, int):
                unique_page_ids.add(page_ids)
            elif isinstance(page_ids, (list, tuple)):
                unique_page_ids.update(page_ids)
    return unique_page_ids



def get_unique_user_ids_visited_page_after_ts(
        records: list[tp.Mapping[str, tp.Any]],
        ts: int,
        page_id: int
        ) -> set[int]:
    """
    Get unique users visited given web page after some timestamp (not included)
    :param records: records of hit-log
    :param ts: timestamp
    :param page_id: web page identifier
    :return: Unique users visited given web page after some timestamp
    """
    unique_user_ids = set()
    for record in records:
        if record.get('EventTime', 0) > ts and record.get('PageID') == page_id:
            unique_user_ids.add(record.get('UserID'))
    return unique_user_ids



def get_events_by_device_type(
        records: list[tp.Mapping[str, tp.Any]],
        device_type: str
        ) -> list[tp.Mapping[str, tp.Any]]:
    """
    Filter events for given device type with order preservation
    :param records: records of hit-log
    :param device_type: device type name to filter by
    :return: filtered events
    """
    return [record for record in records if record.get('DeviceType') == device_type]






DEFAULT_REGION_ID = 100500

def get_region_ids_with_none_replaces_by_default(
        records: list[tp.Mapping[str, tp.Any]]
        ) -> list[int]:
    """
    Extract visited regions with order preservation. If region not defined, replace it by default region id
    :param records: records of hit-log
    :return: region ids
    """
    return [record.get('RegionID', DEFAULT_REGION_ID) for record in records]


def get_region_id_if_not_none(
        records: list[tp.Mapping[str, tp.Any]]
        ) -> list[int]:
    """
    Extract visited regions if they are defined with order preservation
    :param records: records of hit-log
    :return: region ids
    """
    return [record['RegionID'] for record in records if 'RegionID' in record]



def get_keys_where_value_is_not_none(r: tp.Mapping[str, tp.Any]) -> list[str]:
    """
    Extract keys where values are defined
    :param r: record of hit-log
    :return: keys where values are defined
    """
    return [key for key, value in r.items() if value is not None]



def get_record_with_none_if_key_not_in_keys(
        r: tp.Mapping[str, tp.Any],
        keys: set[str]
        ) -> dict[str, tp.Any]:
    """
    Get record with other keys replaced by None
    :param r: record of hit-log
    :param keys: keys to filter by
    :return: record with other keys replaced by None
    """
    return {key: (r[key] if key in keys else None) for key in r}



def get_record_with_key_in_keys(
        r: tp.Mapping[str, tp.Any],
        keys: set[str]
        ) -> dict[str, tp.Any]:
    """
    Filter record by keys
    :param r: record of hit-log
    :param keys: keys to filter by
    :return: filtered record
    """
    return {key: r[key] for key in keys if key in r}



def get_keys_if_key_in_keys(
        r: tp.Mapping[str, tp.Any],
        keys: set[str]
        ) -> set[str]:
    """
    Filter keys from record by given keys
    :param r: record of hit-log
    :param keys: keys to filter by
    :return: filtered keys
    """
    return {key for key in keys if key in r}
