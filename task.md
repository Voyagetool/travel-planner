# 旅遊支出計算中心 (Travel Expense Calculator) 開發任務清單

## 任務目標
打造一個專為旅遊費用設計的「極簡、響應式全視窗與手機友善」旅遊支出計算網頁。解決舊版行程規劃頁面中費用分散繁雜的問題，提供每日餐食景點精算、每日交通與大項交通區分、彈性多模式住宿計費、即時雙幣別與人數分攤統計，並支援 **Google Firebase Firestore 雲端跨裝置即時雙向同步** 與 **主行程資料一鍵連動**。

---

## 任務階段與進度

- [x] **階段一：架構與介面設計規格確立**
  - [x] 撰寫 `task.md` 與 `implementation.plan.md`
  - [x] 定義資料模型（大項交通、每日餐食/景點/交通、彈性住宿模式）
  - [x] 規劃極簡色彩風格與雙平台（桌面滿版 / 手機觸控）自適應排版

- [x] **階段二：核心頁面 `expenses.html` 與樣式實作**
  - [x] 建置響應式網格骨架（桌面側邊/全視窗適應、手機底部抽屜與橫向日期滑軌）
  - [x] 實作頂部/側欄支出儀表板（總金額、人均、分類甜甜圈/進度條、每日對比）
  - [x] 實作幣別切換（TWD/外幣）與即時匯率換算設定
  - [x] 實作人數設定（自動分攤計算）

- [x] **階段三：大項交通與住宿模組實作**
  - [x] 大項交通清單（機票、跨城高鐵、包車、簽證、保險等）
  - [x] 住宿專屬彈性計算器：
    - 單日不同定價模式
    - 連續多日定價模式（每晚單價 / 區間總額）
    - 整趟旅程定價模式與平攤選項

- [x] **階段四：每日餐食、景點、每日交通記帳與分類模組**
  - [x] 每日天數切換與全旅程總覽切換
  - [x] 每日餐食專區（早餐、午餐、晚餐、點心飲料）
  - [x] 每日景點專區（門票、體驗活動、導覽）
  - [x] 每日交通專區（地鐵、捷運、叫車滴滴、公車）
  - [x] 支援單人/全團計費模式轉換

- [x] **階段五：互動功能、資料持久化與範本載入**
  - [x] LocalStorage 自動儲存與讀取
  - [x] 預載重慶 7 天自由行精選支出範本（一鍵體驗）
  - [x] 支援清空資料、匯出 JSON、匯入 JSON
  - [x] 支援列印 / 匯出乾淨費用清單
  - [x] 手機版 Bottom Sheet 新增/編輯彈窗與觸控優化

- [x] **階段六：使用者反饋優化 (字體、頁面加寬、Excel 匯出)**
  - [x] 字體調整：導入現代科技俐落無襯線字體 `Plus Jakarta Sans`（字重 800、微收縮緊湊字距），中文搭配 `Noto Sans TC`，還原第一張截圖視覺質感
  - [x] 加入截圖同款暖沙金膠囊標籤（`badge-warm`）
  - [x] 頁面加寬：主內容區改為全寬 `max-width: 100%`，大幅減少左右空白，使卡片內容寬廣延展
  - [x] 匯出升級：整合 `SheetJS` 支援原生匯出 Excel (.xlsx) 試算表（含【支出總覽】、【每日支出明細】、【大項交通與住宿】三大工作表），並具備離線 UTF-8 BOM CSV Fallback

- [x] **階段七：雲端跨裝置即時同步與主行程雙向連動**
  - [x] 串接 Google Firebase Firestore 雲端即時雙向連線（同一房間多人跨裝置即時同步記帳）
  - [x] 支援房間代碼機制（預設 `chongqing-2026`，支援網址參數 `?room=...` 自訂房間）
  - [x] 頂部配置雲端狀態標籤與彈窗，提供「手機/外部裝置存取專屬連結」一鍵複製
  - [x] 實作 `syncFromMainPlan`：一鍵自動從主行程（`index.html`）抓取旅程資訊、機票大交通、飯店住宿與各天活動費用並自動智慧分類
  - [x] 主行程（`index.html`）與支出計算中心（`expenses.html`）雙向跳轉自動帶入同一個房間代碼
  - [x] 通過單元測試並提交 Git 分支

