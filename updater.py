import requests

UPDATES_URL = "https://raw.githubusercontent.com/kokokoko200/ai_self_updates/main/updates.txt"
KNOWLEDGE_FILE = "knowledge.txt"

def fetch_updates():
    try:
        print("جارٍ جلب التحديثات من الإنترنت...")
        response = requests.get(UPDATES_URL)
        response.raise_for_status()
        updates = response.text.strip().splitlines()
        return updates
    except Exception as e:
        print("خطأ أثناء جلب التحديثات:", e)
        return []

def update_knowledge():
    updates = fetch_updates()
    if not updates:
        return

    try:
        with open(KNOWLEDGE_FILE, "r", encoding="utf-8") as f:
            existing_knowledge = set(f.read().strip().splitlines())
    except FileNotFoundError:
        existing_knowledge = set()

    new_entries = [entry for entry in updates if entry not in existing_knowledge]

    if new_entries:
        with open(KNOWLEDGE_FILE, "a", encoding="utf-8") as f:
            for entry in new_entries:
                f.write(entry + "\n")
        print(f"تم تحميل عدد {len(new_entries)} من الردود الجديدة.")
    else:
        print("لا توجد ردود جديدة.")

if __name__ == "__main__":
    update_knowledge()
