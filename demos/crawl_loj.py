# -*- coding: utf-8 -*-
import time
import requests
import re
import json
import os
from bs4 import BeautifulSoup

# 分离题号、书号和标题，保留题号、标题
code_title_book_spliter = re.compile('^#(\d+)\.\s*「[^」]+」(.+)$')
code_title_spliter = re.compile('^#(\d+)\.\s*(.+)$')
                                     
# 分离key：value
key_value_spliter = re.compile('^([^：]+)：\s*(.+)$')

# 抓取题目数据
def fetch_question_data(code, base_url, data_url):
    # 获取页面HTML内容
    page_response = requests.get(data_url)
    
    # 获取页面bs对象
    page = BeautifulSoup(page_response.text, features="lxml")
    
    # 分析完整包地址
    full_pack_row = page.select('.nine table tbody tr:nth-of-type(1)')[0]
    full_pack_name = full_pack_row.select('td:nth-of-type(1)')[0].text.strip()
    full_pack_link = full_pack_row.select('td:nth-of-type(3) a')[0]['href']
    if full_pack_name != '完整数据包':
        raise NameError('题目' + code + '数据，首条数据非完整数据包，请手工处理')
    
    # 下载完整包到本地/data目录
    full_pack = requests.get(base_url + full_pack_link) 
    with open("data/"+ code + ".zip", "wb") as full_pack_file:
         full_pack_file.write(full_pack.content)

# 抓取题目内容
def fetch_question(base_url, link_url, code):
    question = {}
    question['url'] = link_url

    # 获取页面HTML内容
    page_response = requests.get(link_url)
    
    # 获取页面bs对象
    page = BeautifulSoup(page_response.text, features="lxml")
    rows = page.select('.main .row')
    row_index = 0
    
    # #题号. 标题
    code_title = rows[row_index].find('h1').text.strip()
    code_title_match_result = code_title_spliter.match(code_title)
    if code_title_match_result is None:
        code_title_match_result = code_title_spliter.match(code_title)

    question['code'] = code
    question['title'] = code_title_match_result[2]
    
    # 内存限制，时间限制，输入输出方式
    row_index += 1
    memory_time_io_lables = rows[row_index].select('.label')
    
    memory_limit = memory_time_io_lables[0].text.strip()
    memory_limit_match_result = key_value_spliter.match(memory_limit)
    question['memory_limit'] = memory_limit_match_result[2]
    
    time_limit = memory_time_io_lables[1].text.strip()
    time_limit_match_result = key_value_spliter.match(time_limit)
    question['time_limit'] = time_limit_match_result[2]
    
    question['io'] = memory_time_io_lables[2].text.strip()
    
    # 题目类型，评测方式
    row_index += 1
    question_type_judge_method_labels = rows[row_index].select('.label')
    
    question_type = question_type_judge_method_labels[0].text.strip()
    question_type_match_result = key_value_spliter.match(question_type)
    question['question_type'] = question_type_match_result[2]
    
    judge_method = question_type_judge_method_labels[1].text.strip()
    judge_method_match_result = key_value_spliter.match(judge_method)
    question['judge_method'] = judge_method_match_result[2]

    # 跳过上传
    # 跳过空白
    row_index += 2

    # 页面提交、提交记录、统计、讨论、测试数据 中 获取测试数据压缩包下载地址并完成下载
    data_page_link = None
    if question['judge_method'] != '无测试数据':
        data_page_link_buttons = rows[row_index].select('.button')
        data_page_link_last_button = data_page_link_buttons[len(data_page_link_buttons) - 1]
        data_page_link_relative = data_page_link_last_button['href']
        data_page_link = base_url + data_page_link_relative
    
    htmls = []
    # 题目描述
    # 输入格式
    # 输出格式
    # 样例
    # 数据范围与提示
    # 分类标签
    row_index += 1
    row_length = len(rows)
    while(row_index < row_length):
        block_row = rows[row_index]
        block_title_element = block_row.select('h4')
        if not block_title_element:
            break
        
        block_title = block_title_element[0].text.strip()
        block_content = str(block_row.select('.bottom')[0])
        html = {}
        html['title'] = block_title
        html['content'] = block_content

        htmls.append(html)

        row_index += 1
    
    question['htmls'] = htmls

    if data_page_link is not None and len(htmls) > 1:
        fetch_question_data(code, base_url, data_page_link)
    else:
        question['judge_method'] = '无测试数据'

    return question
    
    

# 主程序
def main():
    # 准备本地文件夹
    if not os.path.exists("data"):
        os.mkdir("data")
    
    # 服务器地址
    base_url = 'https://loj.ac'
    
    # 获取入口页面HTML内容
    main_page = requests.get(base_url + '/article/588')
    
    # 获取题目的全部链接
    links = BeautifulSoup(main_page.text, features="lxml").select('#content a') 
    index = 0
    length = len(links)
    
    # 循环每个链接进行处理
    code = 4001
    for link in links:
        # if code < 4128:
        #     index += 1
        #     code += 1
        #     continue
        
        # 获取抓取题目URL
        link_url = link['href']

        # 抓取并保存题目
        question = fetch_question(base_url, link_url, str(code))
        
        # 无测试数据，从题目中尝试分析正确链接，然后重定向
        if question['judge_method'] == '无测试数据':
            question_description = None;
            question_htmls = question['htmls']
            for question_html in question_htmls:
                if question_html['title'] == '题目描述':
                    question_description = question_html['content']
                    break

            redirect_link = BeautifulSoup(question_description, features="lxml").select('a')[0]
            
            if redirect_link is not None:
                # 从题目重定向
                redirect_link_url = redirect_link['href']
                if redirect_link_url.find('http') == -1:
                    redirect_link_url = base_url + redirect_link_url
                    print('resharp url to ' + redirect_link_url)
                
                print(link_url + " => " + redirect_link_url)
                question = fetch_question(base_url, redirect_link_url, str(code))


        # 休眠，避免过快
        time.sleep(1)
        
        # 写入数据
        with open("questions.json", "a") as full_pack_file:
             full_pack_file.write(json.dumps(question,ensure_ascii=False))
             full_pack_file.write('\n');
        
        index += 1
        code += 1
        print(str(index) + '/' + str(length))

    
# 执行主程序
main()