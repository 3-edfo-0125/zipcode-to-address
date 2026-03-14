# 郵便番号→住所入力ツール

郵便番号（ハイフンなし）を入れるだけで住所を取得してくれるツールです。  

## 主な機能
- 郵便番号入力 → 「住所検索」ボタン or **Enterキー** で即検索
- 日本郵便の公式CSVデータによる検索
- ZipCloud APIによる検索
- 都道府県ドロップダウン（郵便番号が複数都道府県に跨ぐレアケース対応）
- 市区町村・町名・番地などの自動補完（複数候補はドロップダウンで選択）
- 漢数字入力も対応（「四九八〇〇〇〇」でも検索OK）
- 建物・部屋番号欄は手入力
- 「住所をコピー」ボタンで全部結合してクリップボードへ
- 「クリア」ボタンでリセット

## こだわりポイント
- CSV・APIどちらを使用するか選択可能
- 郵便番号が都道府県跨ぎの場合も選択可能\
  <img width="502" height="332" alt="Image" src="https://github.com/user-attachments/assets/8118bd61-3664-4ba7-ade8-9a412938a0eb" />
- 一つの郵便番号で複数の市区町村を跨ぐ場合も選択可能\
  <img width="502" height="332" alt="Image" src="https://github.com/user-attachments/assets/6d902427-52fa-420c-aff0-2b7390174327" />
- 一つの郵便番号で複数の町名を含む場合もドロップダウン対応\
  <img width="502" height="332" alt="Image" src="https://github.com/user-attachments/assets/191d45dc-ddb9-4213-8425-cde66bf0f418" />
- 漢数字入力ケア（「一二三」みたいな入力も変換して検索）

## 使い方
1. 日本郵便の郵便番号データ（CSV）を`yubin_tool.py`と同じフォルダにダウンロード
2. `yubin_tool.py` を実行\
   <img width="502" height="332" alt="Image" src="https://github.com/user-attachments/assets/f1b64603-d6e1-4593-b767-58c818375616" />
3. CSVを使用して検索するか、APIを使用して検索するかを選択
4. 郵便番号入力 → Enterキー or 検索ボタン\
   <img width="502" height="332" alt="Image" src="https://github.com/user-attachments/assets/9face603-c856-42ef-8c6f-b17f6c2ff806" />\
   ↓\
   <img width="502" height="332" alt="Image" src="https://github.com/user-attachments/assets/423036a3-5bbf-41be-b3c1-b662907dc867" />
5. 必要なら都道府県/市区町村/番地など 選択
6. 必要な情報を付け足して、住所コピー!\
   <img width="502" height="332" alt="Image" src="https://github.com/user-attachments/assets/fb4102bb-f4c3-408f-b23e-d7caefb417bd" />\
   →クリップボードに「東京都大田区本羽田○丁目×番地△△マンション203号室」と格納


ご覧いただきありがとうございます！