- [x] **階段八：預算與實際支出對比 (Budget vs Actual) 及交通項目可編輯選項**
  - [x] 升級資料模型：支援 `amount` (預估預算)、`actualAmount` (實際支出)、`isPaid` (已核銷/待支付)
  - [x] 升級頂部/左側統計儀表板：
    - 「預估總預算」vs「實付總支出」雙欄看板
    - 自動計算收支總差額，動態顯示「🟢 結餘節省 +NT$XXX」或「🔴 已超支 -NT$XXX」狀態徽章
    - 人均負擔同步提供「每人實付」與「每人預估」精算
    - 分類統計與每日開支同步呈現實付與預算雙向進度條與對比數據
  - [x] 交通項目編輯彈窗與選項支援：
    - 大項交通清單每一項新增「✏️ 編輯」按鈕，點擊開啟專屬交通編輯彈窗
    - 交通專用設定面板：支援交通工具與模式（往返機票、單程機票、高鐵票、長途包車、租車自駕、客運輪渡、簽證、旅遊平安險等）
    - 支援起訖路線/班次代碼（如 TPE ⇄ CKG / G1234）自訂編輯
    - 同步支援預算、實付金額與核銷狀態隨時修改
    - 每日市區交通（地鐵/捷運、滴滴/叫車、公車等）亦支援獨立編輯
  - [x] Excel 匯出升級：工作表加入預算 vs 實際支出對比欄位與超支/節省分析公式
  - [x] 更新測試腳本並通過驗證 (`uv run python test_expense_calculator.py`)
- [x] **階段九：重構支出分類分佈為 6 大標準模式並徹底修復主行程資料同步**
  - [x] 重構左側支出分類分佈模式：全面改為【✈️ 機票】、【🏨 住宿】、【🚇 交通】、【🍜 餐飲】、【🎫 景點】、【🛍️ 購物】6 大模式
  - [x] 交通類別大整合：將市區日常地鐵/叫車/公車，與城際高鐵/跨城包車/租車統一合併至「🚇 交通」分類
  - [x] 建立多幣別換算樞紐 (`GLOBAL_CURRENCY_RATES`)：支援 CNY, JPY, USD, EUR, KRW 等跨國貨幣換算，徹底杜絕外幣與本幣直接 1:1 造成金額跑掉的錯誤
  - [x] 徹底修復主行程同步與 `undefined` 幽靈活動問題：
    - 嚴格支援活動名稱欄位（`ev.title` / `ev.name` / `ev.target`），過濾名稱異常之無效資料
    - 完整支援主行程 `plan.flights` 機票航段資料結構，不再丟失機票大項
    - 支援主行程中各天獨立三餐、交通與景點欄位同步
    - 自動清理舊版同步產生的 `undefined` 異常項目
  - [x] 更新 Excel 匯出與文字複製摘要，同步採用 6 大標準分類模式
  - [x] 單元測試通過覆蓋驗證
- [x] **階段十：多計畫支出帳本隔離與開啟自動智慧同步 (升級 V3.2.0)**
  - [x] 全站同步升級版本號至 `V3.2.0`（`index.html`、`travel_planner.html`、`blank.html`、`share.html`、`expenses.html`）
  - [x] 主行程跳轉升級：`navigateToExpenses()` 自動攜帶當前計畫參數 `&plan=${appState.activePlanId}`，並於跳轉前自動儲存
  - [x] 支出中心頂部新增旅行計畫切換下拉選單 (`expensePlanSelect`)，支援東京、重慶等多行程一鍵切換
  - [x] 實作多計畫獨立帳本隔離機制 (`expensePlans[planId]`)，東京與重慶帳本完全分開，不再互相覆蓋
  - [x] 實作開啟自動智慧連動 (Auto-Sync on Load)：打開支出中心自動同步最新行程設定（6天/2人/日圓0.2071/長榮航空BR192/市區精選酒店/各天預算）
  - [x] 實作乾淨鏡像同步機制：同步時先清除舊連動項目，徹底解決金額重疊累加與主手帳設定不一致的問題
  - [x] 通過單元測試全項驗證

