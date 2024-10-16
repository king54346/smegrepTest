import subprocess
import json
import os

def remove_existing_json(json_file):
    # 检查并删除已有的 semgrep.json 文件
    if os.path.exists(json_file):
        os.remove(json_file)
        print(f"{json_file} 文件已删除。")
    else:
        print(f"{json_file} 文件不存在，无需删除。")

def run_semgrep(scan_path):
    # 检查路径是否存在
    if not os.path.exists(scan_path):
        print(f"路径 {scan_path} 不存在，请检查后重新输入。")
        return
    
    # 构建 semgrep 扫描命令
    command = ['semgrep', 'scan', '--config', './semgrep-rules/', '--json', '--json-output=semgrep.json', scan_path]
    
    try:
        subprocess.run(command, check=True)
        print("Semgrep 扫描已完成，结果保存为 semgrep.json")
    except subprocess.CalledProcessError as e:
        print(f"执行 Semgrep 时出错: {e}")

def parse_semgrep_json(json_file):
    # 读取 semgrep.json 文件
    if not os.path.exists(json_file):
        print(f"JSON 文件 {json_file} 不存在。")
        return

    with open(json_file, 'r', encoding='utf-8') as f:
        semgrep_result = json.load(f)
    
    # 解析结果
    findings = semgrep_result.get('results', [])
    if not findings:
        print("没有发现任何结果。")
        return

    for finding in findings:
        # 获取路径、漏洞类型、描述和语言
        path = finding.get('path', '未知文件')
        start_line = finding.get('start', {}).get('line', '未知行')
        vuln_type = finding.get('extra', {}).get('metadata', {}).get('category', '未知类型')
        message = finding.get('extra', {}).get('message', '无描述')
        lang = finding.get('extra', {}).get('engine_name', '未知语言')
        severity = finding.get('extra', {}).get('severity', '未定义严重性')
        # 打印信息
        print(f"文件: {path}, 行号: {start_line}, 严重性: {severity}")
        print(f"漏洞类型: {vuln_type}")
        print(f"描述: {message}")
        print(f"语言: {lang}")
        print("-" * 50)


if __name__ == '__main__':
    # 指定 JSON 文件名
    json_file = 'semgrep.json'
    
    # 删除现有的 semgrep.json 文件
    remove_existing_json(json_file)
    
    # 输入扫描路径
    scan_path = input("请输入扫描路径: ")
    
    # 运行 semgrep 扫描
    run_semgrep(scan_path)
    
    # 解析 semgrep.json
    parse_semgrep_json(json_file)