# ==========================================
# 作業名稱：Python 資料型別實作作業 - 聚餐費用試算器
# 姓名：[葉柏澤]
# 學號：[D1446728]
# ==========================================

# ------------------------------------------
# 測試一：使用原始資料（4 人、折價券 100 元）
# ------------------------------------------
print("=== 測試一 ===")

# 1. 原始資料輸入
event_name = "  WEEKEND DINNER  "
meal_amount = " NT$1,200 "
people = "4"

service_rate = 0.10
discount = 100
budget_per_person = 300

# 2. 資料整理與型別轉換
# 使用 .strip() 去除頭尾空白，.lower() 轉成小寫
clean_event_name = event_name.strip().lower()

# 使用 .replace() 移除 "NT$" 與逗號，.strip() 去除空白，最後用 float() 轉成浮點數
clean_meal_str = meal_amount.replace("NT$", "").replace(",", "").strip()
meal_cost = float(clean_meal_str)

# 使用 int() 將文字人數轉成整數
num_people = int(people)

# 3. 分步計算費用（先算服務費，再扣折價券）
service_fee = meal_cost * service_rate
total_amount = meal_cost + service_fee - discount
cost_per_person = total_amount / num_people

# 4. 判斷是否超過預算（產生布林值 True 或 False）
is_over_budget = cost_per_person > budget_per_person

# 5. 輸出費用摘要（使用 :.2f 顯示到小數點後兩位）
print(f"聚餐名稱：{clean_event_name}")
print(f"原始餐費：{meal_cost:.2f} 元")
print(f"服務費：{service_fee:.2f} 元")
print(f"折價券：{discount:.2f} 元")
print(f"應付總額：{total_amount:.2f} 元")
print(f"分攤人數：{num_people} 人")
print(f"每人費用：{cost_per_person:.2f} 元")
print(f"每人預算：{budget_per_person:.2f} 元")
print(f"是否超過預算：{is_over_budget}")
print("\n")


# ------------------------------------------
# 測試二：只將人數改成 "5"，折價券維持 100 元
# ------------------------------------------
print("=== 測試二 ===")

# 1. 原始資料輸入
event_name = "  WEEKEND DINNER  "
meal_amount = " NT$1,200 "
people = "5"  # 修改人數為 "5"

service_rate = 0.10
discount = 100
budget_per_person = 300

# 2. 資料整理與型別轉換
clean_event_name = event_name.strip().lower()
clean_meal_str = meal_amount.replace("NT$", "").replace(",", "").strip()
meal_cost = float(clean_meal_str)
num_people = int(people)

# 3. 分步計算費用
service_fee = meal_cost * service_rate
total_amount = meal_cost + service_fee - discount
cost_per_person = total_amount / num_people

# 4. 判斷是否超過預算
is_over_budget = cost_per_person > budget_per_person

# 5. 輸出費用摘要
print(f"聚餐名稱：{clean_event_name}")
print(f"原始餐費：{meal_cost:.2f} 元")
print(f"服務費：{service_fee:.2f} 元")
print(f"折價券：{discount:.2f} 元")
print(f"應付總額：{total_amount:.2f} 元")
print(f"分攤人數：{num_people} 人")
print(f"每人費用：{cost_per_person:.2f} 元")
print(f"每人預算：{budget_per_person:.2f} 元")
print(f"是否超過預算：{is_over_budget}")
print("\n")


# ------------------------------------------
# 測試三：人數恢復為 "4"，只將折價券改成 220 元
# ------------------------------------------
print("=== 測試三 ===")

# 1. 原始資料輸入
event_name = "  WEEKEND DINNER  "
meal_amount = " NT$1,200 "
people = "4"  # 人數恢復為 "4"

service_rate = 0.10
discount = 220  # 修改折價券為 220
budget_per_person = 300

# 2. 資料整理與型別轉換
clean_event_name = event_name.strip().lower()
clean_meal_str = meal_amount.replace("NT$", "").replace(",", "").strip()
meal_cost = float(clean_meal_str)
num_people = int(people)

# 3. 分步計算費用
service_fee = meal_cost * service_rate
total_amount = meal_cost + service_fee - discount
cost_per_person = total_amount / num_people

# 4. 判斷是否超過預算
is_over_budget = cost_per_person > budget_per_person

# 5. 輸出費用摘要
print(f"聚餐名稱：{clean_event_name}")
print(f"原始餐費：{meal_cost:.2f} 元")
print(f"服務費：{service_fee:.2f} 元")
print(f"折價券：{discount:.2f} 元")
print(f"應付總額：{total_amount:.2f} 元")
print(f"分攤人數：{num_people} 人")
print(f"每人費用：{cost_per_person:.2f} 元")
print(f"每人預算：{budget_per_person:.2f} 元")
print(f"是否超過預算：{is_over_budget}")
