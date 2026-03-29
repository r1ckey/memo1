import os
import json
import glob

base_dir = r"c:\Users\jorda\Documents\ANTIGRAVITY\STUDY\Databricks_Learning"
output_js = os.path.join(base_dir, "portal_data.js")

weeks = ["Week1", "Week2", "Week3", "Week4"]
portal_data = {}

print("Building Study Portal Data...")

# Fetch Roadmap first
roadmap_path = os.path.join(base_dir, "Databricks_1Month_Roadmap.md")
if os.path.exists(roadmap_path):
    with open(roadmap_path, 'r', encoding='utf-8') as file:
        portal_data["Roadmap"] = [{
            "id": "Roadmap_1Month",
            "title": "Databricks 1ヶ月ロードマップ",
            "content": file.read()
        }]
    print("- Found Roadmap")

# Fetch weekly content
for week in weeks:
    week_dir = os.path.join(base_dir, week)
    portal_data[week] = []
    if os.path.exists(week_dir):
        files = glob.glob(os.path.join(week_dir, "*.md"))
        files.sort() # Ensure 01, 02, 03 order
        for f in files:
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()
                filename = os.path.basename(f)
                portal_data[week].append({
                     "id": f"{week}_{filename}",
                     "title": filename.replace(".md", ""),
                     "content": content
                })
        print(f"- Found {len(files)} files in {week}")

js_content = f"const portalData = {json.dumps(portal_data, ensure_ascii=False)};"

with open(output_js, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"\n✅ Build Complete! Wrote database to {output_js}")
print("You can now open index.html in your browser!")
