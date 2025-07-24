import pandas as pd
import json
import os
import re

# 中文表头到英文key的映射
en_key_map = {
    '序号': 'index',
    '学校名称': 'name',
    '学校标识码': 'code',
    '主管部门': 'department',
    '备注': 'remark',
    '所在地': 'location',
    '办学层次': 'level',
}

def is_excel(filename):
    return filename.lower().endswith(('.xls', '.xlsx'))

dir_path = os.path.dirname(os.path.abspath(__file__))
files = [f for f in os.listdir(dir_path) if is_excel(f)]

if not files:
    print('未找到Excel文件，请将Excel文件放入本目录。')
else:
    for excel_file in files:
        try:
            df = pd.read_excel(excel_file, header=None)
            # 查找表头行（通常为第二行）
            header_row = None
            for i, row in df.iterrows():
                if '序号' in row.values and '学校名称' in row.values:
                    header_row = i
                    break
            if header_row is None:
                print(f'{excel_file} 未找到表头，跳过。')
                continue
            # 取表头并映射为英文key
            header = [en_key_map.get(str(x).strip(), str(x).strip()) for x in df.iloc[header_row]]
            # 只保留表头下方的数据
            data_rows = df.iloc[header_row+1:]
            data_rows.columns = header
            # 只保留index为数字的有效行
            valid_rows = data_rows[data_rows['index'].apply(lambda x: isinstance(x, (int, float)) and not pd.isnull(x))]
            # 转为dict，并确保所有key都用英文，且将NaN转为空字符串
            data = []
            for row in valid_rows.to_dict(orient='records'):
                new_row = {}
                for k, v in row.items():
                    en_key = en_key_map.get(k, k)
                    # 处理NaN为""
                    if pd.isnull(v):
                        new_row[en_key] = ""
                    else:
                        new_row[en_key] = v
                data.append(new_row)
            json_file = os.path.splitext(excel_file)[0] + '.json'
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f'{excel_file} 已优化并转换为 {json_file}')
        except Exception as e:
            print(f'处理 {excel_file} 时出错: {e}') 