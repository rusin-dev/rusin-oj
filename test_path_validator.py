#!/usr/bin/env python3
"""路径验证测试脚本"""
import sys
sys.path.insert(0, '.')

from judge.utils.path_validator import validate_path, validate_source_file, PathValidationError

def test_normal_path():
    """测试正常路径"""
    try:
        result = validate_source_file('solution.py')
        print(f'[PASS] 正常路径测试通过: {result}')
        return True
    except PathValidationError as e:
        print(f'[FAIL] 正常路径测试失败: {e}')
        return False

def test_path_traversal():
    """测试路径遍历攻击"""
    attacks = [
        '../../../etc/passwd',
        '..\\..\\..\\windows\\system32\\cmd.exe',
        'test/../../etc/passwd',
    ]
    passed = True
    for attack in attacks:
        try:
            validate_source_file(attack)
            print(f'[FAIL] 路径遍历测试失败: 未拦截 {attack}')
            passed = False
        except PathValidationError as e:
            print(f'[PASS] 路径遍历测试通过: 拦截了 {attack}')
    return passed

def test_absolute_path():
    """测试绝对路径"""
    attacks = [
        '/etc/passwd',
        'C:\\Windows\\System32\\cmd.exe',
        'D:\\secret.txt',
    ]
    passed = True
    for attack in attacks:
        try:
            validate_source_file(attack)
            print(f'[FAIL] 绝对路径测试失败: 未拦截 {attack}')
            passed = False
        except PathValidationError as e:
            print(f'[PASS] 绝对路径测试通过: 拦截了 {attack}')
    return passed

def test_special_characters():
    """测试特殊字符"""
    attacks = [
        'test.py\x00',
        'test<script>.py',
        'test|pipe.py',
    ]
    passed = True
    for attack in attacks:
        try:
            validate_source_file(attack)
            print(f'[FAIL] 特殊字符测试失败: 未拦截 {attack}')
            passed = False
        except PathValidationError as e:
            print(f'[PASS] 特殊字符测试通过: 拦截了 {attack}')
    return passed

def test_user_home():
    """测试用户主目录"""
    attacks = [
        '~/secret.txt',
        '~root/.ssh/id_rsa',
    ]
    passed = True
    for attack in attacks:
        try:
            validate_source_file(attack)
            print(f'[FAIL] 用户主目录测试失败: 未拦截 {attack}')
            passed = False
        except PathValidationError as e:
            print(f'[PASS] 用户主目录测试通过: 拦截了 {attack}')
    return passed

def test_valid_extensions():
    """测试有效扩展名"""
    valid_files = [
        'solution.py',
        'Main.java',
        'test.c',
        'program.cpp',
        'lib.rs',
        'main.go',
        'Program.cs',
    ]
    passed = True
    for f in valid_files:
        try:
            result = validate_source_file(f)
            print(f'[PASS] 有效扩展名测试通过: {f}')
        except PathValidationError as e:
            print(f'[FAIL] 有效扩展名测试失败: {f} - {e}')
            passed = False
    return passed

def test_invalid_extensions():
    """测试无效扩展名"""
    invalid_files = [
        'malware.exe',
        'script.sh',
        'binary.bin',
    ]
    passed = True
    for f in invalid_files:
        try:
            validate_source_file(f)
            print(f'[FAIL] 无效扩展名测试失败: 未拦截 {f}')
            passed = False
        except PathValidationError as e:
            print(f'[PASS] 无效扩展名测试通过: 拦截了 {f}')
    return passed

if __name__ == '__main__':
    print('=' * 60)
    print('路径验证模块测试')
    print('=' * 60)
    
    results = []
    results.append(('正常路径', test_normal_path()))
    results.append(('路径遍历', test_path_traversal()))
    results.append(('绝对路径', test_absolute_path()))
    results.append(('特殊字符', test_special_characters()))
    results.append(('用户主目录', test_user_home()))
    results.append(('有效扩展名', test_valid_extensions()))
    results.append(('无效扩展名', test_invalid_extensions()))
    
    print('=' * 60)
    print('测试结果汇总:')
    print('=' * 60)
    
    all_passed = True
    for name, passed in results:
        status = 'PASS' if passed else 'FAIL'
        print(f'{name}: {status}')
        if not passed:
            all_passed = False
    
    print('=' * 60)
    if all_passed:
        print('所有测试通过!')
        sys.exit(0)
    else:
        print('部分测试失败!')
        sys.exit(1)
