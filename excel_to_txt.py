import pandas as pd

def excel_to_txt(input_excel_file, output_txt_file):
    # 读取 Excel 文件
    try:
        df = pd.read_excel(input_excel_file)
    except Exception as e:
        print("读取 Excel 文件时出错：", e)
        return

    # 将单词写入到文本文件中
    try:
        with open(output_txt_file, "w", encoding="utf-8") as file:
            for word in df["Word"]:
                file.write(word.strip() + "\n")
        print("成功将单词写入到文本文件中：", output_txt_file)
    except Exception as e:
        print("写入文本文件时出错：", e)

def main():
    input_excel_file = "1.xlsx"  # 输入的 Excel 文件路径
    output_txt_file = "output.txt"    # 输出的文本文件路径
    excel_to_txt(input_excel_file, output_txt_file)

if __name__ == "__main__":
    main()
