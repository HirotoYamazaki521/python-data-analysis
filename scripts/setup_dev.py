#!/usr/bin/env python3
"""
開発環境セットアップスクリプト
"""
import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """コマンドを実行"""
    print(f"実行中: {description}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} 完了")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} 失敗: {e}")
        print(f"エラー出力: {e.stderr}")
        return False

def create_directories():
    """必要なディレクトリを作成"""
    directories = [
        'data',
        'results',
        'notebooks',
        'src',
        'tests',
        'scripts'
    ]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✓ ディレクトリ作成: {directory}")

def install_dependencies():
    """依存関係をインストール"""
    commands = [
        ("pip install -r requirements.txt", "依存関係のインストール"),
        ("pip install --upgrade pip", "pipのアップグレード"),
        ("pip install black flake8 pytest", "開発ツールのインストール"),
    ]
    
    for command, description in commands:
        if not run_command(command, description):
            return False
    return True

def setup_jupyter():
    """Jupyter環境のセットアップ"""
    commands = [
        ("python -m ipykernel install --user --name python-data-analysis", "Jupyterカーネルの設定"),
    ]
    
    for command, description in commands:
        if not run_command(command, description):
            return False
    return True

def run_tests():
    """テストを実行"""
    return run_command("python -m pytest tests/ -v", "テストの実行")

def main():
    """メイン処理"""
    print("=== Pythonデータ分析プロジェクト セットアップ ===\n")
    
    # ディレクトリ作成
    print("1. ディレクトリ構造を作成中...")
    create_directories()
    
    # 依存関係インストール
    print("\n2. 依存関係をインストール中...")
    if not install_dependencies():
        print("依存関係のインストールに失敗しました。")
        sys.exit(1)
    
    # Jupyterセットアップ
    print("\n3. Jupyter環境をセットアップ中...")
    if not setup_jupyter():
        print("Jupyterのセットアップに失敗しました。")
        sys.exit(1)
    
    # テスト実行
    print("\n4. テストを実行中...")
    run_tests()
    
    print("\n=== セットアップ完了 ===")
    print("\n次のコマンドで分析を開始できます:")
    print("python src/example_analysis.py")
    print("jupyter notebook notebooks/")

if __name__ == "__main__":
    main() 