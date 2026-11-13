#!/usr/bin/env bash
# Import TC từ CSV (08_Templates/A3_GitHub_Projects_Import.csv: title,body,tc_id,req_id,priority,status)
# vào GitHub Projects dưới dạng draft item bằng GitHub CLI.
# Dùng: ./scripts/import_tc_to_project.sh <project-number> <owner> <file.csv>
# Yêu cầu: gh CLI đã đăng nhập (gh auth login; với GitHub nội bộ: --hostname <host>) và có scope 'project'.
# GitHub nội bộ phải hỗ trợ Projects và lệnh gh project; nếu chưa hỗ trợ, tạo item thủ công trên giao diện bảng.
# Các trường TC ID/REQ/Priority/Status: tạo custom field trong Project rồi cập nhật bằng 'gh project item-edit'
# hoặc chỉnh trực tiếp trên giao diện bảng. Tối thiểu: title chứa TC ID, body chứa REQ + bước + expected.
set -euo pipefail
PROJECT="$1"; OWNER="$2"; FILE="$3"
python3 - "$FILE" <<'PY' | while IFS=$'\t' read -r title body; do
import csv, sys
for r in csv.DictReader(open(sys.argv[1], encoding='utf-8-sig')):
    body = f"REQ: {r['req_id']} | Priority: {r['priority']} | Status: {r['status']}\n\n{r['body']}"
    print(r['title'].replace('\t',' ') + '\t' + body.replace('\t',' ').replace('\n','\\n'))
PY
  gh project item-create "$PROJECT" --owner "$OWNER" --title "$title" --body "$(printf '%b' "$body")"
  echo "Đã tạo: $title"
done
