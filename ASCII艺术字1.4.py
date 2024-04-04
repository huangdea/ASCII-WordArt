import pyfiglet
import os

def add_border(ascii_art, border_char='#'):
    lines = ascii_art.split('\n')
    max_length = max(len(line) for line in lines)
    
    border_top = border_char * (max_length + 4)
    border_bottom = border_char * (max_length + 4)
    
    result = [border_top]
    for line in lines:
        line_without_tabs = line.replace('\t', '    ')
        result.append(f'{border_char} {line_without_tabs.ljust(max_length)} {border_char}')
    result.append(border_bottom)
    
    return '\n'.join(result)

def select_font():
    fonts = ['standard', 'big', 'block', 'graffiti', 'isometric1']
    print("\033[1;32m请选择字体：\033[0m")
    for i, font in enumerate(fonts, start=1):
        print(f"\033[1;32m{i}. {font}\033[0m")
    
    while True:
        try:
            choice = int(input("\033[1;32m请输入字体序号（默认为 1）：\033[0m") or 1)
            if 1 <= choice <= len(fonts):
                return fonts[choice - 1]
            else:
                print("无效的选择，请输入合适的序号。")
        except ValueError:
            print("无效的输入，请输入一个整数。")

def main():
    while True:
        text = input("\033[1;32m请输入要转换成 ASCII 艺术字的字符串：\033[0m")
    
        font_name = select_font()
    
        use_border = input("\033[1;32m是否需要边框？(y/n，默认为 'y')：\033[0m").lower() or 'y'
        if use_border != 'n':  # 如果用户输入 'n'，则不添加边框
            border_char = input("\033[1;32m请输入边框字符（默认为 '#'）：\033[0m") or '#'
        else:
            border_char = ''  # 如果用户选择不添加边框，则不使用边框字符
    
        width = int(input("\033[1;32m请输入输出宽度（可选，默认为 80）：\033[0m") or 80)
    
        fig = pyfiglet.Figlet(font=font_name, width=width)
        ascii_art = fig.renderText(text)
    
        bordered_ascii = add_border(ascii_art, border_char)
        print(f"\033[1;34m{bordered_ascii}\033[0m")

if __name__ == "__main__":
    os.system("title ASCII艺术字1.4.py")
    os.system("mode con cols=100 lines=30") #修改宽度
    isometric1_fig = pyfiglet.Figlet(font='isometric1', width=100)
    art = isometric1_fig.renderText('HuangDe')
    print(f"\033[1;31m{art}\033[0m")
    main()
