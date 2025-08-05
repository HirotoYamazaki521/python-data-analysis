"""
データ分析用ユーティリティ関数
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional, Tuple, List
import warnings

# 警告を無視
warnings.filterwarnings('ignore')

# 日本語フォント設定
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

def load_data(file_path: str, **kwargs) -> pd.DataFrame:
    """
    データファイルを読み込む
    
    Args:
        file_path: ファイルパス
        **kwargs: pandas.read_csv等の追加引数
    
    Returns:
        pd.DataFrame: 読み込んだデータ
    """
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path, **kwargs)
    elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        return pd.read_excel(file_path, **kwargs)
    elif file_path.endswith('.json'):
        return pd.read_json(file_path, **kwargs)
    else:
        raise ValueError(f"Unsupported file format: {file_path}")

def explore_data(df: pd.DataFrame, show_info: bool = True, show_stats: bool = True) -> None:
    """
    データの基本情報を表示
    
    Args:
        df: データフレーム
        show_info: 基本情報を表示するか
        show_stats: 統計情報を表示するか
    """
    print(f"データ形状: {df.shape}")
    print(f"メモリ使用量: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    
    if show_info:
        print("\n=== 基本情報 ===")
        print(df.info())
    
    if show_stats:
        print("\n=== 統計情報 ===")
        print(df.describe())
    
    print("\n=== 欠損値 ===")
    missing_data = df.isnull().sum()
    missing_percent = (missing_data / len(df)) * 100
    missing_df = pd.DataFrame({
        '欠損数': missing_data,
        '欠損率(%)': missing_percent
    })
    print(missing_df[missing_df['欠損数'] > 0])

def plot_correlation_matrix(df: pd.DataFrame, figsize: Tuple[int, int] = (10, 8)) -> None:
    """
    相関行列をプロット
    
    Args:
        df: データフレーム
        figsize: 図のサイズ
    """
    plt.figure(figsize=figsize)
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
                square=True, linewidths=0.5)
    plt.title('相関行列')
    plt.tight_layout()
    plt.show()

def plot_distributions(df: pd.DataFrame, columns: Optional[List[str]] = None, 
                      figsize: Tuple[int, int] = (15, 10)) -> None:
    """
    数値列の分布をプロット
    
    Args:
        df: データフレーム
        columns: プロットする列名（Noneの場合は数値列すべて）
        figsize: 図のサイズ
    """
    if columns is None:
        columns = df.select_dtypes(include=[np.number]).columns
    
    n_cols = min(3, len(columns))
    n_rows = (len(columns) + n_cols - 1) // n_cols
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)
    if n_rows == 1:
        axes = axes.reshape(1, -1)
    
    for i, col in enumerate(columns):
        row = i // n_cols
        col_idx = i % n_cols
        ax = axes[row, col_idx]
        
        df[col].hist(ax=ax, bins=30, alpha=0.7)
        ax.set_title(f'{col}の分布')
        ax.set_xlabel(col)
        ax.set_ylabel('頻度')
    
    # 余分なサブプロットを非表示
    for i in range(len(columns), n_rows * n_cols):
        row = i // n_cols
        col_idx = i % n_cols
        axes[row, col_idx].set_visible(False)
    
    plt.tight_layout()
    plt.show()

def save_plot(filename: str, dpi: int = 300, bbox_inches: str = 'tight') -> None:
    """
    プロットを保存
    
    Args:
        filename: 保存するファイル名
        dpi: 解像度
        bbox_inches: 余白設定
    """
    plt.savefig(filename, dpi=dpi, bbox_inches=bbox_inches)
    print(f"プロットを保存しました: {filename}")

def create_summary_report(df: pd.DataFrame, output_file: str = "data_summary_report.txt") -> None:
    """
    データのサマリーレポートを作成
    
    Args:
        df: データフレーム
        output_file: 出力ファイル名
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("=== データサマリーレポート ===\n\n")
        
        f.write(f"データ形状: {df.shape}\n")
        f.write(f"メモリ使用量: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB\n\n")
        
        f.write("=== 列情報 ===\n")
        for col in df.columns:
            dtype = df[col].dtype
            missing = df[col].isnull().sum()
            missing_pct = (missing / len(df)) * 100
            f.write(f"{col}: {dtype}, 欠損値: {missing} ({missing_pct:.1f}%)\n")
        
        f.write("\n=== 統計情報 ===\n")
        f.write(df.describe().to_string())
        
        f.write("\n\n=== 相関行列 ===\n")
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 1:
            f.write(df[numeric_cols].corr().to_string())
    
    print(f"サマリーレポートを保存しました: {output_file}") 