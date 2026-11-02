# 旅遊支出計算網頁 (Travel Expense Calculator) 實作計畫

## 1. 背景與需求分析
現有旅遊規劃網站（`https://alicetychen.github.io/travel-planner/?room=chongqing-2026&v=9`）著重於景點行程安排、搶票時程、行李清單與 Notion 風格時間軸，但使用者在「費用支出試算與記帳」方面有更明確的精算需求：
1. **分類計算精細化**：
   - **每日餐食**：早餐、午餐、晚餐、點心等依天分類計算。
   - **每日景點**：門票、活動、體驗等依天分類計算。
   - **交通兩大維度**：
     - **每日交通**：捷運/地鐵、叫車/計程車、公車等市區日常移動。
     - **大項支出**：機票、長途高鐵、包車、簽證、保險等跨城市/跨國固定大項。
   - **住宿多模式彈性計算**：
     - 每日不同計費（例如不同飯店、平日與假日浮動房價）。
     - 連續多日計費（例如連續入住 3 晚，支援每晚價格或區間總額）。
     - 整趟旅程合併計算（例如包週民宿或全趟固定住宿總預算，可自由設定是否攤提入每日）。
2. **極簡版面設計 (Minimalist UI)**：
   - 拒絕多餘刺眼顏色，採用低飽和度的高級灰冷調（Zinc / Slate / Monochromatic），搭配功能性微色調標籤（冷藍、鼠尾草綠、暖杏、柔紫）。
   - 字體清晰排版（Typography & White space），呈現現代輕奢極簡美感。
3. **全視窗自適應 (Auto-fit Full Window)**：
   - 桌面端：採用自適應雙欄/三欄流暢填滿整個視窗（100vh），左側為儀表板統計與快捷篩選，右側為日期分頁與項目卡片列表，內容各自平滑滾動，拒絕外層雙滾動條。
4. **手機端深度適配 (Mobile First)**：
   - 頂部滑動天數導覽與可折疊支出看板。
   - 觸控友善的卡片與「+ 記一筆」浮動大按鈕。
   - 專屬手機滑入式抽屜（Bottom Sheet Modal），方便單手拇指操作。
5. **輔助與實用功能**：
   - 雙幣別與即時匯率換算（例如 TWD / CNY / JPY / USD）。
   - 人數均攤（全團總額 vs 每人負擔）。
   - 預估預算 vs 實際支出追蹤。
   - 本地儲存（LocalStorage）、匯出/匯入 JSON、列印專用清單、重慶行程支出範本一鍵載入。

---

## 2. 系統架構與技術選型
- **架構**：單頁式網頁應用（SPA in Pure Modern HTML5 + CSS3 + Vanilla ES6+）。
  - 不引入肥大的外部重型框架，確保 0 延遲秒開、離線可用、完全相容 GitHub Pages。
  - 圖標：純 SVG 內嵌（Lucide 風格），精巧簡潔。
- **檔案命名**：`expenses.html`（作為獨立且專屬的支出計算器網頁），並在現有 `index.html` 頂部選單加入連動捷徑。

---

## 3. 資料架構設計 (Data Model)
```typescript
interface TravelExpenseState {
  version: string;
  tripInfo: {
    title: string;              // 旅程名稱，如「重慶 7 天 6 夜之旅」
    startDate: string;          // 開始日期，如 2026-04-10
    daysCount: number;          // 總天數
    memberCount: number;        // 同行人數（用於均攤）
    baseCurrency: string;       // 基準幣別（如 TWD）
    foreignCurrency: string;    // 當地外幣（如 CNY）
    exchangeRate: number;       // 1 當地外幣 = 多少基準幣別 (如 4.65)
    displayCurrency: 'base' | 'foreign'; // 目前呈現幣別
  };
  // 大項支出（非每日，全趟大筆費用）
  majorExpenses: Array<{
    id: string;
    category: 'flight' | 'train' | 'rental' | 'insurance' | 'visa' | 'other';
    name: string;
    amount: number;             // 金額
    currency: string;           // 幣別
    pricingType: 'total' | 'per_person'; // 全團總額 或 每人
    isPaid: boolean;            // 是否已支付
    note?: string;
  }>;
  // 住宿計算（支援每日不同、連續多日、整趟旅程）
  accommodations: Array<{
    id: string;
    name: string;
    mode: 'daily' | 'range' | 'trip'; // 單日 / 連續多日 / 整趟
    day?: number;               // 單日模式指定天數 (1~N)
    startDay?: number;          // 區間起始天數
    endDay?: number;            // 區間結束天數
    nights: number;             // 晚數
    pricingType: 'per_night' | 'total'; // 每晚單價 或 該段總額
    amount: number;             // 金額
    currency: string;
    roomCount: number;          // 房間數
    isPaid: boolean;
    note?: string;
  }>;
  // 每日支出項目（餐食、景點、每日交通、購物/其他）
  dailyExpenses: Array<{
    id: string;
    day: number;                // 旅程第幾天 (1~N)
    category: 'dining' | 'spot' | 'transit' | 'shopping' | 'other';
    subType: string;            // 如 dining: breakfast/lunch/dinner/snack; spot: ticket/activity; transit: metro/taxi/bus
    name: string;
    amount: number;
    currency: string;
    pricingType: 'total' | 'per_person';
    isPaid: boolean;
    note?: string;
  }>;
}
```