- [x] **階段十一：優化幣別選單完整顯示、彈窗自適應排版與住宿地點/日期完整串接 (升級 V3.2.1)**
  - [x] 幣別選單與彈窗尺寸/字體優化：
    - 將 `.modal-window` 最大寬度由 `540px` 擴展至 `620px`，雙欄表單在寬度 620px 下每個欄位約 280px，空間寬敞舒適
    - 將 `.input-addon-group .select-field` 寬度由 `90px` 擴展至 `135px`（`min-width: 130px`），內距優化為 `padding: 0 24px 0 10px`
    - 徹底解決「TWD (新台幣)」、「JPY (日圓)」、「CNY (人民幣)」、「USD (美元)」字體被截斷為「TWD (新」的問題
    - 表單「收支差額狀態」對齊美化，形成美觀對稱卡片
  - [x] 住宿地點與日期範圍完整串接：
    - 在支出彈窗的住宿配置區塊（`#lodgingSpecificFields`）新增「住宿城市/商圈 (`lodgingCityInput`)」、「詳細地址/位置說明 (`lodgingAddrInput`)」、「入住日期 (`lodgingCheckInInput`)」與「退房日期 (`lodgingCheckOutInput`)」互動欄位
    - 支援日期連動推算（`onLodgingDateChanged`），自動計算晚數並提示具體日期範圍
    - 升級主行程同步邏輯（`processPlanSync`）：完整串接主手帳中的飯店地點商圈（`city`）、詳細地址（`addr`）、入住日期（`checkIn`）、退房日期（`checkOut`）、天數標籤（`stayLabel`）與房型備註（`notes`）
    - 升級每日紫色住宿橫幅（`renderDayLodgingBanner`）：結構化呈現 🏨 飯店名稱、📍 地點商圈與地址標籤、📅 入住退房日期範圍與晚數、💰 該日攤提與房型備註
    - 升級大項專案列表（`renderLodgingSection`）住宿卡片同步展示地點與日期
  - [x] 依 GEMINI.md 進版規範同步更新版本號至 `V3.2.1`（`index.html`、`travel_planner.html`、`blank.html`、`share.html` 及 `expenses.html`）
  - [x] 擴充單元測試腳本 `test_expense_calculator.py` 並 100% 驗證通過

- [x] **階段十二：修復頂部旅行切換器重新整理消失與範本假資料混雜問題 (升級 V3.2.3)**
  - [x] 頂部旅行計畫選擇選單 (`expensePlanSelect`) 常駐修復：
    - 徹底移除 HTML 上的 `style="display: none;"`
    - 刪除「planKeys <= 1 則隱藏」的錯誤邏輯，確保無論有幾個計畫永遠常駐顯示在頂部
    - 導入 `DEFAULT_PRESET_PLANS`（重慶自由行、東京自由行、北京探索之旅），在頁面一啟動（`initApp()`）首個毫秒立即完成初始化渲染，徹底杜絕重新整理頁面時選單消失、閃爍或時有時無的 bug
    - 支援切換任何旅行時立即載入獨立帳本並自動觸發乾淨鏡像同步
  - [x] 徹底清除範本假資料，杜絕與主行程內容混雜共存：
    - 升級 `processPlanSync(plan)` 中的項目過濾邏輯（`isPresetOrOldSyncItem`）
    - 在鏡像同步時，徹底掃除所有內建範本假資料（威斯汀酒店、武隆依雲、九街民宿、出發前往桃園機場 1200 CNY、花市豌雜麵等歷史假資料）
    - 確保同步後，帳本 100% 乾淨對齊主行程真實內容（重慶解放碑 Moxy 酒店、重慶來福士洲際酒店、陶婆婆火鍋、台北/重慶機場接送），不再出現任何莫名其妙的舊範本項目
  - [x] 依 GEMINI.md 進版規範同步更新版本號至 `V3.2.3`（`index.html`、`travel_planner.html`、`blank.html`、`share.html` 及 `expenses.html`）
  - [x] 單元測試 `test_expense_calculator.py` 100% 驗證通過
- [x] **階段十三：填入預算框格大小一致對稱排版與大項交通編輯後總覽即時同步連動 (升級 V3.3.1)**
  - [x] 輸入框尺寸對稱與排版協調優化：
    - 在「實際支出 (Actual Cost)」輸入框右側新增連動幣別標籤框 #itemActualCurrencyBadge（寬度 135px，外觀尺寸高度 40px 與左側幣別選單完全一模一樣）。
    - 實作 onItemCurrencyChange(curVal)：切換左側幣別選單時，右側幣別標籤框即時同步更新為「TWD (新台幣)」、「JPY (日圓)」、「CNY (人民幣)」、「USD (美元)」。
    - 左右兩側的數字輸入框寬度（lex: 1）與高度（40px）100% 絕對完全一致對稱，下方「計費分攤對象」與「收支差額狀態」高度均為 40px，四個方框形成 2x2 極致對稱的協調矩陣。
  - [x] 大項交通編輯儲存後總覽未更新修復：
    - 修復 calculateStatistics()：將大項交通專案中的固定開銷（如海外旅遊平安險、簽證、交通票券、包車租車等）統籌算入「🚇 交通」分類，不再被誤丟到「🛍️ 購物」分類，左側儀表板「🚇 交通」金額與預估/實付總額在編輯儲存後立即跳動更新。
    - 修復 
enderMajorItemsList：卡片右側同時展示換算後幣別與原始幣別總額及每人單價（例如：411 CNY (實付 2,000 TWD)、預算 411 CNY (2,000 TWD) ‧ 人均 1,000 TWD），數字對應一清二楚。
    - 修復全部行程頂部「全旅程總覽」的差額外幣換算。
  - [x] 依 GEMINI.md 進版規範同步更新全站 5 核心檔案版本號至 V3.3.1（index.html、	ravel_planner.html、lank.html、share.html 及 expenses.html）
  - [x] 擴充單元測試腳本 	est_expense_calculator.py 並 100% 驗證通過

- [x] **階段十四：修復重新整理後右側行程列表空白崩潰問題 (升級 V3.3.2)**
  - [x] 問題根因診斷：在先前針對大項交通與住宿原幣呈現強化時，字串替換範圍導致 `renderAccommodationsList()` 中誤用了未宣告變數（`item.currency`、`totalActualRaw`、`totalBudgetRaw`），執行期拋出 `ReferenceError: item is not defined`，導致整個右側主視圖容器（`renderMainView`）中斷渲染而全白。
  - [x] 函式嚴密隔離修復：
    - `renderMajorItemsList`：嚴格綁定 `item` 物件及 `totalActualRaw`/`totalBudgetRaw`，正確呈現大項交通各項原幣實付與人均。
    - `renderAccommodationsList`：嚴格綁定 `acc` 物件及 `aRaw`/`bRaw`，正確呈現住宿專案原幣實付與人均。
  - [x] 單元測試強化防護：在 `test_expense_calculator.py` 新增第 11 項「大項交通與住宿渲染函式變數獨立性」自動化斷言，徹底杜絕此類未宣告變數導致畫面空白的缺陷。
  - [x] 依 GEMINI.md 進版規範同步更新全站 5 核心檔案版本號至 `V3.3.2`（`index.html`、`travel_planner.html`、`blank.html`、`share.html` 及 `expenses.html`）。

- [x] **階段十五：修復彈跳小視窗內容超出視窗問題 (升級 V3.3.3)**
  - [x] 問題根因診斷：
    - `.modal-window` 未設定 `overflow: hidden`，且直接子元素 `<form>` 為普通區塊元素（非 flex），未受高度約束，高度被內部表單撐大至 750px+，破壞了 flex 限制鏈條。
    - 導致 `.modal-body` 的 `overflow-y: auto` 永遠無法觸發內部滾動，使得彈窗底部的「備註說明」與「取消 / 儲存項目」按鈕被推擠至瀏覽器視窗之外，使用者看不見也點不到。
  - [x] 彈跳小視窗完整自適應優化：
    - `.modal-window` 設定 `max-height: calc(100vh - 32px)`，並加上 `overflow: hidden`，確保整顆彈窗所有邊界與圓角 100% 容納於可視區域中。
    - 替 `.modal-window form` 配置 `display: flex; flex-direction: column; flex: 1; min-height: 0; overflow: hidden;`，打通 flex 限制鏈條。
    - `.modal-header` 與 `.modal-footer` 配置 `flex-shrink: 0`，頂部標題、關閉叉叉與底部「取消」、「儲存項目」操作按鈕永遠常駐固定在彈窗頂端與底端，絕對不被擠出視窗外。
    - `.modal-body` 啟用 `flex: 1; min-height: 0; overflow-y: auto;`，表單內容過多時自動觸發平滑內部滾動條，且優化各區塊 padding 與 gap。
  - [x] 單元測試增加第 12 項彈窗自適應限制斷言防護。
  - [x] 依 GEMINI.md 進版規範同步更新全站 5 核心檔案版本號至 `V3.3.3`（`index.html`、`travel_planner.html`、`blank.html`、`share.html` 及 `expenses.html`）。

- [x] **階段十六：修復同步資訊重複問題並移除非主行程幽靈假資料 (升級 V3.3.4)**
  - [x] 重複問題根因診斷：
    - 主行程中每一天既有「當日預算安排欄位」（`breakfastCost`, `lunchCost`, `dinnerCost`, `transportCost`, `spotCost`），同時時間軸「`events`」也記錄了對應活動的花費（例如 `李子壩吃午餐 100`、`晚上前往野果 100`、`萬象城 50`、`羅漢寺祈福 60`）。
    - 原同步邏輯無條件將欄位預算與時間軸活動全部 push 進每日支出，導致同一餐午餐算兩次、晚餐算兩次、景點門票算兩次、交通算兩次，金額翻倍且清單重複。
  - [x] 智慧去重演算法上線 (`processPlanSync`)：
    - 以主行程「當日預算安排欄位」為權威基準。
    - 遍歷時間軸 `events` 時，實作 `cleanKey()` 字串歸一化比對，自動檢測餐食、景點與交通：
      - 餐飲：當天已有午餐/晚餐/早餐欄位，且活動為同餐期或名稱相似（如李子壩、梁山雞、野果、火鍋等），智慧排除重複！
      - 景點：當天已有景點門票欄位，且活動名稱或地點與景點重疊（如羅漢寺、天生三橋等），智慧排除重複！
      - 交通：當天已有交通欄位，且活動與交通路線重疊（如輕軌、打車、萬象城等），智慧排除重複！
      - 僅保留真正獨立自費項目（例如未在頂部欄位涵蓋的購物伴手禮或額外活動）。
  - [x] 徹底掃除所有非主行程假資料：
    - 升級 `isPresetOrOldSyncItem` 清理器，同步時將所有內建 Demo 範本項目（威斯汀、武隆依雲、九街民宿、花市豌雜麵、珮姐老火鍋、下浩里、南山枇杷園、湖廣會館、來福士烤匠、九街烤腦花等）與舊同步項目 100% 徹底清除，確保帳本純淨鏡像主行程。
  - [x] 單元測試增加第 13 項智慧去重與非主行程假資料排除斷言。
  - [x] 依 GEMINI.md 進版規範同步更新全站 5 核心檔案版本號至 `V3.3.4`（`index.html`、`travel_planner.html`、`blank.html`、`share.html` 及 `expenses.html`）。

- [x] **階段十七：以主行程【預算與實際費用頁面】作為支出計算機同步主要依據 (升級 V3.3.5)**
  - [x] 需求分析與架構對齊：
    - 主行程手帳中具備獨立且權威的「預算規劃與統計分析 (`subpane-budget`)」與「實際花費與行程核銷記帳 (`subpane-actual`)」頁面。
    - 包含：早中晚及點心四餐的預算與實付欄位（`actualBreakfastCost`, `actualLunchCost`, `actualDinnerCost`, `actualSnackCost`）、市區交通明細陣列（`d.transports`）、景點門票明細陣列（`d.spots`）、自訂雜支與購物明細陣列（`d.extraCosts`），以及機票與住宿的預算實付與核銷狀態。
  - [x] 同步核心引擎全面升級 (`processPlanSync`)：
    - 以主行程「預算與實際費用」頁面的數據為第一優先主要依據：
      1. 機票與住宿：同步預估預算、實際支出、幣別、分攤模式、核銷已付狀態與地點日期。
      2. 每日餐食：同步 `MEAL_CONFIGS`（早餐、午餐、晚餐、點心飲料）之名稱、預算與實際花費（`actual...Cost`）、幣別、分攤模式與核銷狀態。
      3. 每日交通：優先以 `d.transports` 陣列同步各筆路線工具、預算、實際支出、幣別與分攤模式；若無陣列則以 `transportCost`/`actualTransportCost` 備援。
      4. 每日景點：優先以 `d.spots` 陣列同步各項門票、預算、實際支出、幣別與分攤模式；若無陣列則以 `spotCost`/`actualSpotCost` 備援。
      5. 其他/購物：以 `d.extraCosts` 陣列同步自訂雜支與購物之預算與實際花費。
      6. 時間軸 events 僅作為未列入上述頁面之自費活動補充，並實作 `existingNames` 比對徹底杜絕重複。
  - [x] 單元測試增加第 14 項「主行程預算與實際費用頁面同步依據」斷言防護。
  - [x] 依 GEMINI.md 進版規範同步更新全站 5 核心檔案版本號至 `V3.3.5`（`index.html`、`travel_planner.html`、`blank.html`、`share.html` 及 `expenses.html`）。

- [x] **階段十八：修復第四天景點誤入交通分類與自動偵測跳轉對應行程 (升級 V3.3.6)**
  - [x] 第四天景點與交通分類誤判根因修復：
    - 修復時間軸事件分類正則：交通關鍵字中移除了容易誤判的單字「車」，收窄為「包車|專車|網約車|租車|接送車|計程車|滴滴|公車|客運|單車|jr|新幹線...」，避免「環保車/觀光電梯」等景點門票內含文字被誤判為交通。
    - 景點類型優先原則：優先依據 `ev.type === "spot"` 或景點活動關鍵字判定為景點門票（`spot`），絕不竄改為市區地鐵交通。
    - 景點去重防護：正確將天生三橋景區參觀活動歸為景點後，成功觸發景點去重邏輯，自動過濾掉與主行程【預算與實際費用】頁面重複的項目，徹底解決第 4 天市區交通多出地鐵 250 CNY 的錯誤。
  - [x] 點開支出計算自動跳轉對應行程：
    - 升級 `getTargetPlanId()`：當 URL 未指定 `plan` 參數時，優先從主手帳 sidebar 狀態快取（`notion_travel_planner_v9_sidebar_state`）中讀取 `activePlanId`，自動鎖定當前主手帳所選的最新計畫（如東京自由行）。
    - 加入視窗焦點監聽（`window.addEventListener('focus', ...)`）：當使用者在主手帳切換不同計畫並切換回支出計算機時，自動平滑切換至對應行程帳本並自動鏡像同步，無需手動下拉選單與手動點擊同步。
  - [x] 單元測試增加第 15 項「第四天景點去重保護與活躍計畫自動跳轉偵測」斷言防護。
  - [x] 依 GEMINI.md 進版規範同步更新全站 5 核心檔案版本號至 `V3.3.6`（`expenses.html`、`index.html`、`travel_planner.html`、`blank.html`、`share.html`）。

- [x] **階段十九：修復幣別與全團/單人分攤模式不一致，徹底消除整體金額 10 倍差距 (升級 V3.3.7)**
  - [x] 顯示幣別預設對齊主程式（台幣 TWD）：
    - 根因：`DEFAULT_STATE` 中的 `displayCurrency` 誤填為 `"TWD"`，而所有判斷邏輯皆為 `=== "base"`，導致系統被誤導將顯示幣別預設為外幣（人民幣 CNY）。
    - 修復：實作 `isBaseCurrency()` 函式，`DEFAULT_STATE` 設為 `"base"`，預設以本國貨幣 **TWD** 呈現全團總額，與主行程手帳「NT$ 台幣」完全一致！點擊頂部切換按鈕可自由切換外幣與台幣。
  - [x] 機場接送專車去重與交通分類校正（根除「門票：出發前往桃園機場 1,200 CNY 每人」幽靈項目）：
    - 根因：主程式預算頁面已設定 `台北機場接送` 1,200 TWD 全團總計，但時間軸第一天活動 `出發前往桃園機場`（1200）未被識別去重，且因名稱未中舊交通正則而被誤判為門票、外幣 CNY、每人單價，暴增成 11,679 TWD！
    - 修復：新增機場專車去重保護（`isAirportShuttle`），若當日或大項交通已有機場接送，時間軸接駁活動一律直接去重排除；擴充交通關鍵字比對備註（含「專車|接送|包車」一律為交通，起訖台灣預設 TWD，交通預設全團總計 `total`）。
  - [x] 全團總計與單人模式精準對齊主行程：
    - 升級 `resolvePricing`：完整支援主程式中的 `total` 與 `group` 模式，交通、門票、餐飲若為全團總計則嚴格定為 `total`，絕不被強制轉為每人單價乘算。
  - [x] 單元測試增加第 16 項「顯示幣別預設 TWD、機場專車去重與全團總計模式支援」斷言防護。
  - [x] 依 GEMINI.md 進版規範同步更新全站 5 核心檔案版本號至 `V3.3.7`（`expenses.html`、`index.html`、`travel_planner.html`、`blank.html`、`share.html`）。

- [x] **階段二十：深度撈取主行程【預算與實際費用】分頁資訊，徹底修復住宿與大項專案巨額偏差 (升級 V3.3.8)**
  - [x] 住宿資料欄位與計價模式 100% 精確對齊：
    - 根因：主行程手帳中飯店資料物件以 `h.priceType`（`perNight`/`total`）、`h.costCurr`（`TWD`/`LOCAL`）、`h.actualCost`、`h.price` 儲存；舊版同步僅讀取 `h.costTotal`（導致整段總額被誤當每晚單價乘算晚數）且僅讀取 `h.currency`（漏掉 `h.costCurr` 導致台幣被盲目定為人民幣），致使解放碑 Moxy（6,000 元）與來福士洲際（16,000 元）被乘上晚數與匯率，膨脹成 116,789 TWD 與 155,718 TWD 巨款！
    - 修復：精確支援 `h.costCurr`（若為 TWD 則 100% 維持 TWD，LOCAL 則為當地幣）、`h.priceType === 'total'`（整段總額定為 `total_stay`，絕不再乘以晚數）、`h.actualCost` 實付房費與 `h.price` 預估房費。
  - [x] 完整同步大項交通專案 (`plan.majorTransports`)：
    - 根因：主行程預算分頁中設定的高鐵、包車、租車、保險、eSIM 存放於 `plan.majorTransports` 陣列，過去同步引擎未撈取該陣列，造成大項專案遺失。
    - 修復：新增 `plan.majorTransports` 深度撈取，自動對齊類別、起訖路線、幣別、分攤模式與實付已付狀態。
  - [x] 一鍵同步點擊即時重新讀取主手帳 localStorage 最新狀態：
    - 根因：`syncFromMainPlan()` 點擊時優先採用了記憶體中的 `availablePlans` 舊快取，未重新讀取 localStorage，導致主手帳更新的資料無法立即反映。
    - 修復：點擊同步時，第一時間立即強制重新自 `notion_travel_planner_v9_sidebar_state` 撈取最新手帳資料，杜絕快取停滯。
  - [x] 單元測試增加第 17 項「主行程預算分頁深度撈取與住宿結構精準對齊」斷言防護。
  - [x] 依 GEMINI.md 進版規範同步更新全站 5 核心檔案版本號至 `V3.3.8`（`expenses.html`、`index.html`、`travel_planner.html`、`blank.html`、`share.html`）。

- [x] **階段二十一：修復旅行計畫選單「東京自由行」重複問題，導入智慧標題去重 (升級 V3.3.9)**
  - [x] 旅行計畫選單重複根因診斷：
    - 根因：`expenses.html` 的多處初始化與更新函式中，無條件使用 `Object.assign({}, DEFAULT_PRESET_PLANS, plans)`；`DEFAULT_PRESET_PLANS` 裡硬編碼了一個假東京行程（ID: `tokyo-2026`），而主手帳傳進來的真實東京行程 ID 是另一個鍵值（如自訂 ID），導致選單同時塞入兩個「東京自由行」。
    - 修復：實作 `filterDuplicatePlans()` 函式；主手帳已有真實 plans 時直接採用手帳真實 plans，不再強行合併 `DEFAULT_PRESET_PLANS`；並加入標題智慧去重演算法，優先保留含有真實活動內容的行程，徹底過濾標題重複項目。
  - [x] 單元測試增加第 18 項「旅行計畫選單智慧去重 (杜絕東京重複)」斷言防護。
  - [x] 依 GEMINI.md 進版規範同步更新全站 5 核心檔案版本號至 `V3.3.9`（`expenses.html`、`index.html`、`travel_planner.html`、`blank.html`、`share.html`）。

- [x] **階段二十二：修復重慶自由行清空問題，導入自動救援 (Auto Recovery) 與防空殼清除安全防線 (升級 V3.3.10)**
  - [x] 重慶自由行資料被清空之根因深入診斷：
    - 根因 1：`filterDuplicatePlans` 過去採用 `replace(/[\s\W_]+/g, '')`，在 JavaScript 中 `\W` 預設為 ASCII，會將所有漢字（重慶、東京、北京、南京等）全部當成非單詞字元誤殺替換成空字串 `""`，導致後續中文行程全部判定為「重複」而被誤拋棄。
    - 根因 2：`DEFAULT_PRESET_PLANS` 裡的重慶計畫只是空殼（無 days、無 hotels、無 flights），當選中空殼時，`processPlanSync` 在處理前無條件執行 `filter(!isPresetOrOldSyncItem)` 清除了所有現存支出項目；隨後因空殼無任何活動，一筆新資料都未加上，直接儲存空狀態洗白了帳本。
    - 根因 3：`updatePlanSwitcherUI` 仍執行 `Object.assign` 強制塞入備援假資料，且雲端連線收到空帳本時反向覆蓋本地資料。
  - [x] 四重防線修復：
    - 防線 1（智慧正規化）：改用 `normalizePlanTitle` 專門移除標點與空格，100% 完整保留中文字元，各城市獨立保留，僅對真實重複項（如 demo 假東京）精準過濾。
    - 防線 2（防空殼清除安全防護）：在 `processPlanSync` 開頭加入 `hasContent` 安全檢查，若為空殼或無實質活動，絕對禁止清空現有支出細項。
    - 防線 3（重慶自由行自動救援）：在 `loadState` 內加入防呆，若重慶行程細項全為 0，立即調用 `DEFAULT_EXPENSE_DATA` 自動還原完整數據（國泰機票、富邦保險、eSIM、Moxy 酒店、來福士、火鍋、天生三橋等）。
    - 防線 4（雲端空帳本防污染）：在 `listenCloudRoom` 收到雲端資料時，若雲端帳本全空，禁止覆蓋本地現存真實數據。
  - [x] 單元測試增加第 19 項「重慶自由行自動救援與防空殼安全防護」斷言防護。
  - [x] 依 GEMINI.md 進版規範同步更新全站 5 核心檔案版本號至 `V3.3.10`（`expenses.html`、`index.html`、`travel_planner.html`、`blank.html`、`share.html`）。

- [x] **階段二十三：修復第三天資料與主行程不一致問題，確立主行程「預算與實際費用」為唯一權威 (升級 V3.3.11)**
  - [x] 第三天資料重複與不一致根因診斷：
    - 根因：主行程手帳「預算與實際費用」分頁是使用者記錄財務真實花費的核心（第三天記錄了飯店早餐、十八梯板凳面、和順港式茶餐廳、美團外賣水果）；但 `processPlanSync` 同步完該分頁後，又跑去讀取時間軸 `events`，將日程建議文字（萬象城時尚商圈、晚上前往野果 Yeego 晚餐等）重複當成自費項目強行塞入，造成同一天出現 2 個晚餐、2 個點心，項目膨脹至 11 項。
  - [x] 確立「預算與實際費用」唯一權威與槽位唯一性防線：
    - 導入 `coveredMealSlots` 集合追蹤已設定餐點槽位（早餐、午餐、晚餐、點心飲料）；
    - 若主手帳預算分頁已明確記錄該餐點槽位，時間軸 `events` 絕對禁止重複塞入任何餐食（徹底消除野果 Yeego、萬象城等重複項目）；
    - 交通與景點同理：若當日已有交通或門票，時間軸上的打車/景點事件一律不重複補入；
    - 成果：第三天完全對齊使用者在主手帳預算分頁填寫的真實明細，徹底消除重複幽靈項目。
  - [x] 單元測試增加第 20 項「主手帳預算頁面唯一權威與槽位唯一性攔截」斷言防護。
  - [x] 依 GEMINI.md 進版規範同步更新全站 5 核心檔案版本號至 `V3.3.11`（`expenses.html`、`index.html`、`travel_planner.html`、`blank.html`、`share.html`）。

- [x] **階段二十四：修復瀏覽器放大顯示異常問題，導入全自適應 RWD、超細平滑滾動條與防切邊佈局 (升級 V3.3.12)**
  - [x] 瀏覽器放大異常根因診斷：
    - 根因 1（頂部按鈕被擠出視窗）：`.app-header` 原設定固定高度 `height: 58px`，左側標籤換行撐開後將右側功能按鈕（同步、記一筆、貨幣切換等）推擠出視窗外；
    - 根因 2（粗暴深灰橫向捲軸）：`.days-nav-bar` 設置 `overflow-x: auto` 但無自訂捲軸，在 Windows 放大時長出 17px 的粗大原生灰色滾動槽橫切畫面；
    - 根因 3（右側內容卡片被切邊）：`.main-content` 缺少 `min-width: 0`，卡片與 `.day-metrics` 缺少 `flex-wrap: wrap`，導致內容撐破容器外層截斷。
  - [x] 全自適應版面與視覺美化修復：
    - 頂部導覽列流式彈性化：`min-height: 58px; height: auto`，右側操作群組設定 `flex-shrink: 0; flex-wrap: wrap`，保證核心功能按鈕永遠留在視窗內；
    - 超細平滑自訂捲軸：增加 `scrollbar-width: thin` 與 `::-webkit-scrollbar` (4px 半透明圓角膠囊)，徹底消除粗糙原生橫向滑塊；
    - 防切邊佈局：`.main-content` 注入 `min-width: 0; overflow-x: hidden`，`.view-container` 優化 padding，`.day-metrics` 與 `.group-header` 支援自然換行，結餘徽章與編輯按鈕 100% 完整可見；
    - 新增中型螢幕與縮放模式斷點（`@media (max-width: 1240px)` 與 `@media (max-width: 1024px)`）。
  - [x] 單元測試增加第 21 項「瀏覽器放大自適應、微型平滑滾動條與防切邊佈局」斷言防護。
  - [x] 依 GEMINI.md 進版規範同步更新全站 5 核心檔案版本號至 `V3.3.12`（`expenses.html`、`index.html`、`travel_planner.html`、`blank.html`、`share.html`）。
