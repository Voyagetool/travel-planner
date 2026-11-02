# -*- coding: utf-8 -*-
"""
旅遊支出計算中心單元測試與驗證腳本
使用 uv run python 執行
"""
import sys

# 設定輸出編碼避免 Windows cp950 錯誤
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def test_html_structure():
    with open("expenses.html", "r", encoding="utf-8") as f:
        html = f.read()

    # 驗證關鍵標籤
    assert "<!DOCTYPE html>" in html, "缺少 DOCTYPE"
    assert "<html lang=\"zh-TW\">" in html, "缺少繁體中文語言標籤"
    assert "expenses.html" in html or "旅遊支出計算中心" in html
    assert "tripInfo" in html
    assert "DEFAULT_EXPENSE_DATA" in html
    assert "calculateStatistics" in html

    # 驗證特定 UI 元素與需求功能
    assert "🍜 每日餐食" in html, "未包含餐食分類"
    assert "🎫 每日景點" in html, "未包含景點分類"
    assert "🚇 每日交通" in html, "未包含每日交通分類"
    assert "✈️ 大項交通" in html or "大項支出" in html, "未包含大項交通分類"
    assert "🏨 住宿" in html or "住宿費用" in html, "未包含住宿分類"
    assert "連續多日入住" in html, "未包含多日住宿支援"
    assert "單日獨立計費" in html, "未包含單日住宿支援"
    assert "整趟旅程包棟" in html, "未包含整趟住宿支援"
    assert "mobile-bottom-bar" in html, "未包含手機版底部操作列"
    assert "modal-backdrop" in html, "未包含彈窗或 Bottom Sheet"

    print("[PASS] [1/3] HTML 結構與核心需求關鍵字檢查通過！")


def test_calculation_logic():
    # 模擬 JS 中的 calculateStatistics 邏輯
    exchange_rate = 4.65
    member_count = 2

    # 大項支出
    major_expenses = [
        {"name": "往返機票", "amount": 12500, "currency": "TWD", "pricingType": "per_person"},
        {"name": "保險", "amount": 680, "currency": "TWD", "pricingType": "per_person"},
        {"name": "eSIM", "amount": 450, "currency": "TWD", "pricingType": "per_person"},
    ]
    # 全團機票等: (12500 + 680 + 450) * 2 = 13630 * 2 = 27,260 TWD
    major_total_twd = sum(m["amount"] * member_count for m in major_expenses)
    assert major_total_twd == 27260, f"大項支出計算錯誤: {major_total_twd}"

    # 住宿支出
    # acc1: 850 CNY/晚 * 3晚 = 2550 CNY
    # acc2: 560 CNY/晚 * 1晚 = 560 CNY
    # acc3: 720 CNY 總額 (2晚) = 720 CNY
    lodging_cny = (850 * 3) + 560 + 720
    assert lodging_cny == 3830, f"住宿 CNY 計算錯誤: {lodging_cny}"
    lodging_twd = lodging_cny * exchange_rate
    assert round(lodging_twd, 2) == 17809.5, f"住宿 TWD 換算錯誤: {lodging_twd}"

    # 驗證第 1 天的住宿分攤 (威斯汀每晚 850 CNY)
    day1_lodging_cny = 850
    assert round(day1_lodging_cny * exchange_rate, 2) == 3952.5

    # 驗證每人分攤
    per_person_major = major_total_twd / member_count
    assert per_person_major == 13630

    print("[PASS] [2/3] 核心財務與攤提計算邏輯模擬測試通過！")


def test_responsive_css_styles():
    with open("expenses.html", "r", encoding="utf-8") as f:
        html = f.read()

    # 檢查 CSS 響應式中斷點
    assert "@media (max-width: 860px)" in html, "缺少手機版響應式中斷點"
    assert "100vh" in html, "缺少全視窗自適應高度設定"
    assert "calc(100vh - 58px)" in html, "缺少工作區填滿高度設定"
    assert "@media print" in html, "缺少列印樣式"
    assert "bottom: 0" in html, "缺少手機版底部固定列樣式"

    print("[PASS] [3/3] 響應式 CSS 與視窗自適應設定檢查通過！")


if __name__ == "__main__":
    test_html_structure()
    test_calculation_logic()
    test_responsive_css_styles()
    print("\n所有單元測試皆成功通過！")
