#!/usr/bin/env python3
"""
Daily Report Generator for Aesthetic Device Industry
光电医疗美容设备行业日报生成器
"""

import json
import os
from datetime import datetime
from pathlib import Path

# 确保目录存在
Path("docs/archive").mkdir(parents=True, exist_ok=True)
Path("docs/assets").mkdir(parents=True, exist_ok=True)

def load_sources():
    """加载数据源配置"""
    with open("data/sources.json", "r", encoding="utf-8") as f:
        return json.load(f)

def generate_html(date_str, articles):
    """生成日报 HTML"""
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>光电医疗美容设备日报 - {date_str}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700&display=swap');
        body {{ font-family: 'Noto Sans SC', sans-serif; }}
    </style>
</head>
<body class="bg-gray-50 min-h-screen">
    <header class="bg-gradient-to-r from-blue-600 to-purple-600 text-white py-8">
        <div class="container mx-auto px-4">
            <h1 class="text-3xl font-bold">光电医疗美容设备行业日报</h1>
            <p class="mt-2 text-blue-100">{date_str}</p>
        </div>
    </header>

    <main class="container mx-auto px-4 py-8">
        <!-- 概览卡片 -->
        <div class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
            <div class="bg-white rounded-lg shadow p-4 border-l-4 border-blue-500">
                <h3 class="text-gray-500 text-sm">今日资讯</h3>
                <p class="text-2xl font-bold text-gray-800">{len(articles)}</p>
            </div>
            <div class="bg-white rounded-lg shadow p-4 border-l-4 border-green-500">
                <h3 class="text-gray-500 text-sm">技术动态</h3>
                <p class="text-2xl font-bold text-gray-800">-</p>
            </div>
            <div class="bg-white rounded-lg shadow p-4 border-l-4 border-yellow-500">
                <h3 class="text-gray-500 text-sm">政策法规</h3>
                <p class="text-2xl font-bold text-gray-800">-</p>
            </div>
            <div class="bg-white rounded-lg shadow p-4 border-l-4 border-purple-500">
                <h3 class="text-gray-500 text-sm">产品发布</h3>
                <p class="text-2xl font-bold text-gray-800">-</p>
            </div>
        </div>

        <!-- 资讯列表 -->
        <div class="bg-white rounded-lg shadow">
            <div class="p-6 border-b">
                <h2 class="text-xl font-bold text-gray-800">今日精选</h2>
            </div>
            <div class="divide-y">
                {generate_articles_html(articles)}
            </div>
        </div>

        <!-- 关于 -->
        <div class="mt-8 text-center text-gray-500 text-sm">
            <p>本报告由 OpenClaw 自动生成</p>
            <p class="mt-1">更新时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        </div>
    </main>
</body>
</html>'''
    return html

def generate_articles_html(articles):
    """生成文章列表 HTML"""
    if not articles:
        return '''
        <div class="p-8 text-center text-gray-500">
            <p>今日暂无新资讯</p>
            <p class="mt-2 text-sm">数据源正在收集中...</p>
        </div>'''
    
    html = ""
    for article in articles:
        html += f'''
        <div class="p-6 hover:bg-gray-50 transition">
            <div class="flex items-start justify-between">
                <div class="flex-1">
                    <span class="inline-block px-2 py-1 text-xs rounded-full bg-blue-100 text-blue-800 mb-2">
                        {article.get('category', '资讯')}
                    </span>
                    <h3 class="text-lg font-semibold text-gray-800 mb-2">
                        <a href="{article.get('url', '#')}" target="_blank" class="hover:text-blue-600">
                            {article.get('title', '无标题')}
                        </a>
                    </h3>
                    <p class="text-gray-600 text-sm mb-2">{article.get('summary', '')}</p>
                    <div class="flex items-center text-xs text-gray-400">
                        <span>{article.get('source', '未知来源')}</span>
                        <span class="mx-2">•</span>
                        <span>{article.get('date', '')}</span>
                    </div>
                </div>
            </div>
        </div>'''
    return html

def main():
    """主函数"""
    today = datetime.now()
    date_str = today.strftime("%Y年%m月%d日")
    date_file = today.strftime("%Y-%m-%d")
    
    print(f"生成日报: {date_str}")
    
    # 加载数据源
    sources = load_sources()
    print(f"已加载 {len(sources['sources'])} 个数据源")
    
    # 模拟文章数据（实际应从网络抓取）
    articles = []  # 这里后续会接入实际抓取逻辑
    
    # 生成 HTML
    html = generate_html(date_str, articles)
    
    # 保存到 docs 目录
    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    
    # 保存历史归档
    with open(f"docs/archive/{date_file}.html", "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"日报已生成: docs/index.html")
    print(f"历史归档: docs/archive/{date_file}.html")

if __name__ == "__main__":
    main()
