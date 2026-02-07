from scholarly import scholarly, ProxyGenerator
import jsonpickle
import json
from datetime import datetime
import os

GOOGLE_SCHOLAR_ID = 'bBc5rVMAAAAJ'

def fetch_data():
    try:
        pg = ProxyGenerator()
        pg.FreeProxies()
        scholarly.use_proxy(pg)
    except Exception:
        pass

    try:
        author = scholarly.search_author_id(GOOGLE_SCHOLAR_ID)
        scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
        
        author['updated'] = str(datetime.now())
        if 'publications' in author:
            author['publications'] = {v['author_pub_id']: v for v in author['publications']}
        
        output_dir = 'google-scholar-stats'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with open(f'{output_dir}/gs_data.json', 'w') as outfile:
            json.dump(author, outfile, ensure_ascii=False, indent=2)
        
        citation_count = author.get('citedby', 0)
        
        shieldio_data = {
            "schemaVersion": 1,
            "label": "citations",
            "message": str(citation_count),
            "color": "4091BD",
            "labelColor": "cecece",
            "namedLogo": "google-scholar",
            "logoColor": "white",
            "style": "flat"
        }
        
        with open(f'{output_dir}/gs_data_shieldsio.json', 'w') as outfile:
            json.dump(shieldio_data, outfile, ensure_ascii=False, indent=2)

    except Exception as e:
        print(e)
        exit(1)

if __name__ == "__main__":
    fetch_data()
