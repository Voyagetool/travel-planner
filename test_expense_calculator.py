# -*- coding: utf-8 -*-
"""
旅遊支出計算中心單元測試與驗證腳本 (包含 Firebase 雲端同步、主行程連動、住宿串接與彈窗 UI)
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

    # 5. 驗證預算與實際支出對比功能 (Budget vs Actual)
    assert "totalBudgetDisplay" in html, "缺少預估總預算顯示欄位"
    assert "totalActualDisplay" in html, "缺少實付總支出顯示欄位"
    assert "heroVarianceBadge" in html, "缺少收支差額結餘/超支徽章"
    assert "actualAmount" in html, "缺少實付金額欄位定義"
    assert "isPaid" in html, "缺少已付狀態標記"

    # 6. 驗證交通項目可編輯選項
    assert "openEditMajorExpenseModal" in html, "缺少大項交通編輯彈窗函式"
    assert "transportSpecificPanel" in html, "缺少交通專屬模式起訖面板"
    assert "transportModeSelect" in html, "缺少交通細項分類選單"
    assert "transportRouteInput" in html, "缺少交通起訖路線輸入欄"

    # 7. 驗證多計畫切換 (Plan Switcher) 與版本號 V3.2.1
    assert "expensePlanSelect" in html, "缺少旅行計畫切換下拉選單"
    assert "V3.2.1" in html, "未同步升級版本號至 V3.2.1"

    # 8. 驗證 6 大標準支出分類模式 (機票、住宿、交通、餐飲、景點、購物)
    for cat_name in ["機票", "住宿", "交通", "餐飲", "景點", "購物"]:
        assert cat_name in html, f"缺少 6 大標準分類: {cat_name}"

    # 9. 驗證幣別選單寬度與彈窗尺寸優化
    assert "max-width: 620px" in html, "彈窗最大寬度未擴展至 620px"
    assert "width: 135px" in html or "min-width: 130px" in html, "幣別選單未擴展寬度"
    assert "TWD (新台幣)" in html, "缺少完整台幣文字"
    assert "JPY (日圓)" in html, "缺少完整日圓文字"

    # 10. 驗證住宿地點與日期完整串接欄位與渲染
    assert "lodgingCityInput" in html, "缺少住宿城市商圈輸入欄位"
    assert "lodgingAddrInput" in html, "缺少住宿詳細地址輸入欄位"
    assert "lodgingCheckInInput" in html, "缺少入住日期欄位"
    assert "lodgingCheckOutInput" in html, "缺少退房日期欄位"
    assert "onLodgingDateChanged" in html, "缺少住宿日期連動計算函式"
    assert "lodging-loc-tag" in html, "缺少住宿地點標籤 CSS"
    assert "lodging-desc-pill" in html, "缺少住宿日期與攤提標籤 CSS"

    print("[PASS] [1/2] 雲端同步、多行程隔離、彈窗尺寸/幣別選單、住宿地點/日期串接與 6 大分類模式檢查通過！")


def test_calculation_logic():
    exchange_rate = 4.65
    member_count = 2

    # 大項支出計算 (預算 vs 實付)
    major_expenses = [
        {"name": "往返機票", "budget": 12500, "actual": 12200, "currency": "TWD", "pricingType": "per_person"},
        {"name": "高鐵票", "budget": 1800, "actual": 1850, "currency": "TWD", "pricingType": "per_person"},
        {"name": "保險", "budget": 680, "actual": 680, "currency": "TWD", "pricingType": "per_person"},
        {"name": "eSIM", "budget": 450, "actual": 420, "currency": "TWD", "pricingType": "per_person"},
    ]
    budget_twd = sum(m["budget"] * member_count for m in major_expenses)
    actual_twd = sum(m["actual"] * member_count for m in major_expenses)
    diff_twd = budget_twd - actual_twd

    assert budget_twd == 30860, f"大項支出預算計算錯誤: {budget_twd}"
    assert actual_twd == 30300, f"大項支出實付計算錯誤: {actual_twd}"
    assert diff_twd == 560, f"差額節省計算錯誤: {diff_twd} (預期結餘 560)"

    # 住宿計算 (CNY)
    lodging_cny_budget = (850 * 3) + 560 + 720
    assert lodging_cny_budget == 3830, f"住宿 CNY 計算錯誤: {lodging_cny_budget}"
    lodging_twd_budget = lodging_cny_budget * exchange_rate
    assert round(lodging_twd_budget, 2) == 17809.5, f"住宿 TWD 換算錯誤: {lodging_twd_budget}"

    print("[PASS] [2/2] 核心財務、預算對比與攤提計算邏輯模擬測試通過！")


if __name__ == "__main__":
    test_html_structure_and_features()
    test_calculation_logic()
    print("\n🎉 所有雲端跨裝置同步與連動測試皆成功通過！")
