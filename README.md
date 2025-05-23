# わたしの職務経歴書(未来版) ✨

生成AIで未来のキャリアを描く  
現在の職務経歴書を元に、目指す姿に向けた未来の職務経歴書とキャリアロードマップを自動生成します。

---

## 🧩 機能概要

- 📥 職務経歴書（テキスト or PDF）を入力
- 🎯 目指すキャリア像と実現希望年数を指定
- 📝 職務経歴書（未来版）を出力
- 🛣️ キャリアロードマップを自動生成
- 📄 PDFダウンロード機能（予定）

---

## ⚙️ 使用技術

- Python 3.x
- [Streamlit](https://streamlit.io/)
- OpenAI API
- GitHub (aki-lab-jp)

---

## 🔐 OpenAI API の設定方法
本アプリは Microsoft の Azure OpenAI Service を利用しています。  
利用には **Azure ポータルでのリソース作成と API キーの設定**が必要です。    
### 🔧 手順：  
1. Azure ポータルで「Azure OpenAI」のリソースを作成  
2. 使用したいモデル（例：gpt-35-turbo など）をデプロイ  
3. 以下の情報を `.env` ファイルに記載してください：  

```env
AZURE_OPENAI_ENDPOINT=https://<あなたのリソース名>.openai.azure.com/
AZURE_OPENAI_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-35-turbo
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

💡 `API_VERSION` は Azure OpenAI の公式ドキュメントまたは Azure ポータルで案内されている最新バージョンを使用してください。  
⚠️ `.env` ファイルには認証情報が含まれるため、**必ず `.gitignore` に追加して GitHub にアップロードしないようにしてください。**  
⚠️ **API キーは絶対に公開しないでください。** GitHub 上や他人に見える場所に含めないよう注意しましょう。  
🛠 `.env` ファイルの読み込みには `python-dotenv` を使用します（`requirements.txt` に含める予定です）。  

---

## 🚀 実行方法（ローカル）

```bash
git clone https://github.com/aki-lab-jp/mirai-resume-generator.git
cd mirai-resume-generator
pip install -r requirements.txt
streamlit run app.py
```

---

## 📌 今後の予定

- アピール軸に応じた出力スタイル切り替え（課題解決型、実績重視型など）
- 入力フォームの改良（ドラッグ&ドロップ、PDF自動解析）
- PDF出力・ダウンロード対応

---

## 👩‍💻 Author
A-Koike
- DX・業務改善・生成AIに情熱を注ぐエンジニア
- 業務プロセスの最適化から生成AIの実運用までを一貫して推進
- Power Platform × 生成AI の先端施策で社内表彰歴あり
- GitHub: @aki-lab-jp
- LinkedIn: 