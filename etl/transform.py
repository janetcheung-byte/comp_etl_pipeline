import pandas as pd

def transform_bls_json(json_data):
    records = []

    for series in json_data['Results']['series']:
        series_id = series['seriesID']
        for item in series['data']:
            year = item['year']
            period = item['period']
            value = float(item['value'])
            if 'M01' <= period <= 'M12':
                records.append({
                    'series_id': series_id,
                    'year': int(year),
                    'month': period,
                    'value': value
                })

    df = pd.DataFrame(records)
    return df