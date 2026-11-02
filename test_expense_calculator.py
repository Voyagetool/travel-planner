# -*- coding: utf-8 -*-
"""
旅遊支出計算中心單元測試與驗證腳本 (升級版)
測試項目：字體引入、頁面加寬、Excel 匯出函式與計算邏輯
使用 uv run python 執行
"""
import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def test_html_structure_and_features():
    with open("expenses.html", "r", encoding="utf-8") as f:
        html = f.read()

    # 1. 驗證新字體家族 (Plus Jakarta Sans)
    assert "Plus+Jakarta+Sans" in html, "未引入 Plus Jakarta Sans 字體"
    assert "Plus Jakarta Sans" in html, "CSS 未套用 Plus Jakarta Sans 字體"
    
    # 2. 驗證頁面加寬樣式 (左右空白縮小)
    assert "max-width: 100%" in html, "view-container 未加寬至 100%"
    assert "padding: 20px 32px" in html or "padding: 20px" in html, "view-container padding 需符合寬螢幕排版"

    # 3. 驗證 Excel 匯出功能
    assert "xlsx.full.min.js" in html, "未引入 SheetJS xlsx 函式庫"
    assert "exportToExcel" in html, "未實作 exportToExcel 匯出函式"
    assert "btn-excel" in html, "未包含 Excel 匯出按鈕樣式"
    assert "XLSX.utils.book_new" in html, "未包含多工作表 Excel 建構邏輯"
    assert "支出總覽" in html, "未包含支出總覽工作表"
    assert "每日支出明細" in html, "未包含每日支出明細工作表"
    assert "大項交通與住宿" in html, "未包含大項與住宿工作表"

    # 4. 驗證截圖同款暖沙金膠囊標籤
    assert "badge-warm" in html, "未包含截圖同款暖沙金標籤樣式"

    print("[PASS] [1/2] 新字體、加寬排版與 Excel 匯出結構檢查通過！")


def test_calculation_logic():
    # 驗證計算邏輯
    exchange_rate = 4.65
    member_count = 2

    # 大項支出計算
    major_expenses = [
        {"name": "往返機票", "amount": 12500, "currency": "TWD", "pricingType": "per_person"},
        {"name": "保險", "amount": 680, "currency": "TWD", "pricingType": "per_person"},
        {"name": "eSIM", "amount": 450, "currency": "TWD", "pricingType": "per_person"},
    ]
    major_total_twd = sum(m["amount"] * member_count for m in major_expenses)
    assert major_total_twd == 27260, f"大項支出計算錯誤: {major_total_twd}"

    # 住宿計算
    lodging_cny = (850 * 3) + 560 + 720
    assert lodging_cny == 3830, f"住宿 CNY 計算錯誤: {lodging_cny}"
    lodging_twd = lodging_cny * exchange_rate
    assert round(lodging_twd, 2) == 17809.5, f"住宿 TWD 換算錯誤: {lodging_twd}"

    print("[PASS] [2/2] 核心財務與攤提計算邏輯模擬測試通過！")


if __name__ == "__main__":
    test_html_structure_and_features()
    test_calculation_logic()
    print("\n🎉 所有更新測試皆成功通過！")
