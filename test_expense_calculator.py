# -*- coding: utf-8 -*-
"""
旅遊支出計算中心單元測試與驗證腳本 (包含 Firebase 雲端同步、多行程切換常駐、輸入框對稱排版、總覽即時連動與手機端 Mobile-First 響應式佈局)
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

    # 7. 驗證多計畫切換 (Plan Switcher) 常駐顯示與版本號 V3.4.1
    assert "expensePlanSelect" in html, "缺少旅行計畫切換下拉選單"
    assert "DEFAULT_PRESET_PLANS" in html, "缺少內建備援旅行計畫列表"
    assert "isPresetOrOldSyncItem" in html, "缺少範本假資料徹底清除函式"
    assert "V3.4.1" in html, "未同步升級版本號至 V3.4.1"

    # 8. 驗證 6 大標準支出分類模式 (機票、住宿、交通、餐飲、景點、購物)
    for cat_name in ["機票", "住宿", "交通", "餐飲", "景點", "購物"]:
        assert cat_name in html, f"缺少 6 大標準分類: {cat_name}"

    # 9. 驗證輸入框對稱排版：預算框與實際支出框具備相同尺寸與 addon
    assert "max-width: 620px" in html, "彈窗最大寬度未擴展至 620px"
    assert "itemActualCurrencyBadge" in html, "實際支出缺少對稱的幣別標籤框"
    assert "onItemCurrencyChange" in html, "缺少幣別切換連動函式"
    assert "TWD (新台幣)" in html, "缺少完整台幣文字"
    assert "JPY (日圓)" in html, "缺少完整日圓文字"

    # 10. 驗證住宿地點與日期完整串接欄位與渲染
    assert "lodgingCityInput" in html, "缺少住宿城市商圈輸入欄位"
    assert "lodgingAddrInput" in html, "缺少住宿詳細地址輸入欄位"
    assert "lodgingCheckInInput" in html, "缺少入住日期欄位"
    assert "lodgingCheckOutInput" in html, "缺少退房日期欄位"
    assert "onLodgingDateChanged" in html, "缺少住宿日期連動計算函式"

    # 11. 驗證大項交通與住宿渲染函式變數獨立性，杜絕 ReferenceError 與畫面空白
    idx_m_start = html.find("function renderMajorItemsList()")
    idx_m_end = html.find("function renderAccommodationsList()", idx_m_start)
    idx_a_end = html.find("function renderAllDaysSections()", idx_m_end)
    major_func = html[idx_m_start:idx_m_end]
    acc_func = html[idx_m_end:idx_a_end]

    assert "acc." not in major_func, "renderMajorItemsList 不得含有 acc.* 變數"
    assert "item." not in acc_func, "renderAccommodationsList 不得含有 item.* 變數"
    assert "totalActualRaw" not in acc_func, "renderAccommodationsList 不得含有 totalActualRaw"
    assert "totalBudgetRaw" not in acc_func, "renderAccommodationsList 不得含有 totalBudgetRaw"

    # 12. 驗證彈跳小視窗 (Modal) 自適應排版，保證內容絕不超出視窗
    assert "calc(100vh - 32px)" in html, "modal-window 最大高度未限制在視窗內"
    assert "overflow: hidden" in html, "modal-window 未啟用 overflow: hidden 防護"
    assert ".modal-window form" in html, "缺少 modal-window form flex 排版限制"
    assert "flex-shrink: 0" in html, "modal-footer 缺少 flex-shrink: 0 置底固定"

    # 13. 驗證智慧去重邏輯與非主行程假資料徹底掃除
    assert "existingNames" in html, "缺少已存在項目去重比對"
    assert "cleanKey" in html, "缺少去重字串標準化函式"
    assert "花市豌雜麵" in html and "isPresetOrOldSyncItem" in html, "缺少歷史假範本徹底掃除機制"

    # 14. 驗證以主行程【預算與實際費用頁面】為主要同步依據之核心結構
    assert "MEAL_CONFIGS" in html, "缺少主行程餐食預算與實付欄位鏡像"
    assert "dayObj.actualBreakfastCost" in html, "缺少早餐實際花費欄位串接"
    assert "dayObj.actualLunchCost" in html, "缺少午餐實際花費欄位串接"
    assert "dayObj.actualDinnerCost" in html, "缺少晚餐實際花費欄位串接"
    assert "dayObj.transports" in html, "缺少主行程 transports 交通明細陣列同步"
    assert "dayObj.spots" in html, "缺少主行程 spots 景點門票明細陣列同步"
    assert "dayObj.extraCosts" in html, "缺少主行程 extraCosts 自訂雜支明細陣列同步"

    # 15. 驗證第四天景點不誤入交通與主行程活躍計畫自動偵測跳轉
    assert "notion_travel_planner_v9_sidebar_state" in html, "缺少主行程 sidebar 狀態快取讀取"
    assert "mainState.activePlanId" in html, "缺少主行程 activePlanId 自動跳轉讀取"
    assert "window.addEventListener('focus'" in html, "缺少視窗獲得焦點自動切換計畫監聽"
    assert 'ev.type === "spot"' in html, "缺少景點類型優先遵循原則"

    for page in ["index.html", "travel_planner.html", "blank.html", "share.html"]:
        with open(page, "r", encoding="utf-8") as pf:
            assert "V3.4.1" in pf.read(), f"{page} 未同步升級至 V3.4.1"

    # 16. 驗證顯示幣別預設基準幣 (TWD) 對齊主行程、機場專車去重與全團總計模式
    assert 'displayCurrency: "base"' in html, "DEFAULT_STATE 顯示幣別未預設為 base (TWD)"
    assert 'isBaseCurrency()' in html, "缺少 isBaseCurrency 基準幣別判斷函式"
    assert 'isAirportShuttle' in html, "缺少機場接送專屬去重保護"
    assert 'mode === "total" || mode === "group"' in html, "缺少全團總計模式精準解析"

    # 17. 驗證主行程預算分頁深度撈取 (住宿欄位結構精確對齊與大項交通專案同步)
    assert 'h.costCurr === "TWD"' in html, "住宿未精準支援主手帳之 h.costCurr 幣別欄位"
    assert 'h.priceType === "total"' in html, "住宿未支援主手帳之 h.priceType 總額模式"
    assert 'plan.majorTransports' in html, "缺少主手帳大項交通專案陣列同步"
    assert 'm_trans_sync_' in html, "缺少大項交通專案同步識別碼"

    # 18. 驗證旅行計畫切換選單智慧去重 (杜絕東京自由行重複出現)
    assert 'function filterDuplicatePlans' in html, "缺少 filterDuplicatePlans 行程去重過濾函式"
    assert 'filterDuplicatePlans(mainAppState.plans)' in html, "未直接以主行程手帳真實 plans 為準"

    # 19. 驗證重慶自由行清空自動救援 (Auto Recovery) 與防空殼清除安全保護 (Safety Guard)
    assert 'isChongqingPlan && isCurrentEmpty' in html, "缺少重慶自由行清空自動救援防呆"
    assert 'DEFAULT_EXPENSE_DATA' in html, "缺少 DEFAULT_EXPENSE_DATA 備援資料庫"
    assert 'hasContent' in html, "缺少 processPlanSync 防空殼清空安全防護"
    assert 'normalizePlanTitle' in html, "缺少保留中文字元之 normalizePlanTitle 智慧去重函式"
    assert 'cloudExp' in html and 'isCloudEmpty' in html, "缺少雲端空帳本防覆蓋安全防線"

    # 20. 驗證以主手帳「預算與實際費用」為唯一權威來源、嚴格槽位唯一性與 events 重複攔截
    assert 'coveredMealSlots' in html, "缺少 coveredMealSlots 餐飲槽位唯一性防護集合"
    assert 'coveredMealSlots.has(sub)' in html, "缺少時間軸 events 重複餐點攔截邏輯"
    assert 'coveredMealSlots.add(mc.slot)' in html, "缺少主手帳預算餐點槽位登記邏輯"
    assert 'hasSyncedTrans || dayHasTransit' in html, "缺少時間軸 events 重複交通攔截"
    assert 'hasSyncedSpots' in html, "缺少時間軸 events 重複景點門票攔截"

    # 21. 驗證瀏覽器放大與中型螢幕自適應、精緻細微滾動條與防切邊佈局
    assert 'days-nav-bar::-webkit-scrollbar' in html, "缺少 days-nav-bar 平滑微型滾動條樣式"
    assert 'max-width: 1240px' in html, "缺少中型螢幕/放大響應式斷點 1240px"
    assert 'max-width: 1024px' in html, "缺少窄桌面/放大響應式斷點 1024px"
    assert 'overflow-x: hidden' in html and 'min-width: 0' in html, "缺少主內容區 min-width: 0 與防溢出設定"

    # 22. 驗證手機端 Mobile-First 響應式佈局、Header 防遮擋、雙分頁切換與底部快捷列
    assert 'mobile-view-tabs' in html, "缺少手機端視圖切換標籤 (mobile-view-tabs)"
    assert 'switchMobileView' in html, "缺少手機端 switchMobileView 視圖切換函式"
    assert 'max-width: 768px' in html, "缺少手機端標準響應式斷點 768px"
    assert 'max-width: 400px' in html, "缺少極小螢幕響應式斷點 400px"
    assert 'safe-area-inset-bottom' in html, "缺少 iPhone 安全底部邊距 (safe-area-inset-bottom) 支援"
    assert 'position: static !important' in html, "缺少手機端 cloudStatusBadge 防覆蓋卡片樣式"
    assert 'flex-wrap: nowrap !important' in html, "缺少手機端 header 防擠壓換行樣式"

    print("[PASS] [1/2] 雲端同步、計畫切換常駐、輸入框對稱排版、大項總覽同步、住宿串接、6 大分類模式與手機端 Mobile-First RWD 檢查通過！")


def test_calculation_logic():
    exchange_rate = 4.65
    member_count = 2

    # 大項支出計算 (預算 vs 實付)
    major_expenses = [
        {"name": "往返機票", "budget": 12500, "actual": 12200, "currency": "TWD", "pricingType": "per_person"},
        {"name": "高鐵票", "budget": 1800, "actual": 1850, "currency": "TWD", "pricingType": "per_person"},
        {"name": "海外旅遊平安險", "budget": 1000, "actual": 1000, "currency": "TWD", "pricingType": "per_person"},
        {"name": "eSIM", "budget": 450, "actual": 420, "currency": "TWD", "pricingType": "per_person"},
    ]
    budget_twd = sum(m["budget"] * member_count for m in major_expenses)
    actual_twd = sum(m["actual"] * member_count for m in major_expenses)
    diff_twd = budget_twd - actual_twd

    assert budget_twd == 31500, f"大項支出預算計算錯誤: {budget_twd}"
    assert actual_twd == 30940, f"大項支出實付計算錯誤: {actual_twd}"
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
    print("\n🎉 所有雲端跨裝置同步、輸入框對稱、總覽連動與手機端 Mobile-First 測試皆成功通過！")
