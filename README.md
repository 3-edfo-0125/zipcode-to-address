# 郵便番号→住所入力ツール

郵便番号（ハイフンなし）を入れるだけで住所を自動入力してくれるツールです。  

## 主な機能
- 郵便番号入力 → 「住所検索」ボタン or **Enterキー** で即検索
- 日本郵便の公式CSVデータ使用
- 都道府県ドロップダウン（郵便番号が複数都道府県に跨ぐレアケース対応）
- 市区町村・町名・番地などの自動補完（複数候補はドロップダウンで選択）
- 漢数字入力も対応（「四九八〇〇〇〇」でも検索OK）
- 建物・部屋番号欄は手入力
- 「住所をコピー」ボタンで全部結合してクリップボードへ
- 「クリア」ボタンでリセット

## こだわりポイント
- 郵便番号が都道府県跨ぎの場合も選択可能\
  <img width="502" height="332" alt="Image" src="https://github.com/user-attachments/assets/b470c90e-1cb3-43b4-bc22-7b85a0fa8ea4" />
- 一つの郵便番号で複数の市区町村を跨ぐ場合も選択可能\
  <img width="502" height="332" alt="Image" src="https://github.com/user-attachments/assets/e8648edd-f553-43ba-9cdc-6d07b0e7796e" />
- 一つの郵便番号で複数の町名を含む場合もドロップダウン対応\
  <img width="502" height="332" alt="Image" src="https://github.com/user-attachments/assets/b6b8d80a-d876-45e8-a49b-01383b9bb81e" />
- 漢数字入力ケア（「一二三」みたいな入力も変換して検索）

## 使い方
1. 日本郵便の郵便番号データ（CSV）を`yubin_tool.py`と同じフォルダにダウンロード
2. `yubin_tool.py` を実行\
   <img width="502" height="332" alt="Image" src="https://github.com/user-attachments/assets/c1fbb6d6-9b51-4335-8e97-1b19342f7ff0" />
3. 郵便番号入力 → Enterキー or 検索ボタン\
   <img width="502" height="332" alt="Image" src="https://github.com/user-attachments/assets/53e3f0b7-1273-41fd-b559-17300482c9bd" />\
   ↓\
   <img width="502" height="332" alt="Image" src="https://github.com/user-attachments/assets/e7b9b2a9-2bc6-4cd6-8324-e04d9df280fe" />
5. 必要なら都道府県/市区町村/番地など 選択
6. 必要な情報を付け足して、住所コピー!\
   <img width="502" height="332" alt="Image" src="https://github.com/user-attachments/assets/71b66546-a324-43fd-8393-2754db05ce0c" />\
   →クリップボードに「東京都大田区本羽田○丁目×番地△△マンション203号室」と格納
   
ご覧いただきありがとうございます！
