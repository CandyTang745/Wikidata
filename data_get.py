import requests
import json
import os
import time

from get_QID import country_qids


def get_entity_data(entity_id):
    url = f"https://www.wikidata.org/wiki/Special:EntityData/{entity_id}.json"
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        print(f"[错误] 获取 {entity_id} 失败：{e}")
        return None

def save_json(data, entity_id, folder="wikidata_json"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    file_path = os.path.join(folder, f"{entity_id}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"[成功] 保存 {entity_id} 到 {file_path}")

def batch_fetch(entity_ids, folder="wikidata_json", delay=1):
    for eid in entity_ids:
        print(f"正在处理实体 {eid} ...")
        data = get_entity_data(eid)
        if data:
            save_json(data, eid, folder)
        time.sleep(delay)  # 加一个间隔防止被限制访问

# ✅ 示例实体 ID（Q148=中国, Q30=美国, Q183=德国, Q2=地球）
entity_list = ["Q148", "Q30", "Q183", "Q2", "Q16", "Q145", "Q159"]

batch_fetch(country_qids, folder="wikidata_json", delay=1)
