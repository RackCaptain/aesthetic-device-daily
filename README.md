# aesthetic-device-daily

光电医疗美容设备行业日报 - 每日自动抓取行业资讯并生成报告

## 🌐 在线访问

**日报网站：** https://rackcaptain.github.io/aesthetic-device-daily/

## 📋 项目简介

本项目每天自动收集光电医疗美容设备行业的最新资讯，包括：
- 技术创新（激光、射频、超声等技术进展）
- 市场动态（新产品发布、市场份额变化）
- 政策法规（NMPA/FDA 审批、行业标准）
- 企业新闻（厂商动态、投融资信息）

## 🔄 自动更新

- **频率：** 每天 08:00 (UTC+8)
- **方式：** GitHub Actions 自动运行
- **数据存储：** Git 版本控制，可追溯历史

## 📁 项目结构

```
.
├── .github/workflows/
│   └── daily-report.yml    # 自动化任务配置
├── data/
│   ├── sources.json        # 数据源配置
│   └── archive/            # 历史日报 JSON
├── docs/                   # GitHub Pages 站点
│   ├── index.html          # 最新日报
│   ├── archive/            # 历史归档
│   └── assets/             # CSS/JS/图片
├── src/
│   ├── scraper.py          # 数据采集脚本
│   ├── generator.py        # 日报生成器
│   └── template.html       # 网站模板
└── README.md
```

## 🛠️ 技术栈

- **定时调度：** GitHub Actions
- **数据采集：** Python + Playwright
- **内容处理：** LLM API
- **站点生成：** 纯 HTML + Tailwind CSS
- **部署托管：** GitHub Pages

## 📊 数据源

- 国家药监局（NMPA）医疗器械审批公告
- FDA 510(k) Clearances
- 行业媒体（医美视界、医美部落等）
- 主要厂商官网（Cynosure, Lumenis, Alma 等）

---

*本项目由 OpenClaw 自动维护*
