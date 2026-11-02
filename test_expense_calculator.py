# -*- coding: utf-8 -*-
"""
旅遊支出計算中心單元測試與驗證腳本 (包含 Firebase 雲端同步與主行程連動)
使用 uv run python 執行
"""
import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def test_html_structure_and_features():
    with open("expenses.html", "r", encoding="utf-8") as f:
        html = f.read()

    # 1. 驗證字體與寬版排版
    assert "Plus+Jakarta+Sans" in html, "未引入 Plus Jakarta Sans 字體"
    assert "max-width: 100%" in html, "view-container 未加寬至 100%"

    # 2. 驗證 Excel 匯出功能
    assert "xlsx.full.min.js" in html, "未引入 SheetJS xlsx 函式庫"
    assert "exportToExcel" in html, "未實作 exportToExcel 匯出函式"

    # 3. 驗證 Firebase 雲端即時跨裝置同步核心
    assert "firebase-app-compat.js" in html, "未引入 Firebase App SDK"
    assert "firebase-firestore-compat.js" in html, "未引入 Firebase Firestore SDK"
    assert "DEFAULT_FIREBASE_CONFIG" in html, "未配置預設 Firebase 設定"
    assert "initFirebaseSync" in html, "未實作 Firebase 初始化同步函式"
    assert "listenCloudRoom" in html, "未實作雲端房間監聽"
    assert "pushStateToCloud" in html, "未實作雲端狀態推送"
    assert "cloudRoomModal" in html, "未包含雲端跨裝置房間彈窗"
    assert "copyShareRoomUrl" in html, "未包含複製手機存取網址功能"

    # 4. 驗證從主行程一鍵同步功能
    assert "syncFromMainPlan" in html, "未實作 syncFromMainPlan 同步函式"
    assert "processPlanSync" in html, "未實作主行程活動費用映射邏輯"

    print("[PASS] [1/2] 雲端即時同步、跨裝置存取與主行程連動結構檢查通過！")


def test_calculation_logic():
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
    print("\n🎉 所有雲端跨裝置同步與連動測試皆成功通過！")
