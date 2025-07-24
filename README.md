# Universities2025

## 数据来源与统计

- 来源：[中华人民共和国教育部官网](http://www.moe.gov.cn/jyb_xxgk/s5743/s5744/A03/202506/t20250627_1195683.html)
- 数据名称：全国高等学校名单
- 截至2025年6月20日，全国高等学校共计 **3167 所**，其中：
  - 普通高等学校：**2919 所**（含本科学校 1365 所、高职/专科学校 1554 所）
  - 成人高等学校：**248 所**
- 本名单未包含港澳台地区高等学校。

## 项目简介

本项目用于将全国高校名单(截至2025年6月20日)等 Excel 文件批量转换为结构化 JSON 文件，便于数据分析、可视化或系统集成。

## 功能特性
- 批量处理目录下所有 .xls/.xlsx 文件
- 自动识别表头并进行中英文字段映射
- 处理缺失值，保证数据整洁
- 输出结构化、统一的 JSON 文件

## 使用方法

1. 将需转换的 Excel 文件（.xls 或 .xlsx）放入项目目录。
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 运行脚本：
   ```bash
   python excel_to_json.py
   ```
4. 脚本会自动将目录下所有 Excel 文件转换为同名 JSON 文件。

## 依赖说明
- pandas
- openpyxl
- xlrd

## 示例数据结构

```json
[
  {
    "index": 1,
    "name": "北京大学",
    "code": 4111010001,
    "department": "教育部",
    "location": "北京市",
    "level": "本科",
    "remark": ""
  }
]
```

## 贡献方式
欢迎提交 Issue 或 Pull Request 以完善本项目。

## License
MIT

## 联系方式

- 维护人：luzhiyong
- 邮箱：1154119938@qq.com
