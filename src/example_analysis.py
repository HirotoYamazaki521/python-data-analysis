"""
データ分析のサンプルスクリプト
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_data, explore_data, plot_correlation_matrix, plot_distributions, save_plot, create_summary_report

def create_sample_data():
    """サンプルデータを作成"""
    np.random.seed(42)
    n_samples = 1000
    
    data = {
        '年齢': np.random.normal(35, 10, n_samples),
        '年収': np.random.normal(5000000, 1500000, n_samples),
        '勤続年数': np.random.exponential(5, n_samples),
        '満足度': np.random.uniform(1, 10, n_samples),
        '部門': np.random.choice(['営業', '開発', '企画', '人事'], n_samples),
        '性別': np.random.choice(['男性', '女性'], n_samples)
    }
    
    # 相関関係を追加
    data['年収'] = data['年収'] + data['年齢'] * 50000 + data['勤続年数'] * 100000
    data['満足度'] = data['満足度'] + (data['年収'] - 5000000) / 1000000
    
    df = pd.DataFrame(data)
    
    # 負の値を修正
    df['年齢'] = df['年齢'].clip(20, 65)
    df['年収'] = df['年収'].clip(2000000, 15000000)
    df['勤続年数'] = df['勤続年数'].clip(0, 30)
    df['満足度'] = df['満足度'].clip(1, 10)
    
    return df

def main():
    """メイン分析処理"""
    print("=== データ分析サンプル ===\n")
    
    # サンプルデータを作成
    print("1. サンプルデータを作成中...")
    df = create_sample_data()
    
    # データを保存
    df.to_csv('data/sample_data.csv', index=False, encoding='utf-8')
    print("サンプルデータを保存しました: data/sample_data.csv")
    
    # データ探索
    print("\n2. データ探索を実行中...")
    explore_data(df)
    
    # 相関行列のプロット
    print("\n3. 相関行列をプロット中...")
    numeric_df = df.select_dtypes(include=[np.number])
    plot_correlation_matrix(numeric_df)
    save_plot('results/correlation_matrix.png')
    
    # 分布のプロット
    print("\n4. 分布をプロット中...")
    plot_distributions(df, columns=['年齢', '年収', '勤続年数', '満足度'])
    save_plot('results/distributions.png')
    
    # 部門別分析
    print("\n5. 部門別分析を実行中...")
    dept_analysis = df.groupby('部門').agg({
        '年齢': ['mean', 'std'],
        '年収': ['mean', 'std'],
        '満足度': ['mean', 'std']
    }).round(2)
    
    print("部門別統計:")
    print(dept_analysis)
    
    # 部門別の箱ひげ図
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    df.boxplot(column='年収', by='部門', ax=plt.gca())
    plt.title('部門別年収')
    plt.suptitle('')
    
    plt.subplot(1, 3, 2)
    df.boxplot(column='満足度', by='部門', ax=plt.gca())
    plt.title('部門別満足度')
    plt.suptitle('')
    
    plt.subplot(1, 3, 3)
    df.boxplot(column='年齢', by='部門', ax=plt.gca())
    plt.title('部門別年齢')
    plt.suptitle('')
    
    plt.tight_layout()
    save_plot('results/department_analysis.png')
    
    # 性別分析
    print("\n6. 性別分析を実行中...")
    gender_analysis = df.groupby('性別').agg({
        '年齢': 'mean',
        '年収': 'mean',
        '満足度': 'mean'
    }).round(2)
    
    print("性別統計:")
    print(gender_analysis)
    
    # サマリーレポート作成
    print("\n7. サマリーレポートを作成中...")
    create_summary_report(df, 'results/data_summary_report.txt')
    
    print("\n=== 分析完了 ===")
    print("結果ファイル:")
    print("- data/sample_data.csv: サンプルデータ")
    print("- results/correlation_matrix.png: 相関行列")
    print("- results/distributions.png: 分布図")
    print("- results/department_analysis.png: 部門別分析")
    print("- results/data_summary_report.txt: サマリーレポート")

if __name__ == "__main__":
    main() 