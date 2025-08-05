# Python データ分析プロジェクト

このプロジェクトは、Pythonを使用したデータ分析のための包括的な環境を提供します。

## 🚀 特徴

- **包括的なライブラリセット**: pandas, numpy, matplotlib, seaborn, scikit-learn等
- **効率的な開発環境**: コードフォーマット、リンティング、テスト環境
- **再利用可能なユーティリティ**: データ分析でよく使用する関数をまとめたモジュール
- **Jupyter Notebook対応**: インタラクティブな分析環境
- **自動化されたセットアップ**: ワンクリックで環境構築

## 📁 プロジェクト構造

```
python-data-analysis/
├── data/                 # データファイル
├── results/              # 分析結果
├── notebooks/            # Jupyter Notebooks
├── src/                  # ソースコード
│   ├── utils.py         # ユーティリティ関数
│   └── example_analysis.py  # サンプル分析
├── tests/               # テストファイル
├── scripts/             # スクリプト
├── requirements.txt     # 依存関係
├── pyproject.toml      # プロジェクト設定
└── README.md           # このファイル
```

## 🛠️ セットアップ

### 1. 依存関係のインストール

```bash
# 基本的なセットアップ
pip install -r requirements.txt

# 開発用ツールも含めてインストール
pip install -e ".[dev]"
```

### 2. 自動セットアップ（推奨）

```bash
python scripts/setup_dev.py
```

## 📊 使用方法

### 基本的なデータ分析

```python
from src.utils import load_data, explore_data, plot_correlation_matrix

# データを読み込み
df = load_data('data/your_data.csv')

# データ探索
explore_data(df)

# 相関行列をプロット
plot_correlation_matrix(df)
```

### サンプル分析の実行

```bash
python src/example_analysis.py
```

### Jupyter Notebookの使用

```bash
jupyter notebook notebooks/
```

## 🧪 開発ツール

### コードフォーマット

```bash
# Blackでコードをフォーマット
black src/

# flake8でリンティング
flake8 src/
```

### テスト実行

```bash
pytest tests/
```

## 📚 利用可能なライブラリ

### データ処理
- **pandas**: データフレーム操作
- **numpy**: 数値計算
- **openpyxl**: Excelファイル読み込み

### 可視化
- **matplotlib**: 基本プロット
- **seaborn**: 統計的可視化
- **plotly**: インタラクティブ可視化
- **bokeh**: 高度な可視化
- **altair**: 宣言的可視化

### 機械学習
- **scikit-learn**: 機械学習アルゴリズム
- **scipy**: 科学技術計算

### 統計分析
- **statsmodels**: 統計モデリング

## 🔧 カスタマイズ

### 新しい分析スクリプトの作成

```python
# src/my_analysis.py
from utils import load_data, explore_data

def my_analysis():
    # あなたの分析コード
    pass

if __name__ == "__main__":
    my_analysis()
```

### 新しいユーティリティ関数の追加

```python
# src/utils.py に追加
def my_utility_function(data):
    """新しいユーティリティ関数"""
    # 実装
    pass
```

## 📈 分析ワークフロー

1. **データ読み込み**: `load_data()` を使用
2. **データ探索**: `explore_data()` で基本情報を確認
3. **可視化**: 分布、相関、トレンドをプロット
4. **前処理**: 欠損値処理、エンコーディング等
5. **分析**: 統計分析、機械学習等
6. **結果保存**: プロットとレポートを保存

## 🤝 貢献

1. このリポジトリをフォーク
2. 機能ブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 🆘 トラブルシューティング

### よくある問題

1. **依存関係の競合**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt --force-reinstall
   ```

2. **Jupyterカーネルの問題**
   ```bash
   python -m ipykernel install --user --name python-data-analysis
   ```

3. **メモリ不足**
   - 大きなデータセットの場合は、チャンク処理を使用
   - 不要な列を削除
   - データ型を最適化

## 📞 サポート

問題が発生した場合は、以下の手順で解決を試してください：

1. READMEを確認
2. エラーメッセージを検索
3. 新しいIssueを作成

---

**Happy Data Analysis! 🎉**