---

## 4. 介面模組規劃 (UI Layout)
1. **頂部導覽列 (Header)**：
   - 品牌與旅程標題（可即時點擊編輯）。
   - 幣別快速切換按鈕（例如 `[🇹🇼 新台幣 TWD] ⇋ [🇨🇳 人民幣 CNY @ 4.65]`）。
   - 人數切換（例如 `👥 2 人 (自動均攤)`）。
   - 旅程設定按鈕（天數、匯率、日期）。
   - 輔助操作：範本載入、匯出/匯入、列印清單、返回主行程。
2. **視窗佈局 (Desktop 滿版雙欄)**：
   - **左欄（數據儀表板與分類總覽，寬約 380px~420px，固定視窗高）**：
     - 總支出總覽卡（全團總花費、平均每人負擔、已付 vs 未付）。
     - 分類花費佔比長條圖與清單（大項交通、每日交通、住宿、餐食、景點、其他）。
     - 每日花費柱狀小圖表（各天花費趨勢，點擊可快速過濾至該天）。
   - **右欄（主操作區，填滿剩餘寬度，平滑滾動）**：
     - 天數切換滑軌標籤（`全部總覽` | `Day 1` | `Day 2` | ... | `大項交通與住宿專案`）。
     - 當選擇某一天時：
       - 該日預算統計條（當日餐食、當日景點、當日交通、當日住宿攤提）。
       - 「🍜 每日餐食」（早餐、午餐、晚餐、點心）清單與新增按鈕。
       - 「🎫 每日景點」（門票、體驗）清單與新增按鈕。
       - 「🚇 每日交通」（捷運、叫車、公車）清單與新增按鈕。
       - 「🏨 該日住宿」（自動顯示該日入住飯店與當日費用/攤提）。
     - 當選擇「大項與住宿」或「全部總覽」時：
       - 「✈️ 大項交通支出」獨立管理面板（新增機票、高鐵、租車等）。
       - 「🏨 住宿管理與攤提中心」獨立管理面板（新增/編輯住宿模式）。
3. **手機端視窗與互動 (Mobile View)**：
   - 全寬單欄佈局，頂部黏性 Header 包含旅程總額與快捷切換。
   - 水平滾動的日期膠囊按鈕（`全部`、`D1`、`D2`...、`大項/住宿`）。
   - 底部固定快捷操作列（含「+ 記一筆」大按鈕，點擊彈出 Bottom Sheet）。
   - Bottom Sheet 支援：快速選擇類別（餐食、景點、每日交通、大項交通、住宿），輸入金額、幣別、每人/全團、備註，單手一秒完成記帳。

---

## 5. 實作步驟
1. 建立 `expenses.html`，編寫結構、極簡現代 CSS 與完整 JavaScript 模組。
2. 預載「重慶 7 天 6 夜之旅」真實支出範本，方便使用者一開啟就能看到清晰直觀的數據。
3. 建立自動化測試腳本（`test_expenses.py`），利用 Python 驗證：
   - 匯率轉換計算。
   - 人數分攤計算。
   - 每日餐食、景點、每日交通分類統計。
   - 住宿模式（單日/多日區間/整趟）計算與每日攤提。
   - 大項交通與全團總額。
4. 在現有 `index.html` 導覽列中加入「💰 支出計算中心」連結，使兩者能互相導流。
5. 提交 Git 紀錄並審閱成果。